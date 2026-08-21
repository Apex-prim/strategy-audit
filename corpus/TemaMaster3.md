# TemaMaster3

Source: [`davidzr/freqtrade-strategies`](https://github.com/davidzr/freqtrade-strategies) · file `TemaMaster3.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 1596 | 4462 |
| expectancy per trade (USDT) | -0.33 | -0.11 |
| mean profit p-value | 0.0125 | 0.676 |
| market change % (baseline) | -55.54 | 347.94 |
| strategy total % | -53.2 | -47.23 |
| Sharpe | -2.61 | -0.23 |
| Sortino | -5.32 | -0.44 |
| max drawdown % | 65.47 | 88.39 |
| profit factor | 0.85 | 0.98 |

**Retained out of sample: negative**

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free. Cross-strategy comparisons in this repository use average profit per trade in percent.

Baseline: buy-and-hold on the same pairs returned **-55.54%**; the strategy returned **-53.2%**.
Out of sample: buy-and-hold **347.94%** vs strategy **-47.23%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | clean | смещения не обнаружено |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | freqtrade ОТКАЗАЛСЯ анализировать: startup_candle_count=0, «приведёт к рекурсивным проблемам у части индикаторов» |
| прогрев не объявлен | **found** | самый длинный индикатор 180 свечей, startup_candle_count не задан (по умолчанию 0) |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **1m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `4a7c7414af9b` · strategy list `dac6309df791d209`*
