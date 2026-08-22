# Candle2

Source: [`jaredrsommer/freqtradestrategies`](https://github.com/jaredrsommer/freqtradestrategies) · file `2Candle (3).py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 1825 | 5801 |
| average profit per trade % | -0.87 | -0.38 |
| win rate % | 25.8 | 29.3 |
| average trade duration, minutes | 2876.0 | 3219.0 |
| duration measured in own candles | 47.93 | 53.65 |
| expectancy per trade (USDT) | -0.48 | -0.17 |
| mean profit p-value | 6.432e-13 | 0.01616 |
| market change % (baseline) | -58.4 | 348.67 |
| strategy total % | -88.33 | -96.67 |
| Sharpe | -8.09 | -1.48 |
| Sortino | -19.37 | -3.34 |
| max drawdown % | 89.29 | 97.82 |
| profit factor | 0.65 | 0.91 |

**Retained out of sample: negative**

> **Read that number with care.** The author's window was a bear market (buy-and-hold −58%) and the out-of-sample window a bull market (+346%). For a long-biased strategy this ratio rewards having done *badly* in 2018–2020, so it measures regime luck as much as robustness. The regime-free comparison is the excess over buy-and-hold, below.

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free either. Cross-strategy comparisons in this repository use average profit per trade in percent.

**Excess over buy-and-hold** (regime-free): author's window **-29.9 pp**, out of sample **-445.3 pp**.

Baseline: buy-and-hold on the same pairs returned **-58.4%**; the strategy returned **-88.33%**.
Out of sample: buy-and-hold **348.67%** vs strategy **-96.67%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | clean | смещения не обнаружено |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | freqtrade ОТКАЗАЛСЯ анализировать: startup_candle_count=0, «приведёт к рекурсивным проблемам у части индикаторов» |
| прогрев не объявлен | **found** | самый длинный индикатор 6 свечей, startup_candle_count не задан (по умолчанию 0) |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **1h** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `590bf74986c5` · strategy list `a039f448c17bed72`*
