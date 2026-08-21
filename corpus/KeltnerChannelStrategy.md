# KeltnerChannelStrategy

Source: [`mlsys-io/PortfolioBench`](https://github.com/mlsys-io/PortfolioBench) · file `KeltnerChannelStrategy.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 6661 | 10059 |
| expectancy per trade (USDT) | -0.13 | -0.1 |
| mean profit p-value | 1.252e-43 | 3.119e-61 |
| market change % (baseline) | -58.52 | 346.34 |
| strategy total % | -85.52 | -96.57 |
| Sharpe | -29.8 | -13.49 |
| Sortino | -48.92 | -17.49 |
| max drawdown % | 85.52 | 96.57 |
| profit factor | 0.59 | 0.54 |

**Retained out of sample: negative**

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free. Cross-strategy comparisons in this repository use average profit per trade in percent.

Baseline: buy-and-hold on the same pairs returned **-58.52%**; the strategy returned **-85.52%**.
Out of sample: buy-and-hold **346.34%** vs strategy **-96.57%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | clean | смещения не обнаружено |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | индикаторы меняются от объёма истории: atr -1.081%, rsi 2.684% |
| прогрев объявлен | clean | 25 при потребности 20 |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **5m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `8d9b3a08743f` · strategy list `a039f448c17bed72`*
