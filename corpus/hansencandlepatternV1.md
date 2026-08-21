# hansencandlepatternV1

Source: [`PeetCrypto/freqtrade-stuff`](https://github.com/PeetCrypto/freqtrade-stuff) · file `hansencandlepatternV1.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 3562 | 13603 |
| expectancy per trade (USDT) | -0.19 | -0.07 |
| mean profit p-value | 1.713e-11 | 6.932e-07 |
| market change % (baseline) | -58.4 | 348.67 |
| strategy total % | -68.87 | -95.94 |
| Sharpe | -10.53 | -4.68 |
| Sortino | -18.09 | -8.53 |
| max drawdown % | 72.11 | 96.28 |
| profit factor | 0.67 | 0.8 |

**Retained out of sample: negative**

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free. Cross-strategy comparisons in this repository use average profit per trade in percent.

Baseline: buy-and-hold on the same pairs returned **-58.4%**; the strategy returned **-68.87%**.
Out of sample: buy-and-hold **348.67%** vs strategy **-95.94%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | could not run | вывод не разобран |
| indicator recursion (freqtrade's own `recursive-analysis`) | clean | рекурсивных отклонений не найдено |
| прогрев не объявлен | **found** | самый длинный индикатор 6 свечей, startup_candle_count не задан (по умолчанию 0) |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **1h** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `4a7c7414af9b` · strategy list `dac6309df791d209`*
