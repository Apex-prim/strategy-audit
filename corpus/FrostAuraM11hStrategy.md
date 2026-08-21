# FrostAuraM11hStrategy

Source: [`PeetCrypto/freqtrade-stuff`](https://github.com/PeetCrypto/freqtrade-stuff) · file `FrostAuraM11hStrategy.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 595 | 2041 |
| expectancy per trade (USDT) | -1.26 | -0.08 |
| mean profit p-value | 0.0004522 | 0.8488 |
| market change % (baseline) | -59.27 | 348.67 |
| strategy total % | -74.81 | -17.3 |
| Sharpe | -2.26 | -0.07 |
| Sortino | -1.36 | -0.04 |
| max drawdown % | 75.2 | 68.42 |
| profit factor | 0.43 | 0.98 |

**Retained out of sample: negative**

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free. Cross-strategy comparisons in this repository use average profit per trade in percent.

Baseline: buy-and-hold on the same pairs returned **-59.27%**; the strategy returned **-74.81%**.
Out of sample: buy-and-hold **348.67%** vs strategy **-17.3%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | could not run | вывод не разобран |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | индикаторы меняются от объёма истории: rsi 4.044% |
| прогрев не объявлен | **found** | самый длинный индикатор 20 свечей, startup_candle_count не задан (по умолчанию 0) |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **1h** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `4a7c7414af9b` · strategy list `dac6309df791d209`*
