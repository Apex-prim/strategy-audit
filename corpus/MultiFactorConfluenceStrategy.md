# MultiFactorConfluenceStrategy

Source: [`mlsys-io/PortfolioBench`](https://github.com/mlsys-io/PortfolioBench) · file `MultiFactorConfluenceStrategy.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 1116 | 4108 |
| expectancy per trade (USDT) | -0.52 | -0.21 |
| mean profit p-value | 2.096e-05 | 0.01764 |
| market change % (baseline) | -53.86 | 340.8 |
| strategy total % | -58.13 | -84.59 |
| Sharpe | -3.78 | -1.23 |
| Sortino | -12.01 | -2.55 |
| max drawdown % | 65.7 | 89.93 |
| profit factor | 0.76 | 0.92 |

**Retained out of sample: negative**

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free. Cross-strategy comparisons in this repository use average profit per trade in percent.

Baseline: buy-and-hold on the same pairs returned **-53.86%**; the strategy returned **-58.13%**.
Out of sample: buy-and-hold **340.8%** vs strategy **-84.59%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | clean | смещения не обнаружено |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | индикаторы меняются от объёма истории: macd 1.070%, macd_signal -0.060%, macd_hist -49.938%, macd_hist_prev -17.714%, rsi -0.395% |
| прогрев объявлен | clean | 50 при потребности 14 |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **4h** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `8d9b3a08743f` · strategy list `a039f448c17bed72`*
