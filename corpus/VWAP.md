# VWAP

Source: [`PeetCrypto/freqtrade-stuff`](https://github.com/PeetCrypto/freqtrade-stuff) · file `VWAP.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 200 | 786 |
| expectancy per trade (USDT) | 1.48 | 0.99 |
| mean profit p-value | 0.0001053 | 0.002752 |
| market change % (baseline) | -58.23 | 346.34 |
| strategy total % | 29.61 | 78.13 |
| Sharpe | 1.47 | 0.68 |
| Sortino | 5.29 | 1.36 |
| max drawdown % | 6.33 | 22.26 |
| profit factor | 2.32 | 1.41 |

**Retained out of sample: 67%**

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free. Cross-strategy comparisons in this repository use average profit per trade in percent.

Baseline: buy-and-hold on the same pairs returned **-58.23%**; the strategy returned **29.61%**.
Out of sample: buy-and-hold **346.34%** vs strategy **78.13%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | could not run | вывод не разобран |
| indicator recursion (freqtrade's own `recursive-analysis`) | clean | рекурсивных отклонений не найдено |
| прогрев не объявлен | **found** | самый длинный индикатор 112 свечей, startup_candle_count не задан (по умолчанию 0) |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **5m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `4a7c7414af9b` · strategy list `dac6309df791d209`*
