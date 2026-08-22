# BollingerBandStrategy

Source: [`flaviosiotto/freqtrade-strategy`](https://github.com/flaviosiotto/freqtrade-strategy) · file `bollingerbands-strategy.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 4239 | 12063 |
| average profit per trade % | -0.29 | -0.22 |
| win rate % | 63.5 | 64.0 |
| average trade duration, minutes | 294.0 | 375.0 |
| duration measured in own candles | 98.0 | 125.0 |
| expectancy per trade (USDT) | -0.19 | -0.08 |
| mean profit p-value | 6.521e-19 | 3.654e-19 |
| market change % (baseline) | -55.61 | 347.44 |
| strategy total % | -79.36 | -96.58 |
| Sharpe | -15.19 | -7.96 |
| Sortino | -9.59 | -4.98 |
| max drawdown % | 79.37 | 96.58 |
| profit factor | 0.24 | 0.41 |

**Retained out of sample: negative**

> **Read that number with care.** The author's window was a bear market (buy-and-hold −58%) and the out-of-sample window a bull market (+346%). For a long-biased strategy this ratio rewards having done *badly* in 2018–2020, so it measures regime luck as much as robustness. The regime-free comparison is the excess over buy-and-hold, below.

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free either. Cross-strategy comparisons in this repository use average profit per trade in percent.

**Excess over buy-and-hold** (regime-free): author's window **-23.8 pp**, out of sample **-444.0 pp**.

Baseline: buy-and-hold on the same pairs returned **-55.61%**; the strategy returned **-79.36%**.
Out of sample: buy-and-hold **347.44%** vs strategy **-96.58%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | clean | смещения не обнаружено |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | freqtrade ОТКАЗАЛСЯ анализировать: startup_candle_count=0, «приведёт к рекурсивным проблемам у части индикаторов» |
| прогрев не объявлен | **found** | самый длинный индикатор 21 свечей, startup_candle_count не задан (по умолчанию 0) |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **3m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `590bf74986c5` · strategy list `a039f448c17bed72`*
