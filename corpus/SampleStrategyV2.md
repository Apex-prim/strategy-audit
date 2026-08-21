# SampleStrategyV2

Source: [`PeetCrypto/freqtrade-stuff`](https://github.com/PeetCrypto/freqtrade-stuff) · file `Machete.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 1400 | 4482 |
| expectancy per trade (USDT) | -0.53 | -0.18 |
| mean profit p-value | 9.909e-07 | 0.0006767 |
| market change % (baseline) | -59.3 | 346.34 |
| strategy total % | -73.72 | -82.76 |
| Sharpe | -4.83 | -1.84 |
| Sortino | -2.87 | -0.83 |
| max drawdown % | 74.09 | 85.26 |
| profit factor | 0.51 | 0.76 |

**Retained out of sample: negative**

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free. Cross-strategy comparisons in this repository use average profit per trade in percent.

Baseline: buy-and-hold on the same pairs returned **-59.3%**; the strategy returned **-73.72%**.
Out of sample: buy-and-hold **346.34%** vs strategy **-82.76%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | could not run | вывод не разобран |
| indicator recursion (freqtrade's own `recursive-analysis`) | clean | рекурсивных отклонений не найдено |
| прогрев не объявлен | **found** | самый длинный индикатор 100 свечей, startup_candle_count не задан (по умолчанию 0) |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **5m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `4a7c7414af9b` · strategy list `dac6309df791d209`*
