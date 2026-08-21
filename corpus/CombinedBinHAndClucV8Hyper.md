# CombinedBinHAndClucV8Hyper

Source: [`PeetCrypto/freqtrade-stuff`](https://github.com/PeetCrypto/freqtrade-stuff) · file `CombinedBinHAndClucV8Hyper.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 287 | 956 |
| expectancy per trade (USDT) | 0.68 | 0.66 |
| mean profit p-value | 6.253e-06 | 1.149e-09 |
| market change % (baseline) | -59.05 | 346.34 |
| strategy total % | 19.59 | 62.89 |
| Sharpe | 2.04 | 1.54 |
| Sortino | 1.41 | 1.15 |
| max drawdown % | 5.55 | 6.36 |
| profit factor | 2.45 | 1.87 |

**Retained out of sample: 97%**

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free. Cross-strategy comparisons in this repository use average profit per trade in percent.

Baseline: buy-and-hold on the same pairs returned **-59.05%**; the strategy returned **19.59%**.
Out of sample: buy-and-hold **346.34%** vs strategy **62.89%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | could not run | вывод не разобран |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | индикаторы меняются от объёма истории: ema_100_1h -0.014% |
| прогрев не объявлен | **found** | самый длинный индикатор 200 свечей, startup_candle_count не задан (по умолчанию 0) |
| мёртвые настройки трейлинга | **found** | trailing_stop=False, но trailing_stop_positive=0.01 задан — читается как работающая защита |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **5m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `2da4e157b88f` · strategy list `dac6309df791d209`*
