# Obelisk_3EMA_StochRSI_ATR

Источник: [`PeetCrypto/freqtrade-stuff`](https://github.com/PeetCrypto/freqtrade-stuff) · файл `Obelisk_3EMA_StochRSI_ATR.py`

## Результат

**НЕ ПРИМЕНИМА** — TypeError: NDFrame.fillna() got an unexpected keyword argument 'method'

## Проверки

| проверка | итог | подробности |
|---|---|---|
| заглядывание в будущее (родной детектор freqtrade) | · НЕ ПРИМЕНИМА | код 1 |
| рекурсия индикаторов (родной детектор freqtrade) | · НЕ ПРИМЕНИМА | код 1 |
| прогрев объявлен | ✅ ПРОШЛА | 500 при потребности 50 |

---

*Прогон настоящим freqtrade, комиссия 0.1% за сторону, 8 пар к USDT, таймфрейм **5m**. Окно автора 2018-03-01…2020-03-01, вне выборки 2020-03-01…2026-08-20. «Не смогли проверить» нигде не печатается как «чисто».*
