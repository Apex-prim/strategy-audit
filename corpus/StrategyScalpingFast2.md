# StrategyScalpingFast2

Source: [`davidzr/freqtrade-strategies`](https://github.com/davidzr/freqtrade-strategies) · file `StrategyScalpingFast2.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 2832 | 10605 |
| expectancy per trade (USDT) | -0.3 | -0.08 |
| mean profit p-value | 3.401e-05 | 0.279 |
| market change % (baseline) | -55.54 | 347.94 |
| strategy total % | -84.15 | -85.65 |
| Sharpe | -5.78 | -0.9 |
| Sortino | -3.35 | -0.5 |
| max drawdown % | 84.41 | 95.14 |
| profit factor | 0.49 | 0.91 |

**Retained out of sample: negative**

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free. Cross-strategy comparisons in this repository use average profit per trade in percent.

Baseline: buy-and-hold on the same pairs returned **-55.54%**; the strategy returned **-84.15%**.
Out of sample: buy-and-hold **347.94%** vs strategy **-85.65%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | clean | смещения не обнаружено |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | freqtrade ОТКАЗАЛСЯ анализировать: startup_candle_count=0, «приведёт к рекурсивным проблемам у части индикаторов» |
| прогрев не объявлен | **found** | самый длинный индикатор 20 свечей, startup_candle_count не задан (по умолчанию 0) |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **1m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `4a7c7414af9b` · strategy list `dac6309df791d209`*
