# BigZ04

Source: [`PeetCrypto/freqtrade-stuff`](https://github.com/PeetCrypto/freqtrade-stuff) · file `BigZ04.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 359 | 954 |
| average profit per trade % | -0.33 | 0.42 |
| win rate % | 88.6 | 90.9 |
| average trade duration, minutes | 2216.0 | 1251.0 |
| duration measured in own candles | 443.2 | 250.2 |
| expectancy per trade (USDT) | -0.42 | 0.66 |
| mean profit p-value | 0.1788 | 0.003521 |
| market change % (baseline) | -59.05 | 346.34 |
| strategy total % | -14.96 | 62.59 |
| Sharpe | -0.67 | 0.73 |
| Sortino | -0.45 | 0.41 |
| max drawdown % | 23.49 | 18.95 |
| profit factor | 0.75 | 1.42 |

**Retained out of sample: n/a**

> **Read that number with care.** The author's window was a bear market (buy-and-hold −58%) and the out-of-sample window a bull market (+346%). For a long-biased strategy this ratio rewards having done *badly* in 2018–2020, so it measures regime luck as much as robustness. The regime-free comparison is the excess over buy-and-hold, below.

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free either. Cross-strategy comparisons in this repository use average profit per trade in percent.

**Excess over buy-and-hold** (regime-free): author's window **+44.1 pp**, out of sample **-283.8 pp**.

⚠ **Not statistically significant in its author's own window** (p = 0.1788 > 0.05): the average trade is not distinguishable from zero.

Baseline: buy-and-hold on the same pairs returned **-59.05%**; the strategy returned **-14.96%**.
Out of sample: buy-and-hold **346.34%** vs strategy **62.59%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | could not run | вывод не разобран |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | индикаторы меняются от объёма истории: bb_lowerband_1h 3.629%, bb_middleband_1h 3.126%, bb_upperband_1h 2.629% |
| прогрев не объявлен | **found** | самый длинный индикатор 200 свечей, startup_candle_count не задан (по умолчанию 0) |
| мёртвые настройки трейлинга | **found** | trailing_stop=False, но trailing_stop_positive=0.01 задан — читается как работающая защита |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **5m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `590bf74986c5` · strategy list `a039f448c17bed72`*
