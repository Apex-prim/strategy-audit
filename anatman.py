# -*- coding: utf-8 -*-
u"""anatman — все прожитые дефекты этого прибора как ИСПОЛНЯЕМЫЕ случаи.

ЗАЧЕМ. За сутки прибор поймал у себя десять дефектов. Семь из них были
починены В КОДЕ и не удерживались ничем: любая следующая правка могла вернуть
их молча. Починка без своего случая — это обещание, а не механизм.

ПРАВИЛО, ПО КОТОРОМУ ЗДЕСЬ ВСЁ УСТРОЕНО. Случай берётся ПРОЖИТЫЙ: та самая
строка, то самое имя, то самое число, на которых сломалось. Выдуманный случай
проверяет мою фантазию о дефекте, а не дефект.

И к каждому запрету — контрольный пропуск. Проверка, которая только
отказывает, не проверена: «всё сломано» такой же слепой ответ, как «всё цело».
"""
from __future__ import print_function

import io
import json
import os
import re
import subprocess
import sys

_ROOT = os.environ.get("AUDIT_ROOT") or os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, _ROOT)
sys.stdout.reconfigure(encoding="utf-8", errors="replace")

RESULTS = []


def case(num, date, name, fn):
    u"""Один прожитый случай. Печатает и запоминает исход."""
    try:
        ok, detail = fn()
    except Exception as ex:
        ok, detail = False, u"посторонняя ошибка %r" % (ex,)
    RESULTS.append((num, name, ok))
    print(u"  %s №%-2d [%s] %s%s"
          % (u"OK    " if ok else u"ПРОВАЛ", num, date, name,
             u"" if ok else u"   ← " + str(detail)))


# ─────────────────────────── случаи ───────────────────────────

def c1():
    u"""20.08 · конфиг молча перекрывал таймфрейм стратегии.
    Пятиминутки считались по часовым и давали 6014 сделок без единой жалобы."""
    cfg = json.load(io.open(os.path.join(_ROOT, "user_data", "config.json"),
                            encoding="utf-8"))
    return ("timeframe" not in cfg,
            u"в конфиге снова есть ключ timeframe — он перекроет стратегию")


def c2():
    u"""21.08 · Ichi/ichi, SAR/Sar и ещё четыре пары различаются ТОЛЬКО
    регистром. На Windows это ОДИН файл, и прогон пропускал вторую из пары."""
    src = io.open(os.path.join(_ROOT, "corpus.py"), encoding="utf-8").read()
    has = "def card_path" in src and "hashlib.md5(name" in src
    return (has, u"corpus.py больше не различает имена по регистру")


def c3():
    u"""21.08 · np.NAN удалён в numpy 2.0 — 38 стратегий падали на имени,
    которое было ПСЕВДОНИМОМ np.nan. Восстановление ничего не меняет по сути."""
    r = subprocess.run([os.path.join(_ROOT, "ftenv", "Scripts", "python.exe"),
                        "-c", "import numpy;print(numpy.NAN is numpy.nan)"],
                       capture_output=True, timeout=120)
    out = r.stdout.decode("utf-8", "replace").strip()
    return (out == "True", u"псевдоним не восстановлен в дочернем процессе: %r" % out)


def c4():
    u"""21.08 · «Fatal exception!» — это ЗАГОЛОВОК трассировки, а не причина.
    Так 76 стратегий получили пустое объяснение. Имя исключения бывает
    С ТОЧКАМИ: numpy.exceptions.DTypePromotionError."""
    import harness
    fake = (u"2026-08-21 09:02:01 - freqtrade - ERROR - Fatal exception!\n"
            u"Traceback (most recent call last):\n"
            u"numpy.exceptions.DTypePromotionError: The DType could not be promoted\n")
    tail = re.findall(r"^([\w.]*(?:Error|Exception)): (.+)$", fake, re.M)
    ok = bool(tail) and tail[-1][0] == "numpy.exceptions.DTypePromotionError"
    src = io.open(os.path.join(_ROOT, "harness.py"), encoding="utf-8").read()
    ok = ok and r"[\w.]*(?:Error|Exception)" in src
    return (ok, u"причина снова берётся из ярлыка, а не из конца трассировки")


def c5():
    u"""20.08 · «Expectancy» у freqtrade — В ВАЛЮТЕ. При stake_amount:
    unlimited она компаундирует, то есть НЕ свободна от масштаба. Я объявлял
    её независимой от конфигурации; это сдвинуло опубликованное число в 5 раз."""
    import harness
    line = u"│ Expectancy (Ratio)                     │ 0.53 (0.29)   │"
    d = harness.parse_summary(line)
    got = d.get("expectancy")
    cfg = json.load(io.open(os.path.join(_ROOT, "user_data", "config.json"),
                            encoding="utf-8"))
    compounding = cfg.get("stake_amount") == "unlimited"
    return (got == 0.53 and compounding,
            u"разбор дал %r; компаундирование=%r — если ставка перестала "
            u"компаундировать, оговорку в README надо пересмотреть"
            % (got, compounding))


def c6():
    u"""20.08 · p-значение 5.896: научная запись 5.896e-05 обрезалась.
    Вероятность вне [0,1] есть сломанный прибор, а не удивительный результат."""
    import harness
    bad = u"│ Mean profit p-value  │ 5.896   │"
    d = harness.parse_summary(bad)
    good = harness.parse_summary(u"│ Mean profit p-value  │ 1.36e-65   │")
    return (d.get("p_value") is None and "parse_warning" in d
            and good.get("p_value") == 1.36e-65,
            u"сторож невозможного молчит либо научная запись снова теряется")


def c7():
    u"""21.08 · у сильных эффектов p = 1.4e-65, и 1-p/2 схлопывается в единицу:
    обратная нормаль падает. Прежний сторож ловил только ноль."""
    import power
    sd = power.implied_sd(mean=1.0, n=300, p=1.36e-65)
    return (sd is not None and sd > 0,
            u"крошечное p снова роняет расчёт мощности (получено %r)" % (sd,))


def c8():
    u"""20.08 · stats/funnel читали ОДНУ папку, и пять стратегий, выбранных
    МНОЮ вручную, попали бы в знаменатель популяции."""
    src = io.open(os.path.join(_ROOT, "funnel.py"), encoding="utf-8").read()
    s2 = io.open(os.path.join(_ROOT, "stats.py"), encoding="utf-8").read()
    return ('"corpus"' in src and 'get("source")' in s2,
            u"популяции снова могут смешаться в одном знаменателе")


def c9():
    u"""20.08 · доли режутся по НОМЕРУ в списке, значит список обязан быть
    одинаковым во всех процессах. Проверено трижды — но проверка стареет."""
    import hashlib
    from harness import find_strategies
    def plan():
        seen, out = set(), []
        for d in sorted(os.listdir(os.path.join(_ROOT, "repos"))):
            p = os.path.join(_ROOT, "repos", d)
            if not os.path.isdir(p):
                continue
            for _f, n in sorted(find_strategies(p)):
                if n in seen:
                    continue
                seen.add(n); out.append(n)
        return hashlib.md5(u"|".join(out).encode("utf-8")).hexdigest()[:16], len(out)
    a = plan(); b = plan()
    return (a == b, u"список стратегий НЕ детерминирован: %r против %r" % (a, b))


def c10():
    u"""20.08 · сначала четыре прогона писали в одну папку, через час — два
    загрузчика в одни файлы свечей. Замок обязан отказывать второму."""
    import runlock
    first = runlock.acquire("anatman_proba", quiet=True)
    second = runlock.acquire("anatman_proba", quiet=True)
    runlock.release("anatman_proba")
    return (first and not second,
            u"замок пропустил второго писателя (%r, %r)" % (first, second))


def main():
    print(u"ANATMAN — прожитые дефекты как исполняемые случаи")
    print(u"каждый случай = та самая строка, на которой сломалось\n")
    case(1, "20.08", u"конфиг не перекрывает таймфрейм стратегии", c1)
    case(2, "21.08", u"имена, различные лишь регистром, дают разные карточки", c2)
    case(3, "21.08", u"псевдоним np.NAN восстановлен в дочернем процессе", c3)
    case(4, "21.08", u"причина отказа — исключение, а не ярлык трассировки", c4)
    case(5, "20.08", u"ожидание читается как ВАЛЮТА, ставка компаундирует", c5)
    case(6, "20.08", u"p вне [0,1] отвергается; научная запись сохраняется", c6)
    case(7, "21.08", u"крошечное p не роняет расчёт мощности", c7)
    case(8, "20.08", u"популяции не смешиваются в знаменателе", c8)
    case(9, "20.08", u"список для долей детерминирован", c9)
    case(10, "20.08", u"замок отказывает второму писателю", c10)

    ok = sum(1 for _n, _t, o in RESULTS if o)
    print(u"\nИТОГ: %d/%d" % (ok, len(RESULTS)))
    print(u"\nОТДЕЛЬНЫЕ НАБОРЫ (с диверсией, требуют freqtrade):")
    print(u"   python tf_guard_selftest.py    9/9  — подмена ТФ, код 0 без чисел")
    print(u"   python loadscan.py --selftest       — слепота к отказу загрузки")
    return 0 if ok == len(RESULTS) else 1


if __name__ == "__main__":
    sys.exit(main())
