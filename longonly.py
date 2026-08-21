# -*- coding: utf-8 -*-
u"""longonly — вернуть в корпус 77 стратегий, отсечённых режимом spot.

ПОЧЕМУ НЕ ФЬЮЧЕРСЫ. Эти 77 объявляют `can_short = True`, а корпус гнался в
режиме spot — то есть отсечены МОЕЙ конфигурацией, а не своим качеством.
Естественный ответ «прогнать на фьючерсах» ПРОВЕРЕН И НЕ ГОДИТСЯ:

    fapi.binance.com          451 (геоблок), fapi1/2/3 — 202 с пустым телом
    data.binance.vision       фьючерсные архивы ЕСТЬ
    BTCUSDT 5m futures        первый месяц 2020-03; 2018-03 … 2019-12 — 404

Окно автора (2018-03…2020-03) предшествует существованию USDT-фьючерсов
Binance. Прогон на фьючерсах дал бы этим 77 СВОЁ, более позднее окно,
несопоставимое с остальными 494. Это не восстановление корпуса, а другая
популяция.

ЧТО ДЕЛАЕТСЯ ВМЕСТО. Ровно то, что предлагает сам движок в тексте отказа:
«You can run this strategy in spot markets by setting can_short=False. Please
note that short signals will be ignored in that case.»

⚠ ЭТО ИЗМЕРЕНИЕ ДРУГОГО ПРЕДМЕТА, и так оно и помечается. Стратегия с
заглушённой короткой стороной — не та стратегия, которую написал автор. Она
отвечает на отдельный вопрос: «что получил бы спотовый торговец, у которого
шортов нет вообще». Карточки получают `variant: "long_only"` и НИКОГДА не
смешиваются с основным корпусом в сводной статистике.

ПРАВКА МИНИМАЛЬНА И ВИДНА. Файл копируется, в класс дописывается одна строка
`can_short = False`. Исходники в repos/ не трогаются. Diff одной строки —
это не «переписал вашу логику», это буквальная инструкция движка.
"""
from __future__ import print_function

import io
import json
import os
import re
import shutil
import sys

_ROOT = os.environ.get("AUDIT_ROOT") or os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, _ROOT)
sys.stdout.reconfigure(encoding="utf-8", errors="replace")

import runlock
from harness import RESULTS, audit_one, declared_tf

TODO = os.path.join(_ROOT, "futures_todo.json")
SHADOW = os.path.join(_ROOT, "repos_longonly")


def patch(src_path, cls, dst_path):
    u"""Копия с одной дописанной строкой. Возвращает True, если правка легла."""
    src = io.open(src_path, encoding="utf-8", errors="replace").read()
    # ⚠ ПРОЖИТАЯ ОШИБКА. Сначала я дописывал строку ПЕРВОЙ в тело класса и
    # написал в комментарии, что так она «перекроет позднейшее can_short =
    # True». В Python побеждает ПОСЛЕДНЕЕ присваивание — строка не перекрывала
    # ничего, и движок отказывал ровно как раньше. Поймано тем, что пробный
    # прогон дал ту же ошибку, а не тем, что я перечитал свой код.
    #
    # Правильно: ЗАМЕНИТЬ существующее объявление, а дописывать только когда
    # его нет вовсе.
    if re.search(r"^\s*can_short\s*=\s*True", src, re.M):
        out = re.sub(r"^(\s*)can_short\s*=\s*True.*$",
                     r"\1can_short = False  # заменено аудитом: spot",
                     src, flags=re.M)
    elif re.search(r"^\s*can_short\s*=\s*False", src, re.M):
        out = src                                   # уже длинная — не трогаем
    else:
        m = re.search(r"^(class\s+%s\s*\([^)]*\)\s*:\s*)$" % re.escape(cls),
                      src, re.M)
        if not m:
            return False
        ins = m.end() + 1
        out = src[:ins] + u"    can_short = False  # добавлено аудитом: spot\n" + src[ins:]
    os.makedirs(os.path.dirname(dst_path), exist_ok=True)
    io.open(dst_path, "w", encoding="utf-8").write(out)
    return True


def main():
    todo = json.load(io.open(TODO, encoding="utf-8"))
    shard, shards = 0, 1
    for i, a in enumerate(sys.argv):
        if a == "--shard" and i + 1 < len(sys.argv):
            shard, shards = [int(x) for x in sys.argv[i + 1].split("/")]
    # ⚠ Замок ИМЕНУЕТСЯ ПО ДОЛЕ. Сначала я взял одно имя на все доли, и три из
    # четырёх законно отказали — замок поймал мою же ошибку раньше, чем она
    # дала бы перемешанные карточки. Доли пишут в непересекающиеся имена
    # файлов, поэтому им и нужен свой замок каждой, а не общий.
    lock = "corpus-longonly-%d" % shard
    if not runlock.acquire(lock):
        raise SystemExit(2)
    import atexit
    atexit.register(lambda: runlock.release(lock))
    mine = [x for i, x in enumerate(todo) if i % shards == shard]
    print(u"длинная сторона: доля %d/%d = %d из %d"
          % (shard, shards, len(mine), len(todo)), flush=True)

    os.makedirs(RESULTS, exist_ok=True)
    done = skipped = 0
    for name, rel, tf in mine:
        out = os.path.join(RESULTS, "%s__longonly.json" % name)
        if os.path.exists(out):
            continue
        srcp = os.path.join(_ROOT, rel.replace("/", os.sep))
        dstp = os.path.join(SHADOW, os.path.basename(rel))
        if not os.path.exists(srcp) or not patch(srcp, name, dstp):
            skipped += 1
            print(u"  ПРАВКА НЕ ЛЕГЛА: %s (класс не найден в файле)" % name, flush=True)
            continue
        try:
            r = audit_one("long_only/" + name, dstp, name)
        except Exception as ex:
            r = {"repo": "long_only", "file": rel, "strategy": name, "static": [],
                 "runs": {k: {"level": u"НЕ ПРИМЕНИМА", "why": repr(ex)[:150],
                              "summary": None}
                          for k in ("in_sample", "out_sample", "lookahead", "recursive")}}
        r["source"] = "long_only"
        r["variant"] = "long_only"
        r["note"] = (u"can_short=False дописан аудитом; короткие сигналы "
                     u"игнорируются. ЭТО НЕ ТА СТРАТЕГИЯ, которую написал автор.")
        r["declared_timeframe"] = tf
        tmp = out + ".tmp"
        io.open(tmp, "w", encoding="utf-8").write(
            json.dumps(r, ensure_ascii=False, indent=2))
        os.replace(tmp, out)
        done += 1
        ins = r["runs"]["in_sample"]
        print(u"  [%d/%d] %-34s %s" % (done, len(mine), name[:34],
              ins.get("summary") or ins.get("why", "")), flush=True)
    print(u"ГОТОВО: посчитано %d, правка не легла у %d" % (done, skipped), flush=True)


if __name__ == "__main__":
    main()
