# BigZ04_TSL4

Source: [`Foxel05/freqtrade-stuff`](https://github.com/Foxel05/freqtrade-stuff) · file `BigZ04_TSL4.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 479 | 1277 |
| average profit per trade % | -0.69 | -0.78 |
| win rate % | 68.5 | 58.6 |
| average trade duration, minutes | 771.0 | 1039.0 |
| duration measured in own candles | 154.2 | 207.8 |
| expectancy per trade (USDT) | -0.72 | -0.56 |
| mean profit p-value | 6.899e-05 | 2.162e-16 |
| market change % (baseline) | -59.23 | 346.34 |
| strategy total % | -34.67 | -71.49 |
| Sharpe | -2.31 | -2.41 |
| Sortino | -2.38 | -2.3 |
| max drawdown % | 39.93 | 72.01 |
| profit factor | 0.58 | 0.48 |

**Retained out of sample: negative**

> **Read that number with care.** The author's window was a bear market (buy-and-hold −58%) and the out-of-sample window a bull market (+346%). For a long-biased strategy this ratio rewards having done *badly* in 2018–2020, so it measures regime luck as much as robustness. The regime-free comparison is the excess over buy-and-hold, below.

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free either. Cross-strategy comparisons in this repository use average profit per trade in percent.

**Excess over buy-and-hold** (regime-free): author's window **+24.6 pp**, out of sample **-417.8 pp**.

Baseline: buy-and-hold on the same pairs returned **-59.23%**; the strategy returned **-34.67%**.
Out of sample: buy-and-hold **346.34%** vs strategy **-71.49%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | clean | смещения не обнаружено |
| indicator recursion (freqtrade's own `recursive-analysis`) | clean | рекурсивных отклонений не найдено |
| прогрев не объявлен | **found** | самый длинный индикатор 200 свечей, startup_candle_count не задан (по умолчанию 0) |
| мёртвые настройки трейлинга | **found** | trailing_stop=False, но trailing_stop_positive=0.01 задан — читается как работающая защита |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **5m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `590bf74986c5` · strategy list `a039f448c17bed72`*
