# HSI

Source: [`jaredrsommer/freqtradestrategies`](https://github.com/jaredrsommer/freqtradestrategies) · file `HSI (2).py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 13163 | — |
| average profit per trade % | -0.21 | — |
| win rate % | 19.7 | — |
| average trade duration, minutes | 12.0 | — |
| duration measured in own candles | 2.4 | — |
| expectancy per trade (USDT) | -0.07 | — |
| mean profit p-value | 9.339e-299 | — |
| market change % (baseline) | -58.23 | — |
| strategy total % | -96.58 | — |
| Sharpe | -113.72 | — |
| Sortino | -147.49 | — |
| max drawdown % | 96.58 | — |
| profit factor | 0.29 | — |

**Retained out of sample: —**

> **Read that number with care.** The author's window was a bear market (buy-and-hold −58%) and the out-of-sample window a bull market (+346%). For a long-biased strategy this ratio rewards having done *badly* in 2018–2020, so it measures regime luck as much as robustness. The regime-free comparison is the excess over buy-and-hold, below.

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free either. Cross-strategy comparisons in this repository use average profit per trade in percent.

**Excess over buy-and-hold** (regime-free): author's window **-38.4 pp**.

Baseline: buy-and-hold on the same pairs returned **-58.23%**; the strategy returned **-96.58%**.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | clean | смещения не обнаружено |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | freqtrade ОТКАЗАЛСЯ анализировать: startup_candle_count=0, «приведёт к рекурсивным проблемам у части индикаторов» |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **5m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `590bf74986c5` · strategy list `a039f448c17bed72`*
