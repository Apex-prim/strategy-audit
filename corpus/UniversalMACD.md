# UniversalMACD

Source: [`TheoBrigitte/freqtrade`](https://github.com/TheoBrigitte/freqtrade) · file `UniversalMACD.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 516 | 1574 |
| average profit per trade % | 0.1 | 0.56 |
| win rate % | 74.6 | 75.1 |
| average trade duration, minutes | 1747.0 | 1280.0 |
| duration measured in own candles | 349.4 | 256.0 |
| expectancy per trade (USDT) | 0.07 | 1.02 |
| mean profit p-value | 0.8152 | 0.001483 |
| market change % (baseline) | -58.37 | 346.34 |
| strategy total % | 3.77 | 159.94 |
| Sharpe | 0.14 | 1.02 |
| Sortino | 0.08 | 0.58 |
| max drawdown % | 20.95 | 34.79 |
| profit factor | 1.06 | 1.54 |

**Retained out of sample: 1457%**

> **Read that number with care.** The author's window was a bear market (buy-and-hold −58%) and the out-of-sample window a bull market (+346%). For a long-biased strategy this ratio rewards having done *badly* in 2018–2020, so it measures regime luck as much as robustness. The regime-free comparison is the excess over buy-and-hold, below.

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free either. Cross-strategy comparisons in this repository use average profit per trade in percent.

**Excess over buy-and-hold** (regime-free): author's window **+62.1 pp**, out of sample **-186.4 pp**.

⚠ **Not statistically significant in its author's own window** (p = 0.8152 > 0.05): the average trade is not distinguishable from zero.

Baseline: buy-and-hold on the same pairs returned **-58.37%**; the strategy returned **3.77%**.
Out of sample: buy-and-hold **346.34%** vs strategy **159.94%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | clean | смещения не обнаружено |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | индикаторы меняются от объёма истории: ma26 -0.015%, umacd -645.217% |
| прогрев не объявлен | **found** | самый длинный индикатор 26 свечей, startup_candle_count не задан (по умолчанию 0) |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **5m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `590bf74986c5` · strategy list `a039f448c17bed72`*
