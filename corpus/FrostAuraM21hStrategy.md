# FrostAuraM21hStrategy

Source: [`PeetCrypto/freqtrade-stuff`](https://github.com/PeetCrypto/freqtrade-stuff) · file `FrostAuraM21hStrategy.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 8809 | 11071 |
| expectancy per trade (USDT) | -0.11 | -0.09 |
| mean profit p-value | 1.723e-29 | 1.761e-14 |
| market change % (baseline) | -58.53 | 345.85 |
| strategy total % | -94.75 | -96.57 |
| Sharpe | -27.8 | -6.53 |
| Sortino | -53.3 | -12.73 |
| max drawdown % | 94.77 | 96.57 |
| profit factor | 0.59 | 0.72 |

**Retained out of sample: negative**

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free. Cross-strategy comparisons in this repository use average profit per trade in percent.

Baseline: buy-and-hold on the same pairs returned **-58.53%**; the strategy returned **-94.75%**.
Out of sample: buy-and-hold **345.85%** vs strategy **-96.57%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | could not run | вывод не разобран |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | индикаторы меняются от объёма истории: rsi -0.375% |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **15m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `4a7c7414af9b` · strategy list `dac6309df791d209`*
