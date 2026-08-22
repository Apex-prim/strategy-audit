# -*- coding: utf-8 -*-
u"""traps — проверки из «Backtesting Traps» сообщества freqtrade.

ИСТОЧНИК, И ОН НЕ МОЙ. На вопрос «что ещё, кроме проверок на смещение,
выдаёт подогнанную стратегию» участники freqtrade Discord дали ссылку:
https://brookmiles.github.io/freqtrade-stuff/2021/04/12/backtesting-traps/

Это знание практиков, которого нет ни в одной статистике. Здесь оно
переведено в машинные проверки — без добавлений от меня, потому что
добавления были бы моими догадками поверх их опыта.

ЧТО ПРОВЕРЯЕТСЯ (номера — по их документу):

  №5 Нереалистичный трейлинг. `trailing_stop = True` с очень тесным
     `trailing_stop_positive`: бэктест ведёт цену к максимуму свечи,
     подтягивает стоп и опускает цену — выходит «идеальная свеча»,
     продажа чуть ниже максимума почти всегда. Их красный флаг: трейлинг
     МЕНЬШЕ типичного спреда (0.1–0.5%).

  №5б `trailing_stop = True` БЕЗ `trailing_stop_positive`: стоп тянется на
     полную дистанцию `stoploss`, а не на несколько процентов.

  №6 Эксплуатация ROI. Тесный `minimal_roi` на длинном таймфрейме: цена
     вряд ли дойдёт до цели раньше стопа в реальных условиях.

  Плюс `stoploss = -0.99` — объявленный стоп, который стопом не является.

ЧЕГО ЗДЕСЬ НЕТ И ПОЧЕМУ. Их ловушки №2 (неисполненные лимитные ордера),
№3 (проскальзывание) и №4 (много сделок с малой прибылью) требуют данных о
длительности сделок и средней сделке в процентах, которых в карточках пока
нет. Врать про «проверено» нельзя: они названы здесь как НЕ ПОКРЫТЫЕ.
"""
from __future__ import print_function

import ast
import collections
import glob
import io
import json
import os
import re
import sys

_ROOT = os.environ.get("AUDIT_ROOT") or os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, _ROOT)
sys.stdout.reconfigure(encoding="utf-8", errors="replace")

SPREAD = 0.005          # их число: типичный спред 0.1–0.5%
TF_MIN = {"1m": 1, "3m": 3, "5m": 5, "15m": 15, "30m": 30, "1h": 60,
          "2h": 120, "4h": 240, "6h": 360, "8h": 480, "12h": 720,
          "1d": 1440, "3d": 4320, "1w": 10080}


def num(node):
    if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)):
        return float(node.value)
    if isinstance(node, ast.UnaryOp) and isinstance(node.op, ast.USub):
        v = num(node.operand)
        return -v if v is not None else None
    return None


def inspect(path, cls):
    src = io.open(path, encoding="utf-8", errors="replace").read()
    try:
        tree = ast.parse(src)
    except Exception:
        return None
    node = None
    for n in ast.walk(tree):
        if isinstance(n, ast.ClassDef) and n.name == cls:
            node = n
    if node is None:
        return None

    v = {"trailing_stop": None, "trailing_stop_positive": None,
         "trailing_stop_positive_offset": None, "stoploss": None,
         "timeframe": None, "roi_first": None, "roi_zero": None,
         "leverage": 1.0}
    # ПЛЕЧО. Hippocritical, freqtrade Discord 22.08: «if you have 1% trailing
    # and do 10x leverage then it essentially becomes 0.1% trailing». Это не
    # мнение — это в исходнике движка:
    #     stop_rate = open * (1 + offset - trailing_stop_positive / leverage)
    # Дистанция трейлинга ДЕЛИТСЯ на плечо, значит и сравнивать со спредом надо
    # делённую. Я читал эту строку утром и не связал.
    #
    # ⚠ ЧЕГО ЭТОТ РАЗБОР НЕ ВИДИТ: плечо из конфига, плечо из динамического
    # leverage(), плечо, зависящее от пары. Здесь берётся только буквальный
    # `return <число>` — это НИЖНЯЯ ГРАНИЦА числа таких стратегий, а не оно.
    m = re.search(r"def\s+leverage\s*\(.*?return\s+([0-9.]+)", src, re.S)
    if m:
        try:
            lv = float(m.group(1))
            if lv > 0:
                v["leverage"] = lv
        except ValueError:
            pass
    for st in node.body:
        if not isinstance(st, ast.Assign) or not st.targets:
            continue
        t = st.targets[0]
        name = getattr(t, "id", None)
        if name not in v and name != "minimal_roi":
            continue
        if name == "minimal_roi" and isinstance(st.value, ast.Dict):
            pairs = []
            for k, val in zip(st.value.keys, st.value.values):
                kk = k.value if isinstance(k, ast.Constant) else None
                vv = num(val)
                if kk is not None and vv is not None:
                    try:
                        pairs.append((int(str(kk)), vv))
                    except ValueError:
                        pass
            if pairs:
                pairs.sort()
                v["roi_zero"] = pairs[0][1]
                v["roi_first"] = pairs[0][1]
            continue
        if isinstance(st.value, ast.Constant) and isinstance(st.value.value, bool):
            v[name] = st.value.value
        elif isinstance(st.value, ast.Constant) and isinstance(st.value.value, str):
            v[name] = st.value.value
        else:
            v[name] = num(st.value)
    return v


def flags(v, notes=None):
    u"""Дисквалифицирующие ловушки. `notes` — список для наблюдений,
    которые ловушками НЕ являются (см. 22.08 про широкий трейлинг)."""
    out = []
    if notes is None:
        notes = []
    if not v:
        return out
    tf = v.get("timeframe")
    mins = TF_MIN.get(tf)
    tsp = v.get("trailing_stop_positive")
    if v.get("trailing_stop") is True:
        if tsp is None:
            # ⚠ БОЛЬШЕ НЕ ЛОВУШКА, 22.08. Hippocritical (freqtrade Discord):
            # «if you have loose trailing you wont have a trap; if you have
            # things like 0.1% trailing then not». Он прав: широкий трейлинг
            # (на полном расстоянии стопа) ИСПОЛНИМ в реальности — он далеко от
            # спреда и наливается надёжно. Ловушкой делает ТЕСНОТА, а не сам
            # трейлинг. Это наблюдение, а не дисквалификация.
            #
            # Проверено перед изменением: на корпусе 895 ни один вердикт от
            # этого флага не зависел — из девяти выбитых на G8 ноль выбиты им
            # одним. Правило меняется по существу, а не под результат.
            notes.append((u"loose trailing (no trailing_stop_positive)",
                          u"stop trails at the full stoploss distance (%s). Wide, "
                          u"but executable — a note, not a trap"
                          % (v.get("stoploss"),)))
        else:
            lv = v.get("leverage") or 1.0
            eff = tsp / lv if lv > 0 else tsp
            if eff < SPREAD:
                out.append((u"trailing tighter than the spread",
                            u"trailing_stop_positive = %.4f at %.0fx leverage = "
                            u"%.5f effective, below the 0.1–0.5%% spread the trap "
                            u"article names" % (tsp, lv, eff)))
    if tsp is not None and v.get("trailing_stop") is not True:
        out.append((u"inert trailing setting",
                    u"trailing_stop_positive = %s while trailing_stop is not True" % tsp))
    sl = v.get("stoploss")
    if sl is not None and sl <= -0.9:
        out.append((u"stoploss is not a stop",
                    u"stoploss = %s — losers are effectively never cut" % sl))
    roi = v.get("roi_zero")
    if roi is not None and mins and mins >= 60 and roi <= 0.01:
        out.append((u"tight ROI on a long timeframe",
                    u"first minimal_roi entry %.4f on %s candles" % (roi, tf)))
    return out


def main():
    from harness import find_strategies
    where = {}
    for d in sorted(os.listdir(os.path.join(_ROOT, "repos"))):
        p = os.path.join(_ROOT, "repos", d)
        if os.path.isdir(p):
            for f, n in sorted(find_strategies(p)):
                where.setdefault(n, f)

    survivors, allrows = set(), []
    for f in glob.glob(os.path.join(_ROOT, "results", "*.json")):
        r = json.load(io.open(f, encoding="utf-8"))
        if r.get("source") != "corpus":
            continue
        a = r["runs"]["in_sample"].get("summary")
        b = r["runs"]["out_sample"].get("summary")
        allrows.append(r["strategy"])
        if not isinstance(a, dict) or (a.get("trades") or 0) < 30:
            continue
        if not isinstance(b, dict) or b.get("expectancy") is None:
            continue
        if (a.get("expectancy") or 0) <= 0 or (a.get("p_value") or 1) >= 0.05:
            continue
        if b["expectancy"] <= 0 or (b.get("p_value") or 1) >= 0.05:
            continue
        survivors.add(r["strategy"])

    tally = collections.Counter()
    flagged_all, flagged_surv = set(), set()
    for name in allrows:
        p = where.get(name)
        if not p:
            continue
        fl = flags(inspect(p, name))
        for lab, _d in fl:
            tally[lab] += 1
        if fl:
            flagged_all.add(name)
            if name in survivors:
                flagged_surv.add(name)

    print(u"BACKTESTING TRAPS (источник — сообщество freqtrade, не я)")
    print(u"проверено стратегий: %d · прошедших воронку: %d"
          % (len(allrows), len(survivors)))
    print()
    for lab, c in tally.most_common():
        print(u"   %-42s %4d" % (lab, c))
    print()
    print(u"помечено ХОТЯ БЫ ОДНОЙ ловушкой: %d из %d (%.0f%%)"
          % (len(flagged_all), len(allrows), 100.0 * len(flagged_all) / max(len(allrows), 1)))
    print(u"среди ПРОШЕДШИХ ВОРОНКУ:         %d из %d (%.0f%%)"
          % (len(flagged_surv), len(survivors),
             100.0 * len(flagged_surv) / max(len(survivors), 1)))
    print()
    print(u"НЕ ПОКРЫТО (нужны длительность сделок и средняя сделка в %%):")
    print(u"   их №2 неисполненные лимитные ордера")
    print(u"   их №3 проскальзывание")
    print(u"   их №4 много сделок с прибылью ниже 0.5%%")
    print(u"   их красный флаг: средняя длительность КОРОЧЕ свечи")


if __name__ == "__main__":
    main()
