# -*- coding: utf-8 -*-
u"""СУД НАД ЧУЖИМИ СТРАТЕГИЯМИ ПО НАШЕЙ ДОКТРИНЕ.

ДОМЕН: МАТЕМАТИКА (предмет — свойства заявления о крае, не рынок).

⛔ ПОВОД — УПРЁК ОПЕРАТОРА 21.09, и он справедлив: «мы столько времени
строили машину, которая сама ничего не умеет; а что с чужими стратегиями
и их проверкой?» Я проверял на чужом коде ТРИ проверки КОДА, написанные
за час. Это не ANATMAN. Её содержание — суд над ЗАЯВЛЕННЫМ РЕЗУЛЬТАТОМ,
и на чужие стратегии он не направлялся НИ РАЗУ.

ЧТО СУДИТСЯ — три вещи из доктрины, проверяемые БЕЗ ЗАПУСКА:

    ① ЗАГЛЯДЫВАНИЕ. `shift(-N)` и родня берут БУДУЩУЮ строку. Это не
      «плохой стиль», это отмена результата: край изготавливается из
      знания будущего. Первый убийца бэктестов, и `freqtrade` держит
      отдельную команду `lookahead-analysis` именно из-за него.

    ② СТЕПЕНИ СВОБОДЫ. Каждый подбираемый параметр есть ручка подгонки.
      Двадцать ручек на несколько сотен сделок переподгоняют по
      построению — это D5/DSR, и у нас на своём корпусе дало 0 чистых
      из 456.

    ③ КРАЙ В БАРЬЕРАХ (D3). Если вход тривиален, а «доход» держится на
      таблице целей и стопе — это мартингальная геометрия, чьё ожидание
      равно нулю до издержек. `E[max] = G`.

⚠ ЧЕГО ЭТОТ ПРИБОР НЕ ДЕЛАЕТ: он НЕ говорит «стратегия убыточна». Он
говорит, ЧЕМ ОБЕСПЕЧЕНО ЗАЯВЛЕНИЕ. Заглядывание отменяет результат
целиком; ручки и барьеры — повод не верить без чистого прогона.

    python3 foreign_strategy_audit.py --root DIR
    python3 foreign_strategy_audit.py --selftest
"""
from __future__ import print_function

import argparse
import ast
import io
import os
import re
import sys

METHOD_DECL = {
    "inversion": "н/п: знак не считается — предмет есть НАЛИЧИЕ признака "
                 "в заявлении, а не его величина",
    "effect_injection": "проверено: подсаживается стратегия с явным "
                        "`shift(-1)` и требуется находка; подсаживается "
                        "чистая — требуется молчание",
    "cooccurrence_complement": "н/п: совпадения не сравниваются",
    "detection_floor": "н/п: свойство текста читается точно",
    "power": {
        "MDE_BPS": 0.0, "N_EFFECTIVE": 0.0, "EFFECT_EXPECTED_BPS": 0.0,
        "ESTIMATOR": "разбор дерева и текста; величина точная",
        "CLUSTER_KEY": "файл стратегии; один автор часто пишет несколько "
                       "и его приёмы повторяются ⇒ клетка есть АВТОР",
        "N_EFFECTIVE_TAIL": "н/п", "EFFECTIVE_SCREEN_BPS": 0.0,
    },
    "verdict_domain": {
        "истинно": "указан: признак найден И подтверждён чтением строки",
        "ложно": "указан: признака нет ⇒ заявление этим прибором НЕ "
                 "опровергнуто (что НЕ значит «стратегия работает»)",
        "ни то ни другое": "указан: файл не разбирается ⇒ НЕЧИТАЕМ",
        "и то и другое": "указан: три признака независимы и печатаются "
                         "порознь; схлопывать в один балл запрещено (D4)",
    },
    "FALSIFY_IF": "LOOKAHEAD_FOUND == 0",
    "FALSIFY_RANGE": {"LOOKAHEAD_FOUND": [0, 1000]},
    "ALTERNATIVE_PROXY": [
        "`shift(-N)` как признак заглядывания: бывает законным при "
        "построении МЕТКИ для обучения, а не признака ⇒ смещение в "
        "сторону ЛОЖНОЙ тревоги, и потому каждая находка читается",
        "счёт `*Parameter` как степени свободы: часть из них может быть "
        "закреплена и не подбираться ⇒ признак ЗАВЫШАЕТ подгонку",
        "богатая таблица целей как признак D3: у freqtrade `minimal_roi` "
        "обязателен по API, и его наличие само по себе НЕ дефект",
    ],
    "DECORRELATION": {"THRESHOLD": 0.7,
                      "BASIS": "указан: клетка есть АВТОР/репозиторий, а "
                               "не файл — приёмы повторяются",
                      "PER_PERIOD": True},
    "ZERO_IS_EXACT": True,
    "null": "ТОЧЕН ПО ПОСТРОЕНИЮ: отсутствие признака даёт ровно ноль "
            "находок, а не оценку",
    "control": "ВНУТРИ прогона: подсадка стратегии с заведомым "
               "заглядыванием. ЧУВСТВИТЕЛЬНОСТЬ ЗАМЕРЕНА, а не заявлена — "
               "без неё ноль неотличим от сломанного прибора",
    "baseline": "объявлены обе и ОБЕ СЧИТАЮТСЯ В КОДЕ. СЛУЧАЙНАЯ опора — "
                "слепой выбор: вероятность взять наугад ровно те 4 файла "
                "из 68, что помечены авторами, есть 1/C(68,4) = 1/814385; "
                "прибор печатает это число рядом со своим счётом. "
                "ТРИВИАЛЬНАЯ опора — наш СОБСТВЕННЫЙ корпус: 0 чистых из "
                "456 (DSR/PBO, 24.08); чужой счёт сравнивается с ним, а "
                "не с нулём",
    "POWER_TAIL_DECILE": "н/п: величины нет",
    "TYPE_II_WEIGHT": "3 к 1 против ложной НАХОДКИ. Обвинить чужую работу "
                      "ложно — хуже, чем промолчать: это ровно та "
                      "угодливость наружу, от которой мы отказались на "
                      "детрендировании Аронсона 21.09. ⇒ каждая находка "
                      "ЧИТАЕТСЯ глазами, счёт находкой не является",
}

# ⛔ ФОРМ ЗАГЛЯДЫВАНИЯ ДВЕ, И ВТОРУЮ Я СНАЧАЛА ПРОПУСТИЛ (21.09).
# Корпус `freqtrade-strategies` держит каталог, ПРЯМО НАЗВАННЫЙ
# `lookahead_bias/`, — то есть авторы сами пометили эти стратегии. Первая
# редакция детектора нашла там НОЛЬ: она искала только сдвиг назад.
# Настоящее заглядывание в `wtc.py` выглядит иначе:
#     x = dataframe.iloc[:, 6:].values
#     dataframe.iloc[:, 6:] = pd.DataFrame(x_scaled)   ← min/max ПО ВСЕЙ истории
# Значение в момент t зависит от крайних значений, которые случатся ПОЗЖЕ.
# ⚠ Отличать от законного случая: у `jesse` среднее полной выборки строит
# НУЛЬ (симметрично для наблюдения и для нуля — схема Аронсона). Здесь оно
# строит СИГНАЛ, и это подлог.
LOOKAHEAD = re.compile(
    # ① сдвиг назад — берёт будущую строку прямо
    r"\.shift\(\s*-\s*\d+|\.shift\(\s*-\w+|"
    r"\.iloc\[\s*\w+\s*\+\s*\d+\s*\]|"
    # ⛔ ПРОЖИТО 21.09 НА ШИРОКОМ КОРПУСЕ: игла `future_` ловила
    # `from __future__ import annotations` — служебную строку Python,
    # не имеющую к будущим ценам НИКАКОГО отношения. Пять ложных
    # обвинений у `nateemma` и одно у `raph92`. Это наш класс
    # `self_matching_pattern`: признак совпал со СВОИМ ЖЕ словарём.
    # Отрицательный просмотр отсекает дандер, оставляя `future_close`.
    # ⛔ И ВТОРАЯ ГРАНИЦА ТОЙ ЖЕ ИГЛЫ, ПРОЖИТА НА КАЛИБРОВКЕ 21.09: у двух
    # Ichimoku-стратегий совпало `'future_green': {'color': 'green'}` —
    # ключ словаря НАСТРОЕК ГРАФИКА. Динамика их и вправду роняет, но за
    # другую строку: вердикт верный, улика ложная — «правильно по случаю»
    # засчитывать нельзя. Имя в кавычках есть МЕТКА, не вычисление.
    r"(?<!['\"_])future_|"
    r"\.tail\(\s*1\s*\)\.values|"
    # ② подгонка преобразования по ВСЕЙ выборке — та же беда, иначе одетая
    # ⛔ ТРЕБУЕТСЯ ВЫЗОВ, А НЕ ИМЯ: `MinMaxScaler` без скобки есть импорт
    # или упоминание. Импорт не может БЫТЬ заглядыванием по построению.
    r"fit_transform\s*\(|MinMaxScaler\s*\(|StandardScaler\s*\(|"
    r"RobustScaler\s*\(|"
    r"\.expanding\(\s*\)\.(?!mean|std)|"
    # ③ крайние значения всего ряда, подставленные в сигнал
    r"dataframe\[[^\]]+\]\.(?:max|min)\(\)\s*(?:[-+*/]|\))|"
    # ⑤ ИНТЕРПОЛЯЦИЯ СТАРШЕГО ТАЙМФРЕЙМА ВНИЗ. Найдено 21.09 в ДВУХ
    # НЕПОМЕЧЕННЫХ стратегиях (`ReinforcedQuickie`, `CCIStrategy`):
    #     df = df.resample('15min').agg(...); df['sma'] = SMA(df)
    #     df = df.resample('5min'); df = df.interpolate(method='time')
    # Интерполяция заполняет 10:05 и 10:10, проводя прямую между 10:00 и
    # 10:15. Значения на 10:15 в 10:05 НЕ СУЩЕСТВУЕТ — пятнадцатиминутка
    # не закрылась. Заражённое число идёт ПРЯМО в условие входа.
    # ⚠ Это самая ценная форма: она не похожа на заглядывание. Ни
    # `shift(-1)`, ни `min()/max()` — обычная интерполяция.
    r"\.interpolate\(\s*method\s*=\s*[\"']time[\"']|"
    r"\.interpolate\(\s*\)\s*$|"
    # ⑥ центрированное окно — смотрит вперёд ПО ОПРЕДЕЛЕНИЮ
    r"center\s*=\s*True|"
    # ⑦ ДВЕ СЕМЬИ, ВЗЯТЫЕ У ЧУЖОГО ДЕТЕКТОРА 21.09. `RoboticAutomations`
    # держит 137 стратегий в папке `dirty LA/` по СВОЕМУ ast-детектору из 12
    # правил, с точной строкой на файл. Две его семьи с высокой уверенностью
    # у меня отсутствовали, и обе прожиты на его файлах:
    #   backfill — `bfill()` / `fillna(method='bfill')` тянет ПОЗДНЕЕ
    #   значение в РАННИЕ строки (23 его попадания);
    #   extrema_scan — `argrelextrema` / `find_peaks` / zigzag ищут
    #   экстремумы, а экстремум в точке t известен только ПОСЛЕ t (52).
    # Это и есть «путезависимый пересчёт», который я не мог назвать у Renko.
    # ⚠ Граница: `ffill()` — прошлое в будущее — ЗАКОННО и НЕ ловится.
    r"\.bfill\(|fillna\(\s*method\s*=\s*[\"']bfill[\"']|"
    r"\bargrelextrema\(|\bfind_peaks\(|\bzigzag\(|"
    # ④ РУЧНАЯ нормировка по всей выборке: (X − X.min())/(X.max() − X.min()).
    # ⛔ Прожито 21.09: три из четырёх стратегий каталога `lookahead_bias`
    # написали её БЕЗ `MinMaxScaler`, простой арифметикой, и первая
    # редакция иглы их не видела — она требовала префикса `dataframe[...]`,
    # а там `df.min()` и `tib.min()`. Ловить надо ИДИОМ, а не имя.
    r"\w+\s*-\s*\w+\.min\(\)\s*\)\s*/\s*\(\s*\w+\.max\(\)\s*-\s*\w+\.min\(\)")
PARAM = re.compile(r"\b(Int|Decimal|Real|Categorical|Boolean)Parameter\b")

# ⛔ ④ СЛУЧАЙНОСТЬ В СИГНАЛЕ — НЕ ЗАГЛЯДЫВАНИЕ, А НЕВОСПРОИЗВОДИМОСТЬ. Прожито
# на калибровке 21.09: `freqtrade lookahead-analysis` роняет
# `BuyAllSellAllStrategy` и `FrostAuraRandomStrategy` как «найдено», а в них
# `np.random.randint` в условии входа. Динамика не различает «увидел
# будущее» и «бросил монету»: и то и другое меняет сигнал при удлинении
# ряда. Статика ОБЯЗАНА различать — иначе два вердикта из сорока подписаны
# не за то. Категория ОТДЕЛЬНАЯ и в ① не схлопывается (D4).
RANDOM = re.compile(
    r"\bnp\.random\.\w+\(|\bnumpy\.random\.\w+\(|"
    r"\brandom\.(?:random|randint|choice|uniform|gauss|shuffle)\(|"
    r"(?<![\w.])randint\(")

# ⛔ ⑦ BACKTRADER ГОВОРИТ НА ДРУГОМ ЯЗЫКЕ. У него ряд есть «линия», и
# индекс отсчитывается ОТ ТЕКУЩЕГО БАРА: `close[0]` — сейчас, `close[-1]` —
# прошлый, а `close[1]` — БУДУЩИЙ. Ни одна pandas-игла этого не ловит:
# формы `shift(-1)` там нет вовсе. Без этой строки ноль на backtrader был
# бы не чистотой корпуса, а слепотой прибора.
# ⛔ И СРАЗУ ЖЕ ГРАНИЦА, ПРОЖИТАЯ НА ПЕРВОМ ЖЕ ПРОГОНЕ: `self.datas[1]`
# есть выбор ВТОРОЙ ЛЕНТЫ, а не будущий бар. Признак один и тот же —
# число в скобках, — а предмет разный. Различает их то, что за селектором
# ленты ВСЕГДА идёт точка (`datas[1].open`), а за индексом времени — нет.
BT_FUTURE = re.compile(
    r"\b(?:self\.)?(?:data\w*|close|open|high|low|volume|lines\.\w+)"
    r"\[\s*\+?[1-9]\d*\s*\](?!\s*\.)")

# ⛔ КАРКАС ОПОЗНАЁТСЯ ПО ТОЧКЕ ВХОДА, А НЕ ПО ИМЕНИ ПАПКИ. Первая
# редакция считала стратегией только freqtrade (`populate_entry_trend`)
# ⇒ 19 стратегий jesse и 77 backtrader были НЕВИДИМЫ, и корпус молчал о
# них, не сообщая, что молчит. Это ровно D12: «не знаю» есть долг.
FRAMEWORK = (
    (u"freqtrade", re.compile(r"populate_entry_trend|populate_buy_trend")),
    (u"jesse", re.compile(r"def\s+should_long\b|def\s+go_long\b")),
    (u"backtrader", re.compile(r"\bbt\.Strategy\b|backtrader\.Strategy\b|"
                               r"\bbt\.SignalStrategy\b")),
)


# ⛔ ЯЗЫК ВЫВОДА ЕСТЬ ЗНАЧЕНИЕ, А НЕ ВЕТКА В КОДЕ (D11). Прибор уходит к
# ЧУЖИМ разработчикам, и русский отчёт для них — стена, а не суд. Внутренние
# имена (самотест, дефекты) остаются русскими: они наши и читают их наши.
# ⚠ Ключи обоих словарей обязаны совпадать — это проверяет самотест, иначе
# перевод молча терял бы строку и отчёт выглядел бы полным.
LANG = {
    u"ru": {
        u"head": u"── СУД НАД ЧУЖИМИ СТРАТЕГИЯМИ · %s",
        u"total": u"   стратегий найдено: %d   (%s)",
        u"look": u"   ① ЗАГЛЯДЫВАНИЕ В БУДУЩЕЕ            %3d из %d (%.0f %%)",
        u"dof": u"   ② СТЕПЕНИ СВОБОДЫ (подбираемых параметров)",
        u"dof_n": u"        стратегий с подбором: %d · максимум у одной: %d",
        u"knobs": u"ручек",
        u"bar": u"   ③ КРАЙ ДЕРЖИТСЯ НА БАРЬЕРАХ (D3)     %3d",
        u"bar_n": u"ступеней цели %d, условий входа %d",
        u"rnd1": u"   ⚠ СЛУЧАЙНАЯ ОПОРА, РАЗЫГРАНА: поймано помеченных "
                 u"авторами %d из %d.",
        u"rnd2": u"      слепой выбор %d наугад из %d, %d розыгрышей ⇒ "
                 u"совпало %d раз",
        u"triv": u"   ⚠ ТРИВИАЛЬНАЯ ОПОРА: наш собственный корпус — "
                 u"0 чистых из 456.",
        u"warn1": u"   ⚠ ЭТО КАНДИДАТЫ. Находкой становится ТОЛЬКО прочитанное",
        u"warn2": u"     глазами: `shift(-1)` бывает законным "
                  u"при построении МЕТКИ.",
    },
    u"en": {
        u"head": u"── STRATEGY AUDIT · %s",
        u"total": u"   strategies found: %d   (%s)",
        u"look": u"   (1) LOOKAHEAD                        %3d of %d (%.0f %%)",
        u"dof": u"   (2) DEGREES OF FREEDOM (tunable parameters)",
        u"dof_n": u"        strategies with knobs: %d · largest: %d",
        u"knobs": u"knobs",
        u"bar": u"   (3) EDGE CARRIED BY BARRIERS         %3d",
        u"bar_n": u"exit-grid steps %d, entry conditions %d",
        u"rnd1": u"   ! RANDOM BASELINE, DRAWN: caught %d of %d strategies "
                 u"the authors themselves labelled.",
        u"rnd2": u"      blind pick of %d out of %d, %d draws => matched "
                 u"%d times",
        u"triv": u"   ! TRIVIAL BASELINE: our own corpus — 0 clean of 456.",
        u"warn1": u"   ! THESE ARE CANDIDATES. A flag becomes a finding ONLY",
        u"warn2": u"     after the line is read: `shift(-1)` is legitimate "
                  u"when building a LABEL.",
    },
}


def framework_of(src):
    u"""Имя каркаса или None. Один файл принадлежит ОДНОМУ каркасу."""
    for name, rx in FRAMEWORK:
        if rx.search(src):
            return name
    return None


def _prose_lines(src):
    u"""Номера строк, занятых строками-документации.

    ⛔ D185: при доступном `ast` разбирать надо ДЕРЕВОМ. Наивный пропуск
    строк, начинающихся с `#`, не видит докстрингов — и игла нашла бы
    заглядывание в ПОЯСНЕНИИ к нему. Тот же класс, что D319/D320.
    """
    bad = set()
    try:
        tree = ast.parse(src)
    except (SyntaxError, ValueError):
        return bad
    for node in ast.walk(tree):
        if isinstance(node, (ast.Module, ast.ClassDef, ast.FunctionDef,
                             ast.AsyncFunctionDef)):
            b = getattr(node, "body", None)
            if b and isinstance(b[0], ast.Expr) \
                    and isinstance(b[0].value, ast.Constant) \
                    and isinstance(b[0].value.value, str):
                lo = b[0].lineno
                hi = getattr(b[0], "end_lineno", lo) or lo
                bad.update(range(lo, hi + 1))
    return bad


# ⛔ ПОЧИНКА КЛАССА, А НЕ СЛУЧАЯ (D10). Ложные обвинения 21.09 пришли
# СТРОКАМИ ИМПОРТА: `from sklearn.preprocessing import MinMaxScaler` и
# `from __future__ import annotations`. Чинить каждую иглу порознь — это
# чинить случай. Верно иное: ИМПОРТ НЕ МОЖЕТ БЫТЬ ЗАГЛЯДЫВАНИЕМ ПО
# ПОСТРОЕНИЮ — он вносит имя, а не вычисляет признак. ⇒ вычитается весь
# класс строк, и будущие иглы защищены тем же вычитанием.
_IMPORT = re.compile(r"^\s*(?:from\s+[\w.]+\s+)?import\s")


def _dead_helpers(src):
    u"""Модульные функции, которых в файле НИКТО НЕ ЗОВЁТ.

    ⛔ ТРЕТИЙ ПРОЖИТЫЙ КЛАСС 21.09. Прибор читал ОПРЕДЕЛЕНИЕ, а не
    применение. `BelieveInCoin` и `MyStrategyNew10` объявляют
    `def normalize(df): (df-df.min())/(df.max()-df.min())` — и сами же
    ЗАКОММЕНТИРОВАЛИ единственный вызов. Автор уже вылечил себя, а
    прибор его обвинял. Два ложных обвинения из восьми.

    ⚠ ГРАНИЦА, БЕЗ КОТОРОЙ ПОЧИНКА СТАЛА БЫ СЛЕПОТОЙ: вычитаются
    ТОЛЬКО функции модульного уровня. Метод класса (`populate_indicators`)
    зовёт КАРКАС, а не файл; требовать у него вызова в том же файле —
    ослепить прибор на главном месте. Оттого `tree.body`, а не `walk`.
    """
    try:
        tree = ast.parse(src)
    except (SyntaxError, ValueError):
        return []
    called = set()
    for n in ast.walk(tree):
        if isinstance(n, ast.Call):
            f = n.func
            if isinstance(f, ast.Name):
                called.add(f.id)
            elif isinstance(f, ast.Attribute):
                called.add(f.attr)
    spans = []
    for n in tree.body:
        if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef)) \
                and n.name not in called:
            lo = n.lineno
            spans.append((lo, getattr(n, "end_lineno", lo) or lo))
    return spans


def check_lookahead(src, framework=None):
    u"""Кандидаты на заглядывание. `framework` включает иглы каркаса.

    ⚠ Игла backtrader НЕ применяется к pandas-коду: там `x[1]` есть
    вторая СТРОКА, а не следующий бар. Одна и та же запись означает у
    двух каркасов РАЗНОЕ — подставлять признак по сходству записи было
    бы `match_by_structure_not_vocabulary` наоборот.
    """
    prose = _prose_lines(src)
    dead = _dead_helpers(src)
    extra = BT_FUTURE if framework == u"backtrader" else None
    out = []
    for i, ln in enumerate(src.split("\n"), 1):
        s = ln.strip()
        if s.startswith("#") or i in prose or _IMPORT.match(ln):
            continue
        if any(lo <= i <= hi for lo, hi in dead):
            continue
        if LOOKAHEAD.search(ln) or (extra is not None and extra.search(ln)):
            out.append((i, s[:100]))
    return out


def check_random(src):
    u"""Строки со случайностью — вне комментариев, докстрингов и импортов."""
    prose = _prose_lines(src)
    out = []
    for i, ln in enumerate(src.split("\n"), 1):
        s = ln.strip()
        if s.startswith("#") or i in prose or _IMPORT.match(ln):
            continue
        if RANDOM.search(ln):
            out.append((i, s[:100]))
    return out


def count_params(src):
    return len(PARAM.findall(src))


def roi_richness(src):
    u"""Сколько ступеней в таблице целей и задан ли стоп."""
    m = re.search(r"minimal_roi\s*=\s*\{(.*?)\}", src, re.S)
    steps = len(re.findall(r"\"[\d.]+\"\s*:", m.group(1))) if m else 0
    has_sl = bool(re.search(r"stoploss\s*=\s*-?[\d.]+", src))
    return steps, has_sl


def entry_complexity(src):
    u"""Грубая мера сложности входа: число условий в сигнале входа."""
    m = re.search(r"populate_entry_trend|populate_buy_trend", src)
    if not m:
        return None
    tail = src[m.start():m.start() + 4000]
    return len(re.findall(r"[&|]", tail))


_DIRTY = u'''
class S:
    def populate_entry_trend(self, df, md):
        df["fut"] = df["close"].shift(-1)
        df.loc[df["fut"] > df["close"], "enter_long"] = 1
        return df
'''
_CLEAN = u'''
class S:
    def populate_entry_trend(self, df, md):
        df.loc[df["rsi"] < 30, "enter_long"] = 1
        return df
'''

_SCALED = u'''
class S:
    def populate_indicators(self, df, md):
        x = df.iloc[:, 6:].values
        x_scaled = MinMaxScaler().fit_transform(x)
        df.iloc[:, 6:] = pd.DataFrame(x_scaled)
        return df
'''

def _fs_probe(body):
    u"""Отпечаток временного каталога с одним файлом (или без файлов).

    ⚠ Проба ТРОГАЕТ ДИСК, потому что предмет `fileset_hash` — именно диск.
    Подменять его словарём значило бы проверять не тот предмет.
    """
    import shutil
    import tempfile
    d = tempfile.mkdtemp(prefix="anatman_fs_")
    try:
        if body is not None:
            with io.open(os.path.join(d, "s.py"), "w",
                         encoding="utf-8") as fh:
                fh.write(body)
        return fileset_hash(d)
    finally:
        # ⛔ чистим ТОЛЬКО свой каталог: 17.08 rmtree снёс чужие файлы
        shutil.rmtree(d, ignore_errors=True)


def _dup_probe(same):
    u"""Две папки-репозитория: с ОДИНАКОВОЙ либо с РАЗНОЙ стратегией.

    Возвращает (сколько засчитано, сколько снято как копия).
    """
    import shutil
    import tempfile
    base = u"class S:\n    def populate_entry_trend(self, d, m):\n        %s\n"
    d = tempfile.mkdtemp(prefix="anatman_dup_")
    try:
        seen, total, dups = set(), 0, 0
        for i, body in enumerate((base % u"return d",
                                  base % (u"return d" if same
                                          else u"return d.copy()"))):
            sub = os.path.join(d, "repo%d" % i)
            os.makedirs(sub)
            with io.open(os.path.join(sub, "s.py"), "w",
                         encoding="utf-8") as fh:
                fh.write(body)
            r = audit_root(sub, seen)
            total += r[u"total"]
            dups += r[u"dups"]
        return (total, dups)
    finally:
        shutil.rmtree(d, ignore_errors=True)


def _lineage_probe(copies, labelled, label_dir=u"lookahead_bias"):
    u"""Корпус из `copies` репозиториев с ОДНОЙ и той же стратегией.

    При `labelled` первая копия лежит в папке-пометке `label_dir` — как у
    авторов freqtrade-strategies (`lookahead_bias`) или RoboticAutomations
    (`dirty LA`). Возвращает (копий у первой записи, помечена ли).
    """
    import shutil
    import tempfile
    body = (u"class S:\n    def populate_entry_trend(self, d, m):\n"
            u"        d['x'] = (d-d.min())/(d.max()-d.min())\n        return d\n")
    d = tempfile.mkdtemp(prefix="anatman_lin_")
    try:
        for i in range(copies):
            sub = os.path.join(d, "repo%d" % i,
                               label_dir if (labelled and i == 0)
                               else "strategies")
            os.makedirs(sub)
            with io.open(os.path.join(sub, "s.py"), "w",
                         encoding="utf-8") as fh:
                fh.write(body)
        rows = lineage(d)
        return (rows[0][0], rows[0][3]) if rows else (0, False)
    finally:
        shutil.rmtree(d, ignore_errors=True)


SELFTEST = [
    (u"①_подсаженное_заглядывание_НАЙДЕНО",
     lambda: len(check_lookahead(_DIRTY)) >= 1),
    # ⛔ ПРОЖИТЫЙ СЛУЧАЙ 21.09: корпус сам пометил каталог `lookahead_bias`,
    # а первая редакция детектора нашла там НОЛЬ — искала не ту форму.
    (u"①_масштабирование_по_всей_выборке_НАЙДЕНО",
     lambda: len(check_lookahead(_SCALED)) >= 1),
    # ⛔ ТА ЖЕ БЕДА РУКАМИ, без библиотеки — три из четырёх размеченных
    (u"①_ручная_нормировка_по_всей_выборке_НАЙДЕНА",
     lambda: len(check_lookahead(
         u"df = (df-df.min())/(df.max()-df.min())\n")) >= 1),
    # ⛔ ПРОЖИТЫЙ СЛУЧАЙ 21.09: две НЕПОМЕЧЕННЫЕ стратегии тянут старший
    # таймфрейм вниз интерполяцией — самая ценная форма, не похожая на
    # заглядывание ни одним признаком
    (u"①_интерполяция_старшего_таймфрейма_НАЙДЕНА",
     lambda: len(check_lookahead(
         u"df = df.resample('5min')\n"
         u"df = df.interpolate(method='time')\n")) >= 1),
    (u"①_центрированное_окно_НАЙДЕНО",
     lambda: len(check_lookahead(u"x = s.rolling(20, center=True).mean()\n")) >= 1),
    (u"①_нормировка_по_ОКНУ_не_считается",
     lambda: check_lookahead(
         u"x = (df-df.rolling(20).min())/(df.rolling(20).max()"
         u"-df.rolling(20).min())\n") == []),
    (u"①_чистая_стратегия_МОЛЧИТ",
     lambda: check_lookahead(_CLEAN) == []),
    (u"①_комментарий_НЕ_считается_заглядыванием",
     lambda: check_lookahead(u'# df["x"].shift(-1)\n') == []),
    # ⛔ D185: строка-документации тоже НЕ заявление. Наивный пропуск `#`
    # её не видел, и игла нашла бы заглядывание в ПОЯСНЕНИИ к нему.
    (u"①_строка_документации_НЕ_считается",
     lambda: check_lookahead(
         u'def f():\n    """пример: df.shift(-1) нельзя"""\n    return 1\n'
     ) == []),
    # ⛔⛔ ЧЕТЫРЕ ПРОЖИТЫХ СЛУЧАЯ 21.09, ШИРОКИЙ КОРПУС. Прибор, чисто
    # прошедший 68 файлов, на 349 стал ОБВИНЯТЬ ЛОЖНО: шесть строк
    # `from __future__ import annotations` и две строки импорта scaler'а.
    # ⭐ КАЖДОЕ ГЛУШЕНИЕ ИДЁТ В ПАРЕ С ПОЛОЖИТЕЛЬНЫМ КОНТРОЛЕМ НА ГРАНИЦЕ:
    # без него «стало тихо» неотличимо от «прибор ослеп» — ровно тот
    # отказ, что дал сторож, умевший только словленное.
    (u"①_дандер___future___НЕ_считается",
     lambda: check_lookahead(u"from __future__ import annotations\n") == []),
    (u"①_ключ_словаря_'future_green'_НЕ_считается",
     lambda: check_lookahead(
         u"plot = {'future_green': {'color': 'green'}}\n") == []),
    (u"①_но_переменная_future_close_СЧИТАЕТСЯ",          # граница ①
     lambda: len(check_lookahead(
         u"future_close = df['close'].values\n")) >= 1),
    (u"①_импорт_scaler_НЕ_считается",
     lambda: check_lookahead(
         u"from sklearn.preprocessing import MinMaxScaler\n") == []),
    (u"①_но_ВЫЗОВ_scaler_СЧИТАЕТСЯ",                     # граница ②
     lambda: len(check_lookahead(
         u"x = MinMaxScaler().fit_transform(v)\n")) >= 1),
    # ⛔ ТРЕТИЙ КЛАСС 21.09: определение без применения. И его граница.
    (u"①_мёртвая_функция_нормировки_НЕ_считается",
     lambda: check_lookahead(
         u"def normalize(df):\n"
         u"    return (df-df.min())/(df.max()-df.min())\n"
         u"\n"
         u"def apply(d, k, r):\n"
         u"    # d[k] = normalize(r)\n"
         u"    d[k] = r\n") == []),
    (u"①_но_ЖИВАЯ_та_же_функция_СЧИТАЕТСЯ",              # граница ③
     lambda: len(check_lookahead(
         u"def normalize(df):\n"
         u"    return (df-df.min())/(df.max()-df.min())\n"
         u"\n"
         u"def apply(d, k, r):\n"
         u"    d[k] = normalize(r)\n")) >= 1),
    # ⚠ И граница границы: МЕТОД зовёт каркас, не файл. Требовать у него
    # вызова в том же файле — ослепнуть на главном месте.
    (u"①_метод_класса_БЕЗ_вызова_в_файле_всё_равно_считается",
     lambda: len(check_lookahead(
         u"class S:\n"
         u"    def populate_indicators(self, df, md):\n"
         u"        df['f'] = df['close'].shift(-1)\n"
         u"        return df\n")) >= 1),
    # ⛔⛔ ПОЛОЖИТЕЛЬНЫЙ КОНТРОЛЬ ДЛЯ КАЖДОГО КАРКАСА. Без него ноль на
    # jesse и backtrader означал бы «прибор туда не смотрит», а на экране
    # выглядел бы как «там чисто» — ровно неразличимость, из-за которой
    # сторож печатал «чисто» сутки.
    (u"⑦_backtrader_БУДУЩИЙ_бар_close[1]_НАЙДЕН",
     lambda: len(check_lookahead(
         u"class S(bt.Strategy):\n"
         u"    def next(self):\n"
         u"        if self.data.close[1] > self.data.close[0]:\n"
         u"            self.buy()\n", framework=u"backtrader")) >= 1),
    (u"⑦_backtrader_ПРОШЛЫЙ_бар_close[-1]_МОЛЧИТ",       # граница ④
     lambda: check_lookahead(
         u"class S(bt.Strategy):\n"
         u"    def next(self):\n"
         u"        if self.data.close[-1] > self.data.close[0]:\n"
         u"            self.buy()\n", framework=u"backtrader") == []),
    (u"⑦_выбор_ВТОРОЙ_ЛЕНТЫ_datas[1]_НЕ_считается",      # граница ⑥
     lambda: check_lookahead(
         u"x = self.datas[1].open[0]\n", framework=u"backtrader") == []),
    (u"⑦_та_же_запись_в_pandas_НЕ_считается_будущим",     # граница ⑤
     lambda: check_lookahead(
         u"x = close[1]\n", framework=u"freqtrade") == []),
    (u"⑧_каркас_freqtrade_опознан",
     lambda: framework_of(u"def populate_entry_trend(self, d, m):\n    pass\n")
     == u"freqtrade"),
    (u"⑧_каркас_jesse_опознан",
     lambda: framework_of(u"def should_long(self):\n    return True\n")
     == u"jesse"),
    (u"⑧_каркас_backtrader_опознан",
     lambda: framework_of(u"class S(bt.Strategy):\n    pass\n")
     == u"backtrader"),
    (u"⑧_обычный_модуль_каркасом_НЕ_считается",
     lambda: framework_of(u"import os\nx = 1\n") is None),
    # ⛔ ПЕРЕВОД, ТЕРЯЮЩИЙ СТРОКУ, ДАЁТ ОТЧЁТ, ВЫГЛЯДЯЩИЙ ПОЛНЫМ. Ключи
    # обоих словарей обязаны совпадать, и это проверяется, а не обещается.
    (u"⑨_словари_языков_несут_ОДНИ_И_ТЕ_ЖЕ_ключи",
     lambda: set(LANG[u"ru"]) == set(LANG[u"en"])),
    # ⛔ ДУБЛЬ КОРПУСА УДВАИВАЕТ ВЕС ОДНОГО АВТОРА. Отпечаток обязан
    # совпасть у одинакового набора и РАЗОЙТИСЬ у разного — иначе снятие
    # дублей либо не работает, либо режет живые корпуса.
    (u"⑩_отпечаток_совпадает_у_ОДИНАКОВЫХ_наборов",
     lambda: _fs_probe(u"a") == _fs_probe(u"a")),
    (u"⑩_отпечаток_РАСХОДИТСЯ_у_разных",             # граница ⑦
     lambda: _fs_probe(u"a") != _fs_probe(u"b")),
    (u"⑩_пустой_каталог_даёт_пустой_отпечаток",
     lambda: _fs_probe(None) == u""),
    # ⛔ 58 % КОРПУСА — КОПИИ. Снятие дублей по СОДЕРЖИМОМУ обязано
    # считать одну стратегию один раз — и не глотать разные.
    (u"⑪_одна_стратегия_в_двух_репозиториях_считается_ОДИН_раз",
     lambda: _dup_probe(same=True) == (1, 1)),
    (u"⑪_но_РАЗНЫЕ_стратегии_считаются_обе",          # граница ⑧
     lambda: _dup_probe(same=False) == (2, 0)),
    # ⛔ ④ СЛУЧАЙНОСТЬ ≠ ЗАГЛЯДЫВАНИЕ, и обе границы: ловится в сигнале,
    # молчит на чистом и на упоминании в комментарии.
    (u"④_случайность_в_сигнале_НАЙДЕНА",
     lambda: len(check_random(
         u"df['buy'] = np.random.randint(0, 2, size=len(df))\n")) >= 1),
    (u"④_и_НЕ_считается_заглядыванием",                  # граница ⑨
     lambda: check_lookahead(
         u"df['buy'] = np.random.randint(0, 2, size=len(df))\n") == []),
    (u"④_чистая_стратегия_МОЛЧИТ",
     lambda: check_random(_CLEAN) == []),
    (u"④_упоминание_в_комментарии_НЕ_считается",
     lambda: check_random(u"# np.random.randint here\n") == []),
    # ⛔ РОДОСЛОВНАЯ: три копии → три; пометка у ОДНОЙ копии — пометка всей
    # родословной (остальные несут дефект БЕЗ пометки); одиночка — не копия.
    (u"⑫_три_копии_одной_стратегии_видны_как_ТРИ",
     lambda: _lineage_probe(3, labelled=False) == (3, False)),
    (u"⑫_пометка_у_одной_копии_помечает_родословную",   # граница ⑩
     lambda: _lineage_probe(3, labelled=True) == (3, True)),
    (u"⑫_одиночка_копией_НЕ_считается",
     lambda: _lineage_probe(1, labelled=False) == (1, False)),
    # ⛔ ПРОЖИТО 21.09: папка-пометка бывает не только `lookahead_bias`.
    # `dirty LA` у RoboticAutomations — та же пометка другим именем.
    (u"⑫_папка_dirty_LA_тоже_пометка_автора",             # граница ⑪
     lambda: _lineage_probe(2, labelled=True, label_dir=u"dirty LA")
     == (2, True)),
    (u"⑫_обычная_папка_пометкой_НЕ_считается",
     lambda: _lineage_probe(2, labelled=True, label_dir=u"strategies")
     == (2, False)),
    # ⛔ ⑦ ДВЕ СЕМЬИ ОТ ЧУЖОГО ДЕТЕКТОРА — и граница для каждой: `ffill`
    # законен (прошлое в будущее), экстремум в комментарии — не вычисление.
    (u"⑦_bfill_тянет_будущее_назад_НАЙДЕН",
     lambda: len(check_lookahead(u"df['x'] = df['x'].bfill()\n")) >= 1),
    (u"⑦_fillna_method_bfill_НАЙДЕН",
     lambda: len(check_lookahead(
         u"df['x'] = df['x'].fillna(method='bfill')\n")) >= 1),
    (u"⑦_но_ffill_ЗАКОНЕН_и_молчит",                       # граница ⑫
     lambda: check_lookahead(u"df['x'] = df['x'].ffill()\n") == []),
    (u"⑦_argrelextrema_НАЙДЕН",
     lambda: len(check_lookahead(
         u"idx = argrelextrema(df['close'].values, np.greater, order=5)\n"
     )) >= 1),
    (u"⑦_find_peaks_в_комментарии_НЕ_считается",
     lambda: check_lookahead(u"# peaks via find_peaks(x)\n") == []),
    (u"②_считает_подбираемые_параметры",
     lambda: count_params(u"a = IntParameter(1,5)\nb = DecimalParameter(0,1)") == 2),
    (u"③_читает_таблицу_целей",
     lambda: roi_richness(u'minimal_roi = {"0": 0.1, "30": 0.05}\n'
                          u'stoploss = -0.10')[0] == 2),
    (u"③_без_стопа_видно",
     lambda: roi_richness(u'minimal_roi = {"0": 0.1}')[1] is False),
]


def selftest():
    ok = fail = 0
    for name, fn in SELFTEST:
        try:
            good = bool(fn())
        except Exception as ex:                          # noqa: BLE001
            good = False
            print(u"  ✗ %s — %r" % (name, ex))
        if good:
            ok += 1
        else:
            fail += 1
            print(u"  ✗ %s" % name)
    # ── диверсия 22.09: main напрямую (класс D321); иглы настоящие ──
    for name, fn, want in REACH:
        got = fn()
        if got == want:
            ok += 1
        else:
            fail += 1
            print(u"  ✗ %s: %r, ждали %r" % (name, got, want))

    print(u"САМОТЕСТ foreign_strategy_audit: %d пройдено, %d провалено"
          % (ok, fail))
    return 1 if fail else 0


def _under(argv, files=None):
    u"""`main` на временном корне с подсаженными стратегиями. (код, stdout)."""
    import contextlib
    import shutil
    import tempfile
    d, buf = tempfile.mkdtemp(prefix="fsa_"), io.StringIO()
    try:
        for nm, src in (files or {}).items():
            io.open(os.path.join(d, nm), "w", encoding="utf-8").write(src)
        argv = [a.replace("{ROOT}", d) for a in argv]
        with contextlib.redirect_stdout(buf), \
                contextlib.redirect_stderr(io.StringIO()):
            rc = main(["foreign_strategy_audit.py"] + argv)
    finally:
        shutil.rmtree(d, ignore_errors=True)
    return rc, buf.getvalue()


_STRAT = (u"from freqtrade.strategy import IStrategy\n\n\n"
          u"class Podd(IStrategy):\n"
          u"    def populate_indicators(self, dataframe, metadata):\n"
          u"        dataframe['x'] = dataframe['close'].shift(-1)\n"
          u"        return dataframe\n\n"
          u"    def populate_entry_trend(self, dataframe, metadata):\n"
          u"        return dataframe\n")


def _r_no_root():
    return _under([])[0]


def _r_lineage_missing():
    return _under(["--lineage", os.path.join(os.sep, "nonexistent")])[0]


def _r_one_lookahead():
    rc, out = _under(["--root", "{ROOT}"], {"podd.py": _STRAT})
    return rc, u"стратегий найдено: 1" in out and u"  1 из 1" in out


def _r_english_head():
    rc, out = _under(["--root", "{ROOT}", "--lang", "en"],
                     {"podd.py": _STRAT})
    return rc, u"STRATEGY AUDIT" in out


REACH = [
    (u"main·без корня → 2", _r_no_root, 2),
    (u"main·--lineage нет каталога → 2", _r_lineage_missing, 2),
    (u"main·одна стратегия с shift(-1) → найдено 1 из 1",
     _r_one_lookahead, (0, True)),
    (u"main·--lang en → английская шапка", _r_english_head, (0, True)),
]


def fileset_hash(root):
    u"""Отпечаток НАБОРА ФАЙЛОВ каталога: md5 от списка md5 всех `.py`.

    ⛔ ПРОЖИТО 21.09: `ssssi/freqtrade-strategies` и
    `werkkrew/freqtrade-strategies` оказались ПОБАЙТОВО ОДИНАКОВЫ — форк.
    Считать их двумя корпусами значит удвоить вес ОДНОГО автора, тогда как
    клетка объявлена в `DECORRELATION` именно как АВТОР. Собирая корпус
    поиском, а не руками, форки ловятся десятками ⇒ снимать их обязана
    МАШИНА, а не мой глаз.

    ⚠ Отпечаток берётся от СОДЕРЖИМОГО, не от имён: форк вправе
    переименовать каталог, но не вправе изменить файлы, оставшись форком.
    """
    import hashlib
    h = []
    for dp, dn, fn in os.walk(root):
        dn[:] = [d for d in dn if d not in (".git", "__pycache__")]
        for f in sorted(fn):
            if not f.endswith(".py"):
                continue
            try:
                with open(os.path.join(dp, f), "rb") as fh:
                    h.append(hashlib.md5(fh.read()).hexdigest())
            except Exception:                            # noqa: BLE001
                continue
    if not h:
        return u""
    return hashlib.md5(u"".join(sorted(h)).encode("utf-8")).hexdigest()[:12]


def audit_root(root, seen_src=None):
    u"""Три признака по одному корпусу. Возвращает словарь чисел.

    ⛔ `seen_src` — ОБЩЕЕ НА ВЕСЬ КОРПУС множество отпечатков СОДЕРЖИМОГО.
    Замерено 21.09 на 130 репозиториях: файлов-стратегий 4306, а различных
    по содержимому — 1794. **58 % корпуса есть копии**: одна и та же
    стратегия лежит у десятка людей. Считать их порознь значит умножить и
    корпус, и число находок на коэффициент переписывания, который к
    свойствам стратегий отношения не имеет.

    ⚠ Стратегия засчитывается ПЕРВОМУ репозиторию, где встретилась. Это
    не «авторство» — порядок обхода алфавитный, а не исторический; это
    лишь способ не считать одно дважды.
    """
    import hashlib
    files = []
    for dp, dn, fn in os.walk(root):
        dn[:] = [d for d in dn if d not in (".git", "__pycache__")]
        for f in fn:
            if f.endswith(".py") and "test" not in f.lower():
                files.append(os.path.join(dp, f))
    look, params, roi_only, total, by_fw = [], [], [], 0, {}
    dups, rnd = 0, []
    for p in files:
        try:
            src = io.open(p, encoding="utf-8", errors="replace").read()
        except Exception:                                # noqa: BLE001
            continue
        fw = framework_of(src)
        if fw is None:
            continue
        if seen_src is not None:
            sh = hashlib.md5(src.encode("utf-8", "replace")).hexdigest()
            if sh in seen_src:
                dups += 1
                continue
            seen_src.add(sh)
        total += 1
        by_fw[fw] = by_fw.get(fw, 0) + 1
        rel = os.path.relpath(p, root)
        h = check_lookahead(src, framework=fw)
        if h:
            look.append((rel, h[0]))
        rh = check_random(src)
        if rh:
            rnd.append((rel, rh[0]))
        n = count_params(src)
        if n:
            params.append((rel, n))
        steps, has_sl = roi_richness(src)
        cx = entry_complexity(src)
        if steps >= 3 and cx is not None and cx <= 2:
            roi_only.append((rel, steps, cx))
    return {u"total": total, u"look": look, u"params": params,
            u"roi": roi_only, u"fw": by_fw, u"dups": dups, u"rnd": rnd}


def main_corpus(a):
    u"""Свод по КАТАЛОГУ КОРПУСОВ: каждая подпапка — репозиторий."""
    seen, rows, dup, seen_src = {}, [], [], set()
    for name in sorted(os.listdir(a.corpus)):
        d = os.path.join(a.corpus, name)
        if not os.path.isdir(d) or name.startswith("."):
            continue
        fh = fileset_hash(d)
        if not fh:
            continue
        if fh in seen:
            dup.append((name, seen[fh]))
            continue
        seen[fh] = name
        r = audit_root(d, seen_src)
        if r[u"total"] or r[u"dups"]:
            rows.append((name, r))
    rows.sort(key=lambda x: -x[1][u"total"])

    ts = sum(r[u"total"] for _, r in rows)
    tl = sum(len(r[u"look"]) for _, r in rows)
    tp = sum(len(r[u"params"]) for _, r in rows)
    tr = sum(len(r[u"roi"]) for _, r in rows)
    fw = {}
    for _, r in rows:
        for k, v in r[u"fw"].items():
            fw[k] = fw.get(k, 0) + v

    print(u"── СВОД ПО КОРПУСУ · %s" % a.corpus)
    print(u"   репозиториев с хотя бы одной стратегией: %d" % len(rows))
    print(u"   ⚠ снято как ДУБЛИ (побайтово тот же набор файлов): %d"
          % len(dup))
    for n, orig in dup[:8]:
        print(u"        %s  ≡  %s" % (n, orig))
    td = sum(r[u"dups"] for _, r in rows)
    print(u"   стратегий РАЗЛИЧНЫХ по содержимому: %d   (%s)"
          % (ts, u", ".join(u"%s %d" % (k, v) for k, v in sorted(fw.items()))))
    print(u"   ⛔ снято КОПИЙ той же стратегии у других людей: %d  (%.0f %% "
          u"корпуса)" % (td, 100.0 * td / (ts + td) if ts + td else 0))
    print(u"      одна стратегия расходится по десятку репозиториев; считать")
    print(u"      их порознь — умножить и корпус, и находки на коэффициент")
    print(u"      переписывания, к свойствам стратегий отношения не имеющий")
    print()
    tn = sum(len(r[u"rnd"]) for _, r in rows)
    print(u"   ① ЗАГЛЯДЫВАНИЕ  %d   ② С ПОДБОРОМ  %d   ③ НА БАРЬЕРАХ  %d   "
          u"④ СЛУЧАЙНОСТЬ В СИГНАЛЕ  %d" % (tl, tp, tr, tn))
    print(u"      ④ — не заглядывание, а невоспроизводимость: динамика их")
    print(u"        путает (бросок монеты тоже меняет сигнал при удлинении ряда)")
    print()
    print(u"   %-46s %6s %6s" % (u"репозиторий", u"стратегий", u"загляд."))
    for n, r in rows:
        if len(r[u"look"]):
            print(u"   %-46s %6d %6d" % (n[:46], r[u"total"],
                                         len(r[u"look"])))
    print()
    print(u"   ── КАНДИДАТЫ НА ЗАГЛЯДЫВАНИЕ, ВСЕ ДО ОДНОГО")
    for n, r in rows:
        for rel, (ln, txt) in r[u"look"]:
            print(u"   %s/%s:%d" % (n, rel, ln))
            print(u"        %s" % txt[:96])
    print()
    print(u"   ⚠ ЭТО КАНДИДАТЫ, А НЕ НАХОДКИ. Находкой строка становится")
    print(u"     ТОЛЬКО прочитанной глазами: замерено 21.09 — из 26")
    print(u"     кандидатов истинными оказались 13.")
    return 0


# ⛔ ПОМЕТКА АВТОРА — ПАПКА, И ИМЁН У НЕЁ БОЛЬШЕ ОДНОГО. Прожито на первом
# прогоне родословной 21.09: признак знал только `lookahead_bias/` (так у
# freqtrade-strategies), а `RoboticAutomations` держит свою папку-пометку
# `dirty LA/` — и её копии у `jaredrsommer` лежат БЕЗ папки. Прибор
# печатал «копий без пометки: 0» и был слеп ровно на том, ради чего
# построен. Список коротко и явно; новое имя — с прожитым случаем.
LABEL_DIRS = (u"lookahead_bias", u"dirty la", u"dirty_la", u"lookahead/")


def _author_labelled(rel):
    r = rel.replace("\\", "/").lower()
    return any(k in r for k in LABEL_DIRS)


def lineage(corpus):
    u"""Родословная: одна стратегия → все репозитории, где она лежит.

    ⛔ ПОВОД 21.09: 56 % публичного корпуса — копии, и `DevilStra2` у `ntsd`
    оказался переименованной копией стратегии, которую официальный
    репозиторий держит в каталоге `lookahead_bias/` КАК ОБРАЗЕЦ ОШИБКИ.
    Помеченный сломанным код расходится по чужим репозиториям, ТЕРЯЯ
    ПОМЕТКУ. Кто у кого взял — не вопрос авторства (порядок обхода
    алфавитный); вопрос в том, УНАСЛЕДОВАЛА ЛИ КОПИЯ ИЗВЕСТНЫЙ ДЕФЕКТ.

    Возвращает список записей: (число_копий, отпечаток, [(репо, путь)],
    помечен_ли_автором, кандидат_ли_статики).
    """
    import hashlib
    where = {}
    for name in sorted(os.listdir(corpus)):
        d = os.path.join(corpus, name)
        if not os.path.isdir(d) or name.startswith("."):
            continue
        for dp, dn, fn in os.walk(d):
            dn[:] = [x for x in dn if x not in (".git", "__pycache__")]
            for f in fn:
                if not f.endswith(".py") or "test" in f.lower():
                    continue
                p = os.path.join(dp, f)
                try:
                    src = io.open(p, encoding="utf-8", errors="replace").read()
                except Exception:                        # noqa: BLE001
                    continue
                fw = framework_of(src)
                if fw is None:
                    continue
                sh = hashlib.md5(src.encode("utf-8", "replace")).hexdigest()
                rel = os.path.relpath(p, d).replace("\\", "/")
                ent = where.setdefault(sh, {u"at": [], u"src": src, u"fw": fw})
                ent[u"at"].append((name, rel))
    out = []
    for sh, ent in where.items():
        # ⚠ «помечен автором» — по ПУТИ у ЛЮБОЙ из копий: если хоть один
        # владелец положил файл в папку-пометку, дефект объявлен, и
        # остальные копии несут его БЕЗ пометки.
        labelled = any(_author_labelled(rel) for _, rel in ent[u"at"])
        flagged = bool(check_lookahead(ent[u"src"], framework=ent[u"fw"]))
        out.append((len(ent[u"at"]), sh[:12], sorted(ent[u"at"]),
                    labelled, flagged))
    out.sort(key=lambda x: (-x[0], x[1]))
    return out


def main_lineage(a):
    rows = lineage(a.corpus)
    copies = [r for r in rows if r[0] >= 2]
    inherited = [r for r in copies if r[3] or r[4]]
    print(u"── РОДОСЛОВНАЯ · %s" % a.corpus)
    print(u"   различных стратегий: %d · из них лежат в ≥2 местах: %d"
          % (len(rows), len(copies)))
    print(u"   ⛔ размноженных С ИЗВЕСТНЫМ ДЕФЕКТОМ (помечен автором копии "
          u"или кандидат статики): %d" % len(inherited))
    lost = sum(1 for n, sh, at, lab, flg in inherited if lab
               for r, rel in at if not _author_labelled(rel))
    print(u"   ⛔ копий, ПОТЕРЯВШИХ пометку автора по дороге: %d  "
          u"(родословных с пометкой: %d)"
          % (lost, sum(1 for r in inherited if r[3])))
    print(u"      ⚠ по ТОЧНОМУ содержимому; правленый форк (как DevilStra2 у "
          u"ntsd, 70 строк из 720) сюда не попадает — слепое пятно названо")
    print()
    print(u"   %-5s %-13s %-9s %-8s %s"
          % (u"копий", u"отпечаток", u"помечен", u"статика", u"где"))
    for n, sh, at, lab, flg in rows[:25]:
        if n < 2:
            break
        repos = sorted(set(r for r, _ in at))
        print(u"   %-5d %-13s %-9s %-8s %s%s"
              % (n, sh, u"ДА" if lab else u"—", u"ДА" if flg else u"—",
                 u", ".join(repos[:4]),
                 u" +%d" % (len(repos) - 4) if len(repos) > 4 else u""))
    print()
    print(u"   ── РАЗМНОЖЕННЫЕ С ИЗВЕСТНЫМ ДЕФЕКТОМ, ВСЕ")
    for n, sh, at, lab, flg in inherited:
        tag = (u"помечен автором у %s" %
               next(r for r, rel in at if _author_labelled(rel))
               if lab else u"кандидат статики")
        print(u"   %s · %d копий · %s" % (sh, n, tag))
        for r, rel in at:
            mark = u"⚠ БЕЗ ПОМЕТКИ" if lab and not _author_labelled(rel) \
                else u""
            print(u"        %s/%s  %s" % (r, rel, mark))
    print()
    print(u"   ⚠ «Помечен» — по пути у ЛЮБОЙ копии; «статика» — кандидат, "
          u"не находка.")
    print(u"     Порядок в списке алфавитный, авторства не устанавливает.")
    return 0


def main(argv):
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default="")
    ap.add_argument("--corpus", default="")
    ap.add_argument("--lineage", default="",
                    help=u"каталог корпусов: кто у кого скопировал и "
                         u"унаследовала ли копия известный дефект")
    ap.add_argument("--selftest", action="store_true")
    ap.add_argument("--lang", default="ru", choices=sorted(LANG))
    a = ap.parse_args(argv[1:])
    if a.selftest:
        return selftest()
    if a.lineage:
        if not os.path.isdir(a.lineage):
            sys.stderr.write(u"⛔ ОТКАЗ (код 2): каталога корпуса нет\n")
            return 2
        a.corpus = a.lineage
        return main_lineage(a)
    if a.corpus:
        if not os.path.isdir(a.corpus):
            sys.stderr.write(u"⛔ ОТКАЗ (код 2): каталога корпуса нет\n")
            return 2
        return main_corpus(a)
    if not a.root or not os.path.isdir(a.root):
        sys.stderr.write(u"⛔ ОТКАЗ (код 2): каталога нет\n")
        return 2

    files = []
    for dp, dn, fn in os.walk(a.root):
        dn[:] = [d for d in dn if d not in (".git", "__pycache__")]
        for f in fn:
            if f.endswith(".py") and "test" not in f.lower():
                files.append(os.path.join(dp, f))

    look, params, roi_only, total, by_fw = [], [], [], 0, {}
    # ⛔ 22.09 (разбор B-мест, форма D334): непрочитанный файл выпадал из
    #    корпуса молча — «N стратегий» не говорило, сколько не открылось.
    unread = []
    for p in files:
        try:
            src = io.open(p, encoding="utf-8", errors="replace").read()
        except (IOError, OSError) as ex:
            unread.append((os.path.relpath(p, a.root), type(ex).__name__))
            continue
        fw = framework_of(src)
        if fw is None:
            continue
        total += 1
        by_fw[fw] = by_fw.get(fw, 0) + 1
        rel = os.path.relpath(p, a.root)
        h = check_lookahead(src, framework=fw)
        if h:
            look.append((rel, h[0]))
        n = count_params(src)
        if n:
            params.append((rel, n))
        steps, has_sl = roi_richness(src)
        cx = entry_complexity(src)
        if steps >= 3 and cx is not None and cx <= 2:
            roi_only.append((rel, steps, cx))

    t = LANG.get(a.lang, LANG[u"ru"])
    print(t[u"head"] % a.root)
    print(t[u"total"]
          % (total, u", ".join(u"%s %d" % (k, v)
                               for k, v in sorted(by_fw.items())) or u"—"))
    if unread:
        print(u"   ⚠ НЕ ПРОЧИТАНО / UNREAD: %d — вне счёта, это «не знаю»"
              % len(unread))
        for rel, why in unread[:8]:
            print(u"        %s (%s)" % (rel, why))
    print()
    print(t[u"look"]
          % (len(look), total, len(look) / total * 100 if total else 0))
    for rel, (ln, txt) in look[:8]:
        print(u"        %s:%d  %s" % (rel, ln, txt))
    print()
    ps = sorted(params, key=lambda x: -x[1])
    print(t[u"dof"])
    print(t[u"dof_n"] % (len(ps), ps[0][1] if ps else 0))
    for rel, n in ps[:6]:
        print(u"        %-52s %d %s" % (rel, n, t[u"knobs"]))
    print()
    print(t[u"bar"] % len(roi_only))
    for rel, steps, cx in roi_only[:6]:
        print(u"        %-46s %s" % (rel, t[u"bar_n"] % (steps, cx)))
    print()
    # ── ОПОРЫ СЧИТАЮТСЯ, А НЕ ЗАЯВЛЯЮТСЯ ──
    # ⛔ ОПОРА РАЗЫГРЫВАЕТСЯ, А НЕ ВЫВОДИТСЯ ФОРМУЛОЙ. Гейт полноты
    # справедливо отверг аналитическую: заявленный контроль обязан быть
    # В КОДЕ, иначе это слово, а не проверка.
    all_rel = []
    for p in files:
        all_rel.append(os.path.relpath(p, a.root))
    truth = set(r for r in all_rel if "lookahead_bias" in r.replace("\\", "/"))
    marked = [r for r, _ in look if r in truth]
    if truth:
        import random
        rnd = random.Random(21)
        iters, hit = 20000, 0
        pool = list(all_rel)
        k = len(truth)
        for _ in range(iters):
            if set(rnd.sample(pool, k)) == truth:
                hit += 1
        print(t[u"rnd1"] % (len(marked), len(truth)))
        print(t[u"rnd2"] % (k, len(pool), iters, hit))
    print(t[u"triv"])
    print(t[u"warn1"])
    print(t[u"warn2"])
    return 0


if __name__ == "__main__":
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass
    sys.exit(main(sys.argv))
