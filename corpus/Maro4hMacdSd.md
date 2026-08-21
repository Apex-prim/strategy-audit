# Maro4hMacdSd

Source: [`davidzr/freqtrade-strategies`](https://github.com/davidzr/freqtrade-strategies) · file `Maro4hMacdSd.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 13548 | 16944 |
| expectancy per trade (USDT) | -0.07 | -0.06 |
| mean profit p-value | 5.081e-26 | 5.457e-18 |
| market change % (baseline) | -58.23 | 346.34 |
| strategy total % | -96.31 | -96.73 |
| Sharpe | -32.16 | -9.11 |
| Sortino | -30.66 | -8.9 |
| max drawdown % | 96.34 | 96.75 |
| profit factor | 0.65 | 0.75 |

**Retained out of sample: negative**

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free. Cross-strategy comparisons in this repository use average profit per trade in percent.

Baseline: buy-and-hold on the same pairs returned **-58.23%**; the strategy returned **-96.31%**.
Out of sample: buy-and-hold **346.34%** vs strategy **-96.73%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | clean | смещения не обнаружено |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | freqtrade ОТКАЗАЛСЯ анализировать: startup_candle_count=0, «приведёт к рекурсивным проблемам у части индикаторов» |
| прогрев не объявлен | **found** | самый длинный индикатор 28 свечей, startup_candle_count не задан (по умолчанию 0) |
| мёртвые настройки трейлинга | **found** | trailing_stop=False, но trailing_stop_positive=0.1 задан — читается как работающая защита |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **5m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `4a7c7414af9b` · strategy list `dac6309df791d209`*
