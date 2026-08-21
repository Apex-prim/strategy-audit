# Lateralus

Source: [`werkkrew/freqtrade-strategies`](https://github.com/werkkrew/freqtrade-strategies) · file `Lateralus.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 422 | — |
| expectancy per trade (USDT) | -0.05 | — |
| mean profit p-value | 0.8044 | — |
| market change % (baseline) | -58.23 | — |
| strategy total % | -2.2 | — |
| Sharpe | -0.13 | — |
| Sortino | -0.81 | — |
| max drawdown % | 14.06 | — |
| profit factor | 0.97 | — |

**Retained out of sample: —**

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free. Cross-strategy comparisons in this repository use average profit per trade in percent.

⚠ **Not statistically significant in its author's own window** (p = 0.8044 > 0.05): the average trade is not distinguishable from zero.

Baseline: buy-and-hold on the same pairs returned **-58.23%**; the strategy returned **-2.2%**.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | **found** | ЕСТЬ СМЕЩЕНИЕ: входов 1, выходов 1 из 10 сигналов |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | freqtrade ОТКАЗАЛСЯ анализировать: startup_candle_count=0, «приведёт к рекурсивным проблемам у части индикаторов» |
| прогрев не объявлен | **found** | самый длинный индикатор 55 свечей, startup_candle_count не задан (по умолчанию 0) |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **5m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `4a7c7414af9b` · strategy list `dac6309df791d209`*
