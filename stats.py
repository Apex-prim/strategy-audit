# -*- coding: utf-8 -*-
u"""stats — одно число для заголовка, и все оговорки к нему рядом.

Вопрос, на который отвечает корпус:

    из стратегий, которые авторы сочли достойными публикации,
    сколько сохранили ЗНАЧИМОЕ преимущество вне окна разработки?

⚠ ВЫБОРКА СМЕЩЕНА ПО ПОСТРОЕНИЮ, и это не портит вывод, а усиливает его.
Публикуют те, у кого красив in-sample; версию, проигравшую в бэктесте, на
GitHub не выкладывают. Фильтр выживания срабатывает ДО того, как мы видим
файл. Поэтому низкая доля выживших здесь весомее, чем та же доля на
случайной выборке.

СТУПЕНИ, а не одна цифра: читателю надо видеть, сколько отсеялось на каждой,
иначе «4%» невозможно проверить.
"""
from __future__ import print_function

import glob
import io
import json
import os
import sys

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

RESULTS = "C:/tmp/audit/results"
ALPHA = 0.05
MIN_TRADES = 30          # объявлено ДО просмотра: меньше — тест бессмыслен


def load():
    out = []
    for f in glob.glob(os.path.join(RESULTS, "*.json")):
        try:
            out.append(json.load(io.open(f, encoding="utf-8")))
        except Exception:
            pass
    return out


def g(r, win, key):
    s = r["runs"].get(win, {}).get("summary")
    return s.get(key) if isinstance(s, dict) else None


def main():
    rows = load()
    n = len(rows)
    ran_in = [r for r in rows if g(r, "in_sample", "trades") is not None]
    ran_out = [r for r in ran_in if g(r, "out_sample", "trades") is not None]

    enough = [r for r in ran_out if (g(r, "in_sample", "trades") or 0) >= MIN_TRADES]
    pos_in = [r for r in enough if (g(r, "in_sample", "expectancy") or 0) > 0]
    sig_in = [r for r in pos_in
              if (g(r, "in_sample", "p_value") is not None
                  and g(r, "in_sample", "p_value") < ALPHA)]
    pos_out = [r for r in sig_in if (g(r, "out_sample", "expectancy") or 0) > 0]
    sig_out = [r for r in pos_out
               if (g(r, "out_sample", "p_value") is not None
                   and g(r, "out_sample", "p_value") < ALPHA)]

    def pct(a, b):
        return u"%.1f%%" % (100.0 * a / b) if b else u"—"

    print(u"КОРПУС: разобрано карточек %d" % n)
    print()
    print(u"  ① загрузились и отработали в окне автора   %5d   %s от всех"
          % (len(ran_in), pct(len(ran_in), n)))
    print(u"  ② отработали и ВНЕ окна                    %5d   %s"
          % (len(ran_out), pct(len(ran_out), len(ran_in))))
    print(u"  ③ сделок не меньше %d                      %5d   %s"
          % (MIN_TRADES, len(enough), pct(len(enough), len(ran_out))))
    print(u"  ④ ожидание в выборке > 0                   %5d   %s"
          % (len(pos_in), pct(len(pos_in), len(enough))))
    print(u"  ⑤ и ЗНАЧИМО (p < %.2f) в выборке           %5d   %s"
          % (ALPHA, len(sig_in), pct(len(sig_in), len(pos_in))))
    print(u"  ⑥ и ожидание ВНЕ выборки > 0               %5d   %s"
          % (len(pos_out), pct(len(pos_out), len(sig_in))))
    print(u"  ⑦ и ЗНАЧИМО вне выборки                    %5d   %s"
          % (len(sig_out), pct(len(sig_out), len(pos_out))))
    print()
    print(u"  ЗАГОЛОВОК: из %d разобранных стратегий значимое преимущество"
          % len(ran_out))
    print(u"  вне окна разработки сохранили %d — это %s."
          % (len(sig_out), pct(len(sig_out), len(ran_out))))
    print()

    # что НЕ удалось проверить — печатается, а не замалчивается
    failed = [r for r in rows if g(r, "in_sample", "trades") is None]
    if failed:
        why = {}
        for r in failed:
            w = (r["runs"]["in_sample"].get("why") or u"?")[:60]
            why[w] = why.get(w, 0) + 1
        print(u"  НЕ ПРОВЕРЕНО: %d (%s). Причины:"
              % (len(failed), pct(len(failed), n)))
        for w, c in sorted(why.items(), key=lambda kv: -kv[1])[:6]:
            print(u"    %4d  %s" % (c, w))
        print()
    print(u"  ⚠ Выборка отобрана САМИМИ АВТОРАМИ по лучшему in-sample.")
    print(u"    Это делает низкую долю выживших сильнее, а не слабее.")


if __name__ == "__main__":
    main()
