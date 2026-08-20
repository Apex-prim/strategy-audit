# -*- coding: utf-8 -*-
u"""Догрузка свечей ИЗ МЕСЯЧНЫХ АРХИВОВ Binance, а не постраничным API.

ПОЧЕМУ ПЕРЕПИСАНО. Постраничный вариант (`fetch_tf.py`) отдаёт 1000 свечей за
1.9 с. Для 5m это 29 минут НА ПАРУ, для 1m — 19 часов на пару. Он не был
сломан, он был непригоден по времени, и 25 минут работы дали ноль файлов.
Месячный архив отдаёт 8928 пятиминуток за 1.55 с — тот же источник, те же
данные, в 11 раз быстрее (для 1m — в 60).

ЧЕСТНОСТЬ ПО ГРАНИЦАМ. Пара, не листившаяся в этом месяце, даёт 404. Это НЕ
ошибка сети и не повод молчать: месяц пропускается, а число пропусков
печатается в конце. Отсутствие данных обязано быть видно как отсутствие,
а не как короткий ряд.
"""
from __future__ import print_function
import os as _os
_ROOT = _os.environ.get("AUDIT_ROOT") or _os.path.dirname(_os.path.abspath(__file__))
import io, os, sys, time, urllib.error, urllib.request, zipfile

sys.path.insert(0, _ROOT)
import pandas as pd

OUT = _os.path.join(_ROOT, "user_data/data/binance")
PAIRS = {"BTCUSDT": "BTC_USDT", "LTCUSDT": "LTC_USDT", "ETHUSDT": "ETH_USDT",
         "XRPUSDT": "XRP_USDT", "ADAUSDT": "ADA_USDT", "XLMUSDT": "XLM_USDT",
         "XMRUSDT": "XMR_USDT", "DASHUSDT": "DASH_USDT"}
BASE = "https://data.binance.vision/data/spot/monthly/klines/%s/%s/%s-%s-%s.zip"
DAILY = "https://data.binance.vision/data/spot/daily/klines/%s/%s/%s-%s-%s.zip"
# Месячные архивы кончаются последним ПОЛНЫМ месяцем. Без дневного добора
# 5m обрывались на 2026-07-31, а часовые шли до 2026-08-20 — разные окна у
# разных таймфреймов, то есть несравнимые прогоны. Дыра в 20 дней меньше
# процента, и именно поэтому её легко не заметить.
TAIL_DAYS = ["2026-08-%02d" % d for d in range(1, 21)]
TF = sys.argv[1] if len(sys.argv) > 1 else "5m"
Y0, M0, Y1, M1 = 2018, 3, 2026, 7
RETRY = 4


def months():
    y, m = Y0, M0
    while (y, m) <= (Y1, M1):
        yield y, m
        m += 1
        if m == 13:
            y, m = y + 1, 1


def grab(sym, tf, tag, daily=False):
    u"""(строки, статус). Статус: ok | нет в архиве | СЕТЬ."""
    url = (DAILY if daily else BASE) % (sym, tf, sym, tf, tag)
    for attempt in range(RETRY):
        try:
            raw = urllib.request.urlopen(url, timeout=60).read()
        except urllib.error.HTTPError as e:
            if e.code == 404:
                return [], u"нет в архиве"
            time.sleep(1 + attempt)
            continue
        except Exception:
            time.sleep(1 + attempt)
            continue
        z = zipfile.ZipFile(io.BytesIO(raw))
        rows = []
        for line in z.read(z.namelist()[0]).decode().splitlines():
            p = line.split(",")
            if len(p) < 6 or not p[0][:1].isdigit():   # шапка новых архивов
                continue
            ts = int(float(p[0]))
            if ts > 1e14:                              # микросекунды с 2025-го
                ts //= 1000
            rows.append((ts, float(p[1]), float(p[2]),
                         float(p[3]), float(p[4]), float(p[5])))
        return rows, u"ok"
    return [], u"СЕТЬ"


def main():
    # Тот же замок, что у corpus.py: два загрузчика на одну папку свечей —
    # тот же класс дефекта, и он у меня уже случился (20.08).
    import runlock
    if not runlock.acquire("fetch"):
        raise SystemExit(2)
    import atexit
    atexit.register(lambda: runlock.release("fetch"))
    os.makedirs(OUT, exist_ok=True)
    force = "--refill" in sys.argv
    todo = [(s, f) for s, f in PAIRS.items()
            if force or not (os.path.exists(os.path.join(OUT, "%s-%s.feather" % (f, TF)))
                             and os.path.getsize(os.path.join(OUT, "%s-%s.feather" % (f, TF))) > 100000)]
    print(u"ТАЙМФРЕЙМ %s · пар к загрузке %d из %d" % (TF, len(todo), len(PAIRS)), flush=True)
    for sym, ft in todo:
        t0 = time.time()
        rows, gaps, neterr = [], [], 0
        for y, m in months():
            r, st = grab(sym, TF, "%04d-%02d" % (y, m))
            if st == u"ok":
                rows += r
            elif st == u"нет в архиве":
                gaps.append("%04d-%02d" % (y, m))
            else:
                neterr += 1
        tail = 0
        for day in TAIL_DAYS:                     # добор незакрытого месяца
            r, st = grab(sym, TF, day, daily=True)
            if st == u"ok":
                rows += r
                tail += len(r)
            elif st != u"нет в архиве":
                neterr += 1
        if not rows:
            print(u"  ✗ %-9s НИ ОДНОГО МЕСЯЦА (сетевых отказов %d)" % (sym, neterr), flush=True)
            continue
        d = pd.DataFrame(rows, columns=["ts", "open", "high", "low", "close", "volume"])
        d = d.drop_duplicates("ts").sort_values("ts")
        d["date"] = pd.to_datetime(d["ts"], unit="ms", utc=True)
        d[["date", "open", "high", "low", "close", "volume"]] \
            .reset_index(drop=True).to_feather(os.path.join(OUT, "%s-%s.feather" % (ft, TF)))
        note = u""
        if gaps:
            note += u" · месяцев без листинга %d (с %s)" % (len(gaps), gaps[0])
        note += u" · добор дней %d" % tail
        if neterr:
            note += u" · СЕТЕВЫХ ОТКАЗОВ %d — ряд НЕПОЛОН" % neterr
        print(u"  ✓ %-9s %8d свечей  %s … %s  за %.0f с%s"
              % (sym, len(d), str(d["date"].iloc[0])[:10], str(d["date"].iloc[-1])[:10],
                 time.time() - t0, note), flush=True)
    print(u"ГОТОВО %s" % TF, flush=True)


if __name__ == "__main__":
    main()
