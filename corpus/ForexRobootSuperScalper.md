# ForexRobootSuperScalper

Source: [`jaredrsommer/freqtradestrategies`](https://github.com/jaredrsommer/freqtradestrategies) · file `ForexRobootSuperScalper (2).py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 11876 | 14747 |
| average profit per trade % | -0.22 | -0.18 |
| win rate % | 71.2 | 74.6 |
| average trade duration, minutes | 160.0 | 135.0 |
| duration measured in own candles | 32.0 | 27.0 |
| expectancy per trade (USDT) | -0.08 | -0.07 |
| mean profit p-value | 1.451e-30 | 1.862e-24 |
| market change % (baseline) | -58.23 | 346.34 |
| strategy total % | -96.57 | -96.6 |
| Sharpe | -32.82 | -10.04 |
| Sortino | -23.82 | -6.77 |
| max drawdown % | 96.59 | 96.61 |
| profit factor | 0.64 | 0.67 |

**Retained out of sample: negative**

> **Read that number with care.** The author's window was a bear market (buy-and-hold −58%) and the out-of-sample window a bull market (+346%). For a long-biased strategy this ratio rewards having done *badly* in 2018–2020, so it measures regime luck as much as robustness. The regime-free comparison is the excess over buy-and-hold, below.

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free either. Cross-strategy comparisons in this repository use average profit per trade in percent.

**Excess over buy-and-hold** (regime-free): author's window **-38.3 pp**, out of sample **-442.9 pp**.

Baseline: buy-and-hold on the same pairs returned **-58.23%**; the strategy returned **-96.57%**.
Out of sample: buy-and-hold **346.34%** vs strategy **-96.6%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | clean | смещения не обнаружено |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | freqtrade ОТКАЗАЛСЯ анализировать: startup_candle_count=0, «приведёт к рекурсивным проблемам у части индикаторов» |
| прогрев не объявлен | **found** | самый длинный индикатор 20 свечей, startup_candle_count не задан (по умолчанию 0) |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **5m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `590bf74986c5` · strategy list `a039f448c17bed72`*
