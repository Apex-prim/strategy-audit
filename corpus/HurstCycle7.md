# HurstCycle7

Source: [`jaredrsommer/freqtradestrategies`](https://github.com/jaredrsommer/freqtradestrategies) · file `HurstCycle7 (2).py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 5337 | — |
| average profit per trade % | 0.21 | — |
| win rate % | 49.1 | — |
| average trade duration, minutes | 296.0 | — |
| duration measured in own candles | 19.73 | — |
| expectancy per trade (USDT) | 0.53 | — |
| mean profit p-value | 6.164e-29 | — |
| market change % (baseline) | -58.11 | — |
| strategy total % | 284.88 | — |
| Sharpe | 21.44 | — |
| Sortino | 41.4 | — |
| max drawdown % | 6.21 | — |
| profit factor | 1.65 | — |

**Retained out of sample: —**

> **Read that number with care.** The author's window was a bear market (buy-and-hold −58%) and the out-of-sample window a bull market (+346%). For a long-biased strategy this ratio rewards having done *badly* in 2018–2020, so it measures regime luck as much as robustness. The regime-free comparison is the excess over buy-and-hold, below.

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free either. Cross-strategy comparisons in this repository use average profit per trade in percent.

**Excess over buy-and-hold** (regime-free): author's window **+343.0 pp**.

Baseline: buy-and-hold on the same pairs returned **-58.11%**; the strategy returned **284.88%**.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | could not run | Fatal exception! |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | freqtrade ОТКАЗАЛСЯ анализировать: startup_candle_count=0, «приведёт к рекурсивным проблемам у части индикаторов» |
| прогрев не объявлен | **found** | самый длинный индикатор 10 свечей, startup_candle_count не задан (по умолчанию 0) |
| признак утечки будущего | **found** | центрированное окно center=True |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **15m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `590bf74986c5` · strategy list `a039f448c17bed72`*
