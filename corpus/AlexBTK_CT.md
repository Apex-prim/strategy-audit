# AlexBTK_CT

Source: [`jaredrsommer/freqtradestrategies`](https://github.com/jaredrsommer/freqtradestrategies) · file `AlexBTK_CT.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 264 | — |
| expectancy per trade (USDT) | -0.18 | — |
| mean profit p-value | 0.2541 | — |
| market change % (baseline) | -59.17 | — |
| strategy total % | -4.8 | — |
| Sharpe | -0.49 | — |
| Sortino | -0.7 | — |
| max drawdown % | 7.44 | — |
| profit factor | 0.78 | — |

**Retained out of sample: —**

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free. Cross-strategy comparisons in this repository use average profit per trade in percent.

⚠ **Not statistically significant in its author's own window** (p = 0.2541 > 0.05): the average trade is not distinguishable from zero.

Baseline: buy-and-hold on the same pairs returned **-59.17%**; the strategy returned **-4.8%**.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | **found** | ЕСТЬ СМЕЩЕНИЕ: входов 0, выходов 0 из 20 сигналов |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | индикаторы меняются от объёма истории: rsi -0.013%, atr 0.019%, plus_di 0.015%, minus_di -0.015%, DI_values -0.075% |
| прогрев не объявлен | **found** | самый длинный индикатор 64 свечей, startup_candle_count не задан (по умолчанию 0) |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **15m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `8d9b3a08743f` · strategy list `d43e19f4fcbe76b6`*
