# BinHV45

Source: [`Foxel05/freqtrade-stuff`](https://github.com/Foxel05/freqtrade-stuff) · file `BinHV45.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 123 | 626 |
| average profit per trade % | -0.42 | -0.41 |
| win rate % | 74.0 | 74.1 |
| average trade duration, minutes | 175.0 | 107.0 |
| duration measured in own candles | 175.0 | 107.0 |
| expectancy per trade (USDT) | -0.52 | -0.44 |
| mean profit p-value | 0.0911 | 0.0001461 |
| market change % (baseline) | -55.54 | 347.94 |
| strategy total % | -6.37 | -27.83 |
| Sharpe | -0.5 | -0.77 |
| Sortino | -10.78 | -4.62 |
| max drawdown % | 9.36 | 30.1 |
| profit factor | 0.68 | 0.68 |

**Retained out of sample: negative**

> **Read that number with care.** The author's window was a bear market (buy-and-hold −58%) and the out-of-sample window a bull market (+346%). For a long-biased strategy this ratio rewards having done *badly* in 2018–2020, so it measures regime luck as much as robustness. The regime-free comparison is the excess over buy-and-hold, below.

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free either. Cross-strategy comparisons in this repository use average profit per trade in percent.

**Excess over buy-and-hold** (regime-free): author's window **+49.2 pp**, out of sample **-375.8 pp**.

⚠ **Not statistically significant in its author's own window** (p = 0.0911 > 0.05): the average trade is not distinguishable from zero.

Baseline: buy-and-hold on the same pairs returned **-55.54%**; the strategy returned **-6.37%**.
Out of sample: buy-and-hold **347.94%** vs strategy **-27.83%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | clean | смещения не обнаружено |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | freqtrade ОТКАЗАЛСЯ анализировать: startup_candle_count=0, «приведёт к рекурсивным проблемам у части индикаторов» |
| прогрев не объявлен | **found** | самый длинный индикатор 40 свечей, startup_candle_count не задан (по умолчанию 0) |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **1m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `590bf74986c5` · strategy list `a039f448c17bed72`*
