# NOTankAi_15

Source: [`TheoBrigitte/freqtrade`](https://github.com/TheoBrigitte/freqtrade) · file `NOTankAi_15.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 2859 | 6773 |
| expectancy per trade (USDT) | 175.8 | 43922.02 |
| mean profit p-value | 1.03e-54 | 1.179e-182 |
| market change % (baseline) | -58.11 | 345.85 |
| strategy total % | 50262.5 | 29748386.38 |
| Sharpe | 22.25 | 19.79 |
| Sortino | -100.0 | 1.6 |
| max drawdown % | 4.0 | 4.06 |
| profit factor | 24.98 | 24.61 |

**Retained out of sample: 24984%**

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free. Cross-strategy comparisons in this repository use average profit per trade in percent.

Baseline: buy-and-hold on the same pairs returned **-58.11%**; the strategy returned **50262.5%**.
Out of sample: buy-and-hold **345.85%** vs strategy **29748386.38%** — **beats the baseline**.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | clean | смещения не обнаружено |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | freqtrade ОТКАЗАЛСЯ анализировать: startup_candle_count=0, «приведёт к рекурсивным проблемам у части индикаторов» |
| прогрев не объявлен | **found** | самый длинный индикатор 200 свечей, startup_candle_count не задан (по умолчанию 0) |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **15m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `8d9b3a08743f` · strategy list `a039f448c17bed72`*
