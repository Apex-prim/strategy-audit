# Quickie

Source: [`PeetCrypto/freqtrade-stuff`](https://github.com/PeetCrypto/freqtrade-stuff) · file `Quickie.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 1780 | 5896 |
| expectancy per trade (USDT) | -0.41 | -0.14 |
| mean profit p-value | 0.0001029 | 0.09337 |
| market change % (baseline) | -58.23 | 346.34 |
| strategy total % | -73.81 | -83.74 |
| Sharpe | -4.29 | -1.04 |
| Sortino | -2.43 | -0.44 |
| max drawdown % | 75.21 | 91.87 |
| profit factor | 0.6 | 0.89 |

**Retained out of sample: negative**

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free. Cross-strategy comparisons in this repository use average profit per trade in percent.

Baseline: buy-and-hold on the same pairs returned **-58.23%**; the strategy returned **-73.81%**.
Out of sample: buy-and-hold **346.34%** vs strategy **-83.74%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | could not run | вывод не разобран |
| indicator recursion (freqtrade's own `recursive-analysis`) | clean | рекурсивных отклонений не найдено |
| прогрев не объявлен | **found** | самый длинный индикатор 200 свечей, startup_candle_count не задан (по умолчанию 0) |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **5m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `4a7c7414af9b` · strategy list `dac6309df791d209`*
