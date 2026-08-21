# NostalgiaForInfinityX2

Source: [`davidzr/freqtrade-strategies`](https://github.com/davidzr/freqtrade-strategies) · file `NostalgiaForInfinityX2.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 1148 | 4229 |
| expectancy per trade (USDT) | -0.17 | -0.13 |
| mean profit p-value | 0.2015 | 0.1745 |
| market change % (baseline) | -58.96 | 346.34 |
| strategy total % | -20.08 | -55.98 |
| Sharpe | -1.14 | -0.71 |
| Sortino | -5.11 | -1.56 |
| max drawdown % | 35.8 | 78.43 |
| profit factor | 0.92 | 0.95 |

**Retained out of sample: negative**

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free. Cross-strategy comparisons in this repository use average profit per trade in percent.

⚠ **Not statistically significant in its author's own window** (p = 0.2015 > 0.05): the average trade is not distinguishable from zero.

Baseline: buy-and-hold on the same pairs returned **-58.96%**; the strategy returned **-20.08%**.
Out of sample: buy-and-hold **346.34%** vs strategy **-55.98%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | clean | смещения не обнаружено |
| indicator recursion (freqtrade's own `recursive-analysis`) | clean | рекурсивных отклонений не найдено |
| прогрев не объявлен | **found** | самый длинный индикатор 200 свечей, startup_candle_count не задан (по умолчанию 0) |
| мёртвые настройки трейлинга | **found** | trailing_stop=False, но trailing_stop_positive=0.01 задан — читается как работающая защита |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **5m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `4a7c7414af9b` · strategy list `dac6309df791d209`*
