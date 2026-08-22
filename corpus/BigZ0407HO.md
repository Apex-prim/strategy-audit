# BigZ0407HO

Source: [`davidzr/freqtrade-strategies`](https://github.com/davidzr/freqtrade-strategies) · file `BigZ0407HO.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 299 | 823 |
| average profit per trade % | -0.69 | 0.49 |
| win rate % | 73.2 | 80.6 |
| average trade duration, minutes | 464.0 | 272.0 |
| duration measured in own candles | 92.8 | 54.4 |
| expectancy per trade (USDT) | -0.78 | 0.76 |
| mean profit p-value | 0.001979 | 0.0003268 |
| market change % (baseline) | -59.05 | 346.34 |
| strategy total % | -23.23 | 62.87 |
| Sharpe | -1.41 | 0.84 |
| Sortino | -1.34 | 0.6 |
| max drawdown % | 26.14 | 15.73 |
| profit factor | 0.56 | 1.51 |

**Retained out of sample: n/a**

> **Read that number with care.** The author's window was a bear market (buy-and-hold −58%) and the out-of-sample window a bull market (+346%). For a long-biased strategy this ratio rewards having done *badly* in 2018–2020, so it measures regime luck as much as robustness. The regime-free comparison is the excess over buy-and-hold, below.

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free either. Cross-strategy comparisons in this repository use average profit per trade in percent.

**Excess over buy-and-hold** (regime-free): author's window **+35.8 pp**, out of sample **-283.5 pp**.

Baseline: buy-and-hold on the same pairs returned **-59.05%**; the strategy returned **-23.23%**.
Out of sample: buy-and-hold **346.34%** vs strategy **62.87%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | clean | смещения не обнаружено |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | индикаторы меняются от объёма истории: bb_lowerband_1h 3.629%, bb_middleband_1h 3.126%, bb_upperband_1h 2.629%, ema_100_1h -0.014%, ewo -12.317% |
| прогрев не объявлен | **found** | самый длинный индикатор 200 свечей, startup_candle_count не задан (по умолчанию 0) |
| мёртвые настройки трейлинга | **found** | trailing_stop=False, но trailing_stop_positive=0.01 задан — читается как работающая защита |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **5m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `590bf74986c5` · strategy list `a039f448c17bed72`*
