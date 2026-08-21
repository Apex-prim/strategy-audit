# Rsiqui

Source: [`TheoBrigitte/freqtrade`](https://github.com/TheoBrigitte/freqtrade) · file `Rsiqui.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 6306 | 22472 |
| expectancy per trade (USDT) | 1.42 | 182.66 |
| mean profit p-value | 7.297e-25 | 5.139e-22 |
| market change % (baseline) | -58.23 | 346.34 |
| strategy total % | 894.32 | 410479.55 |
| Sharpe | 21.46 | 11.71 |
| Sortino | 19.24 | 8.95 |
| max drawdown % | 10.79 | 20.47 |
| profit factor | 1.59 | 1.44 |

**Retained out of sample: 12863%**

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free. Cross-strategy comparisons in this repository use average profit per trade in percent.

Baseline: buy-and-hold on the same pairs returned **-58.23%**; the strategy returned **894.32%**.
Out of sample: buy-and-hold **346.34%** vs strategy **410479.55%** — **beats the baseline**.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | **found** | ЕСТЬ СМЕЩЕНИЕ: входов 0, выходов 0 из 20 сигналов |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | freqtrade ОТКАЗАЛСЯ анализировать: startup_candle_count=0, «приведёт к рекурсивным проблемам у части индикаторов» |
| прогрев не объявлен | **found** | самый длинный индикатор 14 свечей, startup_candle_count не задан (по умолчанию 0) |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **5m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `8d9b3a08743f` · strategy list `a039f448c17bed72`*
