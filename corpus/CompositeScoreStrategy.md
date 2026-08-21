# CompositeScoreStrategy

Source: [`mlsys-io/PortfolioBench`](https://github.com/mlsys-io/PortfolioBench) · file `CompositeScoreStrategy.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 13679 | 15092 |
| expectancy per trade (USDT) | -0.07 | -0.06 |
| mean profit p-value | 9.81e-35 | 8.091e-22 |
| market change % (baseline) | -58.37 | 346.34 |
| strategy total % | -96.57 | -96.59 |
| Sharpe | -37.74 | -9.55 |
| Sortino | -61.92 | -15.52 |
| max drawdown % | 96.61 | 96.63 |
| profit factor | 0.65 | 0.7 |

**Retained out of sample: negative**

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free. Cross-strategy comparisons in this repository use average profit per trade in percent.

Baseline: buy-and-hold on the same pairs returned **-58.37%**; the strategy returned **-96.57%**.
Out of sample: buy-and-hold **346.34%** vs strategy **-96.59%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | clean | смещения не обнаружено |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | индикаторы меняются от объёма истории: rsi 0.935%, adx -27.315%, score -50.000% |
| прогрев занижен | **found** | объявлено 30, нужно не менее 50 |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **5m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `8d9b3a08743f` · strategy list `a039f448c17bed72`*
