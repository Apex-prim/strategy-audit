# BcmbigzV1

Source: [`PeetCrypto/freqtrade-stuff`](https://github.com/PeetCrypto/freqtrade-stuff) · file `BcmbigzV1 (1).py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 367 | 1086 |
| expectancy per trade (USDT) | -0.71 | 0.86 |
| mean profit p-value | 0.04299 | 0.007266 |
| market change % (baseline) | -59.05 | 346.34 |
| strategy total % | -26.19 | 93.71 |
| Sharpe | -1.02 | 0.72 |
| Sortino | -1.06 | 0.67 |
| max drawdown % | 34.08 | 22.14 |
| profit factor | 0.69 | 1.3 |

**Retained out of sample: n/a**

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free. Cross-strategy comparisons in this repository use average profit per trade in percent.

Baseline: buy-and-hold on the same pairs returned **-59.05%**; the strategy returned **-26.19%**.
Out of sample: buy-and-hold **346.34%** vs strategy **93.71%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | could not run | вывод не разобран |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | индикаторы меняются от объёма истории: bb_lowerband_1h 3.629%, bb_middleband_1h 3.126%, bb_upperband_1h 2.629% |
| прогрев не объявлен | **found** | самый длинный индикатор 200 свечей, startup_candle_count не задан (по умолчанию 0) |
| мёртвые настройки трейлинга | **found** | trailing_stop=False, но trailing_stop_positive=0.01 задан — читается как работающая защита |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **5m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `4a7c7414af9b` · strategy list `dac6309df791d209`*
