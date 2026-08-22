# TouchEmaDelayStrategy

Source: [`flaviosiotto/freqtrade-strategy`](https://github.com/flaviosiotto/freqtrade-strategy) · file `touchemadelay-strategy.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 474 | 1857 |
| average profit per trade % | -0.86 | -0.38 |
| win rate % | 65.2 | 65.1 |
| average trade duration, minutes | 809.0 | 746.0 |
| duration measured in own candles | 269.67 | 248.67 |
| expectancy per trade (USDT) | -0.85 | -0.32 |
| mean profit p-value | 4.91e-08 | 3.666e-08 |
| market change % (baseline) | -55.61 | 347.44 |
| strategy total % | -40.35 | -58.9 |
| Sharpe | -3.16 | -1.93 |
| Sortino | -2.3 | -1.35 |
| max drawdown % | 41.17 | 59.01 |
| profit factor | 0.28 | 0.51 |

**Retained out of sample: negative**

> **Read that number with care.** The author's window was a bear market (buy-and-hold −58%) and the out-of-sample window a bull market (+346%). For a long-biased strategy this ratio rewards having done *badly* in 2018–2020, so it measures regime luck as much as robustness. The regime-free comparison is the excess over buy-and-hold, below.

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free either. Cross-strategy comparisons in this repository use average profit per trade in percent.

**Excess over buy-and-hold** (regime-free): author's window **+15.3 pp**, out of sample **-406.3 pp**.

Baseline: buy-and-hold on the same pairs returned **-55.61%**; the strategy returned **-40.35%**.
Out of sample: buy-and-hold **347.44%** vs strategy **-58.9%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | clean | смещения не обнаружено |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | freqtrade ОТКАЗАЛСЯ анализировать: startup_candle_count=0, «приведёт к рекурсивным проблемам у части индикаторов» |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **3m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `590bf74986c5` · strategy list `a039f448c17bed72`*
