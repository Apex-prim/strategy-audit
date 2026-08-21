# -*- coding: utf-8 -*-
u"""census_repos — из чего собран корпус и сколько ОРИГИНАЛЬНОГО дал каждый.

Не «сколько файлов», а сколько классов встречается ВПЕРВЫЕ. Экосистема
freqtrade состоит из копий, и репозиторий на пятьсот файлов может добавить
пять оригиналов. Порядок обхода — алфавитный и зафиксирован, иначе «кто первым
внёс» зависело бы от того, в каком порядке я их клонировал.

⚠ ЧЕСТНАЯ ОГОВОРКА К СЛОВУ «ПЕРВЫЙ». Право первенства здесь означает лишь
«встретился раньше при алфавитном обходе», а не «автор оригинала». Кто у кого
списал, из кода не видно, и мы этого не утверждаем.
"""
from __future__ import print_function

import collections
import io
import json
import os
import sys

_ROOT = os.environ.get("AUDIT_ROOT") or os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, _ROOT)
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
from harness import find_strategies

REPOS = os.path.join(_ROOT, "repos")


def main():
    seen = set()
    rows = []
    occurrences = 0
    for d in sorted(os.listdir(REPOS)):
        p = os.path.join(REPOS, d)
        if not os.path.isdir(p):
            continue
        names = {n for _f, n in find_strategies(p)}
        occurrences += len(names)
        first = names - seen
        seen |= names
        rows.append((d.replace("_", "/", 1), len(names), len(first)))

    rows.sort(key=lambda r: (-r[2], -r[1]))
    print(u"%-56s %8s %9s %8s" % (u"репозиторий", u"классов", u"впервые", u"копий %"))
    for name, tot, first in rows:
        dup = 100.0 * (tot - first) / tot if tot else 0.0
        print(u"%-56s %8d %9d %7.0f%%" % (name[:56], tot, first, dup))
    print()
    print(u"репозиториев           %d" % len(rows))
    print(u"вхождений (с копиями)  %d" % occurrences)
    print(u"УНИКАЛЬНЫХ КЛАССОВ     %d" % len(seen))
    print(u"доля копий             %.0f%%"
          % (100.0 * (occurrences - len(seen)) / occurrences if occurrences else 0))
    big = max(rows, key=lambda r: r[1])
    print()
    print(u"самый крупный ОДИН репозиторий: %s — %d классов"
          % (big[0], big[1]))
    print(u"корпус больше него в %.1f раза по уникальным классам"
          % (len(seen) / float(big[1])))
    zero = [r[0] for r in rows if r[2] == 0]
    if zero:
        print()
        print(u"НЕ ДАЛИ НИ ОДНОГО ОРИГИНАЛА (%d): %s"
              % (len(zero), u", ".join(zero)))
    io.open(os.path.join(_ROOT, "corpus_sources.json"), "w",
            encoding="utf-8").write(json.dumps(
                {"repos": [{"repo": a, "classes": b, "first": c} for a, b, c in rows],
                 "unique": len(seen), "occurrences": occurrences},
                ensure_ascii=False, indent=1))


if __name__ == "__main__":
    main()
