# SimpleHopt1Along

Source: [`MelvynClark/Freqtrade-Strategy`](https://github.com/MelvynClark/Freqtrade-Strategy) · file `SimpleHopt1Along.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 973 | 3494 |
| average profit per trade % | -0.63 | -0.28 |
| win rate % | 93.1 | 94.4 |
| average trade duration, minutes | 2858.0 | 3340.0 |
| duration measured in own candles | 11.91 | 13.92 |
| expectancy per trade (USDT) | -0.59 | -0.22 |
| mean profit p-value | 0.0007537 | 0.02557 |
| market change % (baseline) | -57.43 | 340.8 |
| strategy total % | -57.67 | -78.22 |
| Sharpe | -2.76 | -1.07 |
| Sortino | -1.98 | -0.46 |
| max drawdown % | 64.02 | 86.97 |
| profit factor | 0.55 | 0.8 |

**Retained out of sample: negative**

> **Read that number with care.** The author's window was a bear market (buy-and-hold −58%) and the out-of-sample window a bull market (+346%). For a long-biased strategy this ratio rewards having done *badly* in 2018–2020, so it measures regime luck as much as robustness. The regime-free comparison is the excess over buy-and-hold, below.

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free either. Cross-strategy comparisons in this repository use average profit per trade in percent.

**Excess over buy-and-hold** (regime-free): author's window **-0.2 pp**, out of sample **-419.0 pp**.

Baseline: buy-and-hold on the same pairs returned **-57.43%**; the strategy returned **-57.67%**.
Out of sample: buy-and-hold **340.8%** vs strategy **-78.22%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | clean | смещения не обнаружено |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | freqtrade ОТКАЗАЛСЯ анализировать: startup_candle_count=0, «приведёт к рекурсивным проблемам у части индикаторов» |
| прогрев не объявлен | **found** | самый длинный индикатор 12 свечей, startup_candle_count не задан (по умолчанию 0) |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **4h** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `590bf74986c5` · strategy list `a039f448c17bed72`*
