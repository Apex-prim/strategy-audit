# FReinforcedStrategy

Источник: [`freqtrade/freqtrade-strategies`](https://github.com/freqtrade/freqtrade-strategies) · файл `FReinforcedStrategy.py`

## Результат

**НЕ ПРИМЕНИМА** — ImportError: Short strategies cannot run in spot markets. Please make sure that this is the correct strategy and that your trading mode configuration is correct

## Проверки

| проверка | итог | подробности |
|---|---|---|
| заглядывание в будущее (родной детектор freqtrade) | · НЕ ПРИМЕНИМА | Fatal exception! |
| рекурсия индикаторов (родной детектор freqtrade) | · НЕ ПРИМЕНИМА | Fatal exception! |
| прогрев не объявлен | ⚠ НАЙДЕНО | самый длинный индикатор 50 свечей, startup_candle_count не задан (по умолчанию 0) |

---

*Прогон настоящим freqtrade, комиссия 0.1% за сторону, 8 пар к USDT, таймфрейм **5m**. Окно автора 2018-03-01…2020-03-01, вне выборки 2020-03-01…2026-08-20. «Не смогли проверить» нигде не печатается как «чисто».*
