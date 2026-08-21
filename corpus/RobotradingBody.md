# RobotradingBody

Source: [`davidzr/freqtrade-strategies`](https://github.com/davidzr/freqtrade-strategies) · file `RobotradingBody.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 620 | 2275 |
| expectancy per trade (USDT) | -0.25 | -0.08 |
| mean profit p-value | 0.1131 | 0.4163 |
| market change % (baseline) | -50.13 | 340.8 |
| strategy total % | -15.71 | -17.44 |
| Sharpe | -1.06 | -0.31 |
| Sortino | -1.09 | -0.3 |
| max drawdown % | 25.62 | 43.02 |
| profit factor | 0.81 | 0.94 |

**Retained out of sample: negative**

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free. Cross-strategy comparisons in this repository use average profit per trade in percent.

⚠ **Not statistically significant in its author's own window** (p = 0.1131 > 0.05): the average trade is not distinguishable from zero.

Baseline: buy-and-hold on the same pairs returned **-50.13%**; the strategy returned **-15.71%**.
Out of sample: buy-and-hold **340.8%** vs strategy **-17.44%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | clean | смещения не обнаружено |
| indicator recursion (freqtrade's own `recursive-analysis`) | clean | рекурсивных отклонений не найдено |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **4h** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `4a7c7414af9b` · strategy list `dac6309df791d209`*
