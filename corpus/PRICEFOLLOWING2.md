# PRICEFOLLOWING2

Source: [`PeetCrypto/freqtrade-stuff`](https://github.com/PeetCrypto/freqtrade-stuff) · file `PRICEFOLLOWING2 (1).py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 2 | — |
| average profit per trade % | -1.94 | — |
| win rate % | 0.0 | — |
| average trade duration, minutes | 45.0 | — |
| duration measured in own candles | 3.0 | — |
| expectancy per trade (USDT) | -2.41 | — |
| mean profit p-value | 0.1468 | — |
| market change % (baseline) | -58.23 | — |
| strategy total % | -0.48 | — |
| Sharpe | -0.22 | — |
| Sortino | -0.22 | — |
| max drawdown % | 0.48 | — |
| profit factor | 0.0 | — |

**Retained out of sample: —**

> **Read that number with care.** The author's window was a bear market (buy-and-hold −58%) and the out-of-sample window a bull market (+346%). For a long-biased strategy this ratio rewards having done *badly* in 2018–2020, so it measures regime luck as much as robustness. The regime-free comparison is the excess over buy-and-hold, below.

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free either. Cross-strategy comparisons in this repository use average profit per trade in percent.

**Excess over buy-and-hold** (regime-free): author's window **+57.8 pp**.

⚠ **Not statistically significant in its author's own window** (p = 0.1468 > 0.05): the average trade is not distinguishable from zero.

Baseline: buy-and-hold on the same pairs returned **-58.23%**; the strategy returned **-0.48%**.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | could not run | вывод не разобран |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | индикаторы меняются от объёма истории: rsi -20.700% |
| прогрев не объявлен | **found** | самый длинный индикатор 100 свечей, startup_candle_count не задан (по умолчанию 0) |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **15m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `590bf74986c5` · strategy list `a039f448c17bed72`*
