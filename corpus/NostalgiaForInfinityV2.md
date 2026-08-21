# NostalgiaForInfinityV2

Source: [`PeetCrypto/freqtrade-stuff`](https://github.com/PeetCrypto/freqtrade-stuff) · file `NostalgiaForInfinityV2.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 193 | 632 |
| expectancy per trade (USDT) | 0.46 | 3.92 |
| mean profit p-value | 0.3077 | 5.027e-07 |
| market change % (baseline) | -59.05 | 346.34 |
| strategy total % | 8.79 | 247.8 |
| Sharpe | 0.37 | 1.03 |
| Sortino | 0.64 | 2.31 |
| max drawdown % | 10.07 | 6.46 |
| profit factor | 1.25 | 2.1 |

**Retained out of sample: 852%**

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free. Cross-strategy comparisons in this repository use average profit per trade in percent.

⚠ **Not statistically significant in its author's own window** (p = 0.3077 > 0.05): the average trade is not distinguishable from zero.

Baseline: buy-and-hold on the same pairs returned **-59.05%**; the strategy returned **8.79%**.
Out of sample: buy-and-hold **346.34%** vs strategy **247.8%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | could not run | вывод не разобран |
| indicator recursion (freqtrade's own `recursive-analysis`) | clean | рекурсивных отклонений не найдено |
| прогрев не объявлен | **found** | самый длинный индикатор 200 свечей, startup_candle_count не задан (по умолчанию 0) |
| мёртвые настройки трейлинга | **found** | trailing_stop=False, но trailing_stop_positive=0.02 задан — читается как работающая защита |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **5m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `2da4e157b88f` · strategy list `dac6309df791d209`*
