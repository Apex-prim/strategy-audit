# Nostalgia

Source: [`PeetCrypto/freqtrade-stuff`](https://github.com/PeetCrypto/freqtrade-stuff) · file `Nostalgia.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 225 | 609 |
| expectancy per trade (USDT) | -0.04 | 1.76 |
| mean profit p-value | 0.901 | 2.66e-11 |
| market change % (baseline) | -58.96 | 346.34 |
| strategy total % | -0.91 | 107.43 |
| Sharpe | -0.05 | 1.36 |
| Sortino | -0.04 | 1.04 |
| max drawdown % | 9.35 | 5.07 |
| profit factor | 0.97 | 2.36 |

**Retained out of sample: n/a**

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free. Cross-strategy comparisons in this repository use average profit per trade in percent.

⚠ **Not statistically significant in its author's own window** (p = 0.901 > 0.05): the average trade is not distinguishable from zero.

Baseline: buy-and-hold on the same pairs returned **-58.96%**; the strategy returned **-0.91%**.
Out of sample: buy-and-hold **346.34%** vs strategy **107.43%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | could not run | вывод не разобран |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | индикаторы меняются от объёма истории: ema_100_1h -0.014%, ewo -12.317%, stochrsi_fastd_96 -0.557% |
| прогрев не объявлен | **found** | самый длинный индикатор 200 свечей, startup_candle_count не задан (по умолчанию 0) |
| мёртвые настройки трейлинга | **found** | trailing_stop=False, но trailing_stop_positive=0.01 задан — читается как работающая защита |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **5m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `4a7c7414af9b` · strategy list `dac6309df791d209`*
