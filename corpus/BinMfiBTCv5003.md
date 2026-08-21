# BinMfiBTCv5003

Source: [`TheoBrigitte/freqtrade`](https://github.com/TheoBrigitte/freqtrade) · file `BinMfiBTCv5003.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 7 | 164 |
| expectancy per trade (USDT) | 0.78 | -0.32 |
| mean profit p-value | 0.4411 | 0.363 |
| market change % (baseline) | -58.85 | 346.34 |
| strategy total % | 0.54 | -5.25 |
| Sharpe | 0.06 | -0.09 |
| Sortino | 0.11 | -0.12 |
| max drawdown % | 0.52 | 10.54 |
| profit factor | 2.04 | 0.81 |

**Retained out of sample: negative**

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free. Cross-strategy comparisons in this repository use average profit per trade in percent.

⚠ **Not statistically significant in its author's own window** (p = 0.4411 > 0.05): the average trade is not distinguishable from zero.

Baseline: buy-and-hold on the same pairs returned **-58.85%**; the strategy returned **0.54%**.
Out of sample: buy-and-hold **346.34%** vs strategy **-5.25%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | could not run | вывод не разобран |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | индикаторы меняются от объёма истории: rsi -0.033% |
| прогрев не объявлен | **found** | самый длинный индикатор 100 свечей, startup_candle_count не задан (по умолчанию 0) |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **5m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `8d9b3a08743f` · strategy list `a039f448c17bed72`*
