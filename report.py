# -*- coding: utf-8 -*-
u"""report — превращает результаты прогонов в карточки и сводный указатель.

Мера — ОЖИДАНИЕ НА СДЕЛКУ (expectancy), а не «Total profit %».
Причина названа в первом же разборе: итоговый процент зависит от
`max_open_trades`, `stake_amount` и `dry_run_wallet`, то есть от
конфигурации, а не от стратегии. Ожидание на сделку от них не зависит и
потому сравнимо между стратегиями и между окнами.
"""
from __future__ import print_function

import io
import json
import os
import sys

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

ROOT = "C:/tmp/audit"
RESULTS = os.path.join(ROOT, "results")
OUT = os.path.join(ROOT, "repo", "results")

MARK = {u"ПРОШЛА": u"✅", u"НАЙДЕНО": u"⚠", u"НЕ ПРИМЕНИМА": u"·",
        u"НЕ ЗАПУСКАЛИ": u"·"}


def survives(a, b):
    if a is None or b is None:
        return None
    if b < 0:
        return u"отрицательное"
    if a <= 0:
        return u"н/п"
    return u"%.0f%%" % (100.0 * b / a)


def card(r):
    L = []
    s = r["strategy"]
    L.append(u"# %s" % s)
    L.append(u"")
    L.append(u"Источник: [`%s`](https://github.com/%s) · файл `%s`"
             % (r["repo"], r["repo"], os.path.basename(r["file"])))
    L.append(u"")

    ins = r["runs"]["in_sample"]
    out = r["runs"]["out_sample"]
    L.append(u"## Результат")
    L.append(u"")
    if ins["level"] == u"ПРОШЛА" and ins["summary"]:
        n1, p1, e1, w1 = ins["summary"]
        L.append(u"```")
        L.append(u"                  сделок   итог %    ожидание на сделку")
        L.append(u"в выборке автора  %6s   %7s   %s" % (n1, p1, e1))
        if out["level"] == u"ПРОШЛА" and out["summary"]:
            n2, p2, e2, w2 = out["summary"]
            L.append(u"ВНЕ выборки       %6s   %7s   %s" % (n2, p2, e2))
            L.append(u"")
            L.append(u"осталось от ожидания: %s" % survives(e1, e2))
        else:
            L.append(u"ВНЕ выборки       %s — %s" % (out["level"], out["why"]))
        L.append(u"```")
    else:
        L.append(u"**%s** — %s" % (ins["level"], ins["why"]))
    L.append(u"")

    L.append(u"## Проверки")
    L.append(u"")
    L.append(u"| проверка | итог | подробности |")
    L.append(u"|---|---|---|")
    la = r["runs"]["lookahead"]
    rc = r["runs"]["recursive"]
    L.append(u"| заглядывание в будущее (родной детектор freqtrade) | %s %s | %s |"
             % (MARK.get(la["level"], u"·"), la["level"], la["why"]))
    L.append(u"| рекурсия индикаторов (родной детектор freqtrade) | %s %s | %s |"
             % (MARK.get(rc["level"], u"·"), rc["level"], rc["why"]))
    for c in r["static"]:
        L.append(u"| %s | %s %s | %s |"
                 % (c["what"], MARK.get(c["level"], u"·"), c["level"], c["detail"]))
    L.append(u"")
    L.append(u"---")
    L.append(u"")
    L.append(u"*Прогон настоящим freqtrade, комиссия 0.1% за сторону, 8 пар к USDT, "
             u"1h. Окно автора 2018-03-01…2020-03-01, вне выборки "
             u"2020-03-01…2026-08-20. «Не смогли проверить» нигде не "
             u"печатается как «чисто».*")
    return u"\n".join(L)


def index(rows):
    L = [u"# Указатель разборов", u"",
         u"Мера — **ожидание на сделку**, а не итоговый процент: итог зависит "
         u"от `max_open_trades` и размера ставки, то есть от конфигурации, а "
         u"не от стратегии.", u"",
         u"| стратегия | источник | в выборке | вне выборки | осталось | утечка | рекурсия |",
         u"|---|---|---|---|---|---|---|"]
    for r in rows:
        ins = r["runs"]["in_sample"]; out = r["runs"]["out_sample"]
        e1 = ins["summary"][2] if ins["summary"] else None
        e2 = out["summary"][2] if out["summary"] else None
        L.append(u"| [%s](%s.md) | `%s` | %s | %s | **%s** | %s | %s |"
                 % (r["strategy"], r["strategy"], r["repo"].split("/")[0],
                    e1 if e1 is not None else u"—",
                    e2 if e2 is not None else u"—",
                    survives(e1, e2) or u"—",
                    MARK.get(r["runs"]["lookahead"]["level"], u"·"),
                    MARK.get(r["runs"]["recursive"]["level"], u"·")))
    L.append(u"")
    L.append(u"✅ проверка пройдена · ⚠ найден дефект · · проверить не удалось")
    return u"\n".join(L)


if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    rows = []
    for f in sorted(os.listdir(RESULTS)):
        if not f.endswith(".json"):
            continue
        r = json.load(io.open(os.path.join(RESULTS, f), encoding="utf-8"))
        rows.append(r)
        io.open(os.path.join(OUT, r["strategy"] + ".md"), "w",
                encoding="utf-8").write(card(r) + u"\n")
    io.open(os.path.join(OUT, "INDEX.md"), "w",
            encoding="utf-8").write(index(rows) + u"\n")
    print(u"карточек записано: %d" % len(rows))
    print(u"указатель: %s" % os.path.join(OUT, "INDEX.md"))
