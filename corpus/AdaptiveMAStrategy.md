# AdaptiveMAStrategy

Source: [`mlsys-io/PortfolioBench`](https://github.com/mlsys-io/PortfolioBench) · file `AdaptiveMAStrategy.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 3237 | — |
| expectancy per trade (USDT) | -0.2 | — |
| mean profit p-value | 9.271e-42 | — |
| market change % (baseline) | -58.48 | — |
| strategy total % | -64.79 | — |
| Sharpe | -20.45 | — |
| Sortino | -32.13 | — |
| max drawdown % | 64.99 | — |
| profit factor | 0.51 | — |

**Retained out of sample: —**

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free. Cross-strategy comparisons in this repository use average profit per trade in percent.

Baseline: buy-and-hold on the same pairs returned **-58.48%**; the strategy returned **-64.79%**.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | clean | смещения не обнаружено |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | индикаторы меняются от объёма истории: kama_slow -0.028%, kama_slow_prev -0.028%, rsi 0.765%, adx -1.964% |
| прогрев объявлен | clean | 50 при потребности 14 |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **5m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `8d9b3a08743f` · strategy list `a039f448c17bed72`*
