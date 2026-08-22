# HurstCycleV6

Source: [`jaredrsommer/freqtradestrategies`](https://github.com/jaredrsommer/freqtradestrategies) · file `HurstCycleV6.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 1558 | — |
| average profit per trade % | 4.26 | — |
| win rate % | 75.0 | — |
| average trade duration, minutes | 1907.0 | — |
| duration measured in own candles | 127.13 | — |
| expectancy per trade (USDT) | 1494.29 | — |
| mean profit p-value | 1.638e-33 | — |
| market change % (baseline) | -58.11 | — |
| strategy total % | 232810.76 | — |
| Sharpe | 12.75 | — |
| Sortino | 29.1 | — |
| max drawdown % | 5.61 | — |
| profit factor | 5.74 | — |

**Retained out of sample: —**

> **Read that number with care.** The author's window was a bear market (buy-and-hold −58%) and the out-of-sample window a bull market (+346%). For a long-biased strategy this ratio rewards having done *badly* in 2018–2020, so it measures regime luck as much as robustness. The regime-free comparison is the excess over buy-and-hold, below.

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free either. Cross-strategy comparisons in this repository use average profit per trade in percent.

**Excess over buy-and-hold** (regime-free): author's window **+232868.9 pp**.

Baseline: buy-and-hold on the same pairs returned **-58.11%**; the strategy returned **232810.76%**.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | could not run | Fatal exception! |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | freqtrade ОТКАЗАЛСЯ анализировать: startup_candle_count=0, «приведёт к рекурсивным проблемам у части индикаторов» |
| признак утечки будущего | **found** | центрированное окно center=True |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **15m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `590bf74986c5` · strategy list `a039f448c17bed72`*
