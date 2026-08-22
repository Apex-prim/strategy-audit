# Freqtrade_backtest_validation_freqtrade1

Source: [`TheoBrigitte/freqtrade`](https://github.com/TheoBrigitte/freqtrade) · file `Freqtrade_backtest_validation_freqtrade1.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 2128 | 8036 |
| average profit per trade % | 0.08 | 0.07 |
| win rate % | 30.8 | 33.3 |
| average trade duration, minutes | 1476.0 | 1496.0 |
| duration measured in own candles | 24.6 | 24.93 |
| expectancy per trade (USDT) | 0.04 | 0.01 |
| mean profit p-value | 0.7433 | 0.9594 |
| market change % (baseline) | -58.4 | 348.67 |
| strategy total % | 8.34 | 5.43 |
| Sharpe | 0.39 | 0.04 |
| Sortino | 1.03 | 0.08 |
| max drawdown % | 36.09 | 80.21 |
| profit factor | 1.03 | 1.0 |

**Retained out of sample: 25%**

> **Read that number with care.** The author's window was a bear market (buy-and-hold −58%) and the out-of-sample window a bull market (+346%). For a long-biased strategy this ratio rewards having done *badly* in 2018–2020, so it measures regime luck as much as robustness. The regime-free comparison is the excess over buy-and-hold, below.

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free either. Cross-strategy comparisons in this repository use average profit per trade in percent.

**Excess over buy-and-hold** (regime-free): author's window **+66.7 pp**, out of sample **-343.2 pp**.

⚠ **Not statistically significant in its author's own window** (p = 0.7433 > 0.05): the average trade is not distinguishable from zero.

Baseline: buy-and-hold on the same pairs returned **-58.4%**; the strategy returned **8.34%**.
Out of sample: buy-and-hold **348.67%** vs strategy **5.43%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | clean | смещения не обнаружено |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | freqtrade ОТКАЗАЛСЯ анализировать: startup_candle_count=0, «приведёт к рекурсивным проблемам у части индикаторов» |
| прогрев не объявлен | **found** | самый длинный индикатор 28 свечей, startup_candle_count не задан (по умолчанию 0) |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **1h** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `590bf74986c5` · strategy list `a039f448c17bed72`*
