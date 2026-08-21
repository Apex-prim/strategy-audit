# FrostAuraM31hStrategy

Source: [`PeetCrypto/freqtrade-stuff`](https://github.com/PeetCrypto/freqtrade-stuff) · file `FrostAuraM31hStrategy.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 533 | 1936 |
| expectancy per trade (USDT) | -1.29 | -0.32 |
| mean profit p-value | 1.195e-05 | 0.08998 |
| market change % (baseline) | -59.27 | 348.67 |
| strategy total % | -68.7 | -62.28 |
| Sharpe | -2.68 | -0.6 |
| Sortino | -2.01 | -0.46 |
| max drawdown % | 68.96 | 71.59 |
| profit factor | 0.39 | 0.84 |

**Retained out of sample: negative**

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free. Cross-strategy comparisons in this repository use average profit per trade in percent.

Baseline: buy-and-hold on the same pairs returned **-59.27%**; the strategy returned **-68.7%**.
Out of sample: buy-and-hold **348.67%** vs strategy **-62.28%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | could not run | вывод не разобран |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | индикаторы меняются от объёма истории: rsi 4.044% |
| прогрев не объявлен | **found** | самый длинный индикатор 20 свечей, startup_candle_count не задан (по умолчанию 0) |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **1h** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `4a7c7414af9b` · strategy list `dac6309df791d209`*
