# -*- coding: utf-8 -*-
u"""ledger_block — ЕДИНСТВЕННОЕ место, где числа превращаются в текст.

ЗАЧЕМ ОТДЕЛЬНЫМ ФАЙЛОМ. Блок чисел в README обязан быть проверяем на ЧИСТОЙ
машине, где нет ни карточек `results/`, ни клонов `repos/`, ни freqtrade.
Поэтому сборка блока отделена от источника: `ledger.py` кормит её карточками,
`verify_ledger.py` — опубликованным LEDGER.csv. Реализация ОДНА, и это
существенно: две независимые реализации «одного и того же» расходятся молча,
а расхождение обнаруживается только тем, кто читает обе.

Здесь нет ни pandas, ни freqtrade, ни обращений к сети — только stdlib, иначе
проверка не пройдёт в CI и правило снова станет прозой.

ЛЕСТНИЦА МОНОТОННА ПО ЭПОХАМ. Ступени идут E0,E0,…,E1,E2,E3,E4 — эпоха не
убывает. Отсюда следует, что для восстановления всей картины достаточно ОДНОГО
поля `dropped_at`: стратегия жива до своей ступени и мертва на ней и после.
Именно поэтому CSV несёт одно поле, а не одиннадцать булевых.
"""
from __future__ import print_function

LADDER = [
    ("G0_measured",   "E0", u"обе половины посчитаны"),
    ("G1_trades",     "E0", u"сделок >= 30 в окне автора"),
    ("G2_is_pos",     "E0", u"ожидание > 0 в окне автора"),
    ("G3_is_sig",     "E0", u"p < 0.05 в окне автора"),
    ("G4_os_pos",     "E0", u"ожидание > 0 вне выборки"),
    ("G5_os_sig",     "E0", u"p < 0.05 вне выборки"),
    ("G6_lookahead",  "E0", u"нет заглядывания вперёд"),
    ("G7_recursive",  "E1", u"индикаторы не зависят от объёма истории"),
    ("G8_traps",      "E2", u"ни одной ловушки сообщества"),
    ("G9_candle",     "E3", u"длительность ИЗМЕРЕНА и не короче свечи"),
    ("G10_fdr",       "E4", u"p вне выборки проходит порог Бенджамини-Хохберга"),
]
EPOCHS = ["E0", "E1", "E2", "E3", "E4"]
GATE_EPOCH = dict((k, e) for k, e, _d in LADDER)
GATE_ORDER = dict((k, i) for i, (k, _e, _d) in enumerate(LADDER))
ALPHA = 0.05


def bh(pvals, alpha=ALPHA):
    u"""Бенджамини–Хохберг. Возвращает (порог, сколько отвергнуто).

    Повторён здесь, а не импортирован из multiplicity.py, ровно по одной
    причине: этот модуль обязан работать в CI без остального дерева. Чтобы
    копия не разошлась с оригиналом молча, `multiplicity.py` импортирует ЕЁ,
    а не наоборот — источник один, направление зависимости объявлено.
    """
    n = len(pvals)
    if not n:
        return 0.0, 0
    s = sorted(pvals)
    k = 0
    for i, p in enumerate(s, 1):
        if p <= alpha * i / n:
            k = i
    return (s[k - 1] if k else 0.0), k


def alive_at(row, gate):
    u"""Дожила ли строка ДО этой ступени (не пройдя её ещё)."""
    d = row.get("dropped_at") or ""
    return (not d) or GATE_ORDER[d] >= GATE_ORDER[gate]


def passed(row, gate):
    u"""Прошла ли строка эту ступень."""
    d = row.get("dropped_at") or ""
    return (not d) or GATE_ORDER[d] > GATE_ORDER[gate]


def survivors_at(rows, epoch):
    u"""Кто выжил бы, если применять ТОЛЬКО правила эпох <= epoch."""
    lim = EPOCHS.index(epoch)
    out = []
    for r in rows:
        d = r.get("dropped_at") or ""
        if not d or EPOCHS.index(GATE_EPOCH[d]) > lim:
            out.append(r)
    return out


def bh_population(rows):
    u"""p-значения вне выборки для поправки на множественность.

    Популяция та же, что в multiplicity.py: сделок >= 30, ожидание и
    значимость в окне автора, положительное ожидание вне его. Считается из
    полей строки, поэтому воспроизводима из опубликованного CSV."""
    p = []
    for r in rows:
        try:
            if (r.get("is_trades") or 0) < 30:
                continue
            if (r.get("is_exp") or 0) <= 0:
                continue
            ip = r.get("is_p")
            op = r.get("os_p")
            if ip is None or op is None or ip >= ALPHA:
                continue
            if (r.get("os_exp") or 0) <= 0:
                continue
            p.append(op)
        except TypeError:
            continue
    return p


def n_repos(path):
    u"""Сколько репозиториев вошло в свип.

    ⚠ ДЕФЕКТ 22.08, опубликованный. Считалось `len(src.keys())`, а
    `corpus_sources.json` — словарь из трёх ключей, где список репозиториев
    лежит внутри `repos`. В README ушло «repositories swept 3» вместо 53.

    Проверка `verify_ledger` это НЕ ПОЙМАЛА, и не могла: обе стороны считали
    одной и той же неверной формулой. Сверка двух величин, выведенных из
    общего источника, доказывает согласие, а не правильность. Отсюда второй
    заслон ниже — проверка правдоподобия, независимая от формулы.
    """
    import io as _io
    import json as _json
    try:
        src = _json.load(_io.open(path, encoding="utf-8"))
    except Exception:
        return 0
    if isinstance(src, dict):
        n = len(src["repos"]) if isinstance(src.get("repos"), list) else len(src)
    else:
        n = len(src)
    return n


def repos_plausible(n_repo, n_rows):
    u"""Заслон, не зависящий от формулы: столько стратегий из стольких
    репозиториев физически неправдоподобно. Возвращает текст жалобы или None."""
    if n_repo <= 0:
        return u"репозиториев 0 при %d стратегиях" % n_rows
    if n_rows and n_rows / float(n_repo) > 200:
        return (u"%d стратегий из %d репозиториев — %.0f на репозиторий, "
                u"похоже на ошибку счёта" % (n_rows, n_repo, n_rows / float(n_repo)))
    return None


def build(rows, n_repo):
    u"""Тот самый блок, который лежит в README между маркерами."""
    codes = sorted(set(r.get("code_md5") or "" for r in rows))
    plans = sorted(set(r.get("plan_md5") or "" for r in rows))
    thr, k_bh = bh(bh_population(rows))
    n_bh = len(bh_population(rows))

    L = [u"```"]
    L.append(u"generated by ledger.py — do not edit by hand")
    L.append(u"harness code md5   %s%s"
             % (codes[0] if codes else u"-",
                u"" if len(codes) <= 1 else u"   MIXED (%d versions)" % len(codes)))
    L.append(u"corpus plan md5    %s%s"
             % (plans[0] if plans else u"-",
                u"" if len(plans) <= 1 else u"   MIXED (%d versions)" % len(plans)))
    bad = repos_plausible(n_repo, len(rows))
    if bad:
        L.append(u"repositories swept   %d   ⚠ SUSPECT: %s" % (n_repo, bad))
    else:
        L.append(u"repositories swept   %d" % n_repo)
    L.append(u"strategies in ledger %d" % len(rows))
    L.append(u"")
    L.append(u"the ladder, and where the corpus leaves it")
    for kname, ep, _d in LADDER:
        a = sum(1 for r in rows if alive_at(r, kname))
        p = sum(1 for r in rows if passed(r, kname))
        L.append(u"  %-13s %s  %4d -> %4d" % (kname, ep, a, p))
    L.append(u"")
    L.append(u"survivors under each decision set")
    for ep in EPOCHS:
        s = survivors_at(rows, ep)
        beat = [r for r in s if r.get("beats_bh")]
        L.append(u"  rules declared up to %s   survivors %4d   beat buy-and-hold %3d"
                 % (ep, len(s), len(beat)))
    L.append(u"")
    L.append(u"Benjamini-Hochberg threshold %s over %d tests, %d rejected"
             % ((u"%.3e" % thr) if k_bh else u"none", n_bh, k_bh))
    L.append(u"```")
    return u"\n".join(L)
