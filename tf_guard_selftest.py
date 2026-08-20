# -*- coding: utf-8 -*-
u"""Самопроверка сторожа предмета — ДИВЕРСИЕЙ, а не рассуждением.

Дефект 20.08: ключ `timeframe` в конфиге ПЕРЕОПРЕДЕЛЯЛ таймфрейм, объявленный
стратегией. Пятиминутки считались по часовым и выдавали правдоподобные числа.
Ключ убран — но это чинит СЛУЧАЙ. Здесь проверяется, что чинится КЛАСС:
сторож обязан поймать подмену, даже если ключ вернут.

M-17: контроль обязан УВИДЕТЬ и отказ, и норму. Сторож, который всегда
отказывает, ничего не проверяет.
"""
from __future__ import print_function
import os as _os
_ROOT = _os.environ.get("AUDIT_ROOT") or _os.path.dirname(_os.path.abspath(__file__))
import io, json, os, sys

sys.path.insert(0, _ROOT)
try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass
import harness
_ROOT = os.environ.get("AUDIT_ROOT") or os.path.dirname(os.path.abspath(__file__))

REAL = harness.CFG
SAB = _os.path.join(_ROOT, "user_data/_config_sabotage.json")
S5M = _os.path.join(_ROOT, "repos/davidzr_freqtrade-strategies/strategies/ASDTSRockwellTrading/ASDTSRockwellTrading.py")
S1H = _os.path.join(_ROOT, "user_data/strategies/MACDCrossoverWithTrend.py")
RANGE = "20190101-20190301"

ok = fail = 0


def case(n, cond, detail=u""):
    global ok, fail
    if cond:
        ok += 1
        print(u"  ✓ %s" % n)
    else:
        fail += 1
        print(u"  ✗ %s   %s" % (n, detail))


print(u"СТОРОЖ ПРЕДМЕТА — самопроверка диверсией\n")

# ── №1: САМ ДЕФЕКТ, дословно. Конфиг навязывает 1h пятиминутной стратегии.
cfg = json.load(io.open(REAL, encoding="utf-8"))
cfg["timeframe"] = "1h"
io.open(SAB, "w", encoding="utf-8").write(json.dumps(cfg, ensure_ascii=False, indent=2))
harness.CFG = SAB
src5 = io.open(S5M, encoding="utf-8", errors="replace").read()
tf5 = harness.declared_tf(src5)
case(u"№0 стратегия объявляет 5m", tf5 == "5m", u"объявлено %r" % tf5)
lvl, why, s = harness.backtest("ASDTSRockwellTrading", RANGE, path=S5M, want_tf=tf5)
case(u"№1 подмена таймфрейма ОТВЕРГНУТА", lvl == harness.NA, u"вернулось %s / %s" % (lvl, why))
case(u"№2 причина названа предметно", u"ПРЕДМЕТ НЕ ТОТ" in (why or u""), why)
case(u"№3 число НЕ отдано наружу", s is None, u"отдано %r" % (s,))
print(u"     движок сказал: %s" % why)

# ── №4-6: КОНТРОЛЬ. Тот же сторож обязан ПРОПУСТИТЬ честный прогон.
harness.CFG = REAL
src1 = io.open(S1H, encoding="utf-8", errors="replace").read()
tf1 = harness.declared_tf(src1)
lvl2, why2, s2 = harness.backtest("MACDCrossoverWithTrend", RANGE,
                                  path=None, want_tf=tf1)
case(u"№4 честный прогон ПРОПУЩЕН", lvl2 == harness.PASS, u"%s / %s" % (lvl2, why2))
case(u"№5 таймфрейм движка записан в карточку",
     bool(s2) and s2.get("used_timeframe") == tf1,
     u"%r" % (s2.get("used_timeframe") if s2 else None))
case(u"№6 пропущенные пары перечислены полем",
     bool(s2) and isinstance(s2.get("missing_pairs"), list),
     u"%r" % (s2.get("missing_pairs") if s2 else None))
if s2:
    print(u"     считано на %s, пар без истории: %s"
          % (s2.get("used_timeframe"), s2.get("missing_pairs") or u"нет"))

# ── №7-8: КОД 0 НЕ ЕСТЬ РЕЗУЛЬТАТ. freqtrade выходит С НУЛЁМ при ошибке
# конфигурации. Случай прожит: ClucCrypROI без `stoploss` давал карточку
# из одних None, помеченную как УСПЕШНЫЙ прогон.
S_ERR = os.path.join(_ROOT, "repos", "PeetCrypto_freqtrade-stuff", "ClucCrypROI.py")
if os.path.exists(S_ERR):
    lvl3, why3, s3 = harness.backtest("ClucCrypROI", RANGE, path=S_ERR, want_tf=None)
    case(u"№7 код 0 без чисел НЕ считается прогоном",
         lvl3 == harness.NA and s3 is None, u"%s / %r" % (lvl3, s3))
    case(u"№8 причина взята из ERROR движка",
         u"stoploss" in (why3 or u""), why3)
    print(u"     движок сказал: %s" % why3)
else:
    case(u"№7-8 случай ClucCrypROI доступен", False, S_ERR)

try:
    os.remove(SAB)
except Exception:
    pass
print(u"\nИТОГ: %d/%d" % (ok, ok + fail))
sys.exit(1 if fail else 0)
