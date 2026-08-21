# multi_tf

Источник: [`freqtrade/freqtrade-strategies`](https://github.com/freqtrade/freqtrade-strategies) · файл `multi_tf.py`

## Результат

**НЕ ПРИМЕНИМА** — Impossible to load Strategy 'multi_tf'. This class does not exist or contains Python code errors.

## Проверки

| проверка | итог | подробности |
|---|---|---|
| заглядывание в будущее (родной детектор freqtrade) | · НЕ ПРИМЕНИМА | Impossible to load Strategy 'multi_tf'. This class does not exist or contains Python code errors. |
| рекурсия индикаторов (родной детектор freqtrade) | · НЕ ПРИМЕНИМА | Impossible to load Strategy 'multi_tf'. This class does not exist or contains Python code errors. |
| прогрев объявлен | ✅ ПРОШЛА | 100 при потребности 14 |
| мёртвые настройки трейлинга | ⚠ НАЙДЕНО | trailing_stop=False, но trailing_stop_positive=0.001 задан — читается как работающая защита |

---

*Прогон настоящим freqtrade, комиссия 0.1% за сторону, 8 пар к USDT, таймфрейм **5m**. Окно автора 2018-03-01…2020-03-01, вне выборки 2020-03-01…2026-08-20. «Не смогли проверить» нигде не печатается как «чисто».*
