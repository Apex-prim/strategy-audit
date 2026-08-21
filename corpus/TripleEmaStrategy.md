# TripleEmaStrategy

Source: [`mlsys-io/PortfolioBench`](https://github.com/mlsys-io/PortfolioBench) · file `TripleEmaStrategy.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 4621 | 13049 |
| expectancy per trade (USDT) | -0.13 | -0.07 |
| mean profit p-value | 2.021e-22 | 1.314e-37 |
| market change % (baseline) | -58.37 | 346.34 |
| strategy total % | -59.39 | -96.57 |
| Sharpe | -17.42 | -11.88 |
| Sortino | -40.95 | -22.14 |
| max drawdown % | 59.6 | 96.64 |
| profit factor | 0.66 | 0.64 |

**Retained out of sample: negative**

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free. Cross-strategy comparisons in this repository use average profit per trade in percent.

Baseline: buy-and-hold on the same pairs returned **-58.37%**; the strategy returned **-59.39%**.
Out of sample: buy-and-hold **346.34%** vs strategy **-96.57%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | clean | смещения не обнаружено |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | индикаторы меняются от объёма истории: rsi 0.935% |
| прогрев занижен | **found** | объявлено 30, нужно не менее 55 |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **5m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `8d9b3a08743f` · strategy list `a039f448c17bed72`*
