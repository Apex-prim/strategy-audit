# SMAOffsetProtectOptV1Mod

Source: [`davidzr/freqtrade-strategies`](https://github.com/davidzr/freqtrade-strategies) · file `SMAOffsetProtectOptV1Mod.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 25 | 177 |
| average profit per trade % | 1.0 | 1.01 |
| win rate % | 84.0 | 91.0 |
| average trade duration, minutes | 44.0 | 46.0 |
| duration measured in own candles | 8.8 | 9.2 |
| expectancy per trade (USDT) | 1.25 | 1.39 |
| mean profit p-value | 0.002395 | 0.0001898 |
| market change % (baseline) | -58.37 | 346.34 |
| strategy total % | 3.12 | 24.66 |
| Sharpe | 0.45 | 0.41 |
| Sortino | 0.45 | 0.16 |
| max drawdown % | 0.46 | 4.61 |
| profit factor | 5.19 | 2.89 |

**Retained out of sample: 111%**

> **Read that number with care.** The author's window was a bear market (buy-and-hold −58%) and the out-of-sample window a bull market (+346%). For a long-biased strategy this ratio rewards having done *badly* in 2018–2020, so it measures regime luck as much as robustness. The regime-free comparison is the excess over buy-and-hold, below.

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free either. Cross-strategy comparisons in this repository use average profit per trade in percent.

**Excess over buy-and-hold** (regime-free): author's window **+61.5 pp**, out of sample **-321.7 pp**.

Baseline: buy-and-hold on the same pairs returned **-58.37%**; the strategy returned **3.12%**.
Out of sample: buy-and-hold **346.34%** vs strategy **24.66%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | could not run | вывод не разобран |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | индикаторы меняются от объёма истории: rsi 0.935% |
| прогрев не объявлен | **found** | самый длинный индикатор 14 свечей, startup_candle_count не задан (по умолчанию 0) |
| мёртвые настройки трейлинга | **found** | trailing_stop=False, но trailing_stop_positive=0.001 задан — читается как работающая защита |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **5m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `590bf74986c5` · strategy list `a039f448c17bed72`*
