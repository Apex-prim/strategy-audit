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

ROOT = os.environ.get("AUDIT_ROOT") or os.path.dirname(os.path.abspath(__file__))
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
    def g(s, k):
        return s.get(k) if isinstance(s, dict) else None
    if ins["level"] == u"ПРОШЛА" and ins["summary"]:
        a = ins["summary"]; b = out["summary"] if out["level"] == u"ПРОШЛА" else None
        L.append(u"| показатель | в выборке автора | вне выборки |")
        L.append(u"|---|---|---|")
        for key, lab in (("trades", u"сделок"), ("expectancy", u"ожидание на сделку"),
                         ("p_value", u"p-значение средней"),
                         ("market_change_pct", u"«купил и держи», %"),
                         ("total_pct", u"итог стратегии, %"),
                         ("sharpe", u"Шарп"), ("sortino", u"Сортино"),
                         ("drawdown_pct", u"просадка, %"),
                         ("profit_factor", u"фактор прибыли")):
            L.append(u"| %s | %s | %s |" % (lab, g(a, key), g(b, key) if b else u"—"))
        L.append(u"")
        e1, e2 = g(a, "expectancy"), (g(b, "expectancy") if b else None)
        L.append(u"**Осталось от ожидания вне выборки: %s**" % (survives(e1, e2) or u"—"))
        pv = g(a, "p_value")
        if pv is not None and pv > 0.05:
            L.append(u"")
            L.append(u"⚠ **В окне автора средняя доходность НЕ ЗНАЧИМА** "
                     u"(p = %s > 0.05). То есть даже in-sample результат "
                     u"неотличим от нуля." % pv)
        mc = g(a, "market_change_pct")
        if mc is not None and g(a, "total_pct") is not None:
            L.append(u"")
            L.append(u"Базовая линия: «купил и держи» на тех же парах дал "
                     u"**%s%%**, стратегия — **%s%%**." % (mc, g(a, "total_pct")))
    else:
        L.append(u"**%s** — %s" % (ins["level"], ins["why"]))
    L.append(u"")

    miss = g(ins.get("summary"), "missing_pairs") or []
    if miss:
        L.append(u"⚠ **Охват неполон:** движок не нашёл истории по парам %s и "
                 u"посчитал по остальным. Такой результат НЕ сравним с полным."
                 % u", ".join(miss))
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
    # ⚠ Подвал РАНЬШЕ утверждал «1h» текстом — при том, что таймфрейм у каждой
    # стратегии свой. Ровно тот дефект, который этот проект и ловит: проза
    # называет предмет, которого не проверяла. Теперь печатается то, что сказал
    # движок, а если он не сказал — так и пишется.
    tfu = g(ins.get("summary"), "used_timeframe") or r.get("declared_timeframe")
    L.append(u"*Прогон настоящим freqtrade, комиссия 0.1%% за сторону, 8 пар к USDT, "
             u"таймфрейм **%s**. Окно автора 2018-03-01…2020-03-01, вне выборки "
             u"2020-03-01…2026-08-20. «Не смогли проверить» нигде не "
             u"печатается как «чисто».*" % (tfu or u"НЕ ОПРЕДЕЛЁН"))
    return u"\n".join(L)


def index(rows):
    L = [u"# Указатель разборов", u"",
         u"Мера — **ожидание на сделку**, а не итоговый процент: итог зависит "
         u"от `max_open_trades` и размера ставки, то есть от конфигурации, а "
         u"не от стратегии.", u"",
         u"| стратегия | источник | ТФ | в выборке | вне выборки | осталось | утечка | рекурсия |",
         u"|---|---|---|---|---|---|---|---|"]
    for r in rows:
        ins = r["runs"]["in_sample"]; out = r["runs"]["out_sample"]
        e1 = ins["summary"].get("expectancy") if isinstance(ins["summary"], dict) else None
        e2 = out["summary"].get("expectancy") if isinstance(out["summary"], dict) else None
        tf = (ins["summary"].get("used_timeframe")
              if isinstance(ins["summary"], dict) else None) or r.get("declared_timeframe")
        L.append(u"| [%s](%s.md) | `%s` | %s | %s | %s | **%s** | %s | %s |"
                 % (r["strategy"], r["strategy"], r["repo"].split("/")[0], tf or u"—",
                    e1 if e1 is not None else u"—",
                    e2 if e2 is not None else u"—",
                    survives(e1, e2) or u"—",
                    MARK.get(r["runs"]["lookahead"]["level"], u"·"),
                    MARK.get(r["runs"]["recursive"]["level"], u"·")))
    L.append(u"")
    L.append(u"✅ проверка пройдена · ⚠ найден дефект · · проверить не удалось")
    return u"\n".join(L)


def corpus_index(rows):
    u"""Указатель корпуса. Отдельный от разбора НАМЕРЕННО: пять стратегий
    paulcpk выбраны мной, корпус — популяция. Свести их в одну таблицу значило
    бы предложить читателю сравнивать выбранное со случайным."""
    ran = [r for r in rows if isinstance(r["runs"]["in_sample"].get("summary"), dict)]
    dead = [r for r in rows if not isinstance(r["runs"]["in_sample"].get("summary"), dict)]
    L = [u"# Корпус: указатель", u"",
         u"Разобрано карточек **%d**, отработали в окне автора **%d**, "
         u"не удалось **%d**." % (len(rows), len(ran), len(dead)), u"",
         u"Мера — **ожидание на сделку**. Сортировка по ожиданию в окне автора: "
         u"сверху то, что выглядело лучше всего ДО проверки вне выборки.", u"",
         u"| стратегия | репозиторий | ТФ | сделок | в выборке | p | вне | p | осталось |",
         u"|---|---|---|---|---|---|---|---|---|"]

    def key(r):
        a = r["runs"]["in_sample"]["summary"]
        e = a.get("expectancy")
        return -(e if e is not None else -9)

    for r in sorted(ran, key=key):
        a = r["runs"]["in_sample"]["summary"]
        b = r["runs"]["out_sample"].get("summary")
        b = b if isinstance(b, dict) else {}
        L.append(u"| [%s](%s.md) | `%s` | %s | %s | %s | %s | %s | %s | **%s** |"
                 % (r["strategy"], r["strategy"], r["repo"].split("/")[0],
                    a.get("used_timeframe") or u"—", a.get("trades"),
                    a.get("expectancy"), a.get("p_value"),
                    b.get("expectancy", u"—"), b.get("p_value", u"—"),
                    survives(a.get("expectancy"), b.get("expectancy")) or u"—"))
    if dead:
        L += [u"", u"## Не удалось измерить — %d" % len(dead), u"",
              u"Категория, а не молчание: «не смогли проверить» нигде не "
              u"печатается как «чисто».", u"",
              u"| стратегия | ТФ объявлен | причина |", u"|---|---|---|"]
        for r in sorted(dead, key=lambda x: x["strategy"]):
            L.append(u"| %s | %s | %s |"
                     % (r["strategy"], r.get("declared_timeframe") or u"НЕ ОБЪЯВЛЕН",
                        (r["runs"]["in_sample"].get("why") or u"")[:110]))
    return chr(10).join(L)


if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    CORP = os.path.join(ROOT, "repo", "corpus")
    os.makedirs(CORP, exist_ok=True)
    rows, crows = [], []
    for f in sorted(os.listdir(RESULTS)):
        if not f.endswith(".json"):
            continue
        r = json.load(io.open(os.path.join(RESULTS, f), encoding="utf-8"))
        if r.get("source") == "corpus":
            crows.append(r)
            io.open(os.path.join(CORP, r["strategy"] + ".md"), "w",
                    encoding="utf-8").write(card(r) + chr(10))
        else:
            rows.append(r)
            io.open(os.path.join(OUT, r["strategy"] + ".md"), "w",
                    encoding="utf-8").write(card(r) + chr(10))
    if rows:
        io.open(os.path.join(OUT, "INDEX.md"), "w",
                encoding="utf-8").write(index(rows) + chr(10))
    if crows:
        io.open(os.path.join(CORP, "INDEX.md"), "w",
                encoding="utf-8").write(corpus_index(crows) + chr(10))
    print(u"разбор: %d карточек · корпус: %d карточек" % (len(rows), len(crows)))
