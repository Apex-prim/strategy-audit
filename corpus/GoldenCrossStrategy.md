# GoldenCrossStrategy

Source: [`mlsys-io/PortfolioBench`](https://github.com/mlsys-io/PortfolioBench) · file `GoldenCrossStrategy.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 1184 | 4736 |
| expectancy per trade (USDT) | -0.13 | -0.14 |
| mean profit p-value | 0.01547 | 1.448e-08 |
| market change % (baseline) | -58.46 | 346.34 |
| strategy total % | -15.64 | -67.37 |
| Sharpe | -2.18 | -3.16 |
| Sortino | -4.09 | -5.24 |
| max drawdown % | 17.9 | 69.48 |
| profit factor | 0.84 | 0.79 |

**Retained out of sample: negative**

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free. Cross-strategy comparisons in this repository use average profit per trade in percent.

Baseline: buy-and-hold on the same pairs returned **-58.46%**; the strategy returned **-15.64%**.
Out of sample: buy-and-hold **346.34%** vs strategy **-67.37%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | clean | смещения не обнаружено |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | индикаторы меняются от объёма истории: ema50 0.013%, ema50_prev 0.013%, rsi 0.841% |
| прогрев занижен | **found** | объявлено 55, нужно не менее 200 |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **5m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `8d9b3a08743f` · strategy list `a039f448c17bed72`*
