# NostalgiaForInfinityNext

Источник: [`PeetCrypto/freqtrade-stuff`](https://github.com/PeetCrypto/freqtrade-stuff) · файл `NFI731 BUSD.py`

## Результат

**НЕ ПРИМЕНИМА** — numpy.exceptions.DTypePromotionError: The DType <class 'numpy.dtypes.StrDType'> could not be promoted by <class 'numpy.dtypes._PyFloatDType'>. This means that n

## Проверки

| проверка | итог | подробности |
|---|---|---|
| заглядывание в будущее (родной детектор freqtrade) | · НЕ ПРИМЕНИМА | код 1 |
| рекурсия индикаторов (родной детектор freqtrade) | · НЕ ПРИМЕНИМА | код 1 |
| прогрев не объявлен | ⚠ НАЙДЕНО | самый длинный индикатор 200 свечей, startup_candle_count не задан (по умолчанию 0) |
| мёртвые настройки трейлинга | ⚠ НАЙДЕНО | trailing_stop=False, но trailing_stop_positive=0.01 задан — читается как работающая защита |

---

*Прогон настоящим freqtrade, комиссия 0.1% за сторону, 8 пар к USDT, таймфрейм **5m**. Окно автора 2018-03-01…2020-03-01, вне выборки 2020-03-01…2026-08-20. «Не смогли проверить» нигде не печатается как «чисто».*
