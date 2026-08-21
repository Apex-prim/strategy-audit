# TrixV21Strategy

Source: [`PeetCrypto/freqtrade-stuff`](https://github.com/PeetCrypto/freqtrade-stuff) · file `TrixV21Strategy.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 227 | 925 |
| expectancy per trade (USDT) | -0.24 | -0.23 |
| mean profit p-value | 0.4779 | 0.172 |
| market change % (baseline) | -54.8 | 348.67 |
| strategy total % | -5.5 | -21.67 |
| Sharpe | -0.28 | -0.34 |
| Sortino | -0.4 | -0.47 |
| max drawdown % | 10.01 | 33.45 |
| profit factor | 0.88 | 0.88 |

**Retained out of sample: negative**

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free. Cross-strategy comparisons in this repository use average profit per trade in percent.

⚠ **Not statistically significant in its author's own window** (p = 0.4779 > 0.05): the average trade is not distinguishable from zero.

Baseline: buy-and-hold on the same pairs returned **-54.8%**; the strategy returned **-5.5%**.
Out of sample: buy-and-hold **348.67%** vs strategy **-21.67%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | could not run | вывод не разобран |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | индикаторы меняются от объёма истории: atr_30 -0.035% |
| прогрев не объявлен | **found** | самый длинный индикатор 14 свечей, startup_candle_count не задан (по умолчанию 0) |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **1h** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `4a7c7414af9b` · strategy list `dac6309df791d209`*
