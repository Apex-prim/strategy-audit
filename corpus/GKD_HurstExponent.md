# GKD_HurstExponent

Source: [`jaredrsommer/freqtradestrategies`](https://github.com/jaredrsommer/freqtradestrategies) · file `GKD_HurstExponent.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 1061 | 4835 |
| average profit per trade % | -0.25 | -0.12 |
| win rate % | 84.6 | 86.4 |
| average trade duration, minutes | 1395.0 | 1564.0 |
| duration measured in own candles | 23.25 | 26.07 |
| expectancy per trade (USDT) | -0.28 | -0.12 |
| mean profit p-value | 0.01681 | 0.02305 |
| market change % (baseline) | -58.4 | 348.67 |
| strategy total % | -29.87 | -57.58 |
| Sharpe | -2.04 | -1.28 |
| Sortino | -2.29 | -1.27 |
| max drawdown % | 32.45 | 63.74 |
| profit factor | 0.79 | 0.9 |

**Retained out of sample: negative**

> **Read that number with care.** The author's window was a bear market (buy-and-hold −58%) and the out-of-sample window a bull market (+346%). For a long-biased strategy this ratio rewards having done *badly* in 2018–2020, so it measures regime luck as much as robustness. The regime-free comparison is the excess over buy-and-hold, below.

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free either. Cross-strategy comparisons in this repository use average profit per trade in percent.

**Excess over buy-and-hold** (regime-free): author's window **+28.5 pp**, out of sample **-406.2 pp**.

Baseline: buy-and-hold on the same pairs returned **-58.4%**; the strategy returned **-29.87%**.
Out of sample: buy-and-hold **348.67%** vs strategy **-57.58%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | clean | смещения не обнаружено |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | freqtrade ОТКАЗАЛСЯ анализировать: startup_candle_count=0, «приведёт к рекурсивным проблемам у части индикаторов» |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **1h** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `590bf74986c5` · strategy list `a039f448c17bed72`*
