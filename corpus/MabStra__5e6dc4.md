# MabStra

Source: [`davidzr/freqtrade-strategies`](https://github.com/davidzr/freqtrade-strategies) · file `mabStra.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 916 | 3387 |
| average profit per trade % | -0.75 | -0.04 |
| win rate % | 52.6 | 55.8 |
| average trade duration, minutes | 6819.0 | 6779.0 |
| duration measured in own candles | 28.41 | 28.25 |
| expectancy per trade (USDT) | -0.77 | -0.22 |
| mean profit p-value | 0.0003712 | 0.3966 |
| market change % (baseline) | -57.43 | 340.8 |
| strategy total % | -70.85 | -75.67 |
| Sharpe | -2.83 | -0.4 |
| Sortino | -4.2 | -0.53 |
| max drawdown % | 76.8 | 93.14 |
| profit factor | 0.73 | 0.96 |

**Retained out of sample: negative**

> **Read that number with care.** The author's window was a bear market (buy-and-hold −58%) and the out-of-sample window a bull market (+346%). For a long-biased strategy this ratio rewards having done *badly* in 2018–2020, so it measures regime luck as much as robustness. The regime-free comparison is the excess over buy-and-hold, below.

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free either. Cross-strategy comparisons in this repository use average profit per trade in percent.

**Excess over buy-and-hold** (regime-free): author's window **-13.4 pp**, out of sample **-416.5 pp**.

Baseline: buy-and-hold on the same pairs returned **-57.43%**; the strategy returned **-70.85%**.
Out of sample: buy-and-hold **340.8%** vs strategy **-75.67%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | clean | смещения не обнаружено |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | freqtrade ОТКАЗАЛСЯ анализировать: startup_candle_count=0, «приведёт к рекурсивным проблемам у части индикаторов» |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **4h** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `590bf74986c5` · strategy list `a039f448c17bed72`*
