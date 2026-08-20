# -*- coding: utf-8 -*-
u"""power — предполётный расчёт мощности: СКОЛЬКО СТОИТ УЗНАТЬ, что стратегия работает.

ВОПРОС, КОТОРОГО НЕТ НИ В ОДНОМ АУДИТЕ. Бэктест говорит «ожидание +0.53 на
сделку». Он не говорит, СКОЛЬКО ЖИВЫХ СДЕЛОК нужно, чтобы это отличить от нуля.
А это вычислимо — и часто оказывается, что опыт не поставить за человеческую
жизнь.

ПОВОД — СВОЙ СОБСТВЕННЫЙ СЛУЧАЙ. Наш движок: валовый +6.94 бпс на сделку при
разбросе 82.9 бпс, издержка 10.00 бпс с разбросом РОВНО НОЛЬ. Чтобы различить
нужный эффект при мощности 80%, требуется 429 872 сделки и $487 952 комиссии.
Два года живой торговли были опытом, неспособным закончиться выводом —
недомощным на три порядка С ПЕРВОГО ДНЯ, и этого никто не посчитал.

ОТКУДА БЕРЁТСЯ РАЗБРОС, КОТОРОГО НЕТ В СВОДКЕ. freqtrade печатает
`Mean profit p-value`. Это t-критерий: t = mean/(SD/sqrt(n)). Зная mean, n и p,
разброс ВОССТАНАВЛИВАЕТСЯ: SD = mean*sqrt(n)/t. Ничего нового измерять не надо.

ЧТО СЧИТАЕТСЯ ОТВЕТОМ «НЕПРОВЕРЯЕМО»
  * среднее <= 0            — никакое n не докажет положительность
  * p >= 0.999              — t неотличим от нуля, разброс не восстанавливается
  * требуемые годы > 100    — опыт не поставить за жизнь

Всё это КАТЕГОРИИ, а не пропуски: «не смогли посчитать» нигде не печатается
как «хорошо».
"""
from __future__ import print_function

import glob
import io
import json
import os
import sys
from statistics import NormalDist

_ROOT = os.environ.get("AUDIT_ROOT") or os.path.dirname(os.path.abspath(__file__))
sys.stdout.reconfigure(encoding="utf-8", errors="replace")

RESULTS = os.path.join(_ROOT, "results")
WIN_DAYS = 731.0            # окно автора 2018-03-01 … 2020-03-01
POWER_Z = 0.8416            # 80% мощности
ALPHA_Z = 1.9600            # два хвоста, 0.05
LIFETIME_Y = 100.0
MIN_N = 30                  # объявлено заранее, как в STRATA_PREREG


def implied_sd(mean, n, p):
    u"""Разброс, восстановленный из p-значения. None — восстановить нельзя."""
    if n is None or n < 2 or mean is None or p is None:
        return None
    if p >= 0.999:
        return None
    # ⚠ ЗАЖИМ, А НЕ ОТКАЗ. У сильных эффектов p бывает 1.4e-65; тогда
    # 1 - p/2 схлопывается в РОВНО единицу и обратная нормаль падает.
    # Прежний сторож ловил только ноль и пропускал этот случай. Очень
    # малое p означает «эффект огромен», а не «измерить нельзя»: возвращать
    # None здесь значило бы записать сильнейший результат в «не смогли».
    p = max(p, 1e-12)
    t = NormalDist().inv_cdf(1.0 - p / 2.0)
    if t <= 1e-9:
        return None
    return abs(mean) * (n ** 0.5) / t


def required_n(mean, sd):
    if not sd or mean is None or mean <= 0:
        return None
    return ((ALPHA_Z + POWER_Z) ** 2) * (sd * sd) / (mean * mean)


def main():
    rows, biased = [], []
    for f in sorted(glob.glob(os.path.join(RESULTS, "*.json"))):
        try:
            r = json.load(io.open(f, encoding="utf-8"))
        except Exception:
            continue
        s = r["runs"]["in_sample"].get("summary")
        if not isinstance(s, dict) or s.get("trades") is None:
            continue
        n, mean, p = s.get("trades"), s.get("expectancy"), s.get("p_value")
        if n < MIN_N:
            continue
        # ⚠ ГРАНИЦА ЭТОГО ИНСТРУМЕНТА, НАЗВАННАЯ ПРЯМО. Расчёт наследует
        # оптимизм бэктеста. Если бэктест содержит заглядывание в будущее,
        # «нужно сделок» выйдет ничтожным — не потому что стратегия сильна,
        # а потому что вход в число фиктивен. Пример из этого же корпуса:
        # ichiV1, родной детектор freqtrade нашёл смещение (7 входов из 20
        # сигналов), вне выборки нарисовано +18 701 080%.
        #
        # Поэтому стратегии с найденным смещением НЕ считаются, а называются
        # отдельной категорией. И наоборот: ничтожное «нужно сделок» само
        # становится признаком того, что бэктест стоит перепроверить.
        if r["runs"].get("lookahead", {}).get("level") == u"НАЙДЕНО":
            biased.append(r["strategy"])
            continue
        sd = implied_sd(mean, n, p)
        need = required_n(mean, sd)
        rate = n / WIN_DAYS                      # сделок в сутки в окне автора
        years = (need / rate / 365.0) if (need and rate > 0) else None
        rows.append({"name": r["strategy"], "src": r.get("source"), "n": n,
                     "mean": mean, "p": p, "sd": sd, "need": need,
                     "years": years})

    corpus = [r for r in rows if r["src"] == "corpus"]
    case = [r for r in rows if r["src"] != "corpus"]

    def block(title, rs):
        print(u"\n%s — %d стратегий с числами" % (title, len(rs)))
        if not rs:
            return
        neg = [r for r in rs if r["mean"] is None or r["mean"] <= 0]
        nosd = [r for r in rs if r not in neg and r["sd"] is None]
        good = [r for r in rs if r["need"]]
        life = [r for r in good if r["years"] and r["years"] > LIFETIME_Y]
        print(u"  ожидание <= 0 — никакое n не поможет      %4d" % len(neg))
        print(u"  разброс не восстановить (p ~ 1)           %4d" % len(nosd))
        print(u"  посчитано                                 %4d" % len(good))
        if good:
            print(u"  из них НЕПРОВЕРЯЕМЫ за 100 лет            %4d   (%.0f%% от посчитанных)"
                  % (len(life), 100.0 * len(life) / len(good)))
            good.sort(key=lambda r: r["years"] if r["years"] else 9e9)
            print(u"\n  %-30s %6s %9s %9s %12s %10s"
                  % (u"стратегия", u"сделок", u"ожид.", u"разброс", u"нужно сделок", u"лет"))
            for r in good[:10]:
                print(u"  %-30s %6d %9.3f %9.2f %12s %10s"
                      % (r["name"][:30], r["n"], r["mean"], r["sd"],
                         format(int(r["need"]), ",").replace(",", " "),
                         (u"%.1f" % r["years"]) if r["years"] else u"—"))
            if len(good) > 10:
                print(u"  … и ещё %d" % (len(good) - 10))

    block(u"КОРПУС", corpus)
    block(u"РАЗБОР paulcpk", case)

    allg = [r for r in rows if r["need"]]
    if allg:
        med = sorted(r["years"] for r in allg if r["years"])
    if biased:
        print("")
        print(u"ИСКЛЮЧЕНЫ: %d стратегий с ЗАГЛЯДЫВАНИЕМ В БУДУЩЕЕ "
              u"(родной детектор freqtrade) — их ожидание фиктивно:" % len(biased))
        for _b in sorted(biased):
            print(u"    " + _b)
        print(u"\nМЕДИАНА по всем посчитанным: %.1f лет живой торговли, "
              u"чтобы доказать, что стратегия работает."
              % med[len(med) // 2])
    print(u"\nНАШ ДВИЖОК ДЛЯ СРАВНЕНИЯ: 429 872 сделки, $487 952 комиссии — "
          u"опыт, который нельзя поставить.")


if __name__ == "__main__":
    main()
