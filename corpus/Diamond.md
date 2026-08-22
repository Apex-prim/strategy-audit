# Diamond

Source: [`TheoBrigitte/freqtrade`](https://github.com/TheoBrigitte/freqtrade) · file `Diamond.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 1084 | 3519 |
| average profit per trade % | -0.52 | -0.16 |
| win rate % | 66.0 | 69.6 |
| average trade duration, minutes | 1690.0 | 1737.0 |
| duration measured in own candles | 338.0 | 347.4 |
| expectancy per trade (USDT) | -0.49 | -0.16 |
| mean profit p-value | 0.0004721 | 0.03004 |
| market change % (baseline) | -58.23 | 346.34 |
| strategy total % | -52.79 | -54.75 |
| Sharpe | -3.02 | -1.04 |
| Sortino | -1.87 | -0.61 |
| max drawdown % | 53.42 | 63.41 |
| profit factor | 0.41 | 0.74 |

**Retained out of sample: negative**

> **Read that number with care.** The author's window was a bear market (buy-and-hold −58%) and the out-of-sample window a bull market (+346%). For a long-biased strategy this ratio rewards having done *badly* in 2018–2020, so it measures regime luck as much as robustness. The regime-free comparison is the excess over buy-and-hold, below.

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free either. Cross-strategy comparisons in this repository use average profit per trade in percent.

**Excess over buy-and-hold** (regime-free): author's window **+5.4 pp**, out of sample **-401.1 pp**.

Baseline: buy-and-hold on the same pairs returned **-58.23%**; the strategy returned **-52.79%**.
Out of sample: buy-and-hold **346.34%** vs strategy **-54.75%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | clean | смещения не обнаружено |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | freqtrade ОТКАЗАЛСЯ анализировать: startup_candle_count=0, «приведёт к рекурсивным проблемам у части индикаторов» |
| прогрев не объявлен | **found** | самый длинный индикатор 18 свечей, startup_candle_count не задан (по умолчанию 0) |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **5m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `590bf74986c5` · strategy list `a039f448c17bed72`*
