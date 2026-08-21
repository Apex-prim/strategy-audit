# MinimumVariancePortfolio

Source: [`mlsys-io/PortfolioBench`](https://github.com/mlsys-io/PortfolioBench) · file `min_var.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 11 | 105 |
| expectancy per trade (USDT) | -6.15 | 252.15 |
| mean profit p-value | 0.7282 | 0.3029 |
| market change % (baseline) | -45.75 | 352.61 |
| strategy total % | -6.77 | 2647.59 |
| Sharpe | -0.03 | 0.09 |
| Sortino | -0.08 | 0.18 |
| max drawdown % | 21.72 | 37.44 |
| profit factor | 0.74 | 1.92 |

**Retained out of sample: n/a**

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free. Cross-strategy comparisons in this repository use average profit per trade in percent.

⚠ **Not statistically significant in its author's own window** (p = 0.7282 > 0.05): the average trade is not distinguishable from zero.

Baseline: buy-and-hold on the same pairs returned **-45.75%**; the strategy returned **-6.77%**.
Out of sample: buy-and-hold **352.61%** vs strategy **2647.59%** — **beats the baseline**.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | could not run | вывод не разобран |
| indicator recursion (freqtrade's own `recursive-analysis`) | clean | рекурсивных отклонений не найдено |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **1d** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `8d9b3a08743f` · strategy list `a039f448c17bed72`*
