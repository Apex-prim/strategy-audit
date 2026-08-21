# AlexBattleTankKillerV40H

Source: [`jaredrsommer/freqtradestrategies`](https://github.com/jaredrsommer/freqtradestrategies) · file `AlexBattleTankKillerV4H.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 1072 | 3898 |
| expectancy per trade (USDT) | -0.12 | -0.05 |
| mean profit p-value | 0.000138 | 0.0001232 |
| market change % (baseline) | -54.03 | 348.67 |
| strategy total % | -12.56 | -21.04 |
| Sharpe | -3.32 | -1.94 |
| Sortino | -2.18 | -1.27 |
| max drawdown % | 13.96 | 22.96 |
| profit factor | 0.51 | 0.71 |

**Retained out of sample: negative**

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free. Cross-strategy comparisons in this repository use average profit per trade in percent.

Baseline: buy-and-hold on the same pairs returned **-54.03%**; the strategy returned **-12.56%**.
Out of sample: buy-and-hold **348.67%** vs strategy **-21.04%** — loses to it.

⚠ **Incomplete coverage:** the engine found no history for AVAX/USDT, BNB/USDT, SOL/USDT and computed on the rest. Not comparable to a full-coverage result.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | **found** | ЕСТЬ СМЕЩЕНИЕ: входов 4, выходов 2 из 20 сигналов |
| indicator recursion (freqtrade's own `recursive-analysis`) | clean | рекурсивных отклонений не найдено |
| прогрев не объявлен | **found** | самый длинный индикатор 50 свечей, startup_candle_count не задан (по умолчанию 0) |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **1h** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `8d9b3a08743f` · strategy list `d43e19f4fcbe76b6`*
