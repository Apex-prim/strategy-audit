# NotAnotherSMAOffsetStrategyModHO

Source: [`PeetCrypto/freqtrade-stuff`](https://github.com/PeetCrypto/freqtrade-stuff) · file `NotAnotherSMAOffsetStrategyModHO.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 159 | 985 |
| expectancy per trade (USDT) | 0.12 | 0.51 |
| mean profit p-value | 0.5183 | 2.003e-05 |
| market change % (baseline) | -59.05 | 346.34 |
| strategy total % | 1.98 | 50.12 |
| Sharpe | 0.21 | 1.09 |
| Sortino | 0.21 | 1.03 |
| max drawdown % | 5.77 | 7.86 |
| profit factor | 1.15 | 1.5 |

**Retained out of sample: 425%**

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free. Cross-strategy comparisons in this repository use average profit per trade in percent.

⚠ **Not statistically significant in its author's own window** (p = 0.5183 > 0.05): the average trade is not distinguishable from zero.

Baseline: buy-and-hold on the same pairs returned **-59.05%**; the strategy returned **1.98%**.
Out of sample: buy-and-hold **346.34%** vs strategy **50.12%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | could not run | вывод не разобран |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | индикаторы меняются от объёма истории: EWO -12.317% |
| прогрев объявлен | clean | 200 при потребности 100 |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **5m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `4a7c7414af9b` · strategy list `dac6309df791d209`*
