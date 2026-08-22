# -*- coding: utf-8 -*-
u"""harness — ОДИН И ТОТ ЖЕ АУДИТ ДЛЯ ЛЮБОЙ ПУБЛИЧНОЙ СТРАТЕГИИ.

Замысел оператора 20.08: не разбор одного репозитория, а корпус разборов,
сделанных ОДНОЙ И ТОЙ ЖЕ процедурой. Тогда сравнение честно, а не
подобрано.

ЧЕМ ЭТО ОТЛИЧАЕТСЯ ОТ ПЕРВОГО ЗАХОДА
------------------------------------
Первый разбор я делал переписыванием на pandas, и главной оговоркой было
«это не freqtrade». Оговорка снята: здесь работает НАСТОЯЩИЙ freqtrade, а
значит числа авторитетны, а не приблизительны.

Вдобавок запускаются два его СОБСТВЕННЫХ детектора, которые почти никто
не запускает:

    lookahead-analysis    заглядывание в будущее
    recursive-analysis    индикатор, меняющий значение от объёма истории

Второй, столкнувшись с `startup_candle_count = 0`, ОТКАЗЫВАЕТСЯ работать и
сам объявляет это дефектом. Отказ инструмента — тоже результат, и он
записывается как результат, а не как сбой.

ЧЕТЫРЕ ЗНАЧЕНИЯ, А НЕ ДВА
-------------------------
    ПРОШЛА        проверка выполнена, вот число
    НАЙДЕНО       проверка выполнена, дефект есть
    НЕ ПРИМЕНИМА  выполнить нельзя, причина названа
    НЕ ЗАПУСКАЛИ  до неё не дошло

«Не смогли проверить» никогда не печатается как «чисто». Это тот самый
дефект, который в этом проекте стоил $110.
"""
from __future__ import print_function

import ast
import io
import json
import os
import re
import subprocess
import sys

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

# Корень — от самого файла, а не от моего диска: README обещает, что
# harness.py можно запустить у себя. Переопределяется AUDIT_ROOT.
ROOT = os.environ.get("AUDIT_ROOT") or os.path.dirname(os.path.abspath(__file__))
FT = os.path.join(ROOT, "ftenv", "Scripts", "freqtrade.exe")
CFG = os.path.join(ROOT, "user_data", "config.json")
STRAT_DIR = os.path.join(ROOT, "user_data", "strategies")
RESULTS = os.path.join(ROOT, "results")
CODE_MD5 = __import__("hashlib").md5(
    io.open(os.path.abspath(__file__), "rb").read()).hexdigest()[:12]
TF_MINUTES = {"1m": 1, "3m": 3, "5m": 5, "15m": 15, "30m": 30,
              "1h": 60, "2h": 120, "4h": 240, "6h": 360,
              "8h": 480, "12h": 720, "1d": 1440, "3d": 4320,
              "1w": 10080}
IN_RANGE = "20180301-20200301"
OUT_RANGE = "20200301-20260820"

PASS, FOUND, NA, SKIP = u"ПРОШЛА", u"НАЙДЕНО", u"НЕ ПРИМЕНИМА", u"НЕ ЗАПУСКАЛИ"


def sh(args, timeout=900):
    env = dict(os.environ)
    env["PYTHONIOENCODING"] = "utf-8"
    try:
        r = subprocess.run(args, capture_output=True, timeout=timeout, env=env)
        return r.returncode, (r.stdout + r.stderr).decode("utf-8", "replace")
    except subprocess.TimeoutExpired:
        return 124, u"ПРЕВЫШЕНО ВРЕМЯ"
    except Exception as ex:
        return 1, u"НЕ ЗАПУСТИЛОСЬ: %r" % (ex,)


# ─────────────────────── статические проверки ───────────────────────

def find_strategies(path):
    u"""[(файл, имя класса)] — по СТРУКТУРЕ (наследование IStrategy), а не
    по имени файла. Имя обманчиво, база наследования — нет."""
    out = []
    # TOTAL: имена стратегий собираются в множество и сортируются вызывающим
    for dirpath, dirs, names in os.walk(path):
        dirs[:] = [d for d in dirs if d not in (".git", "__pycache__", "venv")]
        for n in names:
            if not n.endswith(".py"):
                continue
            p = os.path.join(dirpath, n)
            try:
                src = io.open(p, encoding="utf-8", errors="replace").read()
                tree = ast.parse(src)
            except Exception:
                continue
            for node in ast.walk(tree):
                if isinstance(node, ast.ClassDef):
                    bases = [b.id if isinstance(b, ast.Name)
                             else getattr(b, "attr", "") for b in node.bases]
                    if "IStrategy" in bases:
                        out.append((p, node.name))
    return out


def static_checks(path, src):
    u"""[(уровень, что, подробности)]. Только механически проверяемое."""
    res = []

    # ① объявленный прогрев против самого длинного индикатора
    periods = [int(m) for m in re.findall(r"timeperiod\s*=\s*(\d+)", src)]
    periods += [int(m) for m in re.findall(r"window\s*=\s*(\d+)", src)]
    declared = re.search(r"^\s*startup_candle_count\s*[:=]\s*(\d+)", src, re.M)
    d = int(declared.group(1)) if declared else 0
    if periods:
        need = max(periods)
        if d == 0:
            res.append((FOUND, u"прогрев не объявлен",
                        u"самый длинный индикатор %d свечей, "
                        u"startup_candle_count не задан (по умолчанию 0)" % need))
        elif d < need:
            res.append((FOUND, u"прогрев занижен",
                        u"объявлено %d, нужно не менее %d" % (d, need)))
        else:
            res.append((PASS, u"прогрев объявлен",
                        u"%d при потребности %d" % (d, need)))

    # ② мёртвые настройки трейлинга
    ts = re.search(r"^\s*trailing_stop\s*[:=]\s*(True|False)", src, re.M)
    tsp = re.search(r"^\s*trailing_stop_positive\s*[:=]\s*([\d.]+)", src, re.M)
    if ts and tsp and ts.group(1) == "False":
        res.append((FOUND, u"мёртвые настройки трейлинга",
                    u"trailing_stop=False, но trailing_stop_positive=%s задан — "
                    u"читается как работающая защита" % tsp.group(1)))
    if ts and ts.group(1) == "True" and not tsp:
        res.append((FOUND, u"трейлинг на полном стопе",
                    u"trailing_stop=True без trailing_stop_positive ⇒ стоп "
                    u"тащится на ВСЁ расстояние стоп-лосса"))

    # ③ minimal_roi объявлен или закомментирован
    if re.search(r"^\s*#\s*minimal_roi", src, re.M) and \
            not re.search(r"^\s*minimal_roi\s*[:=]", src, re.M):
        res.append((FOUND, u"minimal_roi закомментирован",
                    u"правила выхода по прибыли берутся из неопубликованного конфига"))

    # ④ грубые признаки заглядывания в будущее
    for pat, what in ((r"\.shift\(\s*-\d+", u"сдвиг в будущее .shift(-N)"),
                      (r"\[::-1\]", u"разворот ряда [::-1]"),
                      (r"center\s*=\s*True", u"центрированное окно center=True")):
        if re.search(pat, src):
            res.append((FOUND, u"признак утечки будущего", what))
    return res


# ─────────────────────── прогоны freqtrade ───────────────────────

# ⚠ ПОЙМАНО НА СЕБЕ 20.08, ДО ПУБЛИКАЦИИ. Разбор выдал p-значение 5.896,
# чего не бывает: вероятность не превышает единицы. Причина — научная
# запись: из "5.896e-05" шаблон `[\d.]+` брал "5.896" и останавливался на
# букве. Опубликуй я это, критик был бы прав дважды.
# Невозможное значение — не «странность», а сигнал сломанного прибора.
NUM = r"(-?\d+(?:\.\d+)?(?:[eE][+-]?\d+)?)"


def _num(out, pat, cast=float):
    m = re.search(pat, out)
    return cast(m.group(1)) if m else None


def parse_summary(out):
    u"""Словарь показателей из вывода бэктеста.

    ⚠ ЧТО ИСПРАВЛЕНО 20.08 ПО ВНЕШНЕЙ АТАКЕ. Прежняя версия брала только
    число сделок и итог. Критик указал на отсутствие базовой линии и
    статистической значимости — и был прав, причём вдвойне: freqtrade
    СЧИТАЕТ и то и другое, а я просто не выводил.

        Market change        базовая линия «купил и держи» на тех же парах
        Mean profit p-value  значимость средней доходности сделки

    Это ровно наш собственный M-16 («базовая линия первой»), не применённый
    к себе. Числа без базовой линии висят в воздухе — и мой первый разбор
    так и висел.
    """
    d = {
        "trades": _num(out, r"Total/Daily Avg Trades\s*│\s*(\d+)", int),
        "total_pct": _num(out, r"Total profit %\s*│\s*" + NUM + r"%"),
        "expectancy": _num(out, r"Expectancy \(Ratio\)\s*│\s*" + NUM),
        "p_value": _num(out, r"Mean profit p-value\s*│\s*" + NUM),
        "market_change_pct": _num(out, r"Market change\s*│\s*" + NUM + r"%"),
        "sharpe": _num(out, r"Sharpe \(closed trades\)\s*│\s*" + NUM),
        "sortino": _num(out, r"Sortino \(closed trades\)\s*│\s*" + NUM),
        "profit_factor": _num(out, r"Profit factor\s*│\s*" + NUM),
        "drawdown_pct": _num(out, r"Absolute drawdown\s*│\s*[\d.]+ \w+ \((-?[\d.]+)%\)"),
        "cagr_pct": _num(out, r"CAGR %\s*│\s*" + NUM + r"%"),
    }
    # СТОРОЖ НЕВОЗМОЖНОГО. Вероятность вне [0,1] означает не удивительный
    # результат, а сломанный прибор. Публиковать такое нельзя, молча
    # чинить — тоже: значение помечается, чтобы его увидели.
    pv = d.get("p_value")
    if pv is not None and not (0.0 <= pv <= 1.0):
        d["p_value"] = None
        d["parse_warning"] = u"p-значение вне [0,1] (%r) — разбор вывода сломан" % pv
    return d


RX_TF_DECL = re.compile(r"""^\s*timeframe\s*[:=]\s*['"]([^'"]+)['"]""", re.M)


def declared_tf(src):
    u"""Таймфрейм, объявленный САМОЙ стратегией. None — не объявлен."""
    m = RX_TF_DECL.search(src)
    return m.group(1) if m else None


def engine_tf(out):
    u"""Таймфрейм, на котором движок ФАКТИЧЕСКИ считал — его собственными
    словами (`Strategy using timeframe: 1h`), а не моим предположением."""
    m = re.search(r"Strategy using timeframe:\s*(\S+)", out)
    return m.group(1) if m else None


def missing_pairs(out):
    u"""Пары, по которым движок НЕ НАШЁЛ истории. Он об этом предупреждает
    и ПРОДОЛЖАЕТ на остальных — результат выходит полным на вид, но по
    меньшему числу инструментов. Сравнивать такой с полным нельзя.

    ГРАНИЦА ЭТОЙ ПРОВЕРКИ, названная прямо: видно ОТСУТСТВИЕ ФАЙЛА, а не
    частичный охват внутри окна. XRP листился 2018-05-04, и в окне с
    2018-03-01 первые два месяца по нему пусты — предупреждения не будет,
    потому что файл есть. Это свойство рынка, а не дефект, но проверка о нём
    НЕ ЗНАЕТ, и делать вид, что знает, нельзя."""
    return sorted(set(re.findall(r"No history for (\S+), \w+, \S+ found", out)))


RX_TAG_TOTAL = re.compile(
    u"Enter Tag\\s*\\|\\s*Entries.*?\\n.*?\\|\\s*TOTAL\\s*\\|\\s*(\\d+)\\s*\\|\\s*(-?[\\d.]+)\\s*\\|"
    u"[^\\|]*\\|[^\\|]*\\|\\s*([0-9 a-z,:]+?)\\s*\\|",
    re.S)


def _dur_min(txt):
    u"""«2 days, 05:07:00» / «21:37:00» → минуты. None — не разобрано."""
    if not txt:
        return None
    m = re.search(r"(?:(\d+)\s*days?,\s*)?(\d+):(\d+):(\d+)", txt)
    if not m:
        return None
    d = int(m.group(1) or 0)
    return d * 1440 + int(m.group(2)) * 60 + int(m.group(3)) + int(m.group(4)) / 60.0


def tag_total(out):
    u"""Строка TOTAL из ENTER TAG STATS: средняя сделка %, длительность, WR.

    Берётся ИМЕННО этот раздел, а не сводка по парам: у него один TOTAL на
    весь прогон, и его поля совпадают с общими. Раздел LEFT OPEN TRADES
    имеет собственный TOTAL с другими числами — спутать их значило бы
    отчитаться о незакрытых сделках как обо всех."""
    i = out.find("ENTER TAG STATS")
    if i < 0:
        return {}
    seg = out[i:i + 4000]
    for line in seg.splitlines():
        if "TOTAL" not in line:
            continue
        cells = [c.strip() for c in line.split(chr(9474))]
        cells = [c for c in cells if c != ""]
        if len(cells) < 6:
            continue
        try:
            return {"avg_profit_pct": float(cells[2]),
                    "avg_duration_min": _dur_min(cells[5]),
                    "win_pct": float(cells[6].split()[-1])
                    if len(cells) > 6 else None}
        except (ValueError, IndexError):
            return {}
    return {}


def _sp(path):
    u"""--strategy-path: берём стратегию ТАМ, ГДЕ ОНА ЛЕЖИТ, не копируя.
    Копирование в общую папку смешало бы репозитории и дало бы дубли имён —
    ровно то, чем корпус и болен (Schism встречается в 16 местах)."""
    return ["--strategy-path", os.path.dirname(path)] if path else []


def backtest(name, timerange, fee="0.001", path=None, want_tf=None):
    u"""⚠ СТОРОЖ ПРЕДМЕТА (20.08). Корпус считался НЕ НА ТЕХ СВЕЧАХ: в конфиге
    стоял `timeframe`, а он ПЕРЕОПРЕДЕЛЯЕТ объявленный стратегией. Пятиминутки
    шли по часовым и выдавали полноценные правдоподобные числа — 6014 сделок.
    Ключ из конфига убран, но это чинит СЛУЧАЙ. Класс чинится здесь: результат
    не принимается, пока движок своими словами не подтвердит, что считал на том
    же таймфрейме, который объявила стратегия."""
    c, out = sh([FT, "backtesting", "--config", CFG, "--strategy", name,
                 "--timerange", timerange, "--fee", fee] + _sp(path),
                timeout=1200)
    used = engine_tf(out)
    if c == 0 and want_tf and used and used != want_tf:
        return (NA, u"ПРЕДМЕТ НЕ ТОТ: стратегия объявила %s, движок считал на %s"
                % (want_tf, used), None)
    # ⚠ ПРОЖИТЫЙ ДЕФЕКТ 21.08. `ERROR - Fatal exception!` — это ЯРЛЫК, а не
    # причина: настоящая лежит ниже, в конце трассировки. Так 76 стратегий
    # (13% корпуса) получили в отчёте пустое объяснение, и я чуть не
    # опубликовал «не смогли проверить» там, где причина была МОЯ:
    # `ImportError: Short strategies cannot run in spot markets` — они
    # объявляют can_short, а корпус гнался в режиме spot.
    #
    # «Не проверено» обязано быть КАТЕГОРИЕЙ с названной причиной, иначе оно
    # неотличимо от «проверено и чисто».
    err = re.search(r"ERROR - (?:Configuration error: )?(.+)", out)
    # имя исключения может быть С ТОЧКАМИ (numpy.exceptions.DTypePromotionError) —
    # первая версия требовала \w* и потому оставляла ярлык "Fatal exception!"
    tail = re.findall(r"^([\w.]*(?:Error|Exception)): (.+)$", out, re.M)
    if tail and (not err or "Fatal exception" in err.group(1)):
        class _M(object):
            def __init__(self, t):
                self._t = t
            def group(self, _):
                return u"%s: %s" % self._t
        err = _M(tail[-1])
    if c != 0:
        why = (u"ПРЕВЫШЕНО ВРЕМЯ" if c == 124
               else (err.group(1).strip()[:160] if err else u"код %d" % c))
        return (NA, why, None)
    d = parse_summary(out)
    # ⚠ КОД 0 НЕ ЕСТЬ РЕЗУЛЬТАТ. freqtrade завершается УСПЕШНО при ошибке
    # конфигурации: ClucCrypROI печатает "Configuration error: 'stoploss' is a
    # required property" и выходит с нулём. Прежняя версия принимала это за
    # прогон и записывала словарь из одних None — карточку, которая ВЫГЛЯДИТ
    # как измерение. Это моё же запечатанное правило: наличие, нулевой код
    # и существование файла означают «НЕ ЗНАЮ», а не «да».
    #
    # Прогон засчитывается только если в сводке ЕСТЬ ЧИСЛА.
    if d.get("trades") is None:
        return (NA, (err.group(1).strip()[:160] if err
                     else u"движок вышел с кодом 0, но сводки нет "
                          u"(ни одной сделки либо вывод не разобран)"), None)
    d["used_timeframe"] = used
    d["declared_timeframe"] = want_tf
    d["missing_pairs"] = missing_pairs(out)
    d.update(tag_total(out))
    # ⚠ САМЫЙ ОСТРЫЙ ФЛАГ ИЗ СТАТЬИ СООБЩЕСТВА: сделка КОРОЧЕ СВЕЧИ, то есть
    # открылась и закрылась внутри одной свечи. В бэктесте так бывает, вживую
    # по большей части нет. В КОДЕ это невидимо — только в длительностях.
    tf_min = TF_MINUTES.get(used or want_tf)
    ad = d.get("avg_duration_min")
    # TOTAL: неизвестная свеча ⇒ поля не пишутся, и G9_candle ниже по течению
    # ВАЛИТ стратегию с неизмеренной длительностью (починено 22.08). Отсутствие
    # здесь не пропуск, а отказ — просто выносится он в другом месте.
    if tf_min and ad is not None:  # TOTAL: отсутствие ⇒ отказ на G9
        d["dur_over_candle"] = round(ad / float(tf_min), 2)
        d["intracandle"] = bool(ad < tf_min)
    return (PASS, u"", d)


def lookahead(name, timerange="20190101-20190401", path=None):
    c, out = sh([FT, "lookahead-analysis", "--config", CFG, "--strategy", name,
                 "--timerange", timerange] + _sp(path), timeout=1200)
    if c != 0:
        m = re.search(r"ERROR - (?:Configuration error: )?(.+)", out)
        return (NA, (m.group(1)[:160] if m else u"код %d" % c))
    if re.search(r"no bias detected", out):
        return (PASS, u"смещения не обнаружено")
    m = re.search(r"│\s*(Yes|No)\s*│\s*(\d+)\s*│\s*(\d+)\s*│\s*(\d+)", out)
    if m and m.group(1) == "Yes":
        return (FOUND, u"ЕСТЬ СМЕЩЕНИЕ: входов %s, выходов %s из %s сигналов"
                % (m.group(3), m.group(4), m.group(2)))
    return (NA, u"вывод не разобран")


def recursive(name, timerange="20190101-20190401", path=None):
    c, out = sh([FT, "recursive-analysis", "--config", CFG, "--strategy", name,
                 "--timerange", timerange] + _sp(path), timeout=1200)
    if "invalid startup candle count of 0" in out:
        return (FOUND, u"freqtrade ОТКАЗАЛСЯ анализировать: startup_candle_count=0, "
                       u"«приведёт к рекурсивным проблемам у части индикаторов»")
    if c != 0:
        m = re.search(r"ERROR - (?:Configuration error: )?(.+)", out)
        return (NA, (m.group(1)[:160] if m else u"код %d" % c))
    rows = re.findall(r"│\s*([a-zA-Z_0-9]+)\s*│\s*(-?[\d.]+)%", out)
    bad = [(k, v) for k, v in rows if abs(float(v)) > 0.01]
    if bad:
        return (FOUND, u"индикаторы меняются от объёма истории: " +
                u", ".join("%s %s%%" % kv for kv in bad[:5]))
    return (PASS, u"рекурсивных отклонений не найдено")


def audit_one(repo, path, name):
    r = {"repo": repo, "file": os.path.relpath(path).replace("\\", "/"),
         "strategy": name, "static": [], "runs": {}}
    src = io.open(path, encoding="utf-8", errors="replace").read()
    r["static"] = [{"level": a, "what": b, "detail": c}
                   for a, b, c in static_checks(path, src)]
    tf = declared_tf(src)
    r["declared_timeframe"] = tf
    lvl, why, s = backtest(name, IN_RANGE, path=path, want_tf=tf)
    r["runs"]["in_sample"] = {"level": lvl, "why": why, "summary": s}
    if lvl == PASS:
        lvl2, why2, s2 = backtest(name, OUT_RANGE, path=path, want_tf=tf)
        r["runs"]["out_sample"] = {"level": lvl2, "why": why2, "summary": s2}
    else:
        r["runs"]["out_sample"] = {"level": SKIP,
                                   "why": u"в выборке не отработала", "summary": None}
    lvl3, why3 = lookahead(name, path=path)
    r["runs"]["lookahead"] = {"level": lvl3, "why": why3}
    lvl4, why4 = recursive(name, path=path)
    r["runs"]["recursive"] = {"level": lvl4, "why": why4}
    r["code_md5"] = CODE_MD5      # чем посчитано — свойство карточки, не памяти
    return r


if __name__ == "__main__":
    # Прямой запуск harness.py пишет в ТУ ЖЕ папку карточек, что и corpus.py.
    # Замок общий и по имени ресурса, а не по имени скрипта — иначе «у меня
    # свой замок» вернуло бы ровно тот дефект, ради которого он заведён.
    import runlock
    if not runlock.acquire("case_study"):
        raise SystemExit(2)
    import atexit
    atexit.register(lambda: runlock.release("case_study"))
    os.makedirs(RESULTS, exist_ok=True)
    repo = sys.argv[1] if len(sys.argv) > 1 else "paulcpk/freqtrade-strategies-that-work"
    names = sys.argv[2:]
    found = find_strategies(STRAT_DIR)
    todo = [(p, n) for p, n in found if not names or n in names]
    print(u"стратегий к разбору: %d" % len(todo))
    for p, n in todo:
        out = os.path.join(RESULTS, "%s.json" % n)
        if os.path.exists(out):
            print(u"  уже есть: %s" % n)
            continue
        print(u"  разбираю %s ..." % n, flush=True)
        res = audit_one(repo, p, n)
        # ⚠ РАЗДЕЛЕНИЕ ЗНАМЕНАТЕЛЕЙ. Пять стратегий paulcpk — разбор, ВЫБРАННЫЙ
        # мной; корпус — популяция. Они лежат в одной папке карточек, и без
        # этого поля сводная статистика корпуса тихо включила бы пять отобранных
        # вручную. Признак машинный, а не «я помню, какие из них какие».
        res["source"] = "case_study"
        io.open(out, "w", encoding="utf-8").write(
            json.dumps(res, ensure_ascii=False, indent=2))
        ins = res["runs"]["in_sample"]["summary"]
        outs = res["runs"]["out_sample"]["summary"]
        print(u"    в выборке %s · вне %s · утечка: %s · рекурсия: %s"
              % (ins, outs, res["runs"]["lookahead"]["level"],
                 res["runs"]["recursive"]["level"]))
