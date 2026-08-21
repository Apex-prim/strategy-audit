# SqueezeMomentumStrategy

Source: [`mlsys-io/PortfolioBench`](https://github.com/mlsys-io/PortfolioBench) · file `SqueezeMomentumStrategy.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 11430 | 11753 |
| expectancy per trade (USDT) | -0.08 | -0.08 |
| mean profit p-value | 4.985e-88 | 1.333e-79 |
| market change % (baseline) | -58.37 | 346.34 |
| strategy total % | -91.91 | -96.57 |
| Sharpe | -56.14 | -16.69 |
| Sortino | -96.7 | -29.01 |
| max drawdown % | 91.93 | 96.57 |
| profit factor | 0.55 | 0.52 |

**Retained out of sample: negative**

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free. Cross-strategy comparisons in this repository use average profit per trade in percent.

Baseline: buy-and-hold on the same pairs returned **-58.37%**; the strategy returned **-91.91%**.
Out of sample: buy-and-hold **346.34%** vs strategy **-96.57%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | clean | смещения не обнаружено |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | индикаторы меняются от объёма истории: atr 0.169%, rsi 0.935% |
| прогрев объявлен | clean | 30 при потребности 14 |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **5m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `8d9b3a08743f` · strategy list `a039f448c17bed72`*
