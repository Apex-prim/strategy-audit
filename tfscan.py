# -*- coding: utf-8 -*-
u"""tfscan — какие таймфреймы объявляют стратегии корпуса.

ЗАЧЕМ. Я гоню весь корпус на часовых свечах, потому что скачал только их.
Стратегия, объявившая `timeframe = '5m'`, на этих данных либо не запустится,
либо — что хуже — запустится не на том. Второе дало бы числа, выглядящие
как результат. Это надо ЗНАТЬ до публикации, а не после.
"""
import collections
import io
import os
import re
import sys

sys.path.insert(0, "C:/tmp/audit")
try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass
from harness import find_strategies

RX = re.compile(r"""^\s*timeframe\s*[:=]\s*['"]([^'"]+)['"]""", re.M)

tf = collections.Counter()
seen = set()
for d in sorted(os.listdir("C:/tmp/audit/repos")):
    p = os.path.join("C:/tmp/audit/repos", d)
    if not os.path.isdir(p):
        continue
    for f, n in find_strategies(p):
        if n in seen:
            continue
        seen.add(n)
        src = io.open(f, encoding="utf-8", errors="replace").read()
        m = RX.search(src)
        tf[m.group(1) if m else u"НЕ ОБЪЯВЛЕН"] += 1

print(u"ТАЙМФРЕЙМЫ (уникальных стратегий %d):" % len(seen))
for k, v in tf.most_common(12):
    mark = u"  ← есть данные" if k == "1h" else u""
    print(u"   %-14s %4d%s" % (k, v, mark))
h1 = tf.get("1h", 0)
print()
print(u"На часовых данных корректны %d из %d (%.0f%%)."
      % (h1, len(seen), 100.0 * h1 / max(1, len(seen))))
print(u"Остальным нужны СВОИ свечи, иначе прогон бессмыслен.")
