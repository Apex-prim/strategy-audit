# -*- coding: utf-8 -*-
u"""funnel — воронка с базовой линией, по популяциям, без смешения.

Три популяции живут в одной папке карточек и НЕ СМЕШИВАЮТСЯ, потому что
отвечают на разные вопросы:

    corpus      571 стратегия, режим spot, как написано автором
    long_only   77 стратегий, у которых can_short заглушён аудитом —
                ДРУГОЙ ПРЕДМЕТ: что получил бы спотовый торговец
    case_study  5 разборов paulcpk, ВЫБРАННЫХ МНОЮ вручную

Смешать их значило бы считать долю выживших по знаменателю, куда я сам
подложил слагаемые. Признак — поле `source`, а не память о том, какие файлы
«те самые».

Пороги объявлены в CORPUS_PLAN.md ДО чисел: 30 сделок, p < 0.05.
Базовая линия — `Market change`, которую freqtrade печатает даром и которую
все пролистывают. Именно она переворачивает вывод.
"""
from __future__ import print_function

import collections
import glob
import io
import json
import os
import sys

_ROOT = os.environ.get("AUDIT_ROOT") or os.path.dirname(os.path.abspath(__file__))
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
RESULTS = os.path.join(_ROOT, "results")
MIN_N = 30
ALPHA = 0.05


def load():
    by = collections.defaultdict(list)
    for f in glob.glob(os.path.join(RESULTS, "*.json")):
        try:
            r = json.load(io.open(f, encoding="utf-8"))
        except Exception:
            print(u"БИТАЯ КАРТОЧКА: %s" % os.path.basename(f))
            continue
        by[r.get("source") or "unknown"].append(r)
    return by


def summ(r, w):
    s = r["runs"].get(w, {}).get("summary")
    return s if isinstance(s, dict) else None


def run(title, rows, note=u""):
    print(u"\n" + u"=" * 66)
    print(u"%s — карточек %d" % (title, len(rows)))
    if note:
        print(note)
    ran = [r for r in rows if summ(r, "in_sample") and summ(r, "in_sample").get("trades") is not None]
    out = [r for r in ran if summ(r, "out_sample") and summ(r, "out_sample").get("expectancy") is not None]
    enough = [r for r in out if summ(r, "in_sample")["trades"] >= MIN_N]
    pos = [r for r in enough if (summ(r, "in_sample").get("expectancy") or 0) > 0]
    sig = [r for r in pos if (summ(r, "in_sample").get("p_value") is not None
                              and summ(r, "in_sample")["p_value"] < ALPHA)]
    po = [r for r in sig if summ(r, "out_sample")["expectancy"] > 0]
    so = [r for r in po if (summ(r, "out_sample").get("p_value") is not None
                            and summ(r, "out_sample")["p_value"] < ALPHA)]
    bias = [r for r in so if r["runs"].get("lookahead", {}).get("level") == u"НАЙДЕНО"]
    clean = [r for r in so if r not in bias]

    print(u"  ① отработали в окне автора            %4d" % len(ran))
    print(u"  ② и вне окна                          %4d" % len(out))
    print(u"  ③ сделок >= %d                        %4d" % (MIN_N, len(enough)))
    print(u"  ④ ожидание в выборке > 0              %4d" % len(pos))
    print(u"  ⑤ и ЗНАЧИМО (p < %.2f)                 %4d" % (ALPHA, len(sig)))
    print(u"  ⑥ и ожидание вне выборки > 0          %4d" % len(po))
    print(u"  ⑦ и ЗНАЧИМО вне выборки               %4d" % len(so))
    print(u"     с заглядыванием (исключены)        %4d" % len(bias))
    print(u"     чистых                             %4d" % len(clean))

    beat = []
    for r in clean:
        b = summ(r, "out_sample")
        t, m = b.get("total_pct"), b.get("market_change_pct")
        if t is not None and m is not None and t > m:
            beat.append((r["strategy"], t, m))
    print(u"\n  ⚑ ОБЫГРАЛИ «КУПИЛ И ДЕРЖИ»            %4d  из %d" % (len(beat), len(clean)))
    for n, t, m in sorted(beat, key=lambda x: -x[1]):
        print(u"      %-34s %8.1f%% против %.1f%%" % (n[:34], t, m))

    # различные по числам — дубли имён не считаются отдельными находками
    keys = set()
    for r in clean:
        a, b = summ(r, "in_sample"), summ(r, "out_sample")
        keys.add((round(a.get("expectancy") or 0, 4), round(b.get("expectancy") or 0, 4),
                  b.get("trades")))
    if clean:
        print(u"  различных по числам: %d (остальные — одна стратегия под разными именами)"
              % len(keys))

    dead = [r for r in rows if r not in ran]
    if dead:
        why = collections.Counter((r["runs"]["in_sample"].get("why") or u"?")[:58]
                                  for r in dead)
        print(u"\n  НЕ ИЗМЕРЕНО: %d — категория с названной причиной, не молчание" % len(dead))
        for w, c in why.most_common(6):
            print(u"    %4d  %s" % (c, w))
    return len(clean), len(beat)


def main():
    by = load()
    tot_clean = tot_beat = 0
    for src, title, note in (
            ("corpus", u"КОРПУС (как написано авторами, режим spot)", u""),
            ("long_only", u"ДЛИННАЯ СТОРОНА (can_short заглушён аудитом)",
             u"  ⚠ ДРУГОЙ ПРЕДМЕТ: это не та стратегия, которую написал автор.\n"
             u"  Отвечает на вопрос «что получил бы спотовый торговец»."),
            ("case_study", u"РАЗБОР paulcpk (ВЫБРАН МНОЮ вручную)",
             u"  ⚠ не популяция: пять стратегий, которые я выбрал сам."),
    ):
        if by.get(src):
            c, b = run(title, by[src], note)
            if src != "case_study":
                tot_clean += c
                tot_beat += b
    print(u"\n" + u"=" * 66)
    print(u"ИТОГ ПО ОБЕИМ ПОПУЛЯЦИЯМ: прошли все статистические ворота %d, "
          u"обыграли «купил и держи» %d." % (tot_clean, tot_beat))


if __name__ == "__main__":
    main()
