# tesla4

Source: [`MMR-19/freqtrade-strategies`](https://github.com/MMR-19/freqtrade-strategies) · file `Tesla4.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 3 | — |
| expectancy per trade (USDT) | -0.27 | — |
| mean profit p-value | 0.8322 | — |
| market change % (baseline) | -59.05 | — |
| strategy total % | -0.08 | — |
| Sharpe | -0.01 | — |
| Sortino | -100.0 | — |
| max drawdown % | 0.25 | — |
| profit factor | 0.68 | — |

**Retained out of sample: —**

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free. Cross-strategy comparisons in this repository use average profit per trade in percent.

⚠ **Not statistically significant in its author's own window** (p = 0.8322 > 0.05): the average trade is not distinguishable from zero.

Baseline: buy-and-hold on the same pairs returned **-59.05%**; the strategy returned **-0.08%**.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | could not run | Fatal exception! |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | индикаторы меняются от объёма истории: EWO -12.317%, vol_ma_200 8.933% |
| прогрев объявлен | clean | 200 при потребности 200 |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **5m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `8d9b3a08743f` · strategy list `d43e19f4fcbe76b6`*
