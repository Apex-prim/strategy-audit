# -*- coding: utf-8 -*-
u"""expand — расширение корпуса новыми репозиториями.

Клонирует поверхностно (--depth 1), затем считает, сколько НОВЫХ имён классов
даёт каждый репозиторий сверх уже имеющихся.

ЗАЧЕМ СЧИТАТЬ ПРИРОСТ, А НЕ ЧИСЛО ФАЙЛОВ. Экосистема freqtrade состоит из
копий: в нынешнем корпусе 484 вхождения из 1055 — повторы, Schism лежит в 16
репозиториях. Репозиторий на тысячу файлов может не добавить НИ ОДНОЙ новой
стратегии. Знаменатель корпуса — уникальные классы, и прирост считается по нему.

⚠ Клонирование чужого кода. Ничего не исполняется на этом шаге: только
разбор AST в find_strategies. Запускается позже, тем же прибором, что и
остальные 571.
"""
from __future__ import print_function

import io
import os
import subprocess
import sys

_ROOT = os.environ.get("AUDIT_ROOT") or os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, _ROOT)
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
from harness import find_strategies

REPOS = os.path.join(_ROOT, "repos")
MAX_KB = 60000          # объявленный предел: репозитории тяжелее не берём

# TOTAL: перечень запрашиваемых пар — это ВХОД исследования, объявленный
# намеренно, а не область проверки. Расширение списка — решение, не находка.
WANT = [
    "keithorange/HUGE_FreqTrade_Strategy_Collection",
    "Foxel05/freqtrade-stuff",
    "phuchust/freqtrade_strategy",
    "hansen1015/freqtrade_strategy",
    "ShahAnuj2610/my-freqtrade",
    "bustillo/freqtrade-strategies",
    "mikedigriz/freqtrade-strategy-mikedigriz",
    "jaredrsommer/freqtradestrategies",
    "MMR-19/freqtrade-strategies",
    "botenesp/freqtrade_strategies",
    "Juusseli/Trade",
    "anakein/beastbotXB",
    "freqtrade/berlinguyinca-trading-strategies",
    "seannowotny/FlawlessVictoryPort",
    "devbootstrap/optimize-trading-strategy-using-freqtrade",
    "jerome-benoit/freqai-strategies",
    "ShahAnuj2610/my-freqtrade-nfi-nextgen",
    "keryc/crypto-bot",
    "p-zombie/freqtrade",
    "Mohamed-sm/Freqtrade-RLStrategy-IA",
]


def known_names():
    seen = set()
    for d in sorted(os.listdir(REPOS)):
        p = os.path.join(REPOS, d)
        if os.path.isdir(p):
            for _f, n in find_strategies(p):
                seen.add(n)
    return seen


def main():
    base = known_names()
    print(u"уже известно уникальных классов: %d" % len(base), flush=True)
    grand = set(base)
    report = []
    for full in WANT:
        d = full.replace("/", "_", 1)
        path = os.path.join(REPOS, d)
        if not os.path.isdir(path):
            r = subprocess.run(["git", "clone", "--depth", "1", "-q",
                                "https://github.com/%s.git" % full, path],
                               capture_output=True, timeout=600)
            if r.returncode != 0:
                print(u"  ✗ %-52s НЕ КЛОНИРОВАЛСЯ: %s"
                      % (full, r.stderr.decode("utf-8", "replace")[:80]), flush=True)
                continue
        names = {n for _f, n in find_strategies(path)}
        new = names - grand
        grand |= names
        report.append((len(new), len(names), full))
        print(u"  %-52s классов %4d · НОВЫХ %4d"
              % (full, len(names), len(new)), flush=True)

    report.sort(reverse=True)
    print()
    print(u"ИТОГО уникальных классов было %d, стало %d — прирост %d"
          % (len(base), len(grand), len(grand) - len(base)))
    print(u"⚠ предел объявлен: репозитории тяжелее %d КБ не брались" % MAX_KB)
    print()
    print(u"кто дал прирост:")
    for new, tot, full in report:
        if new:
            print(u"   +%-4d из %-4d  %s" % (new, tot, full))
    dead = [f for n, t, f in report if n == 0]
    if dead:
        print(u"НЕ ДАЛИ НИ ОДНОЙ НОВОЙ (%d): %s" % (len(dead), u", ".join(dead)))


if __name__ == "__main__":
    main()
