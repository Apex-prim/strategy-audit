# tesla7

Source: [`MMR-19/freqtrade-strategies`](https://github.com/MMR-19/freqtrade-strategies) · file `Tesla7.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 4 | — |
| expectancy per trade (USDT) | 2.21 | — |
| mean profit p-value | 0.005171 | — |
| market change % (baseline) | -59.05 | — |
| strategy total % | 0.88 | — |
| Sharpe | 0.45 | — |
| Sortino | -100.0 | — |
| max drawdown % | 0.0 | — |
| profit factor | 0.0 | — |

**Retained out of sample: —**

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free. Cross-strategy comparisons in this repository use average profit per trade in percent.

Baseline: buy-and-hold on the same pairs returned **-59.05%**; the strategy returned **0.88%**.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | could not run | Fatal exception! |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | индикаторы меняются от объёма истории: EWO -12.317% |
| прогрев объявлен | clean | 200 при потребности 100 |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **5m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `8d9b3a08743f` · strategy list `d43e19f4fcbe76b6`*
