# PrawnstarOBV

Source: [`PeetCrypto/freqtrade-stuff`](https://github.com/PeetCrypto/freqtrade-stuff) · file `PrawnstarOBV.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 1496 | 5570 |
| average profit per trade % | 0.5 | 0.93 |
| win rate % | 76.6 | 79.2 |
| average trade duration, minutes | 4283.0 | 4216.0 |
| duration measured in own candles | 71.38 | 70.27 |
| expectancy per trade (USDT) | 0.43 | 27.85 |
| mean profit p-value | 0.2196 | 0.01684 |
| market change % (baseline) | -59.27 | 348.67 |
| strategy total % | 63.58 | 15514.99 |
| Sharpe | 1.25 | 1.44 |
| Sortino | 2.14 | 1.05 |
| max drawdown % | 48.78 | 39.73 |
| profit factor | 1.08 | 1.13 |

**Retained out of sample: 6477%**

> **Read that number with care.** The author's window was a bear market (buy-and-hold −58%) and the out-of-sample window a bull market (+346%). For a long-biased strategy this ratio rewards having done *badly* in 2018–2020, so it measures regime luck as much as robustness. The regime-free comparison is the excess over buy-and-hold, below.

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free either. Cross-strategy comparisons in this repository use average profit per trade in percent.

**Excess over buy-and-hold** (regime-free): author's window **+122.8 pp**, out of sample **+15166.3 pp**.

⚠ **Not statistically significant in its author's own window** (p = 0.2196 > 0.05): the average trade is not distinguishable from zero.

Baseline: buy-and-hold on the same pairs returned **-59.27%**; the strategy returned **63.58%**.
Out of sample: buy-and-hold **348.67%** vs strategy **15514.99%** — **beats the baseline**.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | could not run | вывод не разобран |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | индикаторы меняются от объёма истории: rsi 4.044%, obv -85.099%, obvSma -90.179% |
| прогрев не объявлен | **found** | самый длинный индикатор 7 свечей, startup_candle_count не задан (по умолчанию 0) |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **1h** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `590bf74986c5` · strategy list `a039f448c17bed72`*
