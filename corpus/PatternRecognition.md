# PatternRecognition

Source: [`TheoBrigitte/freqtrade`](https://github.com/TheoBrigitte/freqtrade) · file `PatternRecognition.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 134 | 520 |
| average profit per trade % | -3.25 | 0.02 |
| win rate % | 67.2 | 74.8 |
| average trade duration, minutes | 22481.0 | 24580.0 |
| duration measured in own candles | 15.61 | 17.07 |
| expectancy per trade (USDT) | -3.56 | -0.48 |
| mean profit p-value | 0.007559 | 0.6741 |
| market change % (baseline) | -59.68 | 352.61 |
| strategy total % | -47.69 | -24.98 |
| Sharpe | -0.82 | -0.08 |
| Sortino | -1.26 | -0.08 |
| max drawdown % | 53.11 | 67.94 |
| profit factor | 0.53 | 0.95 |

**Retained out of sample: negative**

> **Read that number with care.** The author's window was a bear market (buy-and-hold −58%) and the out-of-sample window a bull market (+346%). For a long-biased strategy this ratio rewards having done *badly* in 2018–2020, so it measures regime luck as much as robustness. The regime-free comparison is the excess over buy-and-hold, below.

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free either. Cross-strategy comparisons in this repository use average profit per trade in percent.

**Excess over buy-and-hold** (regime-free): author's window **+12.0 pp**, out of sample **-377.6 pp**.

Baseline: buy-and-hold on the same pairs returned **-59.68%**; the strategy returned **-47.69%**.
Out of sample: buy-and-hold **352.61%** vs strategy **-24.98%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | could not run | Fatal exception! |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | freqtrade ОТКАЗАЛСЯ анализировать: startup_candle_count=0, «приведёт к рекурсивным проблемам у части индикаторов» |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **1d** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `590bf74986c5` · strategy list `a039f448c17bed72`*
