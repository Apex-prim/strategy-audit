# Cluc4

Source: [`davidzr/freqtrade-strategies`](https://github.com/davidzr/freqtrade-strategies) · file `Cluc4.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 942 | 3939 |
| expectancy per trade (USDT) | -0.23 | -0.09 |
| mean profit p-value | 7.025e-08 | 1.585e-05 |
| market change % (baseline) | -55.54 | 347.94 |
| strategy total % | -21.42 | -36.13 |
| Sharpe | -4.36 | -2.19 |
| Sortino | -53.32 | -18.02 |
| max drawdown % | 23.27 | 38.34 |
| profit factor | 0.69 | 0.86 |

**Retained out of sample: negative**

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free. Cross-strategy comparisons in this repository use average profit per trade in percent.

Baseline: buy-and-hold on the same pairs returned **-55.54%**; the strategy returned **-21.42%**.
Out of sample: buy-and-hold **347.94%** vs strategy **-36.13%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | clean | смещения не обнаружено |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | freqtrade ОТКАЗАЛСЯ анализировать: startup_candle_count=0, «приведёт к рекурсивным проблемам у части индикаторов» |
| прогрев не объявлен | **found** | самый длинный индикатор 168 свечей, startup_candle_count не задан (по умолчанию 0) |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **1m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `4a7c7414af9b` · strategy list `dac6309df791d209`*
