# MaxSharpePortfolio

Source: [`mlsys-io/PortfolioBench`](https://github.com/mlsys-io/PortfolioBench) · file `max_sharpe.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 11 | 61 |
| expectancy per trade (USDT) | -63.78 | -1.49 |
| mean profit p-value | 0.02657 | 0.9805 |
| market change % (baseline) | -55.75 | 352.61 |
| strategy total % | -70.16 | -9.07 |
| Sharpe | -0.26 | -0.0 |
| Sortino | -0.27 | -0.0 |
| max drawdown % | 70.16 | 86.19 |
| profit factor | 0.04 | 0.99 |

**Retained out of sample: negative**

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free. Cross-strategy comparisons in this repository use average profit per trade in percent.

Baseline: buy-and-hold on the same pairs returned **-55.75%**; the strategy returned **-70.16%**.
Out of sample: buy-and-hold **352.61%** vs strategy **-9.07%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | could not run | вывод не разобран |
| indicator recursion (freqtrade's own `recursive-analysis`) | clean | рекурсивных отклонений не найдено |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **1d** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `8d9b3a08743f` · strategy list `a039f448c17bed72`*
