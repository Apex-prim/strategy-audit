# Ichess

Source: [`PeetCrypto/freqtrade-stuff`](https://github.com/PeetCrypto/freqtrade-stuff) · file `Ichess.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 62 | 293 |
| average profit per trade % | 1.16 | 2.19 |
| win rate % | 48.4 | 45.4 |
| average trade duration, minutes | 23992.0 | 26230.0 |
| duration measured in own candles | 16.66 | 18.22 |
| expectancy per trade (USDT) | 0.23 | 2.4 |
| mean profit p-value | 0.9539 | 0.4566 |
| market change % (baseline) | -59.68 | 352.61 |
| strategy total % | 1.45 | 70.22 |
| Sharpe | 0.01 | 0.1 |
| Sortino | 0.03 | 0.19 |
| max drawdown % | 34.24 | 44.61 |
| profit factor | 1.02 | 1.12 |

**Retained out of sample: 1043%**

> **Read that number with care.** The author's window was a bear market (buy-and-hold −58%) and the out-of-sample window a bull market (+346%). For a long-biased strategy this ratio rewards having done *badly* in 2018–2020, so it measures regime luck as much as robustness. The regime-free comparison is the excess over buy-and-hold, below.

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free either. Cross-strategy comparisons in this repository use average profit per trade in percent.

**Excess over buy-and-hold** (regime-free): author's window **+61.1 pp**, out of sample **-282.4 pp**.

⚠ **Not statistically significant in its author's own window** (p = 0.9539 > 0.05): the average trade is not distinguishable from zero.

Baseline: buy-and-hold on the same pairs returned **-59.68%**; the strategy returned **1.45%**.
Out of sample: buy-and-hold **352.61%** vs strategy **70.22%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | could not run | вывод не разобран |
| indicator recursion (freqtrade's own `recursive-analysis`) | clean | рекурсивных отклонений не найдено |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **1d** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `590bf74986c5` · strategy list `a039f448c17bed72`*
