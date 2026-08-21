# AlwaysBuy

Source: [`davidzr/freqtrade-strategies`](https://github.com/davidzr/freqtrade-strategies) · file `AlwaysBuy.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 11069 | 21290 |
| expectancy per trade (USDT) | -0.09 | -0.05 |
| mean profit p-value | 2.111e-18 | 4.148e-11 |
| market change % (baseline) | -58.23 | 346.34 |
| strategy total % | -96.63 | -96.88 |
| Sharpe | -24.11 | -7.79 |
| Sortino | -27.59 | -8.5 |
| max drawdown % | 96.74 | 96.96 |
| profit factor | 0.7 | 0.84 |

**Retained out of sample: negative**

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free. Cross-strategy comparisons in this repository use average profit per trade in percent.

Baseline: buy-and-hold on the same pairs returned **-58.23%**; the strategy returned **-96.63%**.
Out of sample: buy-and-hold **346.34%** vs strategy **-96.88%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | clean | смещения не обнаружено |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | freqtrade ОТКАЗАЛСЯ анализировать: startup_candle_count=0, «приведёт к рекурсивным проблемам у части индикаторов» |
| мёртвые настройки трейлинга | **found** | trailing_stop=False, но trailing_stop_positive=0.005 задан — читается как работающая защита |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **5m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `4a7c7414af9b` · strategy list `dac6309df791d209`*
