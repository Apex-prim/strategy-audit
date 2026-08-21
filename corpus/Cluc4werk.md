# Cluc4werk

Source: [`PeetCrypto/freqtrade-stuff`](https://github.com/PeetCrypto/freqtrade-stuff) · file `Cluc4werk.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 522 | 2747 |
| expectancy per trade (USDT) | -0.46 | -0.32 |
| mean profit p-value | 3.548e-10 | 3.271e-78 |
| market change % (baseline) | -55.54 | 347.94 |
| strategy total % | -23.76 | -88.12 |
| Sharpe | -3.82 | -8.2 |
| Sortino | -8.33 | -11.7 |
| max drawdown % | 25.81 | 88.27 |
| profit factor | 0.55 | 0.39 |

**Retained out of sample: negative**

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free. Cross-strategy comparisons in this repository use average profit per trade in percent.

Baseline: buy-and-hold on the same pairs returned **-55.54%**; the strategy returned **-23.76%**.
Out of sample: buy-and-hold **347.94%** vs strategy **-88.12%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | could not run | вывод не разобран |
| indicator recursion (freqtrade's own `recursive-analysis`) | clean | рекурсивных отклонений не найдено |
| прогрев не объявлен | **found** | самый длинный индикатор 168 свечей, startup_candle_count не задан (по умолчанию 0) |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **1m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `4a7c7414af9b` · strategy list `dac6309df791d209`*
