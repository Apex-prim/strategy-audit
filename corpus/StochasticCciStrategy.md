# StochasticCciStrategy

Source: [`mlsys-io/PortfolioBench`](https://github.com/mlsys-io/PortfolioBench) · file `StochasticCciStrategy.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 243 | 1082 |
| expectancy per trade (USDT) | -0.45 | -0.06 |
| mean profit p-value | 0.2302 | 0.7332 |
| market change % (baseline) | -59.27 | 348.67 |
| strategy total % | -10.97 | -6.37 |
| Sharpe | -0.49 | -0.09 |
| Sortino | -0.51 | -0.09 |
| max drawdown % | 18.01 | 28.03 |
| profit factor | 0.78 | 0.97 |

**Retained out of sample: negative**

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free. Cross-strategy comparisons in this repository use average profit per trade in percent.

⚠ **Not statistically significant in its author's own window** (p = 0.2302 > 0.05): the average trade is not distinguishable from zero.

Baseline: buy-and-hold on the same pairs returned **-59.27%**; the strategy returned **-10.97%**.
Out of sample: buy-and-hold **348.67%** vs strategy **-6.37%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | clean | смещения не обнаружено |
| indicator recursion (freqtrade's own `recursive-analysis`) | clean | рекурсивных отклонений не найдено |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **1h** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `8d9b3a08743f` · strategy list `a039f448c17bed72`*
