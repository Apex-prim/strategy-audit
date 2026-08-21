# BB_RPB_TSL_2

Источник: [`davidzr/freqtrade-strategies`](https://github.com/davidzr/freqtrade-strategies) · файл `BB_RPB_TSL_2.py`

## Результат

**НЕ ПРИМЕНИМА** — Cannot determine parameter space for max_slip.

## Проверки

| проверка | итог | подробности |
|---|---|---|
| заглядывание в будущее (родной детектор freqtrade) | · НЕ ПРИМЕНИМА | Cannot determine parameter space for max_slip. |
| рекурсия индикаторов (родной детектор freqtrade) | · НЕ ПРИМЕНИМА | Cannot determine parameter space for max_slip. |
| прогрев не объявлен | ⚠ НАЙДЕНО | самый длинный индикатор 200 свечей, startup_candle_count не задан (по умолчанию 0) |

---

*Прогон настоящим freqtrade, комиссия 0.1% за сторону, 8 пар к USDT, таймфрейм **3m**. Окно автора 2018-03-01…2020-03-01, вне выборки 2020-03-01…2026-08-20. «Не смогли проверить» нигде не печатается как «чисто».*
