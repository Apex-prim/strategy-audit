# true_lambo

Source: [`PeetCrypto/freqtrade-stuff`](https://github.com/PeetCrypto/freqtrade-stuff) · file `true_lambo (1).py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 267 | 927 |
| expectancy per trade (USDT) | 0.06 | 0.81 |
| mean profit p-value | 0.8104 | 2.969e-05 |
| market change % (baseline) | -59.23 | 346.34 |
| strategy total % | 1.71 | 74.67 |
| Sharpe | 0.1 | 1.03 |
| Sortino | 0.09 | 1.01 |
| max drawdown % | 11.56 | 15.12 |
| profit factor | 1.04 | 1.47 |

**Retained out of sample: 1350%**

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free. Cross-strategy comparisons in this repository use average profit per trade in percent.

⚠ **Not statistically significant in its author's own window** (p = 0.8104 > 0.05): the average trade is not distinguishable from zero.

Baseline: buy-and-hold on the same pairs returned **-59.23%**; the strategy returned **1.71%**.
Out of sample: buy-and-hold **346.34%** vs strategy **74.67%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | could not run | вывод не разобран |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | индикаторы меняются от объёма истории: rsi_84 2.859%, rsi_112 3.913%, EWO -12.317%, ema_vwap_diff_50 -0.717% |
| прогрев не объявлен | **found** | самый длинный индикатор 200 свечей, startup_candle_count не задан (по умолчанию 0) |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **5m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `4a7c7414af9b` · strategy list `dac6309df791d209`*
