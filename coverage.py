# -*- coding: utf-8 -*-
u"""coverage — сколько ОКНА реально покрывает каждая пара.

ЗАЧЕМ. Я писал «8 пар к USDT», и это читается как «восемь пар всё окно».
Измерение говорит иначе: DASH листился 2019-03-28 (46% окна автора), XMR
делистнут с Binance 2024-02-20 (61% окна вне выборки). Полностью окно автора
покрывают ТРИ пары из восьми.

Это не портит числа: торговать несуществующей парой нельзя, и движок честно
её не торгует. Но состав корзины МЕНЯЕТСЯ по ходу окна, а читатель об этом не
знает. `missing_pairs` в карточке такого не видит — там проверяется отсутствие
ФАЙЛА, а файл есть, просто короткий.

Граница названа прямо: считается покрытие по КРАЯМ ряда внутри окна, а не
поиск дыр внутри. Дырявый ряд с верными краями покажет 100%.
"""
from __future__ import print_function

import glob
import os
import sys

_ROOT = os.environ.get("AUDIT_ROOT") or os.path.dirname(os.path.abspath(__file__))
try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass
import pandas as pd

WINDOWS = ((u"окно автора", "2018-03-01", "2020-03-01"),
           (u"вне выборки", "2020-03-01", "2026-08-20"))


def cov(dt, lo, hi):
    lo, hi = pd.Timestamp(lo, tz="UTC"), pd.Timestamp(hi, tz="UTC")
    s = dt[(dt >= lo) & (dt <= hi)]
    if len(s) == 0:
        return 0.0
    return 100.0 * (s.iloc[-1] - s.iloc[0]).total_seconds() / (hi - lo).total_seconds()


def main():
    tf = sys.argv[1] if len(sys.argv) > 1 else "1h"
    files = sorted(glob.glob(os.path.join(_ROOT, "user_data", "data", "binance",
                                          "*-%s.feather" % tf)))
    if not files:
        print(u"нет данных для %s" % tf)
        return
    print(u"ПОКРЫТИЕ ОКОН, таймфрейм %s" % tf)
    print(u"%-12s %-12s %-12s %12s %12s" % (u"пара", u"первая", u"последняя",
                                            WINDOWS[0][0], WINDOWS[1][0]))
    full = 0
    for f in files:
        d = pd.read_feather(f)
        dt = d["date"]
        c = [cov(dt, w[1], w[2]) for w in WINDOWS]
        if c[0] > 99.0:
            full += 1
        print(u"%-12s %-12s %-12s %11.1f%% %11.1f%%"
              % (os.path.basename(f).split("-")[0], str(dt.iloc[0])[:10],
                 str(dt.iloc[-1])[:10], c[0], c[1]))
    print()
    print(u"Окно автора покрывают полностью %d пары из %d." % (full, len(files)))
    print(u"«8 пар» — это список запроса, а не то, что торговалось всё окно.")


if __name__ == "__main__":
    main()
