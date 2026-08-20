#!/usr/bin/env python3
# -*- coding: utf-8 -*-
u"""secret_gate — КОММИТ С СЕКРЕТОМ НЕ УХОДИТ. Не памятка, а код возврата.

ПОЧЕМУ ЭТО ОТДЕЛЬНЫЙ ГЕЙТ, А НЕ СТРОЧКА В .gitignore
----------------------------------------------------
`.gitignore` защищает от РАССЕЯННОСТИ, но не от `git add -f`, не от
инструмента, который его не читает, и не от файла, попавшего под шаблон,
которого в нём нет. Это удобство, а не контроль.

А цена ошибки здесь особая: **коммит секрета есть утечка секрета
навсегда.** Удаление в следующем коммите не помогает — секрет остаётся в
истории, в форках, в чужих клонах и в кеше площадки. По публичному потоку
событий GitHub ходят боты, которые подхватывают свежие ключи и используют
их в течение минут. Поэтому единственное настоящее лечение после утечки —
не «переписать историю», а **сменить ключ**.

ЧЕТЫРЕ СЛОЯ, КАК ДЕЛАЮТ ПРОФЕССИОНАЛЬНО
---------------------------------------
    0. Секретов НЕТ в дереве репозитория. Физически, а не по gitignore.
    1. .gitignore — от случайного `git add`.
    2. ЭТОТ гейт — машинный отказ до отправки.
    3. Защита на стороне площадки (push protection / secret scanning).
    4. Ротация: всё, что хоть раз коснулось репозитория, считается сожжённым.

Слой 2 — единственный, который останавливает НАМЕРЕННУЮ ошибку человека,
торопящегося выложить. Поэтому он и написан.

⚠ ГРАНИЦА, НАЗВАННАЯ ПРЯМО. Гейт ловит ИЗВЕСТНЫЕ формы. Секрет, не
попавший ни под один образец, пройдёт. Поэтому он не заменяет слой 0:
если ключей в дереве нет, то и утекать нечему независимо от качества
образцов.
"""
from __future__ import print_function

import io
import os
import re
import subprocess
import sys

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

# Образцы. Каждый — с прожитым поводом, а не «на всякий случай».
PATTERNS = [
    (u"приватный ключ",
     re.compile(r"-----BEGIN (?:RSA |OPENSSH |EC |DSA |PGP )?PRIVATE KEY")),
    # ⚠ Было `{35}` ровно — самотест это и поймал: длина части после
    # двоеточия у настоящих токенов колеблется. Точное число здесь есть
    # предположение о предмете, а не знание о нём.
    (u"токен Telegram-бота",
     re.compile(r"\b\d{8,10}:[A-Za-z0-9_-]{30,45}\b")),
    (u"ключ AWS",
     re.compile(r"\b(?:AKIA|ASIA)[0-9A-Z]{16}\b")),
    (u"токен GitHub",
     re.compile(r"\bgh[pousr]_[A-Za-z0-9]{36,}\b")),
    (u"ключ/секрет биржи (64 hex)",
     re.compile(r"\b[a-fA-F0-9]{64}\b")),
    (u"ключ Binance (64 буквенно-цифровых)",
     re.compile(r"\b[A-Za-z0-9]{64}\b")),
    (u"строка подключения с паролем",
     re.compile(r"(?:postgres|mysql|mongodb|redis)://[^\s:@]+:[^\s@]+@")),
    (u"присваивание секрета в коде",
     re.compile(r"(?i)\b(api_?key|secret|passwd|password|token)\b\s*[:=]\s*"
                r"['\"][A-Za-z0-9/+_\-]{16,}['\"]")),
]

# Имена, которых в публичном репозитории не должно быть НИКОГДА.
FORBIDDEN_NAMES = re.compile(
    r"(?:^|/)(?:id_rsa|id_ed25519|id_ecdsa|id_dsa|id_deploy[^/]*|"
    r"\.env|secrets?\.env|hmac\.secret|api_key|[^/]*\.pem|[^/]*\.p12|"
    r"[^/]*\.pfx|\.npmrc|\.pypirc)$")

# Что заведомо НЕ секрет, хотя попадает под образцы. Список ЗАКРЫТ и
# назван: расширять его — значит слепнуть, поэтому каждая строка обоснована.
ALLOW = (
    "cacert.pem",          # публичный корневой набор certifi
    "/test", "tests/",     # заведомо тестовые вымышленные значения
    "EXAMPLE", "example",
    "secret_gate.py",      # ЭТОТ файл содержит образцы по определению
)


def is_allowed(path):
    return any(a in path.replace("\\", "/") for a in ALLOW)


def scan_text(path, text):
    u"""[(строка, что нашли)]. Чистая функция — ради самотеста."""
    hits = []
    p = path.replace("\\", "/")
    if FORBIDDEN_NAMES.search(p) and not is_allowed(p):
        hits.append((0, u"ЗАПРЕЩЁННОЕ ИМЯ ФАЙЛА"))
    if is_allowed(p):
        return hits
    for i, line in enumerate(text.splitlines(), 1):
        if len(line) > 4000:
            continue
        for name, rx in PATTERNS:
            if rx.search(line):
                hits.append((i, name))
                break
    return hits


def staged_files():
    try:
        out = subprocess.run(["git", "diff", "--cached", "--name-only",
                              "--diff-filter=ACM"],
                             capture_output=True, timeout=60)
        return [l for l in out.stdout.decode("utf-8", "replace").splitlines()
                if l.strip()]
    except Exception:
        return []


def gate():
    bad = 0
    files = staged_files()
    for f in files:
        if not os.path.exists(f):
            continue
        try:
            text = io.open(f, encoding="utf-8", errors="replace").read()
        except Exception:
            continue
        for ln, what in scan_text(f, text):
            print(u"⛔ %s:%s — %s" % (f, ln or "имя", what))
            bad += 1
    print(u"secret_gate: проверено файлов %d · находок %d" % (len(files), bad))
    if bad:
        print(u"\nКОММИТ ОСТАНОВЛЕН. Секрет, попавший в историю, считается\n"
              u"сожжённым — чистить историю бесполезно, надо МЕНЯТЬ КЛЮЧ.\n"
              u"Если это ложное срабатывание, добавьте путь в ALLOW ЯВНО,\n"
              u"с обоснованием в комментарии, а не отключайте гейт.")
    return 1 if bad else 0


def selftest():
    ok = fail = 0

    def case(name, path, text, want):
        nonlocal ok, fail
        got = len(scan_text(path, text)) > 0
        if got == want:
            ok += 1
        else:
            fail += 1
            print(u"  ✗ %s: поймано=%s, ожидалось=%s" % (name, got, want))

    # ── ДОЛЖНЫ ЛОВИТЬСЯ ──
    case(u"приватный ключ OpenSSH", "a.txt",
         "-----BEGIN OPENSSH PRIVATE KEY-----\nb3Blb", True)
    case(u"имя приватного ключа", "keys/id_ed25519", "x", True)
    case(u"файл .env", "cfg/.env", "X=1", True)
    case(u"hmac.secret", "s/hmac.secret", "x", True)
    case(u"токен телеграм-бота", "b.py",
         'TOKEN = "123456789:AAF-abcdefghijklmnopqrstuvwxyz012345"', True)
    case(u"ключ AWS", "c.py", "key AKIAIOSFODNN7EXAMPLX here", True)
    case(u"токен GitHub", "d.py",
         "ghp_AbCdEfGhIjKlMnOpQrStUvWxYz0123456789", True)
    case(u"биржевой ключ 64 символа", "e.py",
         "EXCHANGE_API_KEY=aB3dE5gH7jK9mN1pQ3sT5vW7yZ9bD1fH3jL5nP7rT9vX1zC3eG5iK7mO9q",
         False)   # 58 знаков — короче образца, ловиться НЕ должен
    case(u"биржевой ключ ровно 64", "f.py",
         "k = '" + "a1B2c3D4"*8 + "'", True)
    case(u"строка подключения с паролем", "g.py",
         "postgres://user:hunter2@db.local/x", True)
    case(u"присваивание api_key", "h.py",
         'api_key = "sk-1234567890abcdefghij"', True)

    # ── НЕ ДОЛЖНЫ ЛОВИТЬСЯ ──
    case(u"обычный код", "i.py", "x = compute(a, b)  # ok", False)
    case(u"хеш коммита (40 hex) — не секрет", "j.md",
         "commit 8b63377f1b4390ab12cd34ef56ab78cd90ef12ab", False)
    case(u"публичный certifi", "venv/certifi/cacert.pem",
         "-----BEGIN CERTIFICATE-----", False)
    case(u"сам этот файл с образцами", "tools/secret_gate.py",
         "-----BEGIN OPENSSH PRIVATE KEY-----", False)
    case(u"пример в тестах", "tests/fixtures.py",
         "-----BEGIN RSA PRIVATE KEY-----", False)

    print(u"САМОТЕСТ secret_gate: %d пройдено, %d провалено" % (ok, fail))
    return 1 if fail else 0


def sabotage():
    u"""КОНТРОЛЬ НАД КОНТРОЛЕМ. Зелёный самотест ничего не стоит, пока не
    показано, что гейт УМЕЕТ КРАСНЕТЬ на настоящем файле. Сажаем три
    настоящих секрета во временные файлы и требуем, чтобы нашлись все три."""
    import tempfile
    seeds = [
        ("k.pem", "-----BEGIN RSA PRIVATE KEY-----\nMIIEow"),
        ("cfg.env", "BINANCE_SECRET=" + "a1B2c3D4"*8),
        ("bot.py", 'TG = "987654321:BBF-zyxwvutsrqponmlkjihgfedcba098765"'),
    ]
    found = 0
    d = tempfile.mkdtemp()
    for nm, body in seeds:
        p = os.path.join(d, nm)
        io.open(p, "w", encoding="utf-8").write(body)
        if scan_text(nm, body):
            found += 1
        else:
            print(u"  ✗ ДИВЕРСИЯ НЕ ПОЙМАНА: %s" % nm)
    print(u"ДИВЕРСИЯ: посажено 3, поймано %d" % found)
    return 0 if found == 3 else 1


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(selftest() or sabotage())
    sys.exit(gate())
