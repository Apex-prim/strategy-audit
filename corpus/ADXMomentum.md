# ADXMomentum

Source: [`PeetCrypto/freqtrade-stuff`](https://github.com/PeetCrypto/freqtrade-stuff) · file `ADXMomentum.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 20 | 63 |
| average profit per trade % | 0.13 | -0.5 |
| win rate % | 75.0 | 69.8 |
| average trade duration, minutes | 651.0 | 684.0 |
| duration measured in own candles | 10.85 | 11.4 |
| expectancy per trade (USDT) | 0.16 | -0.61 |
| mean profit p-value | 0.7087 | 0.1589 |
| market change % (baseline) | -59.31 | 348.67 |
| strategy total % | 0.33 | -3.84 |
| Sharpe | 0.05 | -0.09 |
| Sortino | 0.14 | -0.09 |
| max drawdown % | 0.74 | 4.74 |
| profit factor | 1.21 | 0.58 |

**Retained out of sample: negative**

> **Read that number with care.** The author's window was a bear market (buy-and-hold −58%) and the out-of-sample window a bull market (+346%). For a long-biased strategy this ratio rewards having done *badly* in 2018–2020, so it measures regime luck as much as robustness. The regime-free comparison is the excess over buy-and-hold, below.

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free either. Cross-strategy comparisons in this repository use average profit per trade in percent.

**Excess over buy-and-hold** (regime-free): author's window **+59.6 pp**, out of sample **-352.5 pp**.

⚠ **Not statistically significant in its author's own window** (p = 0.7087 > 0.05): the average trade is not distinguishable from zero.

Baseline: buy-and-hold on the same pairs returned **-59.31%**; the strategy returned **0.33%**.
Out of sample: buy-and-hold **348.67%** vs strategy **-3.84%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | could not run | вывод не разобран |
| indicator recursion (freqtrade's own `recursive-analysis`) | clean | рекурсивных отклонений не найдено |
| прогрев не объявлен | **found** | самый длинный индикатор 25 свечей, startup_candle_count не задан (по умолчанию 0) |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **1h** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `590bf74986c5` · strategy list `a039f448c17bed72`*
