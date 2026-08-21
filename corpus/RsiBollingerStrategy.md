# RsiBollingerStrategy

Source: [`mlsys-io/PortfolioBench`](https://github.com/mlsys-io/PortfolioBench) · file `RsiBollingerStrategy.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 648 | 2237 |
| expectancy per trade (USDT) | -0.8 | 0.0 |
| mean profit p-value | 0.0003949 | 0.9906 |
| market change % (baseline) | -59.27 | 348.67 |
| strategy total % | -51.88 | 0.54 |
| Sharpe | -2.38 | 0.0 |
| Sortino | -2.45 | 0.0 |
| max drawdown % | 52.05 | 43.9 |
| profit factor | 0.66 | 1.0 |

**Retained out of sample: n/a**

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free. Cross-strategy comparisons in this repository use average profit per trade in percent.

Baseline: buy-and-hold on the same pairs returned **-59.27%**; the strategy returned **-51.88%**.
Out of sample: buy-and-hold **348.67%** vs strategy **0.54%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | clean | смещения не обнаружено |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | индикаторы меняются от объёма истории: rsi 4.044% |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **1h** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `8d9b3a08743f` · strategy list `a039f448c17bed72`*
