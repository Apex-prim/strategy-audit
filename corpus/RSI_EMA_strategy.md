# RSI_EMA_strategy

Source: [`mlsys-io/PortfolioBench`](https://github.com/mlsys-io/PortfolioBench) · file `RSI_EMA_strategy.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 1323 | 3917 |
| average profit per trade % | -0.29 | -0.27 |
| win rate % | 84.2 | 84.7 |
| average trade duration, minutes | 359.0 | 369.0 |
| duration measured in own candles | 71.8 | 73.8 |
| expectancy per trade (USDT) | -0.29 | -0.19 |
| mean profit p-value | 8.837e-08 | 8.146e-14 |
| market change % (baseline) | -58.23 | 346.34 |
| strategy total % | -38.33 | -74.15 |
| Sharpe | -5.12 | -3.79 |
| Sortino | -7.85 | -4.51 |
| max drawdown % | 40.26 | 74.86 |
| profit factor | 0.59 | 0.6 |

**Retained out of sample: negative**

> **Read that number with care.** The author's window was a bear market (buy-and-hold −58%) and the out-of-sample window a bull market (+346%). For a long-biased strategy this ratio rewards having done *badly* in 2018–2020, so it measures regime luck as much as robustness. The regime-free comparison is the excess over buy-and-hold, below.

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free either. Cross-strategy comparisons in this repository use average profit per trade in percent.

**Excess over buy-and-hold** (regime-free): author's window **+19.9 pp**, out of sample **-420.5 pp**.

Baseline: buy-and-hold on the same pairs returned **-58.23%**; the strategy returned **-38.33%**.
Out of sample: buy-and-hold **346.34%** vs strategy **-74.15%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | clean | смещения не обнаружено |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | freqtrade ОТКАЗАЛСЯ анализировать: startup_candle_count=0, «приведёт к рекурсивным проблемам у части индикаторов» |
| прогрев не объявлен | **found** | самый длинный индикатор 14 свечей, startup_candle_count не задан (по умолчанию 0) |
| minimal_roi закомментирован | **found** | правила выхода по прибыли берутся из неопубликованного конфига |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **5m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `590bf74986c5` · strategy list `a039f448c17bed72`*
