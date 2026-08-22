# ImpulseV1

Source: [`jaredrsommer/freqtradestrategies`](https://github.com/jaredrsommer/freqtradestrategies) · file `ImpulseV1.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 2091 | — |
| average profit per trade % | -0.36 | — |
| win rate % | 78.3 | — |
| average trade duration, minutes | 2939.0 | — |
| duration measured in own candles | 587.8 | — |
| expectancy per trade (USDT) | -0.36 | — |
| mean profit p-value | 0.0003757 | — |
| market change % (baseline) | -58.37 | — |
| strategy total % | -74.88 | — |
| Sharpe | -4.26 | — |
| Sortino | -2.17 | — |
| max drawdown % | 76.84 | — |
| profit factor | 0.55 | — |

**Retained out of sample: —**

> **Read that number with care.** The author's window was a bear market (buy-and-hold −58%) and the out-of-sample window a bull market (+346%). For a long-biased strategy this ratio rewards having done *badly* in 2018–2020, so it measures regime luck as much as robustness. The regime-free comparison is the excess over buy-and-hold, below.

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free either. Cross-strategy comparisons in this repository use average profit per trade in percent.

**Excess over buy-and-hold** (regime-free): author's window **-16.5 pp**.

Baseline: buy-and-hold on the same pairs returned **-58.37%**; the strategy returned **-74.88%**.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | clean | смещения не обнаружено |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | индикаторы меняются от объёма истории: ema1_23 -0.011% |
| прогрев не объявлен | **found** | самый длинный индикатор 200 свечей, startup_candle_count не задан (по умолчанию 0) |
| трейлинг на полном стопе | **found** | trailing_stop=True без trailing_stop_positive ⇒ стоп тащится на ВСЁ расстояние стоп-лосса |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **5m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `590bf74986c5` · strategy list `a039f448c17bed72`*
