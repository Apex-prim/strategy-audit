# SMAOffsetProtectOptV1

Source: [`PeetCrypto/freqtrade-stuff`](https://github.com/PeetCrypto/freqtrade-stuff) · file `SMAOffsetProtectOptV1.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 36 | 243 |
| expectancy per trade (USDT) | 0.53 | 1.48 |
| mean profit p-value | 0.1118 | 7.796e-05 |
| market change % (baseline) | -58.37 | 346.34 |
| strategy total % | 1.9 | 35.87 |
| Sharpe | 0.26 | 0.51 |
| Sortino | 0.27 | 0.3 |
| max drawdown % | 0.61 | 4.03 |
| profit factor | 1.99 | 3.43 |

**Retained out of sample: 279%**

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free. Cross-strategy comparisons in this repository use average profit per trade in percent.

⚠ **Not statistically significant in its author's own window** (p = 0.1118 > 0.05): the average trade is not distinguishable from zero.

Baseline: buy-and-hold on the same pairs returned **-58.37%**; the strategy returned **1.9%**.
Out of sample: buy-and-hold **346.34%** vs strategy **35.87%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | could not run | вывод не разобран |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | индикаторы меняются от объёма истории: rsi 0.935% |
| прогрев объявлен | clean | 30 при потребности 14 |
| мёртвые настройки трейлинга | **found** | trailing_stop=False, но trailing_stop_positive=0.001 задан — читается как работающая защита |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **5m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `4a7c7414af9b` · strategy list `dac6309df791d209`*
