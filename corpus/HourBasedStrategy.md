# HourBasedStrategy

Source: [`PeetCrypto/freqtrade-stuff`](https://github.com/PeetCrypto/freqtrade-stuff) · file `HourBasedStrategy.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 2449 | 8435 |
| expectancy per trade (USDT) | -0.35 | -0.11 |
| mean profit p-value | 2.438e-07 | 0.1326 |
| market change % (baseline) | -58.4 | 348.67 |
| strategy total % | -85.88 | -96.74 |
| Sharpe | -6.7 | -1.12 |
| Sortino | -6.87 | -1.11 |
| max drawdown % | 88.64 | 98.61 |
| profit factor | 0.7 | 0.94 |

**Retained out of sample: negative**

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free. Cross-strategy comparisons in this repository use average profit per trade in percent.

Baseline: buy-and-hold on the same pairs returned **-58.4%**; the strategy returned **-85.88%**.
Out of sample: buy-and-hold **348.67%** vs strategy **-96.74%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | could not run | вывод не разобран |
| indicator recursion (freqtrade's own `recursive-analysis`) | clean | рекурсивных отклонений не найдено |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **1h** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `4a7c7414af9b` · strategy list `dac6309df791d209`*
