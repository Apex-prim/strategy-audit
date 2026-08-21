# BinClucMad

Source: [`davidzr/freqtrade-strategies`](https://github.com/davidzr/freqtrade-strategies) · file `BinClucMad.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 629 | 1888 |
| expectancy per trade (USDT) | -0.06 | 1.18 |
| mean profit p-value | 0.6526 | 1.368e-11 |
| market change % (baseline) | -59.05 | 346.34 |
| strategy total % | -3.96 | 223.45 |
| Sharpe | -0.3 | 2.39 |
| Sortino | -0.27 | 2.27 |
| max drawdown % | 17.47 | 9.27 |
| profit factor | 0.95 | 1.53 |

**Retained out of sample: n/a**

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free. Cross-strategy comparisons in this repository use average profit per trade in percent.

⚠ **Not statistically significant in its author's own window** (p = 0.6526 > 0.05): the average trade is not distinguishable from zero.

Baseline: buy-and-hold on the same pairs returned **-59.05%**; the strategy returned **-3.96%**.
Out of sample: buy-and-hold **346.34%** vs strategy **223.45%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | clean | смещения не обнаружено |
| indicator recursion (freqtrade's own `recursive-analysis`) | clean | рекурсивных отклонений не найдено |
| прогрев не объявлен | **found** | самый длинный индикатор 200 свечей, startup_candle_count не задан (по умолчанию 0) |
| мёртвые настройки трейлинга | **found** | trailing_stop=False, но trailing_stop_positive=0.01 задан — читается как работающая защита |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **5m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `2da4e157b88f` · strategy list `dac6309df791d209`*
