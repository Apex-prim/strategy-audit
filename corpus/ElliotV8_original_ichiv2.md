# ElliotV8_original_ichiv2

Source: [`davidzr/freqtrade-strategies`](https://github.com/davidzr/freqtrade-strategies) · file `ElliotV8_original_ichiv2.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 215 | 1063 |
| expectancy per trade (USDT) | 0.16 | 2.28 |
| mean profit p-value | 0.7675 | 2.85e-06 |
| market change % (baseline) | -59.23 | 346.34 |
| strategy total % | 3.51 | 242.62 |
| Sharpe | 0.11 | 1.24 |
| Sortino | 1.31 | 1.06 |
| max drawdown % | 10.89 | 12.02 |
| profit factor | 1.07 | 1.7 |

**Retained out of sample: 1425%**

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free. Cross-strategy comparisons in this repository use average profit per trade in percent.

⚠ **Not statistically significant in its author's own window** (p = 0.7675 > 0.05): the average trade is not distinguishable from zero.

Baseline: buy-and-hold on the same pairs returned **-59.23%**; the strategy returned **3.51%**.
Out of sample: buy-and-hold **346.34%** vs strategy **242.62%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | could not run | вывод не разобран |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | индикаторы меняются от объёма истории: EWO -12.317% |
| прогрев объявлен | clean | 400 при потребности 50 |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **5m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `4a7c7414af9b` · strategy list `dac6309df791d209`*
