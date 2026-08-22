# GKD_FisherTransformMTF

Source: [`jaredrsommer/freqtradestrategies`](https://github.com/jaredrsommer/freqtradestrategies) · file `GKD_FisherTransformMTF.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 1022 | 3728 |
| average profit per trade % | -0.28 | 0.4 |
| win rate % | 39.3 | 41.4 |
| average trade duration, minutes | 5372.0 | 5475.0 |
| duration measured in own candles | 89.53 | 91.25 |
| expectancy per trade (USDT) | -0.46 | 0.17 |
| mean profit p-value | 0.02878 | 0.79 |
| market change % (baseline) | -58.4 | 348.67 |
| strategy total % | -47.03 | 65.02 |
| Sharpe | -1.83 | 0.13 |
| Sortino | -3.73 | 0.32 |
| max drawdown % | 64.5 | 77.34 |
| profit factor | 0.81 | 1.02 |

**Retained out of sample: n/a**

> **Read that number with care.** The author's window was a bear market (buy-and-hold −58%) and the out-of-sample window a bull market (+346%). For a long-biased strategy this ratio rewards having done *badly* in 2018–2020, so it measures regime luck as much as robustness. The regime-free comparison is the excess over buy-and-hold, below.

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free either. Cross-strategy comparisons in this repository use average profit per trade in percent.

**Excess over buy-and-hold** (regime-free): author's window **+11.4 pp**, out of sample **-283.7 pp**.

Baseline: buy-and-hold on the same pairs returned **-58.4%**; the strategy returned **-47.03%**.
Out of sample: buy-and-hold **348.67%** vs strategy **65.02%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | could not run | Fatal exception! |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | freqtrade ОТКАЗАЛСЯ анализировать: startup_candle_count=0, «приведёт к рекурсивным проблемам у части индикаторов» |
| прогрев не объявлен | **found** | самый длинный индикатор 4 свечей, startup_candle_count не задан (по умолчанию 0) |
| мёртвые настройки трейлинга | **found** | trailing_stop=False, но trailing_stop_positive=0.02 задан — читается как работающая защита |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **1h** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `590bf74986c5` · strategy list `a039f448c17bed72`*
