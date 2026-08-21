# SmoothOperator

Source: [`PeetCrypto/freqtrade-stuff`](https://github.com/PeetCrypto/freqtrade-stuff) · file `SmoothOperator.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 4081 | 13046 |
| expectancy per trade (USDT) | -0.21 | -0.07 |
| mean profit p-value | 2.971e-14 | 8.761e-05 |
| market change % (baseline) | -58.23 | 346.34 |
| strategy total % | -85.73 | -96.66 |
| Sharpe | -12.74 | -3.63 |
| Sortino | -13.79 | -3.9 |
| max drawdown % | 85.8 | 96.85 |
| profit factor | 0.69 | 0.88 |

**Retained out of sample: negative**

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free. Cross-strategy comparisons in this repository use average profit per trade in percent.

Baseline: buy-and-hold on the same pairs returned **-58.23%**; the strategy returned **-85.73%**.
Out of sample: buy-and-hold **346.34%** vs strategy **-96.66%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | could not run | вывод не разобран |
| indicator recursion (freqtrade's own `recursive-analysis`) | clean | рекурсивных отклонений не найдено |
| прогрев не объявлен | **found** | самый длинный индикатор 200 свечей, startup_candle_count не задан (по умолчанию 0) |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **5m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `4a7c7414af9b` · strategy list `dac6309df791d209`*
