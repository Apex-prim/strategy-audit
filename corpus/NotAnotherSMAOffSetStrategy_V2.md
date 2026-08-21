# NotAnotherSMAOffSetStrategy_V2

Source: [`PeetCrypto/freqtrade-stuff`](https://github.com/PeetCrypto/freqtrade-stuff) · file `NotAnotherSMAOffSetStrategy_V2.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 3 | — |
| expectancy per trade (USDT) | 1.2 | — |
| mean profit p-value | 0.3965 | — |
| market change % (baseline) | -59.05 | — |
| strategy total % | 0.36 | — |
| Sharpe | 0.06 | — |
| Sortino | -100.0 | — |
| max drawdown % | 0.09 | — |
| profit factor | 4.77 | — |

**Retained out of sample: —**

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free. Cross-strategy comparisons in this repository use average profit per trade in percent.

⚠ **Not statistically significant in its author's own window** (p = 0.3965 > 0.05): the average trade is not distinguishable from zero.

Baseline: buy-and-hold on the same pairs returned **-59.05%**; the strategy returned **0.36%**.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | could not run | код 1 |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | индикаторы меняются от объёма истории: EWO -12.317% |
| прогрев объявлен | clean | 200 при потребности 100 |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **5m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `4a7c7414af9b` · strategy list `dac6309df791d209`*
