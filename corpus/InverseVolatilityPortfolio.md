# InverseVolatilityPortfolio

Source: [`mlsys-io/PortfolioBench`](https://github.com/mlsys-io/PortfolioBench) · file `inv_vol.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 6 | 18 |
| average profit per trade % | -19.53 | 76.03 |
| win rate % | 33.3 | 66.7 |
| average trade duration, minutes | 948240.0 | 1281200.0 |
| duration measured in own candles | 658.5 | 889.72 |
| expectancy per trade (USDT) | -35.02 | 447.4 |
| mean profit p-value | 0.2757 | 0.1806 |
| market change % (baseline) | -45.75 | 352.61 |
| strategy total % | -21.01 | 805.31 |
| Sharpe | -0.09 | 0.05 |
| Sortino | -0.12 | 0.1 |
| max drawdown % | 25.46 | 37.02 |
| profit factor | 0.25 | 2.51 |

**Retained out of sample: n/a**

> **Read that number with care.** The author's window was a bear market (buy-and-hold −58%) and the out-of-sample window a bull market (+346%). For a long-biased strategy this ratio rewards having done *badly* in 2018–2020, so it measures regime luck as much as robustness. The regime-free comparison is the excess over buy-and-hold, below.

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free either. Cross-strategy comparisons in this repository use average profit per trade in percent.

**Excess over buy-and-hold** (regime-free): author's window **+24.7 pp**, out of sample **+452.7 pp**.

⚠ **Not statistically significant in its author's own window** (p = 0.2757 > 0.05): the average trade is not distinguishable from zero.

Baseline: buy-and-hold on the same pairs returned **-45.75%**; the strategy returned **-21.01%**.
Out of sample: buy-and-hold **352.61%** vs strategy **805.31%** — **beats the baseline**.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | could not run | вывод не разобран |
| indicator recursion (freqtrade's own `recursive-analysis`) | clean | рекурсивных отклонений не найдено |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **1d** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `590bf74986c5` · strategy list `a039f448c17bed72`*
