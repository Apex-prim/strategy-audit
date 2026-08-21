# TrixSignalStrategy

Source: [`mlsys-io/PortfolioBench`](https://github.com/mlsys-io/PortfolioBench) · file `TrixSignalStrategy.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 5071 | 12814 |
| expectancy per trade (USDT) | -0.14 | -0.08 |
| mean profit p-value | 1.095e-24 | 4.91e-24 |
| market change % (baseline) | -58.37 | 346.34 |
| strategy total % | -71.12 | -96.57 |
| Sharpe | -19.22 | -9.28 |
| Sortino | -32.65 | -13.86 |
| max drawdown % | 71.32 | 96.73 |
| profit factor | 0.67 | 0.72 |

**Retained out of sample: negative**

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free. Cross-strategy comparisons in this repository use average profit per trade in percent.

Baseline: buy-and-hold on the same pairs returned **-58.37%**; the strategy returned **-71.12%**.
Out of sample: buy-and-hold **346.34%** vs strategy **-96.57%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | clean | смещения не обнаружено |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | индикаторы меняются от объёма истории: rsi -2.484% |
| прогрев занижен | **found** | объявлено 40, нужно не менее 50 |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **5m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `8d9b3a08743f` · strategy list `a039f448c17bed72`*
