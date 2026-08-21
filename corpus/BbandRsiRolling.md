# BbandRsiRolling

Source: [`PeetCrypto/freqtrade-stuff`](https://github.com/PeetCrypto/freqtrade-stuff) · file `BbandRsiRolling.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 3841 | 14075 |
| expectancy per trade (USDT) | -0.21 | -0.07 |
| mean profit p-value | 7.148e-07 | 0.1451 |
| market change % (baseline) | -58.23 | 346.34 |
| strategy total % | -79.67 | -93.77 |
| Sharpe | -8.04 | -1.4 |
| Sortino | -7.68 | -1.13 |
| max drawdown % | 83.02 | 97.98 |
| profit factor | 0.79 | 0.96 |

**Retained out of sample: negative**

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free. Cross-strategy comparisons in this repository use average profit per trade in percent.

Baseline: buy-and-hold on the same pairs returned **-58.23%**; the strategy returned **-79.67%**.
Out of sample: buy-and-hold **346.34%** vs strategy **-93.77%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | could not run | вывод не разобран |
| indicator recursion (freqtrade's own `recursive-analysis`) | clean | рекурсивных отклонений не найдено |
| прогрев не объявлен | **found** | самый длинный индикатор 20 свечей, startup_candle_count не задан (по умолчанию 0) |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **5m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `4a7c7414af9b` · strategy list `dac6309df791d209`*
