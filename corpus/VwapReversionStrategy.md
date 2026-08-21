# VwapReversionStrategy

Source: [`mlsys-io/PortfolioBench`](https://github.com/mlsys-io/PortfolioBench) · file `VwapReversionStrategy.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 8047 | 14269 |
| expectancy per trade (USDT) | -0.12 | -0.07 |
| mean profit p-value | 5.262e-22 | 2.884e-09 |
| market change % (baseline) | -58.52 | 346.34 |
| strategy total % | -95.37 | -96.61 |
| Sharpe | -22.71 | -5.74 |
| Sortino | -21.13 | -5.93 |
| max drawdown % | 95.4 | 96.71 |
| profit factor | 0.69 | 0.86 |

**Retained out of sample: negative**

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free. Cross-strategy comparisons in this repository use average profit per trade in percent.

Baseline: buy-and-hold on the same pairs returned **-58.52%**; the strategy returned **-95.37%**.
Out of sample: buy-and-hold **346.34%** vs strategy **-96.61%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | clean | смещения не обнаружено |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | индикаторы меняются от объёма истории: rsi 2.684%, atr -1.081% |
| прогрев занижен | **found** | объявлено 25, нужно не менее 100 |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **5m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `8d9b3a08743f` · strategy list `a039f448c17bed72`*
