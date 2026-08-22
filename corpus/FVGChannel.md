# FVGChannel

Source: [`jaredrsommer/freqtradestrategies`](https://github.com/jaredrsommer/freqtradestrategies) · file `FVGChannel.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 4761 | 11838 |
| average profit per trade % | -0.37 | -0.22 |
| win rate % | 49.7 | 50.2 |
| average trade duration, minutes | 329.0 | 299.0 |
| duration measured in own candles | 5.48 | 4.98 |
| expectancy per trade (USDT) | -0.19 | -0.08 |
| mean profit p-value | 8.852e-17 | 2.13e-13 |
| market change % (baseline) | -58.4 | 348.67 |
| strategy total % | -89.9 | -96.57 |
| Sharpe | -15.06 | -6.46 |
| Sortino | -12.98 | -5.89 |
| max drawdown % | 89.9 | 96.61 |
| profit factor | 0.61 | 0.76 |

**Retained out of sample: negative**

> **Read that number with care.** The author's window was a bear market (buy-and-hold −58%) and the out-of-sample window a bull market (+346%). For a long-biased strategy this ratio rewards having done *badly* in 2018–2020, so it measures regime luck as much as robustness. The regime-free comparison is the excess over buy-and-hold, below.

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free either. Cross-strategy comparisons in this repository use average profit per trade in percent.

**Excess over buy-and-hold** (regime-free): author's window **-31.5 pp**, out of sample **-445.2 pp**.

Baseline: buy-and-hold on the same pairs returned **-58.4%**; the strategy returned **-89.9%**.
Out of sample: buy-and-hold **348.67%** vs strategy **-96.57%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | clean | смещения не обнаружено |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | freqtrade ОТКАЗАЛСЯ анализировать: startup_candle_count=0, «приведёт к рекурсивным проблемам у части индикаторов» |
| мёртвые настройки трейлинга | **found** | trailing_stop=False, но trailing_stop_positive=0.01 задан — читается как работающая защита |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **1h** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `590bf74986c5` · strategy list `a039f448c17bed72`*
