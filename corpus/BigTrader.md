# BigTrader

Source: [`TheoBrigitte/freqtrade`](https://github.com/TheoBrigitte/freqtrade) · file `BigTrader.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 23 | 143 |
| expectancy per trade (USDT) | 3.61 | 4.79 |
| mean profit p-value | 5.459e-17 | 2.548e-72 |
| market change % (baseline) | -58.47 | 346.34 |
| strategy total % | 8.31 | 68.55 |
| Sharpe | 2.99 | 3.44 |
| Sortino | -100.0 | -100.0 |
| max drawdown % | 0.0 | 0.0 |
| profit factor | 0.0 | 0.0 |

**Retained out of sample: 133%**

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free. Cross-strategy comparisons in this repository use average profit per trade in percent.

Baseline: buy-and-hold on the same pairs returned **-58.47%**; the strategy returned **8.31%**.
Out of sample: buy-and-hold **346.34%** vs strategy **68.55%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | could not run | вывод не разобран |
| indicator recursion (freqtrade's own `recursive-analysis`) | clean | рекурсивных отклонений не найдено |
| прогрев не объявлен | **found** | самый длинный индикатор 30 свечей, startup_candle_count не задан (по умолчанию 0) |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **5m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `8d9b3a08743f` · strategy list `a039f448c17bed72`*
