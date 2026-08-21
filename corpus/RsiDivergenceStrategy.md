# RsiDivergenceStrategy

Source: [`mlsys-io/PortfolioBench`](https://github.com/mlsys-io/PortfolioBench) · file `RsiDivergenceStrategy.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 104 | 370 |
| expectancy per trade (USDT) | -0.14 | -0.32 |
| mean profit p-value | 0.5985 | 0.02372 |
| market change % (baseline) | -58.52 | 346.34 |
| strategy total % | -1.43 | -11.7 |
| Sharpe | -0.14 | -0.35 |
| Sortino | -0.15 | -0.36 |
| max drawdown % | 4.07 | 14.53 |
| profit factor | 0.87 | 0.71 |

**Retained out of sample: negative**

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free. Cross-strategy comparisons in this repository use average profit per trade in percent.

⚠ **Not statistically significant in its author's own window** (p = 0.5985 > 0.05): the average trade is not distinguishable from zero.

Baseline: buy-and-hold on the same pairs returned **-58.52%**; the strategy returned **-1.43%**.
Out of sample: buy-and-hold **346.34%** vs strategy **-11.7%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | could not run | вывод не разобран |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | индикаторы меняются от объёма истории: rsi 2.684%, rsi_min 2.684% |
| прогрев занижен | **found** | объявлено 25, нужно не менее 50 |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **5m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `8d9b3a08743f` · strategy list `a039f448c17bed72`*
