# NowoIchimoku1hV2

Источник: [`PeetCrypto/freqtrade-stuff`](https://github.com/PeetCrypto/freqtrade-stuff) · файл `NowoIchimoku1hV2 (1).py`

## Результат

**НЕ ПРИМЕНИМА** — Impossible to load Strategy 'NowoIchimoku1hV2'. This class does not exist or contains Python code errors.

## Проверки

| проверка | итог | подробности |
|---|---|---|
| заглядывание в будущее (родной детектор freqtrade) | · НЕ ПРИМЕНИМА | вывод не разобран |
| рекурсия индикаторов (родной детектор freqtrade) | ✅ ПРОШЛА | рекурсивных отклонений не найдено |
| трейлинг на полном стопе | ⚠ НАЙДЕНО | trailing_stop=True без trailing_stop_positive ⇒ стоп тащится на ВСЁ расстояние стоп-лосса |

---

*Прогон настоящим freqtrade, комиссия 0.1% за сторону, 8 пар к USDT, таймфрейм **1h**. Окно автора 2018-03-01…2020-03-01, вне выборки 2020-03-01…2026-08-20. «Не смогли проверить» нигде не печатается как «чисто».*
