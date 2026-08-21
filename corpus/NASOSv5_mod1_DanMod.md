# NASOSv5_mod1_DanMod

Source: [`davidzr/freqtrade-strategies`](https://github.com/davidzr/freqtrade-strategies) · file `NASOSv5_mod1_DanMod.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 29 | 367 |
| expectancy per trade (USDT) | 2.99 | 5.8 |
| mean profit p-value | 0.06708 | 1.396e-11 |
| market change % (baseline) | -59.05 | 346.34 |
| strategy total % | 8.68 | 212.81 |
| Sharpe | 0.27 | 1.08 |
| Sortino | -100.0 | 0.49 |
| max drawdown % | 3.73 | 11.09 |
| profit factor | 3.13 | 3.7 |

**Retained out of sample: 194%**

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free. Cross-strategy comparisons in this repository use average profit per trade in percent.

⚠ **Not statistically significant in its author's own window** (p = 0.06708 > 0.05): the average trade is not distinguishable from zero.

Baseline: buy-and-hold on the same pairs returned **-59.05%**; the strategy returned **8.68%**.
Out of sample: buy-and-hold **346.34%** vs strategy **212.81%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | could not run | Fatal exception! |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | индикаторы меняются от объёма истории: EWO -12.317%, rsi_slow 0.021% |
| прогрев объявлен | clean | 200 при потребности 100 |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **5m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `4a7c7414af9b` · strategy list `dac6309df791d209`*
