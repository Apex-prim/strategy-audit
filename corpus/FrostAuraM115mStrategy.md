# FrostAuraM115mStrategy

Source: [`PeetCrypto/freqtrade-stuff`](https://github.com/PeetCrypto/freqtrade-stuff) · file `FrostAuraM115mStrategy.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 7461 | 23390 |
| expectancy per trade (USDT) | -0.12 | -0.04 |
| mean profit p-value | 3.149e-17 | 0.001517 |
| market change % (baseline) | -58.53 | 345.85 |
| strategy total % | -88.9 | -96.58 |
| Sharpe | -19.13 | -3.92 |
| Sortino | -14.45 | -2.71 |
| max drawdown % | 89.07 | 97.31 |
| profit factor | 0.64 | 0.88 |

**Retained out of sample: negative**

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free. Cross-strategy comparisons in this repository use average profit per trade in percent.

Baseline: buy-and-hold on the same pairs returned **-58.53%**; the strategy returned **-88.9%**.
Out of sample: buy-and-hold **345.85%** vs strategy **-96.58%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | could not run | вывод не разобран |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | индикаторы меняются от объёма истории: rsi -0.375% |
| прогрев не объявлен | **found** | самый длинный индикатор 20 свечей, startup_candle_count не задан (по умолчанию 0) |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **15m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `4a7c7414af9b` · strategy list `dac6309df791d209`*
