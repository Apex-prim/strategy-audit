# -*- coding: utf-8 -*-
u"""corpus — прогон одного и того же аудита по всему собранному корпусу.

Дедупликация по ИМЕНИ КЛАССА: одна и та же стратегия расселена по многим
репозиториям (Schism — в 16), и разбирать её 16 раз значило бы раздуть
корпус повторами и исказить любую сводную статистику. Первое вхождение
выигрывает, остальные записываются как копии.
"""
import io, json, os, sys
sys.path.insert(0, "C:/tmp/audit")
from harness import find_strategies, audit_one, RESULTS

REPOS = "C:/tmp/audit/repos"
LOCK = "C:/tmp/audit/corpus.lock"

# ⚠ ПРОЖИТЫЙ ДЕФЕКТ 20.08. Я трижды перезапускал прогон, ни разу не убив
# предыдущий, и получил ЧЕТЫРЕ процесса, писавших в одну папку РАЗНЫМИ
# версиями кода. По карточке стало невозможно сказать, чем она посчитана —
# и сквозь старую версию пролезло p-значение 2.174, которого не бывает.
#
# Это не неряшливость, а класс: результат неизвестного происхождения хуже
# отсутствующего, потому что выглядит как знание. Тот же класс, что
# «две разные сборки под одной версией» в другом проекте.
#
# Лечение — не «не забывать убивать», а machine-enforced отказ.
if os.path.exists(LOCK):
    try:
        pid = int(io.open(LOCK).read().strip())
    except Exception:
        pid = -1
    alive = False
    try:
        import subprocess
        r = subprocess.run(["tasklist", "/FI", "PID eq %d" % pid],
                           capture_output=True, timeout=30)
        alive = str(pid) in r.stdout.decode("utf-8", "replace")
    except Exception:
        alive = True
    if alive:
        print(u"ОТКАЗ: прогон уже идёт (PID %d). Два процесса на одну папку "
              u"дают карточки неизвестного происхождения." % pid)
        raise SystemExit(2)
    print(u"замок от мёртвого процесса %d снят" % pid)
io.open(LOCK, "w").write(str(os.getpid()))
import atexit
atexit.register(lambda: os.path.exists(LOCK) and os.remove(LOCK))

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
print(u"уникальных стратегий: %d · копий пропущено: %d" % (len(plan), dup), flush=True)
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
    io.open(out, "w", encoding="utf-8").write(json.dumps(r, ensure_ascii=False, indent=2))
    done += 1
    ins = r["runs"]["in_sample"]
    print(u"[%d/%d] %-34s %s" % (done, len(plan), n[:34],
          ins.get("summary") or ins.get("why", "")), flush=True)
