# flawless_lambo

Source: [`davidzr/freqtrade-strategies`](https://github.com/davidzr/freqtrade-strategies) · file `flawless_lambo.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 959 | 3530 |
| average profit per trade % | -0.86 | -0.14 |
| win rate % | 59.4 | 63.9 |
| average trade duration, minutes | 3506.0 | 3215.0 |
| duration measured in own candles | 233.73 | 214.33 |
| expectancy per trade (USDT) | -0.72 | -0.17 |
| mean profit p-value | 1.449e-05 | 0.1239 |
| market change % (baseline) | -58.53 | 345.85 |
| strategy total % | -68.92 | -61.18 |
| Sharpe | -3.53 | -0.74 |
| Sortino | -2.98 | -0.59 |
| max drawdown % | 69.87 | 75.08 |
| profit factor | 0.61 | 0.91 |

**Retained out of sample: negative**

> **Read that number with care.** The author's window was a bear market (buy-and-hold −58%) and the out-of-sample window a bull market (+346%). For a long-biased strategy this ratio rewards having done *badly* in 2018–2020, so it measures regime luck as much as robustness. The regime-free comparison is the excess over buy-and-hold, below.

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free either. Cross-strategy comparisons in this repository use average profit per trade in percent.

**Excess over buy-and-hold** (regime-free): author's window **-10.4 pp**, out of sample **-407.0 pp**.

Baseline: buy-and-hold on the same pairs returned **-58.53%**; the strategy returned **-68.92%**.
Out of sample: buy-and-hold **345.85%** vs strategy **-61.18%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | clean | смещения не обнаружено |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | индикаторы меняются от объёма истории: OBV -100.795%, adx -6.761%, rsi -0.375% |
| прогрев не объявлен | **found** | самый длинный индикатор 20 свечей, startup_candle_count не задан (по умолчанию 0) |
| мёртвые настройки трейлинга | **found** | trailing_stop=False, но trailing_stop_positive=0.006 задан — читается как работающая защита |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **15m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `590bf74986c5` · strategy list `a039f448c17bed72`*
