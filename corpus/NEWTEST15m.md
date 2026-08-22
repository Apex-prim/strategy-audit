# NEWTEST15m

Source: [`PeetCrypto/freqtrade-stuff`](https://github.com/PeetCrypto/freqtrade-stuff) · file `FrayNew-HyperOpt (1).py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 607 | 2037 |
| average profit per trade % | -1.09 | -0.06 |
| win rate % | 83.9 | 87.4 |
| average trade duration, minutes | 9540.0 | 10584.0 |
| duration measured in own candles | 636.0 | 705.6 |
| expectancy per trade (USDT) | -1.14 | -0.33 |
| mean profit p-value | 0.0009625 | 0.3576 |
| market change % (baseline) | -58.34 | 345.85 |
| strategy total % | -69.46 | -66.69 |
| Sharpe | -2.14 | -0.34 |
| Sortino | -2.3 | -0.27 |
| max drawdown % | 71.27 | 86.58 |
| profit factor | 0.63 | 0.93 |

**Retained out of sample: negative**

> **Read that number with care.** The author's window was a bear market (buy-and-hold −58%) and the out-of-sample window a bull market (+346%). For a long-biased strategy this ratio rewards having done *badly* in 2018–2020, so it measures regime luck as much as robustness. The regime-free comparison is the excess over buy-and-hold, below.

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free either. Cross-strategy comparisons in this repository use average profit per trade in percent.

**Excess over buy-and-hold** (regime-free): author's window **-11.1 pp**, out of sample **-412.5 pp**.

Baseline: buy-and-hold on the same pairs returned **-58.34%**; the strategy returned **-69.46%**.
Out of sample: buy-and-hold **345.85%** vs strategy **-66.69%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | could not run | вывод не разобран |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | индикаторы меняются от объёма истории: bb_middleband -0.028%, bb_upperband -0.056%, bb_percent 26.782%, bb_width -22.031% |
| прогрев не объявлен | **found** | самый длинный индикатор 100 свечей, startup_candle_count не задан (по умолчанию 0) |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **15m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `590bf74986c5` · strategy list `a039f448c17bed72`*
