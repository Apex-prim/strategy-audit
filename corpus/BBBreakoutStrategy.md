# BBBreakoutStrategy

Source: [`flaviosiotto/freqtrade-strategy`](https://github.com/flaviosiotto/freqtrade-strategy) · file `bb-breakout-strategy.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 18639 | 14366 |
| expectancy per trade (USDT) | -0.05 | -0.07 |
| mean profit p-value | 5.139e-57 | 1.507e-73 |
| market change % (baseline) | -55.61 | 347.44 |
| strategy total % | -96.57 | -96.57 |
| Sharpe | -56.98 | -17.69 |
| Sortino | -100.04 | -26.1 |
| max drawdown % | 96.57 | 96.59 |
| profit factor | 0.66 | 0.54 |

**Retained out of sample: negative**

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free. Cross-strategy comparisons in this repository use average profit per trade in percent.

Baseline: buy-and-hold on the same pairs returned **-55.61%**; the strategy returned **-96.57%**.
Out of sample: buy-and-hold **347.44%** vs strategy **-96.57%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | **found** | ЕСТЬ СМЕЩЕНИЕ: входов 0, выходов 0 из 20 сигналов |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | freqtrade ОТКАЗАЛСЯ анализировать: startup_candle_count=0, «приведёт к рекурсивным проблемам у части индикаторов» |
| прогрев не объявлен | **found** | самый длинный индикатор 21 свечей, startup_candle_count не задан (по умолчанию 0) |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **3m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `8d9b3a08743f` · strategy list `a039f448c17bed72`*
