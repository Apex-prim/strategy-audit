# SMAOffsetProtectOpt

Source: [`davidzr/freqtrade-strategies`](https://github.com/davidzr/freqtrade-strategies) · file `SMAOffsetProtectOpt.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 20 | 161 |
| expectancy per trade (USDT) | 0.63 | 4.4 |
| mean profit p-value | 0.4865 | 4.681e-08 |
| market change % (baseline) | -59.05 | 346.34 |
| strategy total % | 1.26 | 70.81 |
| Sharpe | 0.09 | 0.59 |
| Sortino | 0.18 | 0.53 |
| max drawdown % | 0.91 | 4.31 |
| profit factor | 1.44 | 4.45 |

**Retained out of sample: 698%**

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free. Cross-strategy comparisons in this repository use average profit per trade in percent.

⚠ **Not statistically significant in its author's own window** (p = 0.4865 > 0.05): the average trade is not distinguishable from zero.

Baseline: buy-and-hold on the same pairs returned **-59.05%**; the strategy returned **1.26%**.
Out of sample: buy-and-hold **346.34%** vs strategy **70.81%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | could not run | вывод не разобран |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | индикаторы меняются от объёма истории: EWO -12.317% |
| прогрев объявлен | clean | 200 при потребности 14 |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **5m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `4a7c7414af9b` · strategy list `dac6309df791d209`*
