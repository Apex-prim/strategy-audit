# wavetrend

Source: [`jaredrsommer/freqtradestrategies`](https://github.com/jaredrsommer/freqtradestrategies) · file `wavetrend.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 963 | 3728 |
| average profit per trade % | 0.53 | 1.08 |
| win rate % | 93.4 | 94.8 |
| average trade duration, minutes | 6166.0 | 5777.0 |
| duration measured in own candles | 102.77 | 96.28 |
| expectancy per trade (USDT) | -0.52 | 0.0 |
| mean profit p-value | 0.01773 | 0.9923 |
| market change % (baseline) | -59.27 | 348.67 |
| strategy total % | -49.89 | 0.65 |
| Sharpe | -1.93 | 0.0 |
| Sortino | -1.06 | 0.0 |
| max drawdown % | 55.83 | 63.38 |
| profit factor | 0.65 | 1.0 |

**Retained out of sample: n/a**

> **Read that number with care.** The author's window was a bear market (buy-and-hold −58%) and the out-of-sample window a bull market (+346%). For a long-biased strategy this ratio rewards having done *badly* in 2018–2020, so it measures regime luck as much as robustness. The regime-free comparison is the excess over buy-and-hold, below.

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free either. Cross-strategy comparisons in this repository use average profit per trade in percent.

**Excess over buy-and-hold** (regime-free): author's window **+9.4 pp**, out of sample **-348.0 pp**.

Baseline: buy-and-hold on the same pairs returned **-59.27%**; the strategy returned **-49.89%**.
Out of sample: buy-and-hold **348.67%** vs strategy **0.65%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | clean | смещения не обнаружено |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | индикаторы меняются от объёма истории: rsi 4.044%, rsi_ma 5.719%, d -3.198%, wave_ci 5.266% |
| прогрев не объявлен | **found** | самый длинный индикатор 200 свечей, startup_candle_count не задан (по умолчанию 0) |
| трейлинг на полном стопе | **found** | trailing_stop=True без trailing_stop_positive ⇒ стоп тащится на ВСЁ расстояние стоп-лосса |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **1h** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `590bf74986c5` · strategy list `a039f448c17bed72`*
