# MoneyFlowStrategy

Source: [`mlsys-io/PortfolioBench`](https://github.com/mlsys-io/PortfolioBench) · file `MoneyFlowStrategy.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 4526 | 14964 |
| expectancy per trade (USDT) | -0.14 | -0.06 |
| mean profit p-value | 3.508e-10 | 2.438e-10 |
| market change % (baseline) | -58.41 | 346.34 |
| strategy total % | -62.5 | -96.67 |
| Sharpe | -11.07 | -6.27 |
| Sortino | -11.83 | -6.19 |
| max drawdown % | 64.62 | 96.67 |
| profit factor | 0.75 | 0.82 |

**Retained out of sample: negative**

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free. Cross-strategy comparisons in this repository use average profit per trade in percent.

Baseline: buy-and-hold on the same pairs returned **-58.41%**; the strategy returned **-62.5%**.
Out of sample: buy-and-hold **346.34%** vs strategy **-96.67%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | clean | смещения не обнаружено |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | индикаторы меняются от объёма истории: rsi 12.447% |
| прогрев занижен | **found** | объявлено 20, нужно не менее 100 |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **5m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `8d9b3a08743f` · strategy list `a039f448c17bed72`*
