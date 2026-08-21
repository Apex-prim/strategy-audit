# AdxStrengthStrategy

Source: [`mlsys-io/PortfolioBench`](https://github.com/mlsys-io/PortfolioBench) · file `AdxStrengthStrategy.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 5560 | 11392 |
| expectancy per trade (USDT) | -0.15 | -0.08 |
| mean profit p-value | 1.13e-61 | 1.288e-64 |
| market change % (baseline) | -58.52 | 346.34 |
| strategy total % | -81.04 | -96.58 |
| Sharpe | -32.75 | -14.75 |
| Sortino | -55.07 | -22.31 |
| max drawdown % | 81.1 | 96.58 |
| profit factor | 0.52 | 0.56 |

**Retained out of sample: negative**

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free. Cross-strategy comparisons in this repository use average profit per trade in percent.

Baseline: buy-and-hold on the same pairs returned **-58.52%**; the strategy returned **-81.04%**.
Out of sample: buy-and-hold **346.34%** vs strategy **-96.58%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | clean | смещения не обнаружено |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | индикаторы меняются от объёма истории: plus_di 3.015%, minus_di 2.061%, rsi 2.684% |
| прогрев занижен | **found** | объявлено 25, нужно не менее 50 |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **5m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `8d9b3a08743f` · strategy list `a039f448c17bed72`*
