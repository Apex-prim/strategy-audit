# NFI5MOHO_WIP

Source: [`PeetCrypto/freqtrade-stuff`](https://github.com/PeetCrypto/freqtrade-stuff) · file `NFI5MOHO_WIP.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 209 | 742 |
| expectancy per trade (USDT) | 0.47 | 3.77 |
| mean profit p-value | 0.07274 | 4.696e-27 |
| market change % (baseline) | -59.35 | 346.34 |
| strategy total % | 9.89 | 279.93 |
| Sharpe | 0.68 | 2.47 |
| Sortino | 0.46 | 1.76 |
| max drawdown % | 6.48 | 4.89 |
| profit factor | 1.49 | 4.36 |

**Retained out of sample: 802%**

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free. Cross-strategy comparisons in this repository use average profit per trade in percent.

⚠ **Not statistically significant in its author's own window** (p = 0.07274 > 0.05): the average trade is not distinguishable from zero.

Baseline: buy-and-hold on the same pairs returned **-59.35%**; the strategy returned **9.89%**.
Out of sample: buy-and-hold **346.34%** vs strategy **279.93%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | could not run | вывод не разобран |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | индикаторы меняются от объёма истории: ema_100_1h -0.014%, ewo -12.317% |
| прогрев не объявлен | **found** | самый длинный индикатор 200 свечей, startup_candle_count не задан (по умолчанию 0) |
| мёртвые настройки трейлинга | **found** | trailing_stop=False, но trailing_stop_positive=0.01 задан — читается как работающая защита |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **5m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `4a7c7414af9b` · strategy list `dac6309df791d209`*
