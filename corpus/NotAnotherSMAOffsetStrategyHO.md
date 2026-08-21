# NotAnotherSMAOffsetStrategyHO

Source: [`davidzr/freqtrade-strategies`](https://github.com/davidzr/freqtrade-strategies) · file `NotAnotherSMAOffsetStrategyHO.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 185 | 720 |
| expectancy per trade (USDT) | 1.91 | 3.74 |
| mean profit p-value | 1.079e-11 | 1.069e-11 |
| market change % (baseline) | -59.05 | 346.34 |
| strategy total % | 35.4 | 269.2 |
| Sharpe | 2.59 | 1.5 |
| Sortino | 3.33 | 0.73 |
| max drawdown % | 5.04 | 12.8 |
| profit factor | 3.36 | 2.67 |

**Retained out of sample: 196%**

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free. Cross-strategy comparisons in this repository use average profit per trade in percent.

Baseline: buy-and-hold on the same pairs returned **-59.05%**; the strategy returned **35.4%**.
Out of sample: buy-and-hold **346.34%** vs strategy **269.2%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | could not run | Fatal exception! |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | индикаторы меняются от объёма истории: EWO -12.317% |
| прогрев объявлен | clean | 200 при потребности 100 |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **5m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `4a7c7414af9b` · strategy list `dac6309df791d209`*
