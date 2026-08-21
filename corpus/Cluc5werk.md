# Cluc5werk

Source: [`PeetCrypto/freqtrade-stuff`](https://github.com/PeetCrypto/freqtrade-stuff) · file `Cluc5werk.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 466 | 1744 |
| expectancy per trade (USDT) | 0.01 | 2.11 |
| mean profit p-value | 0.9783 | 2.885e-05 |
| market change % (baseline) | -55.54 | 347.94 |
| strategy total % | 0.42 | 367.91 |
| Sharpe | 0.02 | 1.42 |
| Sortino | 0.01 | 0.61 |
| max drawdown % | 21.94 | 30.89 |
| profit factor | 1.01 | 1.53 |

**Retained out of sample: 21100%**

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free. Cross-strategy comparisons in this repository use average profit per trade in percent.

⚠ **Not statistically significant in its author's own window** (p = 0.9783 > 0.05): the average trade is not distinguishable from zero.

Baseline: buy-and-hold on the same pairs returned **-55.54%**; the strategy returned **0.42%**.
Out of sample: buy-and-hold **347.94%** vs strategy **367.91%** — **beats the baseline**.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | could not run | вывод не разобран |
| indicator recursion (freqtrade's own `recursive-analysis`) | clean | рекурсивных отклонений не найдено |
| прогрев не объявлен | **found** | самый длинный индикатор 168 свечей, startup_candle_count не задан (по умолчанию 0) |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **1m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `4a7c7414af9b` · strategy list `dac6309df791d209`*
