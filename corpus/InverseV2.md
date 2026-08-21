# InverseV2

Source: [`PeetCrypto/freqtrade-stuff`](https://github.com/PeetCrypto/freqtrade-stuff) · file `InverseV2.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 198 | 791 |
| expectancy per trade (USDT) | 0.4 | 0.41 |
| mean profit p-value | 0.349 | 0.1689 |
| market change % (baseline) | -54.03 | 348.67 |
| strategy total % | 7.97 | 32.29 |
| Sharpe | 0.35 | 0.31 |
| Sortino | 0.87 | 0.89 |
| max drawdown % | 10.47 | 23.75 |
| profit factor | 1.24 | 1.18 |

**Retained out of sample: 102%**

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free. Cross-strategy comparisons in this repository use average profit per trade in percent.

⚠ **Not statistically significant in its author's own window** (p = 0.349 > 0.05): the average trade is not distinguishable from zero.

Baseline: buy-and-hold on the same pairs returned **-54.03%**; the strategy returned **7.97%**.
Out of sample: buy-and-hold **348.67%** vs strategy **32.29%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | could not run | вывод не разобран |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | индикаторы меняются от объёма истории: ema_100_4h -0.020%, ema_200 -0.448% |
| прогрев не объявлен | **found** | самый длинный индикатор 200 свечей, startup_candle_count не задан (по умолчанию 0) |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **1h** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `2da4e157b88f` · strategy list `dac6309df791d209`*
