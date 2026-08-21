# SimpleHopt1Along

Source: [`MelvynClark/Freqtrade-Strategy`](https://github.com/MelvynClark/Freqtrade-Strategy) · file `SimpleHopt1Along.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 973 | 3494 |
| expectancy per trade (USDT) | -0.59 | -0.22 |
| mean profit p-value | 0.0007537 | 0.02557 |
| market change % (baseline) | -57.43 | 340.8 |
| strategy total % | -57.67 | -78.22 |
| Sharpe | -2.76 | -1.07 |
| Sortino | -1.98 | -0.46 |
| max drawdown % | 64.02 | 86.97 |
| profit factor | 0.55 | 0.8 |

**Retained out of sample: negative**

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free. Cross-strategy comparisons in this repository use average profit per trade in percent.

Baseline: buy-and-hold on the same pairs returned **-57.43%**; the strategy returned **-57.67%**.
Out of sample: buy-and-hold **340.8%** vs strategy **-78.22%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | clean | смещения не обнаружено |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | freqtrade ОТКАЗАЛСЯ анализировать: startup_candle_count=0, «приведёт к рекурсивным проблемам у части индикаторов» |
| прогрев не объявлен | **found** | самый длинный индикатор 12 свечей, startup_candle_count не задан (по умолчанию 0) |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **4h** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `8d9b3a08743f` · strategy list `a039f448c17bed72`*
