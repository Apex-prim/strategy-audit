# NostalgiaForInfinityNextGen

Source: [`PeetCrypto/freqtrade-stuff`](https://github.com/PeetCrypto/freqtrade-stuff) · file `NostalgiaForInfinityNextGen.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 26 | 132 |
| expectancy per trade (USDT) | 1.82 | 2.07 |
| mean profit p-value | 0.01923 | 0.00124 |
| market change % (baseline) | -59.37 | 345.85 |
| strategy total % | 4.73 | 27.34 |
| Sharpe | 0.34 | 0.31 |
| Sortino | 1.21 | 0.22 |
| max drawdown % | 1.04 | 5.44 |
| profit factor | 3.41 | 2.31 |

**Retained out of sample: 114%**

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free. Cross-strategy comparisons in this repository use average profit per trade in percent.

Baseline: buy-and-hold on the same pairs returned **-59.37%**; the strategy returned **4.73%**.
Out of sample: buy-and-hold **345.85%** vs strategy **27.34%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | could not run | вывод не разобран |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | индикаторы меняются от объёма истории: ema_100_1h -0.014%, ema_100 0.019%, ema_200 0.123%, ema_vwma_osc_32 59.436%, ema_vwma_osc_64 1276.906% |
| прогрев не объявлен | **found** | самый длинный индикатор 200 свечей, startup_candle_count не задан (по умолчанию 0) |
| мёртвые настройки трейлинга | **found** | trailing_stop=False, но trailing_stop_positive=0.01 задан — читается как работающая защита |
| признак утечки будущего | **found** | центрированное окно center=True |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **15m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `4a7c7414af9b` · strategy list `dac6309df791d209`*
