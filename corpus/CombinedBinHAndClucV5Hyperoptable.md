# CombinedBinHAndClucV5Hyperoptable

Источник: [`davidzr/freqtrade-strategies`](https://github.com/davidzr/freqtrade-strategies) · файл `CombinedBinHAndClucV5Hyperoptable.py`

## Результат

**НЕ ПРИМЕНИМА** — Impossible to load Strategy 'CombinedBinHAndClucV5Hyperoptable'. This class does not exist or contains Python code errors.

## Проверки

| проверка | итог | подробности |
|---|---|---|
| заглядывание в будущее (родной детектор freqtrade) | · НЕ ПРИМЕНИМА | вывод не разобран |
| рекурсия индикаторов (родной детектор freqtrade) | ✅ ПРОШЛА | рекурсивных отклонений не найдено |
| прогрев не объявлен | ⚠ НАЙДЕНО | самый длинный индикатор 50 свечей, startup_candle_count не задан (по умолчанию 0) |

---

*Прогон настоящим freqtrade, комиссия 0.1% за сторону, 8 пар к USDT, таймфрейм **5m**. Окно автора 2018-03-01…2020-03-01, вне выборки 2020-03-01…2026-08-20. «Не смогли проверить» нигде не печатается как «чисто».*
