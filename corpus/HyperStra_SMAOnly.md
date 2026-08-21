# HyperStra_SMAOnly

Source: [`PeetCrypto/freqtrade-stuff`](https://github.com/PeetCrypto/freqtrade-stuff) · file `HyperStra_SMAOnly.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 8 | 9 |
| expectancy per trade (USDT) | 6.24 | 22.9 |
| mean profit p-value | 0.00668 | 0.007036 |
| market change % (baseline) | -59.17 | 346.34 |
| strategy total % | 4.99 | 20.61 |
| Sharpe | 0.3 | 0.09 |
| Sortino | -100.0 | 37.77 |
| max drawdown % | 0.0 | 1.28 |
| profit factor | 754923.68 | 17.15 |

**Retained out of sample: 367%**

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free. Cross-strategy comparisons in this repository use average profit per trade in percent.

Baseline: buy-and-hold on the same pairs returned **-59.17%**; the strategy returned **4.99%**.
Out of sample: buy-and-hold **346.34%** vs strategy **20.61%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | could not run | вывод не разобран |
| indicator recursion (freqtrade's own `recursive-analysis`) | clean | рекурсивных отклонений не найдено |
| мёртвые настройки трейлинга | **found** | trailing_stop=False, но trailing_stop_positive=0.005 задан — читается как работающая защита |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **5m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `4a7c7414af9b` · strategy list `dac6309df791d209`*
