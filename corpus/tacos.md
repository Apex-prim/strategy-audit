# tacos

Source: [`jaredrsommer/freqtradestrategies`](https://github.com/jaredrsommer/freqtradestrategies) · file `tacos.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 198 | 683 |
| average profit per trade % | -0.57 | -0.57 |
| win rate % | 70.2 | 68.8 |
| average trade duration, minutes | 17869.0 | 21412.0 |
| duration measured in own candles | 12.41 | 14.87 |
| expectancy per trade (USDT) | -1.26 | -0.93 |
| mean profit p-value | 0.3464 | 0.3352 |
| market change % (baseline) | -45.75 | 352.61 |
| strategy total % | -25.02 | -63.71 |
| Sharpe | -0.36 | -0.2 |
| Sortino | -0.6 | -0.2 |
| max drawdown % | 45.42 | 87.27 |
| profit factor | 0.84 | 0.9 |

**Retained out of sample: negative**

> **Read that number with care.** The author's window was a bear market (buy-and-hold −58%) and the out-of-sample window a bull market (+346%). For a long-biased strategy this ratio rewards having done *badly* in 2018–2020, so it measures regime luck as much as robustness. The regime-free comparison is the excess over buy-and-hold, below.

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free either. Cross-strategy comparisons in this repository use average profit per trade in percent.

**Excess over buy-and-hold** (regime-free): author's window **+20.7 pp**, out of sample **-416.3 pp**.

⚠ **Not statistically significant in its author's own window** (p = 0.3464 > 0.05): the average trade is not distinguishable from zero.

Baseline: buy-and-hold on the same pairs returned **-45.75%**; the strategy returned **-25.02%**.
Out of sample: buy-and-hold **352.61%** vs strategy **-63.71%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | clean | смещения не обнаружено |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | индикаторы меняются от объёма истории: wave_ci -0.282%, OBV -52.426%, rsi 1.778%, rsi_slope 3.253%, rsi_ma 1.709% |
| прогрев не объявлен | **found** | самый длинный индикатор 21 свечей, startup_candle_count не задан (по умолчанию 0) |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **1d** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `590bf74986c5` · strategy list `a039f448c17bed72`*
