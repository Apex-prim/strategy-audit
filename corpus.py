# -*- coding: utf-8 -*-
u"""corpus — прогон одного и того же аудита по всему собранному корпусу.

Дедупликация по ИМЕНИ КЛАССА: одна и та же стратегия расселена по многим
репозиториям (Schism — в 16), и разбирать её 16 раз значило бы раздуть
корпус повторами и исказить любую сводную статистику. Первое вхождение
выигрывает, остальные записываются как копии.
"""
import io, json, os, sys
import os as _os
_ROOT = _os.environ.get("AUDIT_ROOT") or _os.path.dirname(_os.path.abspath(__file__))
sys.path.insert(0, _ROOT)
from harness import find_strategies, audit_one, RESULTS

REPOS = _os.path.join(_ROOT, "repos")
LOCK = _os.path.join(_ROOT, "corpus.lock")

# ⚠ ПРОЖИТЫЙ ДЕФЕКТ 20.08, ДВАЖДЫ. Сначала я трижды перезапустил прогон, ни
# разу не убив предыдущий, и получил ЧЕТЫРЕ процесса, писавших в одну папку
# РАЗНЫМИ версиями кода: по карточке стало невозможно сказать, чем она
# посчитана. Починил здесь — и через час два ЗАГРУЗЧИКА свечей писали одни и
# те же файлы. Тот же класс, второе место, потому что я чинил случай.
#
# Результат неизвестного происхождения хуже отсутствующего: он выглядит как
# знание. Поэтому замок вынесен в runlock.py и берётся ВЕЗДЕ, где пишут в
# общее, а не пересказывается в каждом файле заново.
#
# РАСПАРАЛЛЕЛИВАНИЕ. Пятиминутная стратегия — 55 с в окне автора и 149 с вне
# него (замерено, не прикинуто); 351 таких = 26 часов в одну нитку. Работа
# режется на НЕПЕРЕСЕКАЮЩИЕСЯ доли по остатку от деления, у каждой свой
# замок. Запрет двух писателей никуда не делся: он был про РАЗНЫЕ ВЕРСИИ кода
# в одной папке, а не про число процессов. Поэтому вдобавок к замку каждая
# карточка ШТАМПУЕТСЯ отпечатком harness.py: замок предотвращает смешение,
# отпечаток даёт его ОБНАРУЖИТЬ. Запрет без обнаружения — обещание.
import hashlib
import runlock

SHARD, SHARDS = 0, 1
for i, a in enumerate(sys.argv):
    if a == "--shard" and i + 1 < len(sys.argv):
        SHARD, SHARDS = [int(x) for x in sys.argv[i + 1].split("/")]
CODE_MD5 = hashlib.md5(
    io.open(_os.path.join(_ROOT, "harness.py"), "rb").read()).hexdigest()[:12]

if not runlock.acquire("corpus-%d" % SHARD):
    raise SystemExit(2)
import atexit
atexit.register(lambda: runlock.release("corpus-%d" % SHARD))

os.makedirs(RESULTS, exist_ok=True)
seen, plan, dup = set(), [], 0
for d in sorted(os.listdir(REPOS)):
    p = os.path.join(REPOS, d)
    if not os.path.isdir(p):
        continue
    repo = d.replace("_", "/", 1)
    for f, n in sorted(find_strategies(p)):
        if n in seen:
            dup += 1
            continue
        seen.add(n)
        plan.append((repo, f, n))
# Доли режутся по НОМЕРУ в списке, поэтому список обязан быть одинаковым во
# всех процессах. Проверено: три независимых запуска дали один отпечаток
# (dac6309df791d209, 571). Но проверка «однажды» стареет, поэтому отпечаток
# ПЕЧАТАЕТСЯ каждой долей: разойдутся списки — это будет видно в логах, а не
# останется тихой потерей стратегий.
PLAN_MD5 = hashlib.md5(u"|".join(n for _, _, n in plan).encode("utf-8")).hexdigest()[:16]
mine = [x for i, x in enumerate(plan) if i % SHARDS == SHARD]
print(u"уникальных стратегий: %d · копий пропущено: %d · доля %d/%d = %d шт · код %s · список %s"
      % (len(plan), dup, SHARD, SHARDS, len(mine), CODE_MD5, PLAN_MD5), flush=True)
plan = mine
done = 0
for repo, f, n in plan:
    out = os.path.join(RESULTS, n + ".json")
    if os.path.exists(out):
        continue
    try:
        r = audit_one(repo, f, n)
    except Exception as ex:
        r = {"repo": repo, "file": f, "strategy": n, "static": [],
             "runs": {k: {"level": u"НЕ ПРИМЕНИМА", "why": repr(ex)[:150],
                          "summary": None} for k in
                      ("in_sample", "out_sample", "lookahead", "recursive")}}
    r["code_md5"], r["plan_md5"] = CODE_MD5, PLAN_MD5
    r["source"] = "corpus"          # чем посчитано — свойство карточки, не памяти
    # запись через временный файл: оборванный процесс не оставит полукарточку,
    # которую следующий прогон примет за готовую и пропустит
    tmp = out + ".tmp"
    io.open(tmp, "w", encoding="utf-8").write(json.dumps(r, ensure_ascii=False, indent=2))
    _os.replace(tmp, out)
    done += 1
    ins = r["runs"]["in_sample"]
    print(u"[%d/%d] %-34s %s" % (done, len(plan), n[:34],
          ins.get("summary") or ins.get("why", "")), flush=True)
