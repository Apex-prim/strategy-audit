# BB_RPB_TSL_RNG

Source: [`PeetCrypto/freqtrade-stuff`](https://github.com/PeetCrypto/freqtrade-stuff) · file `BB_RPB_TSL_RNG.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 101 | 677 |
| expectancy per trade (USDT) | 1.47 | 1.84 |
| mean profit p-value | 4.228e-06 | 3.237e-09 |
| market change % (baseline) | -58.23 | 346.34 |
| strategy total % | 14.86 | 124.67 |
| Sharpe | 1.28 | 1.26 |
| Sortino | 2.24 | 1.34 |
| max drawdown % | 1.91 | 9.37 |
| profit factor | 3.45 | 2.46 |

**Retained out of sample: 125%**

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free. Cross-strategy comparisons in this repository use average profit per trade in percent.

Baseline: buy-and-hold on the same pairs returned **-58.23%**; the strategy returned **14.86%**.
Out of sample: buy-and-hold **346.34%** vs strategy **124.67%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | could not run | вывод не разобран |
| indicator recursion (freqtrade's own `recursive-analysis`) | clean | рекурсивных отклонений не найдено |
| прогрев не объявлен | **found** | самый длинный индикатор 100 свечей, startup_candle_count не задан (по умолчанию 0) |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **5m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `4a7c7414af9b` · strategy list `dac6309df791d209`*
