# ClucHAnix_BB_RPB_MOD_E0V1E_ROI

Источник: [`davidzr/freqtrade-strategies`](https://github.com/davidzr/freqtrade-strategies) · файл `ClucHAnix_BB_RPB_MOD_E0V1E_ROI.py`

## Результат

**НЕ ПРИМЕНИМА** — Impossible to load Strategy 'ClucHAnix_BB_RPB_MOD_E0V1E_ROI'. This class does not exist or contains Python code errors.

## Проверки

| проверка | итог | подробности |
|---|---|---|
| заглядывание в будущее (родной детектор freqtrade) | · НЕ ПРИМЕНИМА | вывод не разобран |
| рекурсия индикаторов (родной детектор freqtrade) | ✅ ПРОШЛА | рекурсивных отклонений не найдено |
| прогрев объявлен | ✅ ПРОШЛА | 200 при потребности 168 |
| мёртвые настройки трейлинга | ⚠ НАЙДЕНО | trailing_stop=False, но trailing_stop_positive=0.3207 задан — читается как работающая защита |

---

*Прогон настоящим freqtrade, комиссия 0.1% за сторону, 8 пар к USDT, таймфрейм **5m**. Окно автора 2018-03-01…2020-03-01, вне выборки 2020-03-01…2026-08-20. «Не смогли проверить» нигде не печатается как «чисто».*
