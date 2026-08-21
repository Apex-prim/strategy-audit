# Minmax

Source: [`PeetCrypto/freqtrade-stuff`](https://github.com/PeetCrypto/freqtrade-stuff) · file `MinmaxF.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 898 | 2984 |
| expectancy per trade (USDT) | -0.8 | -0.16 |
| mean profit p-value | 3.103e-08 | 0.3454 |
| market change % (baseline) | -58.4 | 348.67 |
| strategy total % | -71.98 | -46.64 |
| Sharpe | -4.38 | -0.42 |
| Sortino | -15.21 | -2.37 |
| max drawdown % | 71.98 | 66.89 |
| profit factor | 0.65 | 0.96 |

**Retained out of sample: negative**

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free. Cross-strategy comparisons in this repository use average profit per trade in percent.

Baseline: buy-and-hold on the same pairs returned **-58.4%**; the strategy returned **-71.98%**.
Out of sample: buy-and-hold **348.67%** vs strategy **-46.64%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | could not run | вывод не разобран |
| indicator recursion (freqtrade's own `recursive-analysis`) | clean | рекурсивных отклонений не найдено |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **1h** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `4a7c7414af9b` · strategy list `dac6309df791d209`*
