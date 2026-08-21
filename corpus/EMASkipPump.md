# EMASkipPump

Source: [`PeetCrypto/freqtrade-stuff`](https://github.com/PeetCrypto/freqtrade-stuff) · file `EMASkipPump.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 11468 | 22854 |
| expectancy per trade (USDT) | -0.08 | -0.04 |
| mean profit p-value | 5.273e-25 | 1.169e-11 |
| market change % (baseline) | -58.23 | 346.34 |
| strategy total % | -96.61 | -96.65 |
| Sharpe | -28.97 | -8.3 |
| Sortino | -24.49 | -7.99 |
| max drawdown % | 96.65 | 96.76 |
| profit factor | 0.63 | 0.85 |

**Retained out of sample: negative**

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free. Cross-strategy comparisons in this repository use average profit per trade in percent.

Baseline: buy-and-hold on the same pairs returned **-58.23%**; the strategy returned **-96.61%**.
Out of sample: buy-and-hold **346.34%** vs strategy **-96.65%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | could not run | вывод не разобран |
| indicator recursion (freqtrade's own `recursive-analysis`) | clean | рекурсивных отклонений не найдено |
| прогрев не объявлен | **found** | самый длинный индикатор 30 свечей, startup_candle_count не задан (по умолчанию 0) |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **5m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `4a7c7414af9b` · strategy list `dac6309df791d209`*
