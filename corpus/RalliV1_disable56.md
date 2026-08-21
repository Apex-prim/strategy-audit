# RalliV1_disable56

Source: [`PeetCrypto/freqtrade-stuff`](https://github.com/PeetCrypto/freqtrade-stuff) · file `RalliV1_disable56.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 145 | 506 |
| expectancy per trade (USDT) | 1.0 | 1.86 |
| mean profit p-value | 9.373e-05 | 6.154e-18 |
| market change % (baseline) | -59.05 | 346.34 |
| strategy total % | 14.49 | 93.87 |
| Sharpe | 1.27 | 1.63 |
| Sortino | 1.57 | 1.45 |
| max drawdown % | 4.69 | 4.75 |
| profit factor | 2.32 | 2.9 |

**Retained out of sample: 186%**

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free. Cross-strategy comparisons in this repository use average profit per trade in percent.

Baseline: buy-and-hold on the same pairs returned **-59.05%**; the strategy returned **14.49%**.
Out of sample: buy-and-hold **346.34%** vs strategy **93.87%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | could not run | вывод не разобран |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | индикаторы меняются от объёма истории: EWO -12.317% |
| прогрев объявлен | clean | 200 при потребности 100 |
| мёртвые настройки трейлинга | **found** | trailing_stop=False, но trailing_stop_positive=0.005 задан — читается как работающая защита |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **5m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `4a7c7414af9b` · strategy list `dac6309df791d209`*
