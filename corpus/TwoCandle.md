# TwoCandle

Source: [`jaredrsommer/freqtradestrategies`](https://github.com/jaredrsommer/freqtradestrategies) · file `TwoCandle.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 8368 | 10567 |
| average profit per trade % | -0.32 | -0.25 |
| win rate % | 34.2 | 40.8 |
| average trade duration, minutes | 257.0 | 233.0 |
| duration measured in own candles | 4.28 | 3.88 |
| expectancy per trade (USDT) | -0.12 | -0.09 |
| mean profit p-value | 2.72e-38 | 8.332e-31 |
| market change % (baseline) | -58.4 | 348.67 |
| strategy total % | -96.57 | -96.6 |
| Sharpe | -31.09 | -9.62 |
| Sortino | -37.5 | -12.02 |
| max drawdown % | 96.6 | 96.6 |
| profit factor | 0.61 | 0.7 |

**Retained out of sample: negative**

> **Read that number with care.** The author's window was a bear market (buy-and-hold −58%) and the out-of-sample window a bull market (+346%). For a long-biased strategy this ratio rewards having done *badly* in 2018–2020, so it measures regime luck as much as robustness. The regime-free comparison is the excess over buy-and-hold, below.

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free either. Cross-strategy comparisons in this repository use average profit per trade in percent.

**Excess over buy-and-hold** (regime-free): author's window **-38.2 pp**, out of sample **-445.3 pp**.

Baseline: buy-and-hold on the same pairs returned **-58.4%**; the strategy returned **-96.57%**.
Out of sample: buy-and-hold **348.67%** vs strategy **-96.6%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | clean | смещения не обнаружено |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | freqtrade ОТКАЗАЛСЯ анализировать: startup_candle_count=0, «приведёт к рекурсивным проблемам у части индикаторов» |
| прогрев не объявлен | **found** | самый длинный индикатор 80 свечей, startup_candle_count не задан (по умолчанию 0) |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **1h** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `590bf74986c5` · strategy list `a039f448c17bed72`*
