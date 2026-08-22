# GoldHedgeZeroMACD

Source: [`ingpawat/freqtrade-strategy-with-backtest`](https://github.com/ingpawat/freqtrade-strategy-with-backtest) · file `GoldHedgeZeroMACD.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 59 | 276 |
| average profit per trade % | 4.27 | 9.92 |
| win rate % | 23.7 | 29.7 |
| average trade duration, minutes | 37904.0 | 39235.0 |
| duration measured in own candles | 26.32 | 27.25 |
| expectancy per trade (USDT) | 0.85 | 1.98 |
| mean profit p-value | 0.3878 | 0.02303 |
| market change % (baseline) | -55.75 | 352.61 |
| strategy total % | 5.04 | 54.74 |
| Sharpe | 0.19 | 0.31 |
| Sortino | 0.95 | 3.46 |
| max drawdown % | 4.96 | 5.81 |
| profit factor | 1.5 | 2.61 |

**Retained out of sample: 233%**

> **Read that number with care.** The author's window was a bear market (buy-and-hold −58%) and the out-of-sample window a bull market (+346%). For a long-biased strategy this ratio rewards having done *badly* in 2018–2020, so it measures regime luck as much as robustness. The regime-free comparison is the excess over buy-and-hold, below.

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free either. Cross-strategy comparisons in this repository use average profit per trade in percent.

**Excess over buy-and-hold** (regime-free): author's window **+60.8 pp**, out of sample **-297.9 pp**.

⚠ **Not statistically significant in its author's own window** (p = 0.3878 > 0.05): the average trade is not distinguishable from zero.

Baseline: buy-and-hold on the same pairs returned **-55.75%**; the strategy returned **5.04%**.
Out of sample: buy-and-hold **352.61%** vs strategy **54.74%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | could not run | вывод не разобран |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | индикаторы меняются от объёма истории: macd 7.494%, macdsignal 12.583%, macdhist -24.552% |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **1d** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `590bf74986c5` · strategy list `a039f448c17bed72`*
