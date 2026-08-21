# NostalgiaForInfinityXw

Source: [`PeetCrypto/freqtrade-stuff`](https://github.com/PeetCrypto/freqtrade-stuff) · file `NostalgiaForInfinityXw (1).py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 29 | 155 |
| expectancy per trade (USDT) | 1.17 | 3.13 |
| mean profit p-value | 0.1418 | 3.174e-05 |
| market change % (baseline) | -58.96 | 346.34 |
| strategy total % | 3.4 | 48.45 |
| Sharpe | 0.22 | 0.43 |
| Sortino | 1.04 | 0.24 |
| max drawdown % | 1.38 | 4.27 |
| profit factor | 2.3 | 3.72 |

**Retained out of sample: 268%**

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free. Cross-strategy comparisons in this repository use average profit per trade in percent.

⚠ **Not statistically significant in its author's own window** (p = 0.1418 > 0.05): the average trade is not distinguishable from zero.

Baseline: buy-and-hold on the same pairs returned **-58.96%**; the strategy returned **3.4%**.
Out of sample: buy-and-hold **346.34%** vs strategy **48.45%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | could not run | вывод не разобран |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | индикаторы меняются от объёма истории: ema_100_1h -0.014%, ema_100_15m 0.019%, ema_vwma_osc_32 -11.624%, ema_vwma_osc_64 8410.479%, ema_vwma_osc_96 41 |
| прогрев не объявлен | **found** | самый длинный индикатор 200 свечей, startup_candle_count не задан (по умолчанию 0) |
| мёртвые настройки трейлинга | **found** | trailing_stop=False, но trailing_stop_positive=0.01 задан — читается как работающая защита |
| признак утечки будущего | **found** | центрированное окно center=True |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **5m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `4a7c7414af9b` · strategy list `dac6309df791d209`*
