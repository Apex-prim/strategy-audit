# XebTradeStrat

Source: [`PeetCrypto/freqtrade-stuff`](https://github.com/PeetCrypto/freqtrade-stuff) · file `XebTradeStrat.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 12612 | 13320 |
| expectancy per trade (USDT) | -0.08 | -0.07 |
| mean profit p-value | 1.217e-196 | 1.046e-185 |
| market change % (baseline) | -55.54 | 347.94 |
| strategy total % | -96.59 | -96.58 |
| Sharpe | -89.39 | -27.57 |
| Sortino | -69.23 | -21.61 |
| max drawdown % | 96.6 | 96.58 |
| profit factor | 0.31 | 0.33 |

**Retained out of sample: negative**

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free. Cross-strategy comparisons in this repository use average profit per trade in percent.

Baseline: buy-and-hold on the same pairs returned **-55.54%**; the strategy returned **-96.59%**.
Out of sample: buy-and-hold **347.94%** vs strategy **-96.58%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | could not run | вывод не разобран |
| indicator recursion (freqtrade's own `recursive-analysis`) | clean | рекурсивных отклонений не найдено |
| прогрев не объявлен | **found** | самый длинный индикатор 10 свечей, startup_candle_count не задан (по умолчанию 0) |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **1m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `4a7c7414af9b` · strategy list `dac6309df791d209`*
