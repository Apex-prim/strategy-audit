# RSIDirectionalWithTrend

Source: [`paulcpk/freqtrade-strategies-that-work`](https://github.com/paulcpk/freqtrade-strategies-that-work) · file `RSIDirectionalWithTrend.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 167 | 697 |
| average profit per trade % | 0.34 | -0.07 |
| win rate % | 40.1 | 36.9 |
| average trade duration, minutes | 831.0 | 849.0 |
| duration measured in own candles | 13.85 | 14.15 |
| expectancy per trade (USDT) | 0.42 | -0.09 |
| mean profit p-value | 0.2377 | 0.5562 |
| market change % (baseline) | -58.4 | 348.67 |
| strategy total % | 7.01 | -6.19 |
| Sharpe | 0.4 | -0.13 |
| Sortino | 0.84 | -0.24 |
| max drawdown % | 7.12 | 11.14 |
| profit factor | 1.26 | 0.94 |

**Retained out of sample: negative**

> **Read that number with care.** The author's window was a bear market (buy-and-hold −58%) and the out-of-sample window a bull market (+346%). For a long-biased strategy this ratio rewards having done *badly* in 2018–2020, so it measures regime luck as much as robustness. The regime-free comparison is the excess over buy-and-hold, below.

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free either. Cross-strategy comparisons in this repository use average profit per trade in percent.

**Excess over buy-and-hold** (regime-free): author's window **+65.4 pp**, out of sample **-354.9 pp**.

⚠ **Not statistically significant in its author's own window** (p = 0.2377 > 0.05): the average trade is not distinguishable from zero.

Baseline: buy-and-hold on the same pairs returned **-58.4%**; the strategy returned **7.01%**.
Out of sample: buy-and-hold **348.67%** vs strategy **-6.19%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | clean | смещения не обнаружено |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | freqtrade ОТКАЗАЛСЯ анализировать: startup_candle_count=0, «приведёт к рекурсивным проблемам у части индикаторов» |
| прогрев не объявлен | **found** | самый длинный индикатор 100 свечей, startup_candle_count не задан (по умолчанию 0) |
| трейлинг на полном стопе | **found** | trailing_stop=True без trailing_stop_positive ⇒ стоп тащится на ВСЁ расстояние стоп-лосса |
| minimal_roi закомментирован | **found** | правила выхода по прибыли берутся из неопубликованного конфига |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **1h** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `590bf74986c5` · strategy list `—`*
