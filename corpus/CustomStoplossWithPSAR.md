# CustomStoplossWithPSAR

Source: [`PeetCrypto/freqtrade-stuff`](https://github.com/PeetCrypto/freqtrade-stuff) · file `custom_stoploss_with_psar.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 62 | 78 |
| expectancy per trade (USDT) | -8.78 | 55.86 |
| mean profit p-value | 0.0002515 | 0.1366 |
| market change % (baseline) | -58.4 | 348.67 |
| strategy total % | -54.41 | 435.73 |
| Sharpe | -0.81 | 0.11 |
| Sortino | -2.42 | 1.16 |
| max drawdown % | 76.2 | 23.46 |
| profit factor | 0.3 | 2.37 |

**Retained out of sample: n/a**

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free. Cross-strategy comparisons in this repository use average profit per trade in percent.

Baseline: buy-and-hold on the same pairs returned **-58.4%**; the strategy returned **-54.41%**.
Out of sample: buy-and-hold **348.67%** vs strategy **435.73%** — **beats the baseline**.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | could not run | вывод не разобран |
| indicator recursion (freqtrade's own `recursive-analysis`) | clean | рекурсивных отклонений не найдено |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **1h** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `4a7c7414af9b` · strategy list `dac6309df791d209`*
