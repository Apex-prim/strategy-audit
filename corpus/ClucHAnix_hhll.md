# ClucHAnix_hhll

Source: [`PeetCrypto/freqtrade-stuff`](https://github.com/PeetCrypto/freqtrade-stuff) · file `ClucHAnix_hhll (1).py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 467 | 1811 |
| average profit per trade % | 0.25 | 0.29 |
| win rate % | 57.8 | 53.1 |
| average trade duration, minutes | 103.0 | 59.0 |
| duration measured in own candles | 20.6 | 11.8 |
| expectancy per trade (USDT) | 0.32 | 0.48 |
| mean profit p-value | 0.02267 | 1.5e-06 |
| market change % (baseline) | -59.11 | 346.34 |
| strategy total % | 15.0 | 87.57 |
| Sharpe | 1.29 | 1.66 |
| Sortino | 1.12 | 1.44 |
| max drawdown % | 6.35 | 7.09 |
| profit factor | 1.39 | 1.51 |

**Retained out of sample: 150%**

> **Read that number with care.** The author's window was a bear market (buy-and-hold −58%) and the out-of-sample window a bull market (+346%). For a long-biased strategy this ratio rewards having done *badly* in 2018–2020, so it measures regime luck as much as robustness. The regime-free comparison is the excess over buy-and-hold, below.

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free either. Cross-strategy comparisons in this repository use average profit per trade in percent.

**Excess over buy-and-hold** (regime-free): author's window **+74.1 pp**, out of sample **-258.8 pp**.

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

*Code fingerprint `590bf74986c5` · strategy list `a039f448c17bed72`*
