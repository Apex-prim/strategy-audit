# ClucHAnix_5m1

Source: [`PeetCrypto/freqtrade-stuff`](https://github.com/PeetCrypto/freqtrade-stuff) · file `ClucHAnix 5m trailbuy2 + BBRSIV5 offsets.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 673 | 2376 |
| expectancy per trade (USDT) | 0.08 | -0.05 |
| mean profit p-value | 0.5402 | 0.5238 |
| market change % (baseline) | -59.11 | 346.34 |
| strategy total % | 5.37 | -11.52 |
| Sharpe | 0.42 | -0.25 |
| Sortino | 0.36 | -0.21 |
| max drawdown % | 8.93 | 43.08 |
| profit factor | 1.08 | 0.96 |

**Retained out of sample: negative**

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free. Cross-strategy comparisons in this repository use average profit per trade in percent.

⚠ **Not statistically significant in its author's own window** (p = 0.5402 > 0.05): the average trade is not distinguishable from zero.

Baseline: buy-and-hold on the same pairs returned **-59.11%**; the strategy returned **5.37%**.
Out of sample: buy-and-hold **346.34%** vs strategy **-11.52%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | could not run | вывод не разобран |
| indicator recursion (freqtrade's own `recursive-analysis`) | clean | рекурсивных отклонений не найдено |
| прогрев объявлен | clean | 168 при потребности 168 |
| мёртвые настройки трейлинга | **found** | trailing_stop=False, но trailing_stop_positive=0.001 задан — читается как работающая защита |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **5m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `4a7c7414af9b` · strategy list `dac6309df791d209`*
