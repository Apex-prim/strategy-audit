# -*- coding: utf-8 -*-
u"""Один писатель на общий ресурс. Замок с проверкой ЖИВОСТИ, не с обещанием.

ПОВОД, ДВАЖДЫ. 20.08 я трижды перезапустил corpus.py, ни разу не убив
предыдущий: четыре процесса писали карточки, и по карточке нельзя было
сказать, какой версией кода она посчитана. Починил — но починил СЛУЧАЙ:
через час два загрузчика писали одни и те же файлы свечей. Тот же класс,
второе место. Поэтому замок вынесен сюда и берётся ВЕЗДЕ, где пишут в
общее.

Мёртвый замок (процесса нет) снимается сам — иначе первое же падение
заблокировало бы работу навсегда, и замок начали бы обходить руками.
"""
from __future__ import print_function
import io, os, sys

LOCKDIR = "C:/tmp/audit"


def _alive(pid):
    u"""Жив ли процесс. Пустой ответ tasklist = мёртв."""
    try:
        import subprocess
        out = subprocess.check_output(
            ["tasklist", "/FI", "PID eq %d" % pid, "/NH"],
            stderr=subprocess.STDOUT).decode("cp866", "replace")
        return str(pid) in out
    except Exception:
        return True          # не смог проверить ⇒ считаю живым (осторожная сторона)


def acquire(name, quiet=False):
    u"""True — замок наш. False — работает другой, его PID НАЗВАН."""
    p = os.path.join(LOCKDIR, "%s.lock" % name)
    if os.path.exists(p):
        try:
            old = int(io.open(p, encoding="utf-8").read().strip())
        except Exception:
            old = None
        if old and _alive(old):
            if not quiet:
                print(u"ОТКАЗ: «%s» уже занят процессом PID %d. "
                      u"Два писателя на один ресурс дают результат "
                      u"неизвестного происхождения." % (name, old))
            return False
        if not quiet:
            print(u"замок «%s» был мёртв (PID %s) — снимаю" % (name, old))
    io.open(p, "w", encoding="utf-8").write(u"%d" % os.getpid())
    return True


def release(name):
    try:
        os.remove(os.path.join(LOCKDIR, "%s.lock" % name))
    except Exception:
        pass
