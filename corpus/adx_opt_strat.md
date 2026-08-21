# adx_opt_strat

Источник: [`davidzr/freqtrade-strategies`](https://github.com/davidzr/freqtrade-strategies) · файл `adx_opt_strat.py`

## Результат

**НЕ ПРИМЕНИМА** — Timeframe needs to be set in either configuration or as cli argument `--timeframe 5m`

## Проверки

| проверка | итог | подробности |
|---|---|---|
| заглядывание в будущее (родной детектор freqtrade) | · НЕ ПРИМЕНИМА | Timeframe needs to be set in either configuration or as cli argument `--timeframe 5m` |
| рекурсия индикаторов (родной детектор freqtrade) | · НЕ ПРИМЕНИМА | Timeframe needs to be set in either configuration or as cli argument `--timeframe 5m` |
| прогрев не объявлен | ⚠ НАЙДЕНО | самый длинный индикатор 25 свечей, startup_candle_count не задан (по умолчанию 0) |

---

*Прогон настоящим freqtrade, комиссия 0.1% за сторону, 8 пар к USDT, таймфрейм **НЕ ОПРЕДЕЛЁН**. Окно автора 2018-03-01…2020-03-01, вне выборки 2020-03-01…2026-08-20. «Не смогли проверить» нигде не печатается как «чисто».*
