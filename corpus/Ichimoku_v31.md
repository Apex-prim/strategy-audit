# Ichimoku_v31

Source: [`PeetCrypto/freqtrade-stuff`](https://github.com/PeetCrypto/freqtrade-stuff) · file `Ichimoku_v31_Heikin.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 238 | 1326 |
| expectancy per trade (USDT) | 3.68 | 4.26 |
| mean profit p-value | 0.0115 | 0.07244 |
| market change % (baseline) | -57.84 | 348.67 |
| strategy total % | 87.57 | 564.95 |
| Sharpe | 1.04 | 0.53 |
| Sortino | 6.65 | 2.87 |
| max drawdown % | 14.48 | 26.11 |
| profit factor | 2.16 | 1.36 |

**Retained out of sample: 116%**

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free. Cross-strategy comparisons in this repository use average profit per trade in percent.

Baseline: buy-and-hold on the same pairs returned **-57.84%**; the strategy returned **87.57%**.
Out of sample: buy-and-hold **348.67%** vs strategy **564.95%** — **beats the baseline**.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | could not run | вывод не разобран |
| indicator recursion (freqtrade's own `recursive-analysis`) | clean | рекурсивных отклонений не найдено |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **1h** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `4a7c7414af9b` · strategy list `dac6309df791d209`*
