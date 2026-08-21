# AdxSmas

Source: [`PeetCrypto/freqtrade-stuff`](https://github.com/PeetCrypto/freqtrade-stuff) · file `AdxSmas.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 1530 | 5474 |
| expectancy per trade (USDT) | -0.29 | -0.15 |
| mean profit p-value | 0.02062 | 0.03616 |
| market change % (baseline) | -58.4 | 348.67 |
| strategy total % | -44.76 | -82.85 |
| Sharpe | -2.37 | -1.25 |
| Sortino | -2.99 | -1.24 |
| max drawdown % | 51.7 | 89.46 |
| profit factor | 0.83 | 0.89 |

**Retained out of sample: negative**

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free. Cross-strategy comparisons in this repository use average profit per trade in percent.

Baseline: buy-and-hold on the same pairs returned **-58.4%**; the strategy returned **-44.76%**.
Out of sample: buy-and-hold **348.67%** vs strategy **-82.85%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | could not run | вывод не разобран |
| indicator recursion (freqtrade's own `recursive-analysis`) | clean | рекурсивных отклонений не найдено |
| прогрев не объявлен | **found** | самый длинный индикатор 14 свечей, startup_candle_count не задан (по умолчанию 0) |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **1h** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `4a7c7414af9b` · strategy list `dac6309df791d209`*
