# GKD_CT

Source: [`jaredrsommer/freqtradestrategies`](https://github.com/jaredrsommer/freqtradestrategies) · file `GKD_CT.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 1382 | — |
| average profit per trade % | -0.96 | — |
| win rate % | 60.9 | — |
| average trade duration, minutes | 3565.0 | — |
| duration measured in own candles | 59.42 | — |
| expectancy per trade (USDT) | -0.62 | — |
| mean profit p-value | 9.93e-09 | — |
| market change % (baseline) | -58.4 | — |
| strategy total % | -85.1 | — |
| Sharpe | -5.61 | — |
| Sortino | -5.0 | — |
| max drawdown % | 85.22 | — |
| profit factor | 0.59 | — |

**Retained out of sample: —**

> **Read that number with care.** The author's window was a bear market (buy-and-hold −58%) and the out-of-sample window a bull market (+346%). For a long-biased strategy this ratio rewards having done *badly* in 2018–2020, so it measures regime luck as much as robustness. The regime-free comparison is the excess over buy-and-hold, below.

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free either. Cross-strategy comparisons in this repository use average profit per trade in percent.

**Excess over buy-and-hold** (regime-free): author's window **-26.7 pp**.

Baseline: buy-and-hold on the same pairs returned **-58.4%**; the strategy returned **-85.1%**.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | could not run | Fatal exception! |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | freqtrade ОТКАЗАЛСЯ анализировать: startup_candle_count=0, «приведёт к рекурсивным проблемам у части индикаторов» |
| признак утечки будущего | **found** | центрированное окно center=True |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **1h** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `590bf74986c5` · strategy list `a039f448c17bed72`*
