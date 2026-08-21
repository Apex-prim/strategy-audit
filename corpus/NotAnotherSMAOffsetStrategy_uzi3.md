# NotAnotherSMAOffsetStrategy_uzi3

Source: [`PeetCrypto/freqtrade-stuff`](https://github.com/PeetCrypto/freqtrade-stuff) · file `NotAnotherSMAOffsetStrategy_uzi3.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 217 | 954 |
| expectancy per trade (USDT) | 0.58 | 1.44 |
| mean profit p-value | 0.07369 | 1.396e-07 |
| market change % (baseline) | -59.23 | 346.34 |
| strategy total % | 12.67 | 137.43 |
| Sharpe | 0.7 | 1.33 |
| Sortino | 0.57 | 0.91 |
| max drawdown % | 3.83 | 7.64 |
| profit factor | 1.4 | 1.68 |

**Retained out of sample: 248%**

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free. Cross-strategy comparisons in this repository use average profit per trade in percent.

⚠ **Not statistically significant in its author's own window** (p = 0.07369 > 0.05): the average trade is not distinguishable from zero.

Baseline: buy-and-hold on the same pairs returned **-59.23%**; the strategy returned **12.67%**.
Out of sample: buy-and-hold **346.34%** vs strategy **137.43%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | could not run | код 1 |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | индикаторы меняются от объёма истории: EWO -12.317% |
| прогрев объявлен | clean | 400 при потребности 100 |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **5m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `4a7c7414af9b` · strategy list `dac6309df791d209`*
