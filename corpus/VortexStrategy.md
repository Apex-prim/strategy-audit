# VortexStrategy

Source: [`mlsys-io/PortfolioBench`](https://github.com/mlsys-io/PortfolioBench) · file `VortexStrategy.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 15221 | 14566 |
| expectancy per trade (USDT) | -0.06 | -0.07 |
| mean profit p-value | 1.411e-70 | 3.092e-60 |
| market change % (baseline) | -58.41 | 346.34 |
| strategy total % | -95.9 | -96.57 |
| Sharpe | -57.65 | -16.06 |
| Sortino | -94.62 | -27.44 |
| max drawdown % | 95.91 | 96.57 |
| profit factor | 0.58 | 0.59 |

**Retained out of sample: negative**

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free. Cross-strategy comparisons in this repository use average profit per trade in percent.

Baseline: buy-and-hold on the same pairs returned **-58.41%**; the strategy returned **-95.9%**.
Out of sample: buy-and-hold **346.34%** vs strategy **-96.57%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | clean | смещения не обнаружено |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | индикаторы меняются от объёма истории: rsi 12.447% |
| прогрев занижен | **found** | объявлено 20, нужно не менее 50 |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **5m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `8d9b3a08743f` · strategy list `a039f448c17bed72`*
