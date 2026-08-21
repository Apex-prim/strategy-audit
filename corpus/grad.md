# grad

Source: [`jaredrsommer/freqtradestrategies`](https://github.com/jaredrsommer/freqtradestrategies) · file `grad (copy).py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 6173 | 20915 |
| expectancy per trade (USDT) | 6.8 | 6091.9 |
| mean profit p-value | 3.022e-56 | 8.889e-78 |
| market change % (baseline) | -59.31 | 348.67 |
| strategy total % | 4197.88 | 12741211.14 |
| Sharpe | 32.83 | 21.92 |
| Sortino | 95.67 | 60.48 |
| max drawdown % | 2.27 | 1.18 |
| profit factor | 2.92 | 2.56 |

**Retained out of sample: 89587%**

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free. Cross-strategy comparisons in this repository use average profit per trade in percent.

Baseline: buy-and-hold on the same pairs returned **-59.31%**; the strategy returned **4197.88%**.
Out of sample: buy-and-hold **348.67%** vs strategy **12741211.14%** — **beats the baseline**.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | **found** | ЕСТЬ СМЕЩЕНИЕ: входов 0, выходов 0 из 20 сигналов |
| indicator recursion (freqtrade's own `recursive-analysis`) | clean | рекурсивных отклонений не найдено |
| мёртвые настройки трейлинга | **found** | trailing_stop=False, но trailing_stop_positive=0.015 задан — читается как работающая защита |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **1h** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `8d9b3a08743f` · strategy list `d43e19f4fcbe76b6`*
