# AroonTrendStrategy

Source: [`mlsys-io/PortfolioBench`](https://github.com/mlsys-io/PortfolioBench) · file `AroonTrendStrategy.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 10297 | 13974 |
| expectancy per trade (USDT) | -0.09 | -0.07 |
| mean profit p-value | 8.593e-69 | 9.778e-36 |
| market change % (baseline) | -58.37 | 346.34 |
| strategy total % | -96.58 | -96.57 |
| Sharpe | -46.9 | -11.97 |
| Sortino | -60.57 | -15.98 |
| max drawdown % | 96.58 | 96.6 |
| profit factor | 0.53 | 0.64 |

**Retained out of sample: negative**

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free. Cross-strategy comparisons in this repository use average profit per trade in percent.

Baseline: buy-and-hold on the same pairs returned **-58.37%**; the strategy returned **-96.58%**.
Out of sample: buy-and-hold **346.34%** vs strategy **-96.57%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | clean | смещения не обнаружено |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | индикаторы меняются от объёма истории: rsi 0.935% |
| прогрев занижен | **found** | объявлено 30, нужно не менее 50 |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **5m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `8d9b3a08743f` · strategy list `a039f448c17bed72`*
