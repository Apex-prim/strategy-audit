# Ichimoku_v37

Source: [`PeetCrypto/freqtrade-stuff`](https://github.com/PeetCrypto/freqtrade-stuff) · file `Ichimoku_v37_HeikinAshi.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 57 | 450 |
| expectancy per trade (USDT) | 4.96 | 15.5 |
| mean profit p-value | 0.1946 | 0.03365 |
| market change % (baseline) | -51.25 | 340.8 |
| strategy total % | 28.27 | 697.65 |
| Sharpe | 0.27 | 0.37 |
| Sortino | 2.42 | 2.35 |
| max drawdown % | 6.26 | 28.22 |
| profit factor | 2.57 | 1.95 |

**Retained out of sample: 312%**

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free. Cross-strategy comparisons in this repository use average profit per trade in percent.

⚠ **Not statistically significant in its author's own window** (p = 0.1946 > 0.05): the average trade is not distinguishable from zero.

Baseline: buy-and-hold on the same pairs returned **-51.25%**; the strategy returned **28.27%**.
Out of sample: buy-and-hold **340.8%** vs strategy **697.65%** — **beats the baseline**.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | could not run | вывод не разобран |
| indicator recursion (freqtrade's own `recursive-analysis`) | clean | рекурсивных отклонений не найдено |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **4h** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `4a7c7414af9b` · strategy list `dac6309df791d209`*
