# HilbertSineWave

Source: [`jaredrsommer/freqtradestrategies`](https://github.com/jaredrsommer/freqtradestrategies) · file `HilbertSineWave.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 935 | 3512 |
| average profit per trade % | -0.75 | -0.34 |
| win rate % | 41.3 | 44.7 |
| average trade duration, minutes | 2194.0 | 2344.0 |
| duration measured in own candles | 36.57 | 39.07 |
| expectancy per trade (USDT) | -0.65 | -0.23 |
| mean profit p-value | 9.419e-06 | 0.002657 |
| market change % (baseline) | -58.4 | 348.67 |
| strategy total % | -60.55 | -82.19 |
| Sharpe | -3.56 | -1.44 |
| Sortino | -12.38 | -3.1 |
| max drawdown % | 64.46 | 87.79 |
| profit factor | 0.72 | 0.88 |

**Retained out of sample: negative**

> **Read that number with care.** The author's window was a bear market (buy-and-hold −58%) and the out-of-sample window a bull market (+346%). For a long-biased strategy this ratio rewards having done *badly* in 2018–2020, so it measures regime luck as much as robustness. The regime-free comparison is the excess over buy-and-hold, below.

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free either. Cross-strategy comparisons in this repository use average profit per trade in percent.

**Excess over buy-and-hold** (regime-free): author's window **-2.1 pp**, out of sample **-430.9 pp**.

Baseline: buy-and-hold on the same pairs returned **-58.4%**; the strategy returned **-60.55%**.
Out of sample: buy-and-hold **348.67%** vs strategy **-82.19%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | clean | смещения не обнаружено |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | freqtrade ОТКАЗАЛСЯ анализировать: startup_candle_count=0, «приведёт к рекурсивным проблемам у части индикаторов» |
| прогрев не объявлен | **found** | самый длинный индикатор 5 свечей, startup_candle_count не задан (по умолчанию 0) |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **1h** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `590bf74986c5` · strategy list `a039f448c17bed72`*
