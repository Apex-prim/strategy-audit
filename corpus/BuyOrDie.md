# BuyOrDie

Source: [`mikedigriz/freqtrade-strategy-mikedigriz`](https://github.com/mikedigriz/freqtrade-strategy-mikedigriz) · file `BuyOrDie.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 911 | 2336 |
| average profit per trade % | -0.31 | 1.48 |
| win rate % | 3.7 | 4.9 |
| average trade duration, minutes | 7107.0 | 10160.0 |
| duration measured in own candles | 1421.4 | 2032.0 |
| expectancy per trade (USDT) | -0.59 | 0.62 |
| mean profit p-value | 0.004883 | 0.617 |
| market change % (baseline) | -58.23 | 346.34 |
| strategy total % | -53.64 | 143.79 |
| Sharpe | -2.23 | 0.2 |
| Sortino | -28.0 | 3.14 |
| max drawdown % | 72.75 | 78.29 |
| profit factor | 0.56 | 1.08 |

**Retained out of sample: n/a**

> **Read that number with care.** The author's window was a bear market (buy-and-hold −58%) and the out-of-sample window a bull market (+346%). For a long-biased strategy this ratio rewards having done *badly* in 2018–2020, so it measures regime luck as much as robustness. The regime-free comparison is the excess over buy-and-hold, below.

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free either. Cross-strategy comparisons in this repository use average profit per trade in percent.

**Excess over buy-and-hold** (regime-free): author's window **+4.6 pp**, out of sample **-202.5 pp**.

Baseline: buy-and-hold on the same pairs returned **-58.23%**; the strategy returned **-53.64%**.
Out of sample: buy-and-hold **346.34%** vs strategy **143.79%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | clean | смещения не обнаружено |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | freqtrade ОТКАЗАЛСЯ анализировать: startup_candle_count=0, «приведёт к рекурсивным проблемам у части индикаторов» |
| прогрев не объявлен | **found** | самый длинный индикатор 20 свечей, startup_candle_count не задан (по умолчанию 0) |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **5m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `590bf74986c5` · strategy list `a039f448c17bed72`*
