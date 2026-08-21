# Bandtastic

Source: [`davidzr/freqtrade-strategies`](https://github.com/davidzr/freqtrade-strategies) · file `Bandtastic.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 7384 | 21361 |
| expectancy per trade (USDT) | -0.12 | -0.05 |
| mean profit p-value | 5.092e-14 | 0.0254 |
| market change % (baseline) | -58.11 | 345.85 |
| strategy total % | -92.14 | -96.81 |
| Sharpe | -16.94 | -2.64 |
| Sortino | -13.44 | -1.95 |
| max drawdown % | 92.22 | 98.17 |
| profit factor | 0.67 | 0.92 |

**Retained out of sample: negative**

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free. Cross-strategy comparisons in this repository use average profit per trade in percent.

Baseline: buy-and-hold on the same pairs returned **-58.11%**; the strategy returned **-92.14%**.
Out of sample: buy-and-hold **345.85%** vs strategy **-96.81%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | clean | смещения не обнаружено |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | freqtrade ОТКАЗАЛСЯ анализировать: startup_candle_count=0, «приведёт к рекурсивным проблемам у части индикаторов» |
| прогрев не объявлен | **found** | самый длинный индикатор 20 свечей, startup_candle_count не задан (по умолчанию 0) |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **15m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `4a7c7414af9b` · strategy list `dac6309df791d209`*
