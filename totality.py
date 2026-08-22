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

  P5  ЧЕРЕЗ ПЕРЕМЕННУЮ: `v = d.get(k)` … `if v:` — та же частичность, просто
      разнесённая на две строки. Закрыта 22.08: пока её не было, ноль находок
      держался на слепоте прибора, а не на качестве кода.
      Снимается явной развилкой по `is None` где-либо в той же функции.
  P6  ДЕТЕРМИНИЗМ (свойство 3): время, случайность, порядок файловой системы и
      обход множества — вход, которого нет в объявленных входах. Тот же вердикт
      на тех же данных обязан воспроизводиться.
  P7  ПРЕДМЕТ ПРОВЕРКИ ПЕРЕЧИСЛЕН РУКОЙ (свойство 2): список файлов/модулей
      литералом, по которому идёт обход. Ровно дефект freeze_guard и первый
      дефект этого прибора: новый файл молча остаётся непроверенным.

ЧЕГО ОН НЕ УМЕЕТ — названо, чтобы не выдать за полноту:
  · не прослеживает значение через возврат функции и через поля объектов;
  · не знает, законно ли умолчание по смыслу задачи;
  · P7 узнаёт список по виду имени (.py/.json/путь), а не по употреблению.

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
    # TOTAL: порядок обхода не важен — результат сортируется перед возвратом
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
        self.exempt = set()     # снято по существу (sorted вокруг обхода)

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
        # ⚠ 22.08: пометку принимали ТОЛЬКО на самой строке, и объявление,
        # написанное прилегающим комментарием сверху, не засчитывалось. Автор
        # пишет пояснение над строкой — это нормальный способ, и прибор обязан
        # его понимать, иначе он вынуждает писать неудобно ради своей простоты.
        if "# TOTAL:" in txt or self._declared_above(ln):
            self.declared.append((code, ln, txt[:96]))
            return
        self.hits.append((code, ln, txt[:96], why))

    def _declared_above(self, ln):
        u"""Прилегающий сверху блок комментариев принадлежит этой строке."""
        i = ln - 2
        while i >= 0:
            t = self.lines[i].strip()
            if not t.startswith("#"):
                return False
            if "# TOTAL:" in t or t.startswith("# TOTAL"):
                return True
            i -= 1
        return False

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

    # ── P5: частичность, разнесённая на две строки ───────────────────
    def visit_FunctionDef(self, node):
        risky = {}          # имя → строка, где взято из .get()
        guarded = set()     # имя, для которого есть развилка по None
        for n in ast.walk(node):
            if isinstance(n, ast.Assign) and len(n.targets) == 1                     and isinstance(n.targets[0], ast.Name)                     and isinstance(n.value, ast.Call)                     and isinstance(n.value.func, ast.Attribute)                     and n.value.func.attr == "get"                     and len(n.value.args) == 1:
                risky.setdefault(n.targets[0].id, n.lineno)
            if isinstance(n, ast.Compare):
                for side in [n.left] + list(n.comparators):
                    if isinstance(side, ast.Name) and any(
                            isinstance(c, ast.Constant) and c.value is None
                            for c in n.comparators):
                        guarded.add(side.id)
        for n in ast.walk(node):
            for t in self._tests(n):
                for e, neg in self._walk_test(t):
                    if isinstance(e, ast.Name) and e.id in risky                             and e.id not in guarded:
                        self._report(e, "P5",
                                     u"`%s` взято из .get() на строке %d и "
                                     u"решает ветку без развилки по None"
                                     % (e.id, risky[e.id]))
        self.generic_visit(node)

    visit_AsyncFunctionDef = visit_FunctionDef

    # ── P6: недетерминизм ────────────────────────────────────────────
    NONDET = {("time", "time"), ("time", "localtime"), ("time", "gmtime"),
              ("random", "random"), ("random", "choice"), ("random", "shuffle"),
              ("os", "listdir"), ("os", "walk"), ("datetime", "now"),
              ("datetime", "today"), ("uuid", "uuid4")}

    ORDER_ONLY = {("os", "listdir"), ("os", "walk")}

    def visit_Call(self, node):
        # ⚠ уточнено 22.08: `sorted(os.listdir(...))` УЖЕ детерминирован по
        # порядку, и считать его дефектом — то же самое, что считать ловушкой
        # широкий трейлинг. Прибор обязан отличать «недетерминизм» от
        # «перечисления». Сортированный обход снимается по существу; время и
        # случайность — только объявлением, потому что законность зависит от
        # употребления (в freeze_guard время и ЕСТЬ предмет измерения).
        f = node.func
        if isinstance(f, ast.Name) and f.id == "sorted":
            # обход может стоять и прямо в аргументе, и внутри генератора:
            # `sorted(os.listdir(p))` и `sorted(f for f in os.listdir(p) ...)`
            # — оба упорядочены. Ищем во ВСЁМ поддереве аргументов.
            for a in node.args:
                for sub in ast.walk(a):
                    if isinstance(sub, ast.Call) and isinstance(sub.func, ast.Attribute)                             and isinstance(sub.func.value, ast.Name)                             and (sub.func.value.id, sub.func.attr) in self.ORDER_ONLY:
                        self.exempt.add(id(sub))
        if isinstance(f, ast.Attribute) and isinstance(f.value, ast.Name):
            key = (f.value.id, f.attr)
            # time.gmtime(epoch) / localtime(epoch) С АРГУМЕНТОМ — чистая
            # функция от переданного числа, часов она не читает. Считать её
            # недетерминизмом — ошибка того же рода, что «широкий трейлинг».
            pure_arg = (key in (("time", "gmtime"), ("time", "localtime"),
                                ("time", "strftime")) and node.args)
            if key in self.NONDET and id(node) not in self.exempt and not pure_arg:
                self._report(node, "P6",
                             u"%s.%s — %s"
                             % (f.value.id, f.attr,
                                u"порядок не задан: обернуть в sorted()"
                                if key in self.ORDER_ONLY
                                else u"вход вне объявленных; объявить # TOTAL:"))
        self.generic_visit(node)

    def generic_visit(self, node):
        for t in self._tests(node):
            for e, neg in self._walk_test(t):
                self._check_expr(e, neg)
        ast.NodeVisitor.generic_visit(self, node)


def hand_scope(tree, lines):
    u"""P7: предмет проверки перечислен рукой (список путей/модулей литералом)."""
    out = []
    for n in tree.body:
        if not isinstance(n, ast.Assign) or not isinstance(n.value, (ast.List, ast.Tuple, ast.Set)):
            continue
        vals = [e.value for e in n.value.elts if isinstance(e, ast.Constant)
                and isinstance(e.value, str)]
        if len(vals) < 2:
            continue
        looks = sum(1 for v in vals if v.endswith(".py") or v.endswith(".json")
                    or "/" in v or "\\" in v)
        if looks >= max(2, len(vals) // 2):
            ln = n.lineno
            txt = lines[ln - 1].strip() if 0 < ln <= len(lines) else u""
            above = False
            i = ln - 2
            while i >= 0 and lines[i].strip().startswith("#"):
                if "# TOTAL" in lines[i]:
                    above = True
                    break
                i -= 1
            if "# TOTAL:" not in txt and not above:
                out.append(("P7", ln, txt[:96],
                            u"%d путей перечислены рукой — новый файл молча "
                            u"не проверится" % len(vals)))
    return out


def scan(path):
    src = io.open(path, encoding="utf-8").read()
    try:
        tree = ast.parse(src)
    except SyntaxError as exc:
        return None, exc
    s = Scan(path, src)
    s.visit(tree)
    s.hits += hand_scope(tree, s.lines)
    return s, None


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    files = args or enumerate_py(ROOT)
    total = {"P1": 0, "P2": 0, "P3": 0, "P5": 0, "P6": 0, "P7": 0}
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
        bad = [h for h in s.hits if h[0] in ("P1", "P2", "P5", "P6", "P7")]
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
    print(u"  P5 частичность через переменную%4d" % total["P5"])
    print(u"  P6 недетерминизм               %4d" % total["P6"])
    print(u"  P7 предмет перечислен рукой    %4d" % total["P7"])
    print(u"  P4 громкий отказ (эталон)      %4d" % honest)
    print(u"  объявлено тотальным (# TOTAL)  %4d" % declared)
    if unread:
        # непрочитанный файл — НЕ «ок»: это и есть тот самый дефект
        print(u"  ⛔ НЕ ПРОЧИТАНО                %4d  — %s"
              % (len(unread), ", ".join(unread[:4])))
    print()
    print(u"⚠ ПОЛ, А НЕ СЧЁТ. Закрыто 22.08: переменная (P5), детерминизм (P6),")
    print(u"  перечисление предмета рукой (P7). НЕ закрыто и потому не заявляю")
    print(u"  полноту: значение через возврат функции и через поля объектов;")
    print(u"  законность умолчания по смыслу; P7 узнаёт список по виду имени.")
    return 1 if (total["P1"] or total["P2"] or total["P5"]
                 or total["P6"] or total["P7"] or unread) else 0


if __name__ == "__main__":
    sys.exit(main())
