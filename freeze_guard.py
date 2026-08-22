# -*- coding: utf-8 -*-
u"""freeze_guard — правило, изменённое после данных, лишает прогон статуса.

Дисциплину «не менять правило под ответ» до сих пор соблюдал человек. Человек
устаёт, торопится и находит убедительные причины. Это делает её обещанием, а
обещание не имеет кода возврата.

ПРАВИЛО, ИСПОЛНЯЕМОЕ ЗДЕСЬ:

    t(последнее изменение лестницы)  >  t(первое наблюдение корпуса)
    ⟹  текущий прогон НЕ confirmatory, а repair-adjusted.

Обе величины берутся не из прозы:
  · t(правила)  — `git log` по файлу, где живёт LADDER;
  · t(данных)   — поле `first_card_utc` в CORPUS_RUN.json, записанное при свипе.

Если реестр называет первичный результат pre-registered, а времена говорят
обратное — это отказ, а не предупреждение.

    python freeze_guard.py             вердикт; код 1 при расхождении
    python freeze_guard.py --selftest  доказать, что проверка умеет отказать

⚠ ЧЕГО ЭТА ПРОВЕРКА НЕ ДЕЛАЕТ. Она не судит, ХОРОШЕЕ ли правило. Она отвечает
на единственный вопрос: было ли оно старше данных. Правило может быть верным и
всё равно не иметь права на confirmatory статус в этом прогоне.
"""
from __future__ import print_function

import csv
import io
import json
import os
import subprocess
import sys
import time

_HERE = os.path.dirname(os.path.abspath(__file__))
try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

# ⚠ 22.08: сторож следил ТОЛЬКО за ledger_block.py — файлом, где лежат ИМЕНА
# ступеней. Но смысл ступени живёт в коде, который её ВЫЧИСЛЯЕТ: G8 задаётся
# traps.py, G11/G12 — ledger.py. В тот день traps.py менялся трижды, смысл G8
# менялся вместе с ним, а сторож продолжал показывать позавчерашнее время.
# Ровно тот класс, что уже записан в память: проверка спрашивала про СЛОВО
# (где объявлены имена), а не про ПРЕДМЕТ (где решается судьба стратегии).
# Берём МАКСИМУМ по всем файлам, определяющим правило.
# TOTAL: список ведётся РУКОЙ — осознанный остаток. Вывести машинно нельзя,
# пока «файл, определяющий ступень» не имеет признака в коде. Риск назван:
# новый модуль с логикой ступени сюда сам не попадёт. Долг: пометить функции
# ступеней декоратором и выводить список из него.
LADDER_FILES = ["ledger_block.py", "traps.py", "ledger.py"]  # TOTAL: рукой, риск назван
LADDER_FILE = LADDER_FILES[0]          # для сообщений
RUN_FILE = "CORPUS_RUN.json"
CLAIMS_FILE = "CLAIMS.csv"
PRIMARY = "survivors under the full rule set"


def ts(epoch):
    return time.strftime("%Y-%m-%d %H:%M:%S UTC", time.gmtime(epoch))


def rule_time(files=None):
    u"""Когда правило менялось в последний раз, по git.

    Правило — это НЕ только список имён ступеней, но и код, который решает,
    кто ступень проходит. Возвращаем самое ПОЗДНЕЕ изменение среди них:
    правило не старше своей самой свежей части.
    """
    best = None
    for f in (files or LADDER_FILES):
        try:
            out = subprocess.run(
                ["git", "log", "-1", "--format=%ct", "--", f],
                cwd=_HERE, capture_output=True, timeout=30)
            v = out.stdout.decode().strip()
            if v:
                v = int(v)
                if best is None or v > best:
                    best = v
        except Exception:
            continue
    return best


def rule_parts():
    u"""Время по каждому файлу правила — чтобы вердикт можно было проверить."""
    out = {}
    for f in LADDER_FILES:
        out[f] = rule_time([f])
    return out


def data_time():
    p = os.path.join(_HERE, RUN_FILE)
    if not os.path.exists(p):
        return None
    try:
        return int(json.load(io.open(p, encoding="utf-8"))["first_card_epoch"])
    except Exception:
        return None


def claimed_class():
    p = os.path.join(_HERE, CLAIMS_FILE)
    if not os.path.exists(p):
        return None
    for r in csv.DictReader(io.open(p, encoding="utf-8", newline="")):
        if r.get("claim") == PRIMARY:
            return r.get("class")
    return None


def verdict(t_rule, t_data):
    if t_rule is None or t_data is None:
        return None, u"времена не прочитаны — статус НЕ УСТАНОВЛЕН, а не «ок»"
    if t_rule > t_data:
        return "repair-adjusted", (
            u"правило изменено через %.1f ч ПОСЛЕ первого наблюдения"
            % ((t_rule - t_data) / 3600.0))
    return "confirmatory", (
        u"правило заморожено за %.1f ч ДО первого наблюдения"
        % ((t_data - t_rule) / 3600.0))


def main():
    t_rule, t_data = rule_time(), data_time()
    v, why = verdict(t_rule, t_data)
    print(u"ladder last changed : %s" % (ts(t_rule) if t_rule else u"—"))
    print(u"first observation   : %s" % (ts(t_data) if t_data else u"—"))
    print(u"verdict             : %s" % (v or u"UNDETERMINED"))
    print(u"                      %s" % why)
    if v is None:
        return 1

    got = claimed_class()
    print(u"CLAIMS.csv says     : %s" % (got or u"—"))
    if got is None:
        print(u"⛔ первичное утверждение не найдено в CLAIMS.csv")
        return 1
    if v == "repair-adjusted" and got != "repair-adjusted":
        print(u"⛔ РАСХОЖДЕНИЕ: правило моложе данных, но результат объявлен «%s»"
              % got)
        return 1
    if v == "confirmatory" and got == "repair-adjusted":
        print(u"note: правило старше данных, но результат помечен консервативнее —"
              u" это допустимо, занижать статус можно всегда")
    print(u"согласовано")
    return 0


def selftest():
    ok = []
    ok.append((u"правило моложе данных → repair-adjusted",
               verdict(2000, 1000)[0] == "repair-adjusted"))
    ok.append((u"правило старше данных → confirmatory",
               verdict(1000, 2000)[0] == "confirmatory"))
    ok.append((u"одновременно → repair-adjusted не выдаётся",
               verdict(1000, 1000)[0] == "confirmatory"))
    ok.append((u"нет времени правила → НЕ УСТАНОВЛЕН",
               verdict(None, 1000)[0] is None))
    ok.append((u"нет времени данных → НЕ УСТАНОВЛЕН",
               verdict(1000, None)[0] is None))
    # незнание не должно читаться как «ок» — это отдельный случай
    ok.append((u"незнание не равно согласию",
               verdict(None, None)[0] is None))
    # ⚠ прожитый дефект 22.08: сторож смотрел только на файл ИМЁН ступеней,
    # а traps.py трижды менял смысл G8 — и сторож этого не видел. Случай
    # становится исполняемым: правило обязано быть НЕ СТАРШЕ своей самой
    # свежей части, и файлы, задающие ступени, обязаны быть в списке.
    parts = rule_parts()
    known = [v for v in parts.values() if v]
    ok.append((u"смысл ступени учтён, а не только её имя",
               "traps.py" in LADDER_FILES and "ledger.py" in LADDER_FILES))
    ok.append((u"правило не старше своей самой свежей части",
               (not known) or rule_time() == max(known)))
    for n, v in ok:
        print(u"  %-44s %s" % (n, u"OK" if v else u"FAILED"))
    bad = [n for n, v in ok if not v]
    print(u"self-test: %d/%d" % (len(ok) - len(bad), len(ok)))
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(selftest() if "--selftest" in sys.argv else main())
