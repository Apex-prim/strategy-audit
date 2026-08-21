# -*- coding: utf-8 -*-
u"""report — карточки и указатели. ВЫВОД ПО-АНГЛИЙСКИ, комментарии по-русски.

⚠ ПОВОД ПЕРЕПИСАТЬ, 21.08. Внешний читатель во freqtrade Discord написал:
«it also doesn't list strategies that simply don't load». Формально он неправ —
227 неизмеренных перечислены с причиной у каждой. Практически он прав:

  README вёл на results/INDEX.md — а там ПЯТЬ стратегий разбора
  на corpus/ ссылки не было вовсе
  corpus/INDEX.md и все 566 карточек были НА РУССКОМ в англоязычном репозитории

Информация существовала, а парадная дверь вела не в ту комнату. Это мой же
класс дефекта: «мы это опубликовали» — ответ про слово, а не про предмет.
Проверять надо не «есть ли файл», а «может ли читатель его найти и прочесть».

Мера — СРЕДНЯЯ СДЕЛКА В ПРОЦЕНТАХ там, где она есть: ожидание в валюте при
`stake_amount: unlimited` компаундирует и не свободно от масштаба.
"""
from __future__ import print_function

import io
import json
import os
import sys

ROOT = os.environ.get("AUDIT_ROOT") or os.path.dirname(os.path.abspath(__file__))
try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

RESULTS = os.path.join(ROOT, "results")
OUT = os.path.join(ROOT, "repo", "results")
CORP = os.path.join(ROOT, "repo", "corpus")

PASS, FOUND = u"ПРОШЛА", u"НАЙДЕНО"
MARK = {PASS: u"pass", FOUND: u"FOUND", u"НЕ ПРИМЕНИМА": u"n/a",
        u"НЕ ЗАПУСКАЛИ": u"not run"}
EN = {PASS: u"clean", FOUND: u"**found**", u"НЕ ПРИМЕНИМА": u"could not run",
      u"НЕ ЗАПУСКАЛИ": u"not run"}


def g(s, k):
    return s.get(k) if isinstance(s, dict) else None


def survives(a, b):
    if a is None or b is None:
        return None
    if b < 0:
        return u"negative"
    if a <= 0:
        return u"n/a"
    return u"%.0f%%" % (100.0 * b / a)


def card(r):
    L = []
    s = r["strategy"]
    L.append(u"# %s" % s)
    L.append(u"")
    L.append(u"Source: [`%s`](https://github.com/%s) · file `%s`"
             % (r["repo"], r["repo"], os.path.basename(r["file"])))
    if r.get("variant") == "long_only":
        L.append(u"")
        L.append(u"> **Modified by the audit: `can_short = False`.** This is a "
                 u"long/short strategy measured with its short side silenced, "
                 u"because this sweep ran spot. **It is not the strategy its "
                 u"author wrote** and its numbers are not comparable to the "
                 u"main corpus.")
    L.append(u"")

    ins, out = r["runs"]["in_sample"], r["runs"]["out_sample"]
    a = ins.get("summary") if isinstance(ins.get("summary"), dict) else None
    b = out.get("summary") if isinstance(out.get("summary"), dict) else None

    if a and a.get("trades") is not None:
        L.append(u"## Result")
        L.append(u"")
        L.append(u"| metric | author's window | out of sample |")
        L.append(u"|---|---|---|")
        for key, lab in (("trades", u"trades"),
                         ("expectancy", u"expectancy per trade (USDT)"),
                         ("p_value", u"mean profit p-value"),
                         ("market_change_pct", u"market change % (baseline)"),
                         ("total_pct", u"strategy total %"),
                         ("sharpe", u"Sharpe"), ("sortino", u"Sortino"),
                         ("drawdown_pct", u"max drawdown %"),
                         ("profit_factor", u"profit factor")):
            L.append(u"| %s | %s | %s |" % (lab, g(a, key),
                                            g(b, key) if b else u"—"))
        L.append(u"")
        e1, e2 = g(a, "expectancy"), (g(b, "expectancy") if b else None)
        L.append(u"**Retained out of sample: %s**" % (survives(e1, e2) or u"—"))
        L.append(u"")
        # ⚠ ПРОЖИТЫЙ ДЕФЕКТ 21.08. «Удержано» сравнивает МЕДВЕЖЬЕ окно автора
        # (рынок −58%) с БЫЧЬИМ вне выборки (+346%). Для стратегии с длинным
        # перекосом это отношение измеряет везение с режимом, а не стойкость:
        # чем хуже ей было в 2018-2020, тем красивее «удержание». Семейство
        # NFI показало 3.22 против 1.73 у прочих — и при этом ОБЫГРАЛО рынок
        # реже (8% против 12%). Два показателя противоречили друг другу,
        # и сломанным оказался мой.
        L.append(u"> **Read that number with care.** The author's window was a "
                 u"bear market (buy-and-hold −58%) and the out-of-sample window "
                 u"a bull market (+346%). For a long-biased strategy this ratio "
                 u"rewards having done *badly* in 2018–2020, so it measures "
                 u"regime luck as much as robustness. The regime-free "
                 u"comparison is the excess over buy-and-hold, below.")
        L.append(u"")
        L.append(u"> Expectancy above is in USDT and the backtests run with "
                 u"`stake_amount: \"unlimited\"`, which compounds — so it is "
                 u"**not** scale-free either. Cross-strategy comparisons in "
                 u"this repository use average profit per trade in percent.")
        exc = []
        for lab, s in ((u"author's window", a), (u"out of sample", b)):
            if isinstance(s, dict) and s.get("total_pct") is not None \
                    and s.get("market_change_pct") is not None:
                exc.append(u"%s **%+.1f pp**" % (lab, s["total_pct"] - s["market_change_pct"]))
        if exc:
            L.append(u"")
            L.append(u"**Excess over buy-and-hold** (regime-free): %s."
                     % u", ".join(exc))
        pv = g(a, "p_value")
        if pv is not None and pv > 0.05:
            L.append(u"")
            L.append(u"⚠ **Not statistically significant in its author's own "
                     u"window** (p = %s > 0.05): the average trade is not "
                     u"distinguishable from zero." % pv)
        mc, tp = g(a, "market_change_pct"), g(a, "total_pct")
        if mc is not None and tp is not None:
            L.append(u"")
            L.append(u"Baseline: buy-and-hold on the same pairs returned "
                     u"**%s%%**; the strategy returned **%s%%**." % (mc, tp))
        if b and b.get("market_change_pct") is not None:
            bt, bm = b.get("total_pct"), b.get("market_change_pct")
            if bt is not None:
                L.append(u"Out of sample: buy-and-hold **%s%%** vs strategy "
                         u"**%s%%** — %s." % (bm, bt,
                         u"**beats the baseline**" if bt > bm else u"loses to it"))
        miss = g(a, "missing_pairs") or []
        if miss:
            L.append(u"")
            L.append(u"⚠ **Incomplete coverage:** the engine found no history "
                     u"for %s and computed on the rest. Not comparable to a "
                     u"full-coverage result." % u", ".join(miss))
    else:
        L.append(u"## Could not be measured")
        L.append(u"")
        L.append(u"```")
        L.append((ins.get("why") or u"no reason recorded").strip())
        L.append(u"```")
        L.append(u"")
        L.append(u"Declared timeframe: `%s`. This is a named cause, not a "
                 u"verdict on the strategy — see the note on buckets in "
                 u"[../BASELINE.md](../BASELINE.md)."
                 % (r.get("declared_timeframe") or u"none declared"))
    L.append(u"")

    L.append(u"## Checks")
    L.append(u"")
    L.append(u"| check | result | detail |")
    L.append(u"|---|---|---|")
    la, rc = r["runs"]["lookahead"], r["runs"]["recursive"]
    L.append(u"| look-ahead bias (freqtrade's own `lookahead-analysis`) | %s | %s |"
             % (EN.get(la["level"], la["level"]), (la["why"] or u"")[:150]))
    L.append(u"| indicator recursion (freqtrade's own `recursive-analysis`) | %s | %s |"
             % (EN.get(rc["level"], rc["level"]), (rc["why"] or u"")[:150]))
    for c in r["static"]:
        L.append(u"| %s | %s | %s |" % (c["what"],
                 EN.get(c["level"], c["level"]), c["detail"][:150]))
    L.append(u"")
    L.append(u"---")
    L.append(u"")
    tf = g(a, "used_timeframe") or r.get("declared_timeframe") or u"undetermined"
    L.append(u"*Run by freqtrade itself. Fee 0.1%% per side, 8 USDT pairs, "
             u"timeframe **%s** (the strategy's own — never overridden by "
             u"config). Author's window 2018-03-01…2020-03-01, out of sample "
             u"2020-03-01…2026-08-19. \"Could not check\" is never printed as "
             u"\"clean\".*" % tf)
    L.append(u"")
    L.append(u"*Code fingerprint `%s` · strategy list `%s`*"
             % (r.get("code_md5") or u"—", r.get("plan_md5") or u"—"))
    return u"\n".join(L)


def corpus_index(rows):
    ran = [r for r in rows
           if isinstance(r["runs"]["in_sample"].get("summary"), dict)
           and r["runs"]["in_sample"]["summary"].get("trades") is not None]
    dead = [r for r in rows if r not in ran]
    L = [u"# Corpus index — every strategy, measured or explained", u"",
         u"**%d cards. %d produced numbers; %d could not be measured and each "
         u"one names why.**" % (len(rows), len(ran), len(dead)), u"",
         u"Nothing is omitted for being inconvenient: strategies that fail to "
         u"load are listed in the second table with the exception that killed "
         u"them. \"Could not check\" is never folded into \"clean\".", u"",
         u"Sorted by expectancy in the author's window — the ones that looked "
         u"best *before* anyone tested them out of sample.", u"",
         u"**`retained` is confounded and `excess` is not.** The author's "
         u"window was a bear market (buy-and-hold −58%) and the out-of-sample "
         u"window a bull market (+346%), so the retention ratio rewards a "
         u"strategy for having done badly in 2018–2020. `excess` is total "
         u"return minus buy-and-hold in the same window, in percentage points, "
         u"and does not care which way the market went.", u"",
         u"| strategy | repository | tf | trades | in-sample | p | out | p | retained | excess in | excess out |",
         u"|---|---|---|---|---|---|---|---|---|---|---|"]

    def key(r):
        e = r["runs"]["in_sample"]["summary"].get("expectancy")
        return -(e if e is not None else -9)

    for r in sorted(ran, key=key):
        a = r["runs"]["in_sample"]["summary"]
        b = r["runs"]["out_sample"].get("summary")
        b = b if isinstance(b, dict) else {}
        def exc(s):
            if isinstance(s, dict) and s.get("total_pct") is not None \
                    and s.get("market_change_pct") is not None:
                return u"%+.0f" % (s["total_pct"] - s["market_change_pct"])
            return u"—"
        L.append(u"| [%s](%s.md) | `%s` | %s | %s | %s | %s | %s | %s | %s | %s | **%s** |"
                 % (r["strategy"], r["strategy"], r["repo"].split("/")[0],
                    a.get("used_timeframe") or u"—", a.get("trades"),
                    a.get("expectancy"), a.get("p_value"),
                    b.get("expectancy", u"—"), b.get("p_value", u"—"),
                    survives(a.get("expectancy"), b.get("expectancy")) or u"—",
                    exc(a), exc(b)))
    if dead:
        L += [u"", u"## Could not be measured — %d" % len(dead), u"",
              u"These are listed because a bucket with no stated cause is "
              u"indistinguishable from a bucket nobody looked at. Several of "
              u"these causes turned out to be **ours** rather than the "
              u"strategies' — see [../BASELINE.md](../BASELINE.md).", u"",
              u"| strategy | declared tf | reason |", u"|---|---|---|"]
        for r in sorted(dead, key=lambda x: x["strategy"]):
            L.append(u"| [%s](%s.md) | %s | `%s` |"
                     % (r["strategy"], r["strategy"],
                        r.get("declared_timeframe") or u"none",
                        (r["runs"]["in_sample"].get("why") or u"").strip()[:120]))
    return u"\n".join(L)


def index(rows):
    L = [u"# The five hand-picked audits", u"",
         u"These five are a **case study I chose**, not a population. The "
         u"571→900 corpus lives in [../corpus/INDEX.md](../corpus/INDEX.md).", u"",
         u"| strategy | source | tf | in-sample | out | retained | look-ahead | recursion |",
         u"|---|---|---|---|---|---|---|---|"]
    for r in rows:
        ins, out = r["runs"]["in_sample"], r["runs"]["out_sample"]
        e1 = g(ins.get("summary"), "expectancy")
        e2 = g(out.get("summary"), "expectancy")
        tf = g(ins.get("summary"), "used_timeframe") or r.get("declared_timeframe")
        L.append(u"| [%s](%s.md) | `%s` | %s | %s | %s | **%s** | %s | %s |"
                 % (r["strategy"], r["strategy"], r["repo"].split("/")[0],
                    tf or u"—", e1 if e1 is not None else u"—",
                    e2 if e2 is not None else u"—", survives(e1, e2) or u"—",
                    EN.get(r["runs"]["lookahead"]["level"], u"—"),
                    EN.get(r["runs"]["recursive"]["level"], u"—")))
    return u"\n".join(L)


if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    os.makedirs(CORP, exist_ok=True)
    rows, crows = [], []
    for f in sorted(os.listdir(RESULTS)):
        if not f.endswith(".json"):
            continue
        r = json.load(io.open(os.path.join(RESULTS, f), encoding="utf-8"))
        d = CORP if r.get("source") != "case_study" else OUT
        (crows if d is CORP else rows).append(r)
        io.open(os.path.join(d, r["strategy"] + ".md"), "w",
                encoding="utf-8").write(card(r) + chr(10))
    if rows:
        io.open(os.path.join(OUT, "INDEX.md"), "w",
                encoding="utf-8").write(index(rows) + chr(10))
    if crows:
        io.open(os.path.join(CORP, "INDEX.md"), "w",
                encoding="utf-8").write(corpus_index(crows) + chr(10))
    print(u"case study: %d · corpus: %d" % (len(rows), len(crows)))
