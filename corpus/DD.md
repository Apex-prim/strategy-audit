# DD

Source: [`davidzr/freqtrade-strategies`](https://github.com/davidzr/freqtrade-strategies) · file `DD.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 12209 | 19842 |
| expectancy per trade (USDT) | -0.08 | -0.05 |
| mean profit p-value | 2.994e-29 | 1.795e-09 |
| market change % (baseline) | -58.23 | 346.34 |
| strategy total % | -96.71 | -96.78 |
| Sharpe | -32.51 | -6.86 |
| Sortino | -26.04 | -4.92 |
| max drawdown % | 96.74 | 96.86 |
| profit factor | 0.59 | 0.79 |

**Retained out of sample: negative**

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free. Cross-strategy comparisons in this repository use average profit per trade in percent.

Baseline: buy-and-hold on the same pairs returned **-58.23%**; the strategy returned **-96.71%**.
Out of sample: buy-and-hold **346.34%** vs strategy **-96.78%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | clean | смещения не обнаружено |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | freqtrade ОТКАЗАЛСЯ анализировать: startup_candle_count=0, «приведёт к рекурсивным проблемам у части индикаторов» |
| прогрев не объявлен | **found** | самый длинный индикатор 20 свечей, startup_candle_count не задан (по умолчанию 0) |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **5m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `4a7c7414af9b` · strategy list `dac6309df791d209`*
