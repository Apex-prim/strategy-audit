# SMAOffsetProtectOptV1Mod2

Source: [`PeetCrypto/freqtrade-stuff`](https://github.com/PeetCrypto/freqtrade-stuff) · file `SMAOffsetProtectOptV1Mod2_antipump (1).py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 27 | 179 |
| average profit per trade % | 1.14 | 1.0 |
| win rate % | 88.9 | 91.1 |
| average trade duration, minutes | 38.0 | 44.0 |
| duration measured in own candles | 7.6 | 8.8 |
| expectancy per trade (USDT) | 1.43 | 1.37 |
| mean profit p-value | 0.0002127 | 0.0002101 |
| market change % (baseline) | -59.05 | 346.34 |
| strategy total % | 3.86 | 24.51 |
| Sharpe | 0.6 | 0.41 |
| Sortino | 0.51 | 0.16 |
| max drawdown % | 0.46 | 4.61 |
| profit factor | 6.67 | 2.88 |

**Retained out of sample: 96%**

> **Read that number with care.** The author's window was a bear market (buy-and-hold −58%) and the out-of-sample window a bull market (+346%). For a long-biased strategy this ratio rewards having done *badly* in 2018–2020, so it measures regime luck as much as robustness. The regime-free comparison is the excess over buy-and-hold, below.

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free either. Cross-strategy comparisons in this repository use average profit per trade in percent.

**Excess over buy-and-hold** (regime-free): author's window **+62.9 pp**, out of sample **-321.8 pp**.

Baseline: buy-and-hold on the same pairs returned **-59.05%**; the strategy returned **3.86%**.
Out of sample: buy-and-hold **346.34%** vs strategy **24.51%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | could not run | вывод не разобран |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | индикаторы меняются от объёма истории: EWO -12.317% |
| прогрев не объявлен | **found** | самый длинный индикатор 14 свечей, startup_candle_count не задан (по умолчанию 0) |
| мёртвые настройки трейлинга | **found** | trailing_stop=False, но trailing_stop_positive=0.001 задан — читается как работающая защита |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **5m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `590bf74986c5` · strategy list `a039f448c17bed72`*
