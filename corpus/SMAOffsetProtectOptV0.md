# SMAOffsetProtectOptV0

Source: [`PeetCrypto/freqtrade-stuff`](https://github.com/PeetCrypto/freqtrade-stuff) · file `SMAOffsetProtectOptV0.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 33 | 220 |
| expectancy per trade (USDT) | 0.42 | 1.65 |
| mean profit p-value | 0.3107 | 0.0001304 |
| market change % (baseline) | -58.37 | 346.34 |
| strategy total % | 1.38 | 36.35 |
| Sharpe | 0.16 | 0.47 |
| Sortino | 0.15 | 0.26 |
| max drawdown % | 0.74 | 4.15 |
| profit factor | 1.65 | 3.68 |

**Retained out of sample: 393%**

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free. Cross-strategy comparisons in this repository use average profit per trade in percent.

⚠ **Not statistically significant in its author's own window** (p = 0.3107 > 0.05): the average trade is not distinguishable from zero.

Baseline: buy-and-hold on the same pairs returned **-58.37%**; the strategy returned **1.38%**.
Out of sample: buy-and-hold **346.34%** vs strategy **36.35%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | could not run | вывод не разобран |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | индикаторы меняются от объёма истории: ma_sell_24 -0.012%, rsi 0.935% |
| прогрев занижен | **found** | объявлено 30, нужно не менее 200 |
| мёртвые настройки трейлинга | **found** | trailing_stop=False, но trailing_stop_positive=0.001 задан — читается как работающая защита |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **5m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `4a7c7414af9b` · strategy list `dac6309df791d209`*
