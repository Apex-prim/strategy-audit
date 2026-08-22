# AlexBattleTankKiller

Source: [`jaredrsommer/freqtradestrategies`](https://github.com/jaredrsommer/freqtradestrategies) · file `AlexBattleTankKiller.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 264 | — |
| average profit per trade % | -0.71 | — |
| win rate % | 87.5 | — |
| average trade duration, minutes | 9814.0 | — |
| duration measured in own candles | 654.27 | — |
| expectancy per trade (USDT) | -0.18 | — |
| mean profit p-value | 0.2541 | — |
| market change % (baseline) | -59.17 | — |
| strategy total % | -4.8 | — |
| Sharpe | -0.49 | — |
| Sortino | -0.7 | — |
| max drawdown % | 7.44 | — |
| profit factor | 0.78 | — |

**Retained out of sample: —**

> **Read that number with care.** The author's window was a bear market (buy-and-hold −58%) and the out-of-sample window a bull market (+346%). For a long-biased strategy this ratio rewards having done *badly* in 2018–2020, so it measures regime luck as much as robustness. The regime-free comparison is the excess over buy-and-hold, below.

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free either. Cross-strategy comparisons in this repository use average profit per trade in percent.

**Excess over buy-and-hold** (regime-free): author's window **+54.4 pp**.

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

*Code fingerprint `590bf74986c5` · strategy list `a039f448c17bed72`*
