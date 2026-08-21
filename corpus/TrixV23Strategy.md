# TrixV23Strategy

Source: [`PeetCrypto/freqtrade-stuff`](https://github.com/PeetCrypto/freqtrade-stuff) · file `TrixV23Strategy (1).py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 265 | 1040 |
| expectancy per trade (USDT) | -0.39 | -0.17 |
| mean profit p-value | 0.1876 | 0.2774 |
| market change % (baseline) | -54.03 | 348.67 |
| strategy total % | -10.2 | -17.19 |
| Sharpe | -0.57 | -0.28 |
| Sortino | -0.67 | -0.32 |
| max drawdown % | 15.85 | 30.64 |
| profit factor | 0.78 | 0.9 |

**Retained out of sample: negative**

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free. Cross-strategy comparisons in this repository use average profit per trade in percent.

⚠ **Not statistically significant in its author's own window** (p = 0.1876 > 0.05): the average trade is not distinguishable from zero.

Baseline: buy-and-hold on the same pairs returned **-54.03%**; the strategy returned **-10.2%**.
Out of sample: buy-and-hold **348.67%** vs strategy **-17.19%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | could not run | вывод не разобран |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | индикаторы меняются от объёма истории: btc_usdt_ema_184_1h -0.372%, atr_30 -0.035% |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **1h** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `4a7c7414af9b` · strategy list `dac6309df791d209`*
