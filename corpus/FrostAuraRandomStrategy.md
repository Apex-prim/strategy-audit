# FrostAuraRandomStrategy

Source: [`davidzr/freqtrade-strategies`](https://github.com/davidzr/freqtrade-strategies) · file `FrostAuraRandomStrategy.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 1286 | 4513 |
| expectancy per trade (USDT) | -0.56 | -0.14 |
| mean profit p-value | 0.0006464 | 0.554 |
| market change % (baseline) | -59.27 | 348.67 |
| strategy total % | -72.31 | -63.93 |
| Sharpe | -3.22 | -0.32 |
| Sortino | -2.39 | -0.24 |
| max drawdown % | 77.87 | 90.41 |
| profit factor | 0.66 | 0.96 |

**Retained out of sample: negative**

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free. Cross-strategy comparisons in this repository use average profit per trade in percent.

Baseline: buy-and-hold on the same pairs returned **-59.27%**; the strategy returned **-72.31%**.
Out of sample: buy-and-hold **348.67%** vs strategy **-63.93%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | **found** | ЕСТЬ СМЕЩЕНИЕ: входов 20, выходов 17 из 20 сигналов |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | индикаторы меняются от объёма истории: random_number 88.000% |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **1h** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `4a7c7414af9b` · strategy list `dac6309df791d209`*
