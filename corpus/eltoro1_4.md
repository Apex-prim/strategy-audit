# eltoro1_4

Source: [`jaredrsommer/freqtradestrategies`](https://github.com/jaredrsommer/freqtradestrategies) · file `eltoro1_4 (copy).py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 460 | 1933 |
| expectancy per trade (USDT) | -1.24 | -0.32 |
| mean profit p-value | 0.002102 | 0.01524 |
| market change % (baseline) | -59.11 | 348.67 |
| strategy total % | -57.23 | -61.32 |
| Sharpe | -1.75 | -0.86 |
| Sortino | -1.51 | -0.59 |
| max drawdown % | 58.39 | 74.62 |
| profit factor | 0.62 | 0.81 |

**Retained out of sample: negative**

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free. Cross-strategy comparisons in this repository use average profit per trade in percent.

Baseline: buy-and-hold on the same pairs returned **-59.11%**; the strategy returned **-57.23%**.
Out of sample: buy-and-hold **348.67%** vs strategy **-61.32%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | clean | смещения не обнаружено |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | индикаторы меняются от объёма истории: INFEWO_4h -1.742%, BTC_EWO_Fast_4h -1.742%, ema_dif25 2.975%, rsi 0.038%, rsi_ma 0.039% |
| прогрев занижен | **found** | объявлено 79, нужно не менее 200 |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **1h** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `8d9b3a08743f` · strategy list `d43e19f4fcbe76b6`*
