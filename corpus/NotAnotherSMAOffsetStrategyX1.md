# NotAnotherSMAOffsetStrategyX1

Source: [`PeetCrypto/freqtrade-stuff`](https://github.com/PeetCrypto/freqtrade-stuff) · file `NotAnotherSMAOffsetStrategyX1.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 116 | 481 |
| expectancy per trade (USDT) | 0.87 | 0.91 |
| mean profit p-value | 1.005e-05 | 4.64e-07 |
| market change % (baseline) | -59.23 | 346.34 |
| strategy total % | 10.14 | 43.9 |
| Sharpe | 1.31 | 0.91 |
| Sortino | 1.74 | 0.71 |
| max drawdown % | 1.02 | 5.79 |
| profit factor | 2.82 | 2.07 |

**Retained out of sample: 105%**

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free. Cross-strategy comparisons in this repository use average profit per trade in percent.

Baseline: buy-and-hold on the same pairs returned **-59.23%**; the strategy returned **10.14%**.
Out of sample: buy-and-hold **346.34%** vs strategy **43.9%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | could not run | код 1 |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | индикаторы меняются от объёма истории: EWO -12.317% |
| прогрев объявлен | clean | 400 при потребности 100 |
| мёртвые настройки трейлинга | **found** | trailing_stop=False, но trailing_stop_positive=0.005 задан — читается как работающая защита |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **5m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `4a7c7414af9b` · strategy list `dac6309df791d209`*
