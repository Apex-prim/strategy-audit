# Fakebuy

Source: [`davidzr/freqtrade-strategies`](https://github.com/davidzr/freqtrade-strategies) · file `Fakebuy.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 26 | 313 |
| average profit per trade % | -0.44 | 0.04 |
| win rate % | 84.6 | 87.5 |
| average trade duration, minutes | 274.0 | 119.0 |
| duration measured in own candles | 54.8 | 23.8 |
| expectancy per trade (USDT) | -0.55 | 0.04 |
| mean profit p-value | 0.5349 | 0.8684 |
| market change % (baseline) | -59.11 | 346.34 |
| strategy total % | -1.44 | 1.33 |
| Sharpe | -0.09 | 0.02 |
| Sortino | -14.36 | 0.43 |
| max drawdown % | 1.71 | 8.74 |
| profit factor | 0.66 | 1.03 |

**Retained out of sample: n/a**

> **Read that number with care.** The author's window was a bear market (buy-and-hold −58%) and the out-of-sample window a bull market (+346%). For a long-biased strategy this ratio rewards having done *badly* in 2018–2020, so it measures regime luck as much as robustness. The regime-free comparison is the excess over buy-and-hold, below.

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free either. Cross-strategy comparisons in this repository use average profit per trade in percent.

**Excess over buy-and-hold** (regime-free): author's window **+57.7 pp**, out of sample **-345.0 pp**.

⚠ **Not statistically significant in its author's own window** (p = 0.5349 > 0.05): the average trade is not distinguishable from zero.

Baseline: buy-and-hold on the same pairs returned **-59.11%**; the strategy returned **-1.44%**.
Out of sample: buy-and-hold **346.34%** vs strategy **1.33%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | could not run | вывод не разобран |
| indicator recursion (freqtrade's own `recursive-analysis`) | clean | рекурсивных отклонений не найдено |
| прогрев не объявлен | **found** | самый длинный индикатор 168 свечей, startup_candle_count не задан (по умолчанию 0) |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **5m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `590bf74986c5` · strategy list `a039f448c17bed72`*
