# -*- coding: utf-8 -*-
u"""loadscan — сколько корпуса вообще ЗАГРУЖАЕТСЯ, прежде чем тратить часы.

freqtrade сам печатает столбец Status в `list-strategies`. Дешевле спросить
его, чем узнать через пять часов прогона, что треть корпуса не импортируется.
«Не смогли загрузить» — категория для отчёта, а не молчание.

⚠ ПЕРВАЯ ВЕРСИЯ ЭТОЙ ПРОВЕРКИ БЫЛА СЛЕПА. Разбор строки требовал ИМЯ
стратегии, а freqtrade у неудачной загрузки печатает в этом столбце «--».
Отказ не мог быть посчитан НИКОГДА, и проверка отрапортовала «не загрузилось
0» по корпусу, которого не видела. Поймано диверсией, не рассуждением.
Опознаём строку по ФАЙЛУ — он есть всегда, имя при отказе отсутствует.
"""
from __future__ import print_function
import io, os, re, subprocess, sys

_ROOT = os.environ.get("AUDIT_ROOT") or os.path.dirname(os.path.abspath(__file__))
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
FT = os.path.join(_ROOT, "ftenv", "Scripts", "freqtrade.exe")
CFG = os.path.join(_ROOT, "user_data", "config.json")
REPOS = os.path.join(_ROOT, "repos")

env = dict(os.environ)
env["PYTHONIOENCODING"] = "utf-8"
ROWS = re.compile(r"│\s*(\S+)\s*│\s*(\S+\.py)\s*│\s*(OK|LOAD FAILED)\s*│")

BROKEN = u'''from freqtrade.strategy import IStrategy
import this_module_does_not_exist_xyz
class BrokenOnPurpose(IStrategy):
    timeframe = '1h'
    stoploss = -0.10
    def populate_indicators(self, d, m): return d
    def populate_entry_trend(self, d, m): return d
    def populate_exit_trend(self, d, m): return d
'''


def scan(path):
    try:
        r = subprocess.run([FT, "list-strategies", "--strategy-path", path,
                            "--config", CFG], capture_output=True, timeout=300, env=env)
    except Exception:
        return []
    return ROWS.findall((r.stdout + r.stderr).decode("utf-8", "replace"))


def selftest():
    u"""Проверка обязана УМЕТЬ увидеть отказ — иначе «отказов 0» есть свойство
    прибора, а не корпуса. Подкладывается заведомо несобираемая стратегия и
    требуется, чтобы её посчитали; и тут же требуется, чтобы исправные рядом
    считались исправными — «всё сломано» такой же слепой ответ, как «всё цело».
    """
    d = os.path.join(_ROOT, "_sabotage")
    os.makedirs(d, exist_ok=True)
    io.open(os.path.join(d, "BrokenOnPurpose.py"), "w", encoding="utf-8").write(BROKEN)
    rows = scan(d)
    failed = [x for x in rows if x[2] == "LOAD FAILED"]
    okrows = [x for x in rows if x[2] == "OK"]
    good = len(failed) == 1 and failed[0][1] == "BrokenOnPurpose.py"
    print(u"  %s диверсия посчитана как отказ (%d)" % (u"OK" if good else u"ПРОВАЛ", len(failed)))
    print(u"  %s исправные рядом посчитаны исправными (%d)"
          % (u"OK" if okrows else u"ПРОВАЛ", len(okrows)))
    return 0 if (good and okrows) else 1


def main():
    seen = {}
    for d in sorted(os.listdir(REPOS)):
        p = os.path.join(REPOS, d)
        if not os.path.isdir(p):
            continue
        # TOTAL: диагностический обход, в вердикт не входит
    for sub, dirs, _ in os.walk(p):
            dirs[:] = [x for x in dirs if x not in (".git", "__pycache__", "venv")]
            for name, loc, st in scan(sub):
                # ключ — файл в своём репозитории: os.walk заходит и в
                # родителя, и в потомка, поэтому без ключа выйдут повторы
                seen.setdefault((d, loc), st)
    ok = sum(1 for v in seen.values() if v == "OK")
    bad = sum(1 for v in seen.values() if v != "OK")
    print(u"ФАЙЛОВ СО СТРАТЕГИЯМИ: %d · загрузились %d · НЕ ЗАГРУЗИЛИСЬ %d (%.1f%%)"
          % (len(seen), ok, bad, 100.0 * bad / max(1, len(seen))))
    badf = sorted(k[1] for k, v in seen.items() if v != "OK")
    if badf:
        print(u"примеры незагружаемых: %s" % u", ".join(badf[:10]))


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        print(u"loadscan — самопроверка диверсией")
        raise SystemExit(selftest())
    main()
