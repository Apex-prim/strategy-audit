# ClucHAnix_5m

Source: [`PeetCrypto/freqtrade-stuff`](https://github.com/PeetCrypto/freqtrade-stuff) · file `ClucHAnix_5m.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 644 | 2190 |
| expectancy per trade (USDT) | 0.27 | 0.51 |
| mean profit p-value | 0.02739 | 6.489e-05 |
| market change % (baseline) | -59.11 | 346.34 |
| strategy total % | 17.48 | 111.99 |
| Sharpe | 1.47 | 1.52 |
| Sortino | 1.31 | 1.13 |
| max drawdown % | 7.64 | 20.52 |
| profit factor | 1.29 | 1.4 |

**Retained out of sample: 189%**

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free. Cross-strategy comparisons in this repository use average profit per trade in percent.

Baseline: buy-and-hold on the same pairs returned **-59.11%**; the strategy returned **17.48%**.
Out of sample: buy-and-hold **346.34%** vs strategy **111.99%** — loses to it.

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
