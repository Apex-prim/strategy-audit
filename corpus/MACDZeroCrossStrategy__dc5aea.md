# MACDZeroCrossStrategy

Source: [`ingpawat/freqtrade-strategy-with-backtest`](https://github.com/ingpawat/freqtrade-strategy-with-backtest) · file `MACDZeroCrossStrategy.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 64 | 275 |
| average profit per trade % | 3.67 | 9.79 |
| win rate % | 23.4 | 29.8 |
| average trade duration, minutes | 38430.0 | 39273.0 |
| duration measured in own candles | 26.69 | 27.27 |
| expectancy per trade (USDT) | 1.71 | 16.11 |
| mean profit p-value | 0.7003 | 0.1918 |
| market change % (baseline) | -59.68 | 352.61 |
| strategy total % | 10.94 | 443.06 |
| Sharpe | 0.08 | 0.18 |
| Sortino | 0.27 | 0.55 |
| max drawdown % | 30.61 | 33.39 |
| profit factor | 1.17 | 1.4 |

**Retained out of sample: 942%**

> **Read that number with care.** The author's window was a bear market (buy-and-hold −58%) and the out-of-sample window a bull market (+346%). For a long-biased strategy this ratio rewards having done *badly* in 2018–2020, so it measures regime luck as much as robustness. The regime-free comparison is the excess over buy-and-hold, below.

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free either. Cross-strategy comparisons in this repository use average profit per trade in percent.

**Excess over buy-and-hold** (regime-free): author's window **+70.6 pp**, out of sample **+90.4 pp**.

⚠ **Not statistically significant in its author's own window** (p = 0.7003 > 0.05): the average trade is not distinguishable from zero.

Baseline: buy-and-hold on the same pairs returned **-59.68%**; the strategy returned **10.94%**.
Out of sample: buy-and-hold **352.61%** vs strategy **443.06%** — **beats the baseline**.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | could not run | вывод не разобран |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | freqtrade ОТКАЗАЛСЯ анализировать: startup_candle_count=0, «приведёт к рекурсивным проблемам у части индикаторов» |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **1d** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `590bf74986c5` · strategy list `a039f448c17bed72`*
