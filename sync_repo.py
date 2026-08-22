# -*- coding: utf-8 -*-
u"""sync_repo — опубликованный код обязан быть ТЕМ ЖЕ, что считал числа.

ПОВОД, ПРОЖИТЫЙ 21.08. В репозитории лежали `replicate.py` и `stats.py`, давно
выброшенные из работы. Внешний рецензент прочёл репозиторий и **похвалил их как
сильную сторону**. Ничего ложного написано не было: файлы существовали, код
работал. Он просто больше не имел отношения к числам, а отличить это читатель
не мог. Дефект не в рецензенте.

ЧТО ЗДЕСЬ ДВЕ ПРОВЕРКИ, И ВТОРАЯ ВАЖНЕЕ:

  ① РАСХОЖДЕНИЕ — файл есть в обоих местах, но содержимое разное.
     Опубликована не та версия, что считала.

  ② СИРОТА — файл есть в репозитории и НЕТ в рабочем наборе.
     Именно так выжили replicate.py и stats.py. Проверка «все ли мои файлы
     опубликованы» этого НЕ ВИДИТ: она смотрит в одну сторону. Смотреть
     обязательно в обе.

Набор объявлен списком ниже, а не выведен из содержимого папки: иначе любой
случайный файл в рабочей директории молча стал бы «частью конвейера».

ЗАПУСК:  python sync_repo.py             только показать
         python sync_repo.py --apply     скопировать и удалить сирот
         python sync_repo.py --orphans   ТОЛЬКО ② — работает на чистой копии
                                         репозитория, где рабочего дерева нет;
                                         именно эта форма стоит в CI
         python sync_repo.py --selftest  диверсия: проверка обязана находить
"""
from __future__ import print_function

import filecmp
import io
import os
import shutil
import sys

_ROOT = os.environ.get("AUDIT_ROOT") or os.path.dirname(os.path.abspath(__file__))
REPO = os.path.join(_ROOT, "repo")
sys.stdout.reconfigure(encoding="utf-8", errors="replace")

# КОНВЕЙЕР — ровно эти модули считают опубликованные числа.
PIPELINE = [
    "harness.py",        # измерение: движок, оба окна, оба прибора
    "corpus.py",         # свип корпуса долями
    "ledger.py",         # реестр: строка на стратегию, эпохи решений
    "ledger_block.py",   # единственная сборка блока чисел
    "multiplicity.py",   # поправка на множественность
    "traps.py",          # ловушки бэктеста сообщества
    "dof.py",            # степени свободы
    "power.py",          # мощность
    "coverage.py",       # покрытие пар данными
    "loadscan.py",       # причины отказа загрузки
    "report.py",         # карточки и указатели
    "census_repos.py",   # перепись источников
    "harvest.py",        # сбор репозиториев
    "expand.py",         # расширение корпуса
    "longonly.py",       # вариант с выключенным шортом
    "fetch_bulk.py",     # свечи из месячных архивов
    "setup_ft.py",       # рабочая папка freqtrade
    "tfscan.py",         # какие таймфреймы объявлены
    "runlock.py",        # один писатель на общий ресурс
    "anatman.py",        # прожитые дефекты как исполняемые случаи
    "tf_guard_selftest.py",  # диверсия против сторожа таймфрейма
    "sync_repo.py",      # этот файл: опубликованное = рабочее
]

# Живёт только в репозитории: проверяет опубликованное на чистой машине.
REPO_ONLY = ["verify_ledger.py", "freeze_guard.py"]


def orphans_only():
    u"""② без ①. На чистой копии репозитория рабочего дерева нет, поэтому
    сравнивать не с чем — но спросить «есть ли здесь код, которого нет в
    конвейере» можно, и это как раз тот вопрос, который был пропущен."""
    here = os.path.dirname(os.path.abspath(__file__))
    known = set(PIPELINE) | set(REPO_ONLY) | {"sync_repo.py"}
    found = sorted(f for f in os.listdir(here) if f.endswith(".py"))
    orphans = [f for f in found if f not in known]
    absent = [f for f in PIPELINE if not os.path.exists(os.path.join(here, f))]
    print(u"опубликовано модулей: %d, объявлено в конвейере: %d"
          % (len(found), len(PIPELINE)))
    for f in orphans:
        print(u"  СИРОТА: %s — опубликован, но не объявлен частью конвейера" % f)
    for f in absent:
        print(u"  ПРОПАЛ: %s — объявлен конвейером, но не опубликован" % f)
    if orphans or absent:
        print(u"код и его объявление разошлись")
        return 1
    print(u"каждый опубликованный модуль объявлен, и наоборот")
    return 0


def main():
    apply = "--apply" in sys.argv
    if "--orphans" in sys.argv:
        return orphans_only()
    if not os.path.isdir(REPO):
        print(u"нет папки %s" % REPO)
        return 1

    missing, differ, same = [], [], []
    for f in PIPELINE:
        src, dst = os.path.join(_ROOT, f), os.path.join(REPO, f)
        if not os.path.exists(src):
            print(u"⛔ в рабочем наборе НЕТ %s — список конвейера врёт" % f)
            return 1
        if not os.path.exists(dst):
            missing.append(f)
        elif not filecmp.cmp(src, dst, shallow=False):
            differ.append(f)
        else:
            same.append(f)

    known = set(PIPELINE) | set(REPO_ONLY)
    orphans = sorted(f for f in os.listdir(REPO)
                     if f.endswith(".py") and f not in known)

    print(u"КОНВЕЙЕР: %d модулей" % len(PIPELINE))
    print(u"  совпадают         %3d" % len(same))
    print(u"  не опубликованы   %3d   %s" % (len(missing), u", ".join(missing) or u"—"))
    print(u"  расходятся        %3d   %s" % (len(differ), u", ".join(differ) or u"—"))
    print(u"  СИРОТЫ            %3d   %s" % (len(orphans), u", ".join(orphans) or u"—"))
    if orphans:
        print(u"  ⚠ сирота — опубликованный код, которого нет в конвейере.")
        print(u"    Читатель считает его частью работы. Так выжили replicate.py")
        print(u"    и stats.py, и внешний разбор похвалил именно их.")

    if not apply:
        if missing or differ or orphans:
            print(u"\nничего не тронуто. Применить: python sync_repo.py --apply")
            return 1
        print(u"\nопубликованный код совпадает с рабочим")
        return 0

    for f in missing + differ:
        shutil.copy2(os.path.join(_ROOT, f), os.path.join(REPO, f))
        print(u"скопирован %s" % f)
    for f in orphans:
        os.remove(os.path.join(REPO, f))
        print(u"удалён сирота %s" % f)
    print(u"готово: %d скопировано, %d удалено"
          % (len(missing) + len(differ), len(orphans)))
    return 0


def selftest():
    u"""Диверсия: проверка обязана УМЕТЬ находить, а не только соглашаться."""
    import tempfile
    ok = []
    d = tempfile.mkdtemp()
    r = os.path.join(d, "repo")
    os.makedirs(r)
    io.open(os.path.join(d, "a.py"), "w", encoding="utf-8").write(u"x = 1\n")
    io.open(os.path.join(r, "a.py"), "w", encoding="utf-8").write(u"x = 1\n")
    io.open(os.path.join(r, "ghost.py"), "w", encoding="utf-8").write(u"dead\n")

    globals()["_ROOT"], globals()["REPO"] = d, r
    globals()["PIPELINE"], globals()["REPO_ONLY"] = ["a.py"], []
    ok.append((u"сирота найдена", main() == 1))

    os.remove(os.path.join(r, "ghost.py"))
    ok.append((u"чистое состояние проходит", main() == 0))

    io.open(os.path.join(r, "a.py"), "w", encoding="utf-8").write(u"x = 2\n")
    ok.append((u"расхождение найдено", main() == 1))

    shutil.rmtree(d, ignore_errors=True)
    print()
    for n, v in ok:
        print(u"  %-28s %s" % (n, u"OK" if v else u"ПРОВАЛ"))
    bad = [n for n, v in ok if not v]
    print(u"самопроверка: %d/%d" % (len(ok) - len(bad), len(ok)))
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(selftest() if "--selftest" in sys.argv else main())
