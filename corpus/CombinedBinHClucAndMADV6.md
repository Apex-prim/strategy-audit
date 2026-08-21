# CombinedBinHClucAndMADV6

Source: [`PeetCrypto/freqtrade-stuff`](https://github.com/PeetCrypto/freqtrade-stuff) · file `CombinedBinHClucAndMADV6.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 346 | 1270 |
| expectancy per trade (USDT) | 0.27 | 0.97 |
| mean profit p-value | 0.03095 | 4.348e-14 |
| market change % (baseline) | -59.05 | 346.34 |
| strategy total % | 9.39 | 123.7 |
| Sharpe | 1.06 | 2.2 |
| Sortino | 0.81 | 1.81 |
| max drawdown % | 6.09 | 4.98 |
| profit factor | 1.43 | 1.85 |

**Retained out of sample: 359%**

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free. Cross-strategy comparisons in this repository use average profit per trade in percent.

Baseline: buy-and-hold on the same pairs returned **-59.05%**; the strategy returned **9.39%**.
Out of sample: buy-and-hold **346.34%** vs strategy **123.7%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | could not run | вывод не разобран |
| indicator recursion (freqtrade's own `recursive-analysis`) | clean | рекурсивных отклонений не найдено |
| прогрев не объявлен | **found** | самый длинный индикатор 200 свечей, startup_candle_count не задан (по умолчанию 0) |
| мёртвые настройки трейлинга | **found** | trailing_stop=False, но trailing_stop_positive=0.01 задан — читается как работающая защита |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **5m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `2da4e157b88f` · strategy list `dac6309df791d209`*
