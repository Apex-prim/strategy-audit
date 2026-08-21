# ONUR

Source: [`davidzr/freqtrade-strategies`](https://github.com/davidzr/freqtrade-strategies) · file `ONUR.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 55 | 479 |
| expectancy per trade (USDT) | -7.67 | 5.01 |
| mean profit p-value | 0.09592 | 0.1766 |
| market change % (baseline) | -58.11 | 345.85 |
| strategy total % | -42.2 | 240.09 |
| Sharpe | -0.33 | 0.24 |
| Sortino | -0.59 | 0.17 |
| max drawdown % | 52.94 | 56.99 |
| profit factor | 0.35 | 1.53 |

**Retained out of sample: n/a**

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free. Cross-strategy comparisons in this repository use average profit per trade in percent.

⚠ **Not statistically significant in its author's own window** (p = 0.09592 > 0.05): the average trade is not distinguishable from zero.

Baseline: buy-and-hold on the same pairs returned **-58.11%**; the strategy returned **-42.2%**.
Out of sample: buy-and-hold **345.85%** vs strategy **240.09%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | clean | смещения не обнаружено |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | freqtrade ОТКАЗАЛСЯ анализировать: startup_candle_count=0, «приведёт к рекурсивным проблемам у части индикаторов» |
| прогрев не объявлен | **found** | самый длинный индикатор 20 свечей, startup_candle_count не задан (по умолчанию 0) |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **15m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `4a7c7414af9b` · strategy list `dac6309df791d209`*
