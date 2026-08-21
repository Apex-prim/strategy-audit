# ClucHAnix_hhll

Source: [`PeetCrypto/freqtrade-stuff`](https://github.com/PeetCrypto/freqtrade-stuff) · file `ClucHAnix_hhll (1).py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 467 | 1811 |
| expectancy per trade (USDT) | 0.32 | 0.48 |
| mean profit p-value | 0.02267 | 1.5e-06 |
| market change % (baseline) | -59.11 | 346.34 |
| strategy total % | 15.0 | 87.57 |
| Sharpe | 1.29 | 1.66 |
| Sortino | 1.12 | 1.44 |
| max drawdown % | 6.35 | 7.09 |
| profit factor | 1.39 | 1.51 |

**Retained out of sample: 150%**

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free. Cross-strategy comparisons in this repository use average profit per trade in percent.

Baseline: buy-and-hold on the same pairs returned **-59.11%**; the strategy returned **15.0%**.
Out of sample: buy-and-hold **346.34%** vs strategy **87.57%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | could not run | вывод не разобран |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | индикаторы меняются от объёма истории: rsi_slow 0.011%, ema_vwma_osc_32 -80.889%, ema_vwma_osc_64 22713.917%, ema_vwma_osc_96 901243.252% |
| прогрев занижен | **found** | объявлено 168, нужно не менее 200 |
| мёртвые настройки трейлинга | **found** | trailing_stop=False, но trailing_stop_positive=0.001 задан — читается как работающая защита |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **5m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `4a7c7414af9b` · strategy list `dac6309df791d209`*
