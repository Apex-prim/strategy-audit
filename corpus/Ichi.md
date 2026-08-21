# ichi

Source: [`werkkrew/freqtrade-strategies`](https://github.com/werkkrew/freqtrade-strategies) · file `Ichis.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 1192 | 4733 |
| expectancy per trade (USDT) | -0.17 | -0.15 |
| mean profit p-value | 0.001101 | 1.384e-17 |
| market change % (baseline) | -58.4 | 348.67 |
| strategy total % | -20.1 | -71.5 |
| Sharpe | -2.95 | -4.77 |
| Sortino | -41.89 | -19.88 |
| max drawdown % | 27.52 | 71.7 |
| profit factor | 0.82 | 0.75 |

**Retained out of sample: negative**

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free. Cross-strategy comparisons in this repository use average profit per trade in percent.

Baseline: buy-and-hold on the same pairs returned **-58.4%**; the strategy returned **-20.1%**.
Out of sample: buy-and-hold **348.67%** vs strategy **-71.5%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | clean | смещения не обнаружено |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | freqtrade ОТКАЗАЛСЯ анализировать: startup_candle_count=0, «приведёт к рекурсивным проблемам у части индикаторов» |
| прогрев не объявлен | **found** | самый длинный индикатор 14 свечей, startup_candle_count не задан (по умолчанию 0) |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **1h** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `2da4e157b88f` · strategy list `dac6309df791d209`*
