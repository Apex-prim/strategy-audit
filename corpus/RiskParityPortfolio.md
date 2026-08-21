# RiskParityPortfolio

Source: [`mlsys-io/PortfolioBench`](https://github.com/mlsys-io/PortfolioBench) · file `risk_parity.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 6 | 17 |
| expectancy per trade (USDT) | -68.6 | 413.04 |
| mean profit p-value | 0.06361 | 0.2285 |
| market change % (baseline) | -55.75 | 352.61 |
| strategy total % | -41.16 | 702.17 |
| Sharpe | -0.18 | 0.04 |
| Sortino | -0.43 | 0.07 |
| max drawdown % | 42.73 | 39.46 |
| profit factor | 0.08 | 2.17 |

**Retained out of sample: n/a**

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free. Cross-strategy comparisons in this repository use average profit per trade in percent.

⚠ **Not statistically significant in its author's own window** (p = 0.06361 > 0.05): the average trade is not distinguishable from zero.

Baseline: buy-and-hold on the same pairs returned **-55.75%**; the strategy returned **-41.16%**.
Out of sample: buy-and-hold **352.61%** vs strategy **702.17%** — **beats the baseline**.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | could not run | вывод не разобран |
| indicator recursion (freqtrade's own `recursive-analysis`) | clean | рекурсивных отклонений не найдено |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **1d** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `8d9b3a08743f` · strategy list `a039f448c17bed72`*
