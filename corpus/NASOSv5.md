# NASOSv5

Source: [`PeetCrypto/freqtrade-stuff`](https://github.com/PeetCrypto/freqtrade-stuff) · file `NASOSv5.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 117 | 684 |
| expectancy per trade (USDT) | 0.87 | 0.21 |
| mean profit p-value | 0.033 | 0.4225 |
| market change % (baseline) | -59.05 | 346.34 |
| strategy total % | 10.13 | 14.56 |
| Sharpe | 0.61 | 0.17 |
| Sortino | 0.42 | 0.13 |
| max drawdown % | 1.87 | 19.41 |
| profit factor | 1.93 | 1.14 |

**Retained out of sample: 24%**

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free. Cross-strategy comparisons in this repository use average profit per trade in percent.

Baseline: buy-and-hold on the same pairs returned **-59.05%**; the strategy returned **10.13%**.
Out of sample: buy-and-hold **346.34%** vs strategy **14.56%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | could not run | код 1 |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | индикаторы меняются от объёма истории: EWO -12.317% |
| прогрев объявлен | clean | 200 при потребности 200 |
| мёртвые настройки трейлинга | **found** | trailing_stop=False, но trailing_stop_positive=0.001 задан — читается как работающая защита |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **5m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `4a7c7414af9b` · strategy list `dac6309df791d209`*
