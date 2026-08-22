# lambotest

Source: [`jaredrsommer/freqtradestrategies`](https://github.com/jaredrsommer/freqtradestrategies) · file `lambo_testing.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 6064 | 14050 |
| average profit per trade % | -0.23 | -0.18 |
| win rate % | 81.4 | 81.1 |
| average trade duration, minutes | 361.0 | 308.0 |
| duration measured in own candles | 72.2 | 61.6 |
| expectancy per trade (USDT) | -0.14 | -0.07 |
| mean profit p-value | 6.646e-14 | 6.331e-10 |
| market change % (baseline) | -58.41 | 346.34 |
| strategy total % | -82.84 | -96.57 |
| Sharpe | -15.31 | -5.93 |
| Sortino | -9.8 | -3.85 |
| max drawdown % | 82.93 | 96.63 |
| profit factor | 0.65 | 0.79 |

**Retained out of sample: negative**

> **Read that number with care.** The author's window was a bear market (buy-and-hold −58%) and the out-of-sample window a bull market (+346%). For a long-biased strategy this ratio rewards having done *badly* in 2018–2020, so it measures regime luck as much as robustness. The regime-free comparison is the excess over buy-and-hold, below.

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free either. Cross-strategy comparisons in this repository use average profit per trade in percent.

**Excess over buy-and-hold** (regime-free): author's window **-24.4 pp**, out of sample **-442.9 pp**.

Baseline: buy-and-hold on the same pairs returned **-58.41%**; the strategy returned **-82.84%**.
Out of sample: buy-and-hold **346.34%** vs strategy **-96.57%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | clean | смещения не обнаружено |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | индикаторы меняются от объёма истории: OBV -90.445%, rsi 12.447% |
| прогрев не объявлен | **found** | самый длинный индикатор 20 свечей, startup_candle_count не задан (по умолчанию 0) |
| мёртвые настройки трейлинга | **found** | trailing_stop=False, но trailing_stop_positive=0.0069 задан — читается как работающая защита |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **5m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `590bf74986c5` · strategy list `a039f448c17bed72`*
