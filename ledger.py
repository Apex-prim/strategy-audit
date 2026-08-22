# -*- coding: utf-8 -*-
u"""ledger — ОДНА СТРОКА НА СТРАТЕГИЮ, из которой восстановим весь путь.

ЗАЧЕМ. До сих пор итоговые числа («55 прошли», «0 обыграли рынок») жили в
прозе README и в выводе funnel.py. Их нельзя было ни пересчитать из одного
места, ни привязать к версии кода. 21.08 это дало дефект прямо на глазах:
внешний рецензент похвалил два файла, которые давно выброшены, потому что
опубликованные числа выглядели авторитетно и НЕ НЕСЛИ провенанса.

ЧТО ЗДЕСЬ. У каждого числа четыре координаты, и они печатаются вместе с ним:

    ЧТО считалось · КАКИМ кодом (code_md5) · НА КАКОМ корпусе (plan_md5)
                  · ПРИ КАКОМ наборе решений (эпоха)

ЭПОХИ — не украшение. Порядок «правило → данные» или «данные → правило»
меняет доказательную силу вывода, и он ПРОВЕРЕН ПО ГИТУ, не по памяти:

  E0  ОБЪЯВЛЕНО ДО ПРОГОНА
      ступени ①–⑦ (сделки ≥30, ожидание>0 и p<0.05 в окне автора и вне его).
      CHECKLIST.md 20.08 15:00 называет ОБА прибора — lookahead-analysis и
      recursive-analysis — до начала свипа (git: 4d5a937).

  E1  ПОСЛЕ ДАННЫХ, ВЫЗВАНО РЕЗУЛЬТАТОМ  ← настоящая утечка
      Оба прибора МЕРИЛИСЬ с первого коммита харнесса (be77d12, 20.08 14:42),
      но какой из них ИСКЛЮЧАЕТ — объявлено не было. Опубликованная воронка
      (fff3d17, 21.08 10:56) исключала ТОЛЬКО по заглядыванию. Исключение по
      рекурсии добавлено ПОСЛЕ того, как я увидел, что стратегии, обыгравшие
      рынок вне выборки, — NOTankAi_15 (+63 645 298%) и NowoIchimoku1hV2.
      ⚠ Поправка к моей же записи 21.08 22:41: я написал «второй детектор
      введён после данных». По гиту это НЕВЕРНО — введён был не прибор, а
      РЕШЕНИЕ, какой из объявленных приборов считается исключающим.
      Недоопределённость пререгистрации, разрешённая после результата.

  E2  ПОСЛЕ ДАННЫХ, ИСТОЧНИК ВНЕШНИЙ (не вызвано нашим результатом)
      ловушки бэктеста из документации сообщества freqtrade (traps.py).

  E3  ПОСЛЕ ДАННЫХ, ИСТОЧНИК ВНЕШНИЙ
      сделка короче собственной свечи (dur_over_candle < 1).

  E4  ПОСЛЕ ДАННЫХ, ВЫЗВАНО ВНЕШНИМ РАЗБОРОМ
      поправка на множественность (Бенджамини–Хохберг).

Различие E1 и E2/E3 существенно и его НЕЛЬЗЯ схлопывать: E1 — правило,
выбранное потому, что не понравился результат; E2/E3 — правило, пришедшее
из чужого документа, безразличного к нашему результату. Оба — степени
свободы исследователя, и оба помечены. Но виноваты они по-разному.

ЗАПУСК:  python ledger.py            печать сводки
         python ledger.py --csv      + LEDGER.csv рядом с карточками
         python ledger.py --publish  + repo/LEDGER.csv, repo/LEDGER.md и
                                     перезапись блока чисел в repo/README.md
         python ledger.py --verify   сверить блок README с пересчётом,
                                     код возврата 1 при расхождении

ПОЧЕМУ --publish И --verify. Числа в README раньше набирались руками и
устаревали молча: 21.08 опубликованный блок говорил «571 стратегия, 55
чистых», когда корпус был 900. Внешний читатель верит опубликованному, а не
коду. Поэтому блок между маркерами `<!-- LEDGER:BEGIN -->` и
`<!-- LEDGER:END -->` МАШИННЫЙ. Правило без кода возврата не действует.
"""
from __future__ import print_function

import collections
import csv
import glob
import io
import json
import os
import sys
import warnings

# Чужие стратегии содержат неверные escape-последовательности; ast поднимает
# SyntaxWarning про ЧУЖОЙ файл. Глушим только это.
warnings.filterwarnings("ignore", category=SyntaxWarning)

_ROOT = os.environ.get("AUDIT_ROOT") or os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, _ROOT)
sys.stdout.reconfigure(encoding="utf-8", errors="replace")

import traps as traps_mod
from harness import find_strategies
from ledger_block import (ALPHA, EPOCHS, GATE_EPOCH, LADDER, bh, bh_population,
                          build, claims, survivors_at)

FOUND = u"НАЙДЕНО"
BEGIN = u"<!-- LEDGER:BEGIN -->"
END = u"<!-- LEDGER:END -->"

CSV_COLS = ["strategy", "repo", "file", "population", "code_md5", "plan_md5",
            "is_trades", "is_exp", "is_p", "is_market",
            "os_trades", "os_exp", "os_p", "os_total", "os_market",
            "os_avg_pct", "os_ci_low",
            "beats_bh", "lookahead", "recursive", "recursive_kind",
            "traps_n", "traps",
            "dur_over_candle", "dropped_at", "survives_through"]


def where_map():
    w = {}
    root = os.path.join(_ROOT, "repos")
    if not os.path.isdir(root):
        return w
    for d in sorted(os.listdir(root)):
        p = os.path.join(root, d)
        if os.path.isdir(p):
            for f, n in sorted(find_strategies(p)):
                w.setdefault(n, f)
    return w


def load(population="corpus"):
    rows = []
    for fp in sorted(glob.glob(os.path.join(_ROOT, "results", "*.json"))):
        try:
            r = json.load(io.open(fp, encoding="utf-8"))
        except Exception:
            continue
        if r.get("source") != population:
            continue
        rows.append(r)
    return rows



def ci_low(mean_pct, p_value, n):
    u"""Нижняя граница 95% интервала средней сделки, в процентах.

    Восстанавливается из того, что печатает freqtrade: среднее, p-значение и
    число сделок. z берётся из p (двусторонний), стандартная ошибка = |m| / z,
    граница = m - 1.96*se. Нормальное приближение допустимо: у выживших от 304
    до 2688 сделок.

    ⚠ ЗАЧЕМ (E6, 22.08). Лестница требовала ЗНАЧИМОСТИ и не требовала
    ВЕЛИЧИНЫ. p = 1e-8 при микроскопическом эффекте бесполезнее, чем p = 0.003
    при устойчивом. Возражение внешнее, дыра наша.
    """
    from statistics import NormalDist
    if mean_pct is None or p_value is None or not n:
        return None
    pv = min(max(float(p_value), 1e-300), 0.999999)
    try:
        z = NormalDist().inv_cdf(1.0 - pv / 2.0)
    except Exception:
        return None
    z = min(max(z, 1e-6), 40.0)
    se = abs(mean_pct) / z
    return mean_pct - 1.96 * se


EXTRA_COST_PCT = 0.20   # удвоение издержки 0.1%->0.2% за сторону = 0.20 пп/сделку


def recursive_kind(node):
    u"""РАЗДЕЛИТЬ ДВЕ РАЗНЫЕ ВЕЩИ ПОД ОДНИМ ЯРЛЫКОМ.

    `recursive-analysis` даёт «НАЙДЕНО» в двух несравнимых случаях:
      · ОТКАЗ  — startup_candle_count=0, движок вообще не стал считать. Это
                 проверка ОБЪЯВЛЕНИЯ: автор не сказал, сколько ему нужно
                 прогрева. Дефект реальный, но НИЧЕГО не измерено.
      · ДРЕЙФ  — движок посчитал и увидел, что значения индикаторов зависят
                 от объёма поданной истории. Это ИЗМЕРЕНИЕ.

    Смешивать их — значит выдавать проверку объявления за измерение. Ступень
    G7 остаётся одна (обе причины дисквалифицируют), но в реестре стоит вид,
    и доля каждого вида печатается. Иначе фраза «26 стратегий выбиты
    рекурсией» читается как найденный дрейф, а может оказаться формальностью.
    """
    if not isinstance(node, dict):
        return u""
    if node.get("level") != FOUND:
        return u""
    why = node.get("why") or u""
    if u"ОТКАЗАЛСЯ" in why or u"startup_candle_count" in why:
        return u"refused_no_warmup"
    if u"меняются" in why or u"%" in why:
        return u"drift_measured"
    return u"other"


def beats_precomputed(b):
    if b.get("total_pct") is None or b.get("market_change_pct") is None:
        return None
    return b["total_pct"] > b["market_change_pct"]


def row_of(r, where):
    u"""Одна строка реестра. G10 (поправка на множественность) заполняется
    вторым проходом: порог считается по всей популяции, а не по строке."""
    a = r["runs"]["in_sample"].get("summary")
    b = r["runs"]["out_sample"].get("summary")
    a = a if isinstance(a, dict) else {}
    b = b if isinstance(b, dict) else {}
    p = where.get(r["strategy"])
    tr = traps_mod.flags(traps_mod.inspect(p, r["strategy"])) if p else []

    g = collections.OrderedDict()
    g["G0_measured"] = bool(a.get("trades") is not None and b.get("trades") is not None)
    g["G1_trades"] = (a.get("trades") or 0) >= 30
    g["G2_is_pos"] = (a.get("expectancy") or 0) > 0
    g["G3_is_sig"] = (a.get("p_value") if a.get("p_value") is not None else 1) < ALPHA
    g["G4_os_pos"] = (b.get("expectancy") or 0) > 0
    g["G5_os_sig"] = (b.get("p_value") if b.get("p_value") is not None else 1) < ALPHA
    g["G6_lookahead"] = r["runs"]["lookahead"]["level"] != FOUND
    g["G7_recursive"] = r["runs"]["recursive"]["level"] != FOUND
    g["G8_traps"] = len(tr) == 0
    # ⚠ ОТСУТСТВИЕ ПОЛЯ — НЕ «ПРОШЛА». Карточки, посчитанные до появления слоя
    # длительности, поля не содержат, и `not card.get("intracandle")` молча
    # читалось как «прошла». Наличие ≠ содержание — ступень требует ИЗМЕРЕНИЯ.
    g["G9_candle"] = (b.get("dur_over_candle") is not None
                      and not bool(b.get("intracandle")))
    g["G10_fdr"] = None                       # второй проход
    lo = ci_low(b.get("avg_profit_pct"), b.get("p_value"), b.get("trades"))
    g["G11_effect"] = bool(lo is not None and (lo - EXTRA_COST_PCT) > 0)
    g["G12_economic"] = bool(beats_precomputed(b))

    lo_ci = ci_low(b.get("avg_profit_pct"), b.get("p_value"), b.get("trades"))
    beats = None
    if b.get("total_pct") is not None and b.get("market_change_pct") is not None:
        beats = b["total_pct"] > b["market_change_pct"]

    return {
        "strategy": r["strategy"], "repo": r.get("repo", ""),
        "file": r.get("file", ""), "population": r.get("source", ""),
        "code_md5": r.get("code_md5", ""), "plan_md5": r.get("plan_md5", ""),
        "is_trades": a.get("trades"), "is_exp": a.get("expectancy"),
        "is_p": a.get("p_value"), "is_market": a.get("market_change_pct"),
        "os_trades": b.get("trades"), "os_exp": b.get("expectancy"),
        "os_p": b.get("p_value"), "os_total": b.get("total_pct"),
        "os_avg_pct": b.get("avg_profit_pct"),
        "os_ci_low": (None if lo_ci is None else round(lo_ci, 4)),
        "os_market": b.get("market_change_pct"), "beats_bh": beats,
        "lookahead": r["runs"]["lookahead"]["level"],
        "recursive": r["runs"]["recursive"]["level"],
        "recursive_kind": recursive_kind(r["runs"]["recursive"]),
        "traps_n": len(tr), "traps": u"; ".join(t[0] for t in tr),
        "dur_over_candle": b.get("dur_over_candle"),
        "gates": g, "dropped_at": "", "survives_through": "",
    }


def finalize(rows):
    u"""Второй проход: порог BH по всей популяции, затем ступень отсева."""
    p_out = bh_population(rows)
    thr, k = bh(p_out)
    for r in rows:
        op = r.get("os_p")
        r["gates"]["G10_fdr"] = bool(k and op is not None and op <= thr)
        dropped = ""
        for kname, _e, _d in LADDER:
            if not r["gates"][kname]:
                dropped = kname
                break
        r["dropped_at"] = dropped
        r["survives_through"] = u"все" if not dropped else GATE_EPOCH[dropped]
    return (thr if k else None), len(p_out), k


def n_repos():
    u"""Одна реализация на два места — в ledger_block. Своя копия здесь уже
    разошлась с истиной и напечатала 3 вместо 53."""
    from ledger_block import n_repos as _n
    return _n(os.path.join(_ROOT, "corpus_sources.json"))


def write_csv(rows, out):
    with io.open(out, "w", encoding="utf-8", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=CSV_COLS, extrasaction="ignore")
        w.writeheader()
        for r in sorted(rows, key=lambda x: x["strategy"].lower()):
            w.writerow(r)


def rewrite_readme(text, blk):
    if BEGIN not in text or END not in text:
        return None
    head = text.split(BEGIN)[0]
    tail = text.split(END, 1)[1]
    return head + BEGIN + u"\n" + blk + u"\n" + END + tail


def ledger_md(rows, blk):
    u"""LEDGER.md — публичное объяснение того, что означают эти числа."""
    surv = survivors_at(rows, "E4")
    L = [
        u"# The ledger",
        u"",
        u"One row per strategy, in [LEDGER.csv](LEDGER.csv). Every count this",
        u"repository publishes is derived from that file, and that file is",
        u"produced by `ledger.py` from the result cards — not typed by hand.",
        u"",
        u"## Why this file exists",
        u"",
        u"On 2026-08-21 an external reviewer read this repository and praised two",
        u"scripts as a strength. Both had been discarded days earlier, and the",
        u"published counts they supported came from a 571-strategy corpus that had",
        u"since grown past 900. Nothing in the repository was lying. The reviewer",
        u"simply had no way to tell which artifacts still stood behind which",
        u"numbers.",
        u"",
        u"So each number now carries four coordinates: **what** was measured, **by",
        u"which code**, **over which corpus**, and **under which set of decisions**.",
        u"The last one is the one usually left out.",
        u"",
        u"## Decision epochs",
        u"",
        u"A rule chosen before the data and a rule chosen after it do not carry the",
        u"same weight, so they are labelled and never merged. The dates come from",
        u"git, not from memory.",
        u"",
        u"| epoch | when the rule was fixed | rules |",
        u"|---|---|---|",
        u"| E0 | **before the sweep** — CHECKLIST.md, 2026-08-20 15:00 (`4d5a937`)"
        u" | trade count, expectancy and p-value in both windows; look-ahead |",
        u"| E1 | **after the results, because of them** | `recursive-analysis`"
        u" promoted from *reported* to *excluding* |",
        u"| E2 | after, from an outside source | the freqtrade community's"
        u" backtesting traps |",
        u"| E3 | after, from an outside source | trades shorter than their own"
        u" candle |",
        u"| E4 | after, prompted by an external review | Benjamini-Hochberg FDR |",
        u"",
        u"**E1 is the one to be suspicious of, and it is mine.** Both bias",
        u"detectors ran on every strategy from the first commit of the harness",
        u"(`be77d12`, 2026-08-20 14:42), and both were named in the checklist",
        u"published before the sweep. What was *not* fixed in advance was which of",
        u"them excludes a strategy from the headline. The published funnel",
        u"(`fff3d17`) excluded on look-ahead only. Exclusion on recursion was added",
        u"after I saw that the strategies beating buy-and-hold out of sample were",
        u"`NOTankAi_15` at +63,645,298% and `NowoIchimoku1hV2`.",
        u"",
        u"That is not a detector invented to kill an inconvenient result — the",
        u"detector predates the result by a day. It is a **degree of freedom left",
        u"open in the pre-registration and closed after seeing the data**, which is",
        u"a smaller sin and still a real one. Both counts are published below, in",
        u"the order the decisions were made. E2 and E3 are post-data too, but they",
        u"came from documents indifferent to our result; a weaker objection, and",
        u"still marked.",
        u"",
        u"## The numbers",
        u"",
        blk,
        u"",
        u"## Reading the ladder",
        u"",
        u"Each line is the same population passing one more gate. `G0_measured` is",
        u"not a quality filter — it counts the strategies that produced numbers in",
        u"both windows at all. The largest single drop is not any bias detector: it",
        u"is `G2_is_pos`, strategies whose expectancy is negative in the window",
        u"their own author chose.",
        u"",
        u"`G9_candle` **fails a strategy whose trade duration was never measured**",
        u"rather than passing it. Cards computed before the duration layer existed",
        u"carry no such field, and `not card.get(\"intracandle\")` would have quietly",
        u"read as *passed*. Absence of a flag is not absence of the defect.",
        u"",
        u"## What a row does not tell you",
        u"",
        u"That a strategy survives every gate is not a claim that it makes money.",
        u"It is a claim that this pipeline could not show that it does not. The last",
        u"column of the epoch table — how many survivors beat buy-and-hold on the",
        u"same pairs over the same window — is the one that matters, and the one",
        u"nearly every published backtest omits.",
        u"",
        u"Survivors under the full rule set: **%d**." % len(surv),
        u"",
    ]
    return u"\n".join(L) + u"\n"


def arg_population():
    u"""Популяции НИКОГДА не смешиваются в одном знаменателе: пять стратегий,
    выбранных мной вручную, не имеют права попасть в знаменатель корпуса."""
    for a in sys.argv[1:]:
        if a.startswith("--pop="):
            return a.split("=", 1)[1]
    return "corpus"


def main():
    where = where_map()
    pop = arg_population()
    rows_raw = load(pop)
    if not rows_raw:
        print(u"популяция %r пуста — считать нечего" % pop)
        return 1
    rows = [row_of(r, where) for r in rows_raw]
    thr, n_bh, k_bh = finalize(rows)

    code = collections.Counter(x["code_md5"] for x in rows)
    plan = collections.Counter(x["plan_md5"] for x in rows)
    homogeneous = len(code) <= 1 and len(plan) <= 1

    print(u"РЕЕСТР — по одной строке на стратегию")
    print(u"=" * 68)
    print(u"ПОПУЛЯЦИЯ: %s (смешивать популяции запрещено)" % pop)
    print(u"КОДОМ:  %s" % u", ".join(u"%s x%d" % (c or u"-", n)
                                     for c, n in code.most_common(3)))
    print(u"КОРПУС: %s" % u", ".join(u"%s x%d" % (c or u"-", n)
                                     for c, n in plan.most_common(3)))
    print(u"СТРОК:  %d   репозиториев: %d" % (len(rows), n_repos()))
    print(u"BH:     порог %s по %d проверкам, отвергнуто %d"
          % ((u"%.3e" % thr) if thr else u"нет", n_bh, k_bh))
    nodur = sum(1 for x in rows
                if x["gates"]["G0_measured"] and x["dur_over_candle"] is None)
    print(u"БЕЗ ⑨:  %d строк посчитаны до появления слоя длительности" % nodur)
    if not homogeneous:
        print(u"⚠ строки посчитаны РАЗНЫМИ версиями кода/плана — реестр")
        print(u"  неоднороден; публиковать итог нельзя до пересчёта")
    print()

    print(u"ЛЕСТНИЦА — где именно сходит корпус")
    print(u"-" * 68)
    alive = rows
    for kname, ep, desc in LADDER:
        p = [r for r in alive if r["gates"][kname]]
        print(u"  %-13s %s  %-44s %4d -> %4d" % (kname, ep, desc, len(alive), len(p)))
        alive = p
    print()

    g7 = [r for r in rows if r["dropped_at"] == "G7_recursive"]
    if g7:
        kinds = collections.Counter(r["recursive_kind"] for r in g7)
        print(u"ЧЕМ ИМЕННО ВЫБИТЫ НА G7 (эпоха E1) — %d стратегий" % len(g7))
        print(u"-" * 68)
        for k, n in kinds.most_common():
            what = {u"refused_no_warmup":
                    u"движок ОТКАЗАЛСЯ считать: прогрев не объявлен (проверка "
                    u"ОБЪЯВЛЕНИЯ, ничего не измерено)",
                    u"drift_measured":
                    u"дрейф индикаторов ИЗМЕРЕН"}.get(k, k or u"без причины")
            print(u"  %4d  %s" % (n, what))
        print()

    print(u"ВЫЖИВШИЕ ПО ЭПОХАМ — одно число на каждый набор решений")
    print(u"-" * 68)
    for ep in EPOCHS:
        s = survivors_at(rows, ep)
        beat = [r for r in s if r["beats_bh"]]
        print(u"  до %s включительно:  выживших %4d   обыграли рынок %3d"
              % (ep, len(s), len(beat)))
        if beat and len(beat) <= 5:
            for r in beat:
                print(u"        %-30s вне выборки %+.1f%% против рынка %+.1f%%"
                      % (r["strategy"][:30], r["os_total"] or 0,
                         r["os_market"] or 0))
    print()
    print(u"ЧИТАТЬ ТАК: разница между строками — это НЕ разные измерения, а")
    print(u"одно измерение при разных наборах решений. E0 объявлено до данных;")
    print(u"E1 выбрано ПОСЛЕ и ИЗ-ЗА результата; E2-E4 пришли извне после.")

    blk = build(rows, n_repos())
    repo_dir = os.path.join(_ROOT, "repo")

    if "--csv" in sys.argv:
        out = os.path.join(_ROOT, "LEDGER.csv")
        write_csv(rows, out)
        print(u"\nзаписан %s (%d строк)" % (out, len(rows)))

    if "--publish" in sys.argv:
        if pop != "corpus":
            print(u"\nОТКАЗ ПУБЛИКОВАТЬ: в README идут числа КОРПУСА, а не")
            print(u"популяции %r. Пять ручных разборов — не популяция." % pop)
            return 1
        if not homogeneous:
            print(u"\nОТКАЗ ПУБЛИКОВАТЬ: реестр неоднороден по коду или корпусу.")
            print(u"Сначала пересчитайте всё одной версией харнесса.")
            return 1
        write_csv(rows, os.path.join(repo_dir, "LEDGER.csv"))
        # класс каждого утверждения — машинно, файлом, а не абзацем
        with io.open(os.path.join(repo_dir, "CLAIMS.csv"), "w",
                     encoding="utf-8", newline="") as fh:
            w = csv.writer(fh)
            w.writerow(["claim", "value", "class", "epochs_required", "source"])
            for row in claims(rows, n_repos()):
                w.writerow(row)
        print(u"записан CLAIMS.csv — класс каждого числа")
        io.open(os.path.join(repo_dir, "LEDGER.md"), "w",
                encoding="utf-8").write(ledger_md(rows, blk))
        rp = os.path.join(repo_dir, "README.md")
        new = rewrite_readme(io.open(rp, encoding="utf-8").read(), blk)
        if new is None:
            print(u"\n⚠ в README нет маркеров реестра — блок НЕ вставлен")
            return 1
        io.open(rp, "w", encoding="utf-8").write(new)
        print(u"\nопубликовано: LEDGER.csv, LEDGER.md, блок чисел в README")

    if "--verify" in sys.argv:
        rp = os.path.join(repo_dir, "README.md")
        txt = io.open(rp, encoding="utf-8").read()
        if BEGIN not in txt or END not in txt:
            print(u"\nОТКАЗ: в README нет маркеров реестра")
            return 1
        have = txt.split(BEGIN, 1)[1].split(END, 1)[0].strip()
        if have != blk.strip():
            print(u"\nРАСХОЖДЕНИЕ: числа в README не совпадают с пересчётом")
            hl, wl = have.splitlines(), blk.strip().splitlines()
            for i in range(max(len(hl), len(wl))):
                a = hl[i] if i < len(hl) else u"(нет строки)"
                b = wl[i] if i < len(wl) else u"(нет строки)"
                if a != b:
                    print(u"  README: %s" % a)
                    print(u"  реестр: %s" % b)
            return 1
        print(u"\nчисла в README совпадают с реестром")
    return 0


if __name__ == "__main__":
    sys.exit(main() or 0)
