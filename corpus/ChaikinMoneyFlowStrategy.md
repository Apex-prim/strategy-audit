# ChaikinMoneyFlowStrategy

Source: [`mlsys-io/PortfolioBench`](https://github.com/mlsys-io/PortfolioBench) · file `ChaikinMoneyFlowStrategy.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 14222 | 15042 |
| expectancy per trade (USDT) | -0.07 | -0.06 |
| mean profit p-value | 4.69e-86 | 7.481e-66 |
| market change % (baseline) | -58.52 | 346.34 |
| strategy total % | -95.89 | -96.57 |
| Sharpe | -61.78 | -17.09 |
| Sortino | -94.66 | -27.51 |
| max drawdown % | 95.89 | 96.67 |
| profit factor | 0.53 | 0.56 |

**Retained out of sample: negative**

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free. Cross-strategy comparisons in this repository use average profit per trade in percent.

Baseline: buy-and-hold on the same pairs returned **-58.52%**; the strategy returned **-95.89%**.
Out of sample: buy-and-hold **346.34%** vs strategy **-96.57%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | clean | смещения не обнаружено |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | индикаторы меняются от объёма истории: cmf 0.963%, cmf_prev 0.626%, rsi 2.684% |
| прогрев занижен | **found** | объявлено 25, нужно не менее 50 |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **5m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `8d9b3a08743f` · strategy list `a039f448c17bed72`*
