# Strategy002

Source: [`davidzr/freqtrade-strategies`](https://github.com/davidzr/freqtrade-strategies) · file `Strategy002.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 277 | 1016 |
| expectancy per trade (USDT) | -0.56 | -0.39 |
| mean profit p-value | 0.02391 | 0.0003699 |
| market change % (baseline) | -58.23 | 346.34 |
| strategy total % | -15.39 | -39.97 |
| Sharpe | -0.99 | -0.92 |
| Sortino | -2.53 | -2.2 |
| max drawdown % | 17.98 | 41.83 |
| profit factor | 0.59 | 0.64 |

**Retained out of sample: negative**

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free. Cross-strategy comparisons in this repository use average profit per trade in percent.

Baseline: buy-and-hold on the same pairs returned **-58.23%**; the strategy returned **-15.39%**.
Out of sample: buy-and-hold **346.34%** vs strategy **-39.97%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | clean | смещения не обнаружено |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | freqtrade ОТКАЗАЛСЯ анализировать: startup_candle_count=0, «приведёт к рекурсивным проблемам у части индикаторов» |
| прогрев не объявлен | **found** | самый длинный индикатор 20 свечей, startup_candle_count не задан (по умолчанию 0) |
| мёртвые настройки трейлинга | **found** | trailing_stop=False, но trailing_stop_positive=0.01 задан — читается как работающая защита |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **5m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `4a7c7414af9b` · strategy list `dac6309df791d209`*
