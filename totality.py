# -*- coding: utf-8 -*-
u"""ТОТАЛЬНОСТЬ ПРОВЕРОК — первый прибор ассемблерного уровня.

Оператор 22.08: «Мне нужна та машина, которая не может ошибаться, если
инструкции правильные… Ты считаешь, что Ассемблер ошибается?»

Он прав, и причина техническая. Семантика инструкции ассемблера определена НА
ВСЕХ входах: `ADD` определён на любой паре регистров, деление на ноль — не
неопределённое поведение, а специфицированная ловушка `#DE`. Входа без
определённого выхода не существует.

Три из четырёх дефектов 22.08 — нарушение ровно этого:
  · контрфакт засчитал «не проверяли» как «прошло»;
  · G9_candle: отсутствующее поле прочиталось как пропуск;
  · G9 до починки: `not card.get("intracandle")` на карточке без поля.
Во всех трёх функция ЧАСТИЧНА: на входе «значения нет» определённого ответа
нет, и молча подставляется умолчание. Умолчание всегда льстивое.

ЧТО ИЩЕТ ЭТОТ ПРИБОР (по AST, не по тексту — D185: regex по питону запрещён):

  P1  результат `.get(k)` (без умолчания) попадает прямо в УСЛОВИЕ.
      Ключа нет → None → ложь. Отсутствие данных прочитано как ответ «нет».
  P2  то же под `not` — отсутствие прочитано как ответ «да».
      ⚠ 22.08: я написал было «хуже P1, льстит». НЕВЕРНО. Прибор НЕ ЗНАЕТ,
      какая ветка льстивая: в system_audit отсутствие пульса даёт FAIL, то есть
      тревогу — направление безопасное. Требование не «не делай так», а
      «ОБЪЯВИ семантику отсутствия»: пометкой `# TOTAL: причина` или кодом.
  P3  `.get(k, D)` в условии, где умолчание D само истинно/ложно молча.
      Умолчание может быть законным, но обязано быть НАЗВАНО, а не подразумеваться.
  P4  индекс `row[k]` в условии — отсутствие даёт исключение (это ЧЕСТНО,
      громкий отказ), поэтому НЕ дефект. Считается отдельно как эталон.

ЧЕГО ОН НЕ УМЕЕТ — названо, чтобы не выдать за полноту:
  · не видит частичность через переменную (`v = d.get(k)` … `if v:`) — только
    прямое употребление. Это ПОЛ, а не счёт;
  · не знает, законно ли умолчание по смыслу задачи;
  · не проверяет свойства 2 (названные входы) и 3 (детерминизм) — они следующие.

Прогон:  python totality.py [файл ...]
Код возврата 1 при находках P1/P2 — правило без кода возврата не действует.
"""
from __future__ import print_function

import ast
import io
import os
import sys

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

ROOT = os.path.dirname(os.path.abspath(__file__))

# ⚠ Здесь СТОЯЛ РУЧНОЙ СПИСОК файлов. Это ровно дефект freeze_guard того же
# дня: ответ зависел от входа, которого не было в объявленных входах, и новый
# файл молча оставался непроверенным. Список заменён на ПОЛНЫЙ ОБХОД — предмет
# проверки перечисляется машиной, а не помнится автором.
SKIP_DIRS = {".git", "__pycache__", "repos", "data", "results", "ftenv", "venv"}


def enumerate_py(root):
    out = []
    for base, dirs, files in os.walk(root):
        dirs[:] = [d for d in dirs if d not in SKIP_DIRS]
        for f in sorted(files):
            if f.endswith(".py"):
                out.append(os.path.relpath(os.path.join(base, f), root))
    return sorted(out)


class Scan(ast.NodeVisitor):
    def __init__(self, path, src):
        self.path = path
        self.lines = src.split("\n")
        self.hits = []          # (код, строка, текст)
        self.declared = []      # снято пометкой # TOTAL:
        self.honest = 0         # P4: громкий отказ

    # ── условия, в которых значение решает судьбу ────────────────────
    def _tests(self, node):
        if isinstance(node, ast.If):
            return [node.test]
        if isinstance(node, (ast.While, ast.Assert)):
            return [node.test]
        if isinstance(node, ast.IfExp):
            return [node.test]
        if isinstance(node, ast.comprehension):
            return list(node.ifs)
        return []

    def _walk_test(self, t, negated=False):
        u"""Разложить условие на элементарные проверки, помня отрицание."""
        if isinstance(t, ast.UnaryOp) and isinstance(t.op, ast.Not):
            return self._walk_test(t.operand, not negated)
        if isinstance(t, ast.BoolOp):
            out = []
            for v in t.values:
                out += self._walk_test(v, negated)
            return out
        return [(t, negated)]

    def _report(self, node, code, why):
        ln = getattr(node, "lineno", 0)
        txt = self.lines[ln - 1].strip() if 0 < ln <= len(self.lines) else u""
        # ⚠ первый прогон дал ЛОЖНОЕ срабатывание: в memory_audit словарь
        # inbound строится ПОЛНЫМ обходом всех файлов, и отсутствие ключа там
        # не «не знаю», а определённый ответ «входящих ссылок нет». Прибор не
        # может решить это за автора — но может ПОТРЕБОВАТЬ, чтобы автор
        # написал определение вслух. Пометка `# TOTAL: причина` на строке
        # снимает находку и остаётся в коде как объявленная семантика.
        if "# TOTAL:" in txt:
            self.declared.append((code, ln, txt[:96]))
            return
        self.hits.append((code, ln, txt[:96], why))

    def _check_expr(self, e, negated):
        # .get(...)
        if (isinstance(e, ast.Call) and isinstance(e.func, ast.Attribute)
                and e.func.attr == "get"):
            if len(e.args) == 1:
                self._report(e, "P2" if negated else "P1",
                             u"отсутствие ключа молча читается как «%s» — "
                             u"семантика не объявлена"
                             % (u"ДА" if negated else u"НЕТ"))
            elif len(e.args) >= 2:
                d = e.args[1]
                lit = isinstance(d, ast.Constant)
                self._report(e, "P3",
                             u"умолчание %s подразумевается, а не объявлено"
                             % (repr(d.value) if lit else u"выражение"))
        # row[k] — падает при отсутствии: честно
        elif isinstance(e, ast.Subscript):
            self.honest += 1
        # bool(x.get(...))
        elif (isinstance(e, ast.Call) and isinstance(e.func, ast.Name)
                and e.func.id == "bool" and e.args):
            self._check_expr(e.args[0], negated)

    def generic_visit(self, node):
        for t in self._tests(node):
            for e, neg in self._walk_test(t):
                self._check_expr(e, neg)
        ast.NodeVisitor.generic_visit(self, node)


def scan(path):
    src = io.open(path, encoding="utf-8").read()
    try:
        tree = ast.parse(src)
    except SyntaxError as exc:
        return None, exc
    s = Scan(path, src)
    s.visit(tree)
    return s, None


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    files = args or enumerate_py(ROOT)
    total = {"P1": 0, "P2": 0, "P3": 0}
    honest = 0
    declared = 0
    unread = []
    print(u"── ТОТАЛЬНОСТЬ: вход без определённого выхода")
    print()
    for rel in files:
        p = rel if os.path.isabs(rel) else os.path.join(ROOT, rel)
        if not os.path.exists(p):
            unread.append(rel)
            continue
        s, err = scan(p)
        if s is None:
            unread.append(u"%s (%s)" % (rel, err.__class__.__name__))
            continue
        honest += s.honest
        declared += len(s.declared)
        bad = [h for h in s.hits if h[0] in ("P1", "P2")]
        soft = [h for h in s.hits if h[0] == "P3"]
        for c, _l, _t, _w in s.hits:
            total[c] = total.get(c, 0) + 1
        if bad or soft:
            print(u"  %s" % rel)
            for c, ln, txt, why in sorted(bad, key=lambda x: x[1]):
                print(u"    ⛔ %s:%-4d %s" % (c, ln, txt))
                print(u"           %s" % why)
            if soft:
                print(u"    · P3 умолчаний в условиях: %d" % len(soft))
            print()

    print(u"=" * 62)
    print(u"  P1 отсутствие → «НЕТ»          %4d" % total["P1"])
    print(u"  P2 отсутствие → «ДА», не объявлено%4d" % total["P2"])
    print(u"  P3 умолчание не объявлено      %4d" % total["P3"])
    print(u"  P4 громкий отказ (эталон)      %4d" % honest)
    print(u"  объявлено тотальным (# TOTAL)  %4d" % declared)
    if unread:
        # непрочитанный файл — НЕ «ок»: это и есть тот самый дефект
        print(u"  ⛔ НЕ ПРОЧИТАНО                %4d  — %s"
              % (len(unread), ", ".join(unread[:4])))
    print()
    print(u"⚠ ПОЛ, А НЕ СЧЁТ: частичность через переменную (v = d.get(k); if v:)")
    print(u"  этот прибор не видит. Свойства «названные входы» и «детерминизм»")
    print(u"  не проверяются вовсе. Число ниже — нижняя граница.")
    return 1 if (total["P1"] or total["P2"] or unread) else 0


if __name__ == "__main__":
    sys.exit(main())
