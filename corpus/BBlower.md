# BBlower

Source: [`davidzr/freqtrade-strategies`](https://github.com/davidzr/freqtrade-strategies) · file `BBlower.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 414 | 1376 |
| average profit per trade % | -0.76 | -0.43 |
| win rate % | 63.0 | 64.0 |
| average trade duration, minutes | 3299.0 | 3836.0 |
| duration measured in own candles | 659.8 | 767.2 |
| expectancy per trade (USDT) | -0.84 | -0.42 |
| mean profit p-value | 0.01405 | 0.01367 |
| market change % (baseline) | -58.23 | 346.34 |
| strategy total % | -34.68 | -57.51 |
| Sharpe | -1.31 | -0.74 |
| Sortino | -1.23 | -0.7 |
| max drawdown % | 37.06 | 57.8 |
| profit factor | 0.66 | 0.8 |

**Retained out of sample: negative**

> **Read that number with care.** The author's window was a bear market (buy-and-hold −58%) and the out-of-sample window a bull market (+346%). For a long-biased strategy this ratio rewards having done *badly* in 2018–2020, so it measures regime luck as much as robustness. The regime-free comparison is the excess over buy-and-hold, below.

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free either. Cross-strategy comparisons in this repository use average profit per trade in percent.

**Excess over buy-and-hold** (regime-free): author's window **+23.5 pp**, out of sample **-403.8 pp**.

Baseline: buy-and-hold on the same pairs returned **-58.23%**; the strategy returned **-34.68%**.
Out of sample: buy-and-hold **346.34%** vs strategy **-57.51%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | clean | смещения не обнаружено |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | freqtrade ОТКАЗАЛСЯ анализировать: startup_candle_count=0, «приведёт к рекурсивным проблемам у части индикаторов» |
| прогрев не объявлен | **found** | самый длинный индикатор 50 свечей, startup_candle_count не задан (по умолчанию 0) |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **5m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `590bf74986c5` · strategy list `a039f448c17bed72`*
