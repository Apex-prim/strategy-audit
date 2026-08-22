# ultratank

Source: [`jaredrsommer/freqtradestrategies`](https://github.com/jaredrsommer/freqtradestrategies) · file `ultratank (copy).py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 685 | 2391 |
| average profit per trade % | -1.04 | -0.35 |
| win rate % | 81.6 | 83.6 |
| average trade duration, minutes | 6133.0 | 6577.0 |
| duration measured in own candles | 102.22 | 109.62 |
| expectancy per trade (USDT) | -0.98 | -0.33 |
| mean profit p-value | 0.0002407 | 0.06706 |
| market change % (baseline) | -59.27 | 348.67 |
| strategy total % | -67.34 | -79.38 |
| Sharpe | -2.53 | -0.72 |
| Sortino | -2.04 | -0.45 |
| max drawdown % | 67.34 | 88.42 |
| profit factor | 0.6 | 0.86 |

**Retained out of sample: negative**

> **Read that number with care.** The author's window was a bear market (buy-and-hold −58%) and the out-of-sample window a bull market (+346%). For a long-biased strategy this ratio rewards having done *badly* in 2018–2020, so it measures regime luck as much as robustness. The regime-free comparison is the excess over buy-and-hold, below.

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free either. Cross-strategy comparisons in this repository use average profit per trade in percent.

**Excess over buy-and-hold** (regime-free): author's window **-8.1 pp**, out of sample **-428.1 pp**.

Baseline: buy-and-hold on the same pairs returned **-59.27%**; the strategy returned **-67.34%**.
Out of sample: buy-and-hold **348.67%** vs strategy **-79.38%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | clean | смещения не обнаружено |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | индикаторы меняются от объёма истории: rsi 4.044%, rsi_ma 5.719%, wave_t1 42.943%, wave_t2 43.460% |
| прогрев не объявлен | **found** | самый длинный индикатор 200 свечей, startup_candle_count не задан (по умолчанию 0) |
| трейлинг на полном стопе | **found** | trailing_stop=True без trailing_stop_positive ⇒ стоп тащится на ВСЁ расстояние стоп-лосса |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **1h** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `590bf74986c5` · strategy list `a039f448c17bed72`*
