# MACDStrategyXRP

Source: [`MelvynClark/Freqtrade-Strategy`](https://github.com/MelvynClark/Freqtrade-Strategy) · file `MACDStrategy - XRP.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 1677 | 5779 |
| average profit per trade % | -0.4 | -0.02 |
| win rate % | 94.9 | 96.2 |
| average trade duration, minutes | 3361.0 | 3576.0 |
| duration measured in own candles | 672.2 | 715.2 |
| expectancy per trade (USDT) | -0.42 | -0.12 |
| mean profit p-value | 0.000823 | 0.2858 |
| market change % (baseline) | -58.23 | 346.34 |
| strategy total % | -70.45 | -67.49 |
| Sharpe | -3.59 | -0.66 |
| Sortino | -2.0 | -0.32 |
| max drawdown % | 72.37 | 84.48 |
| profit factor | 0.6 | 0.92 |

**Retained out of sample: negative**

> **Read that number with care.** The author's window was a bear market (buy-and-hold −58%) and the out-of-sample window a bull market (+346%). For a long-biased strategy this ratio rewards having done *badly* in 2018–2020, so it measures regime luck as much as robustness. The regime-free comparison is the excess over buy-and-hold, below.

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free either. Cross-strategy comparisons in this repository use average profit per trade in percent.

**Excess over buy-and-hold** (regime-free): author's window **-12.2 pp**, out of sample **-413.8 pp**.

Baseline: buy-and-hold on the same pairs returned **-58.23%**; the strategy returned **-70.45%**.
Out of sample: buy-and-hold **346.34%** vs strategy **-67.49%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | clean | смещения не обнаружено |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | freqtrade ОТКАЗАЛСЯ анализировать: startup_candle_count=0, «приведёт к рекурсивным проблемам у части индикаторов» |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **5m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `590bf74986c5` · strategy list `a039f448c17bed72`*
