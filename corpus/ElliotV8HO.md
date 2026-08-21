# ElliotV8HO

Source: [`davidzr/freqtrade-strategies`](https://github.com/davidzr/freqtrade-strategies) · file `ElliotV8HO.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 42 | 344 |
| expectancy per trade (USDT) | 0.93 | 2.28 |
| mean profit p-value | 0.3034 | 3.707e-10 |
| market change % (baseline) | -59.23 | 346.34 |
| strategy total % | 3.92 | 78.43 |
| Sharpe | 0.18 | 0.97 |
| Sortino | 1.81 | 1.0 |
| max drawdown % | 2.36 | 6.41 |
| profit factor | 1.8 | 3.38 |

**Retained out of sample: 245%**

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free. Cross-strategy comparisons in this repository use average profit per trade in percent.

⚠ **Not statistically significant in its author's own window** (p = 0.3034 > 0.05): the average trade is not distinguishable from zero.

Baseline: buy-and-hold on the same pairs returned **-59.23%**; the strategy returned **3.92%**.
Out of sample: buy-and-hold **346.34%** vs strategy **78.43%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | could not run | вывод не разобран |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | индикаторы меняются от объёма истории: EWO -12.317% |
| прогрев объявлен | clean | 400 при потребности 50 |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **5m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `4a7c7414af9b` · strategy list `dac6309df791d209`*
