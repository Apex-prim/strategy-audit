# FrostAuraM315mStrategy

Source: [`PeetCrypto/freqtrade-stuff`](https://github.com/PeetCrypto/freqtrade-stuff) · file `FrostAuraM315mStrategy.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 1892 | 7229 |
| expectancy per trade (USDT) | -0.39 | -0.1 |
| mean profit p-value | 3.135e-09 | 0.05951 |
| market change % (baseline) | -58.53 | 345.85 |
| strategy total % | -73.32 | -74.57 |
| Sharpe | -6.78 | -1.3 |
| Sortino | -4.64 | -0.85 |
| max drawdown % | 75.15 | 84.29 |
| profit factor | 0.45 | 0.88 |

**Retained out of sample: negative**

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free. Cross-strategy comparisons in this repository use average profit per trade in percent.

Baseline: buy-and-hold on the same pairs returned **-58.53%**; the strategy returned **-73.32%**.
Out of sample: buy-and-hold **345.85%** vs strategy **-74.57%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | could not run | вывод не разобран |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | индикаторы меняются от объёма истории: rsi -0.375% |
| прогрев не объявлен | **found** | самый длинный индикатор 20 свечей, startup_candle_count не задан (по умолчанию 0) |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **15m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `4a7c7414af9b` · strategy list `dac6309df791d209`*
