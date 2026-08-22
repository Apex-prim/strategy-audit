# DD

Source: [`davidzr/freqtrade-strategies`](https://github.com/davidzr/freqtrade-strategies) · file `DD.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 12209 | 19842 |
| average profit per trade % | -0.22 | -0.12 |
| win rate % | 55.8 | 60.0 |
| average trade duration, minutes | 186.0 | 181.0 |
| duration measured in own candles | 37.2 | 36.2 |
| expectancy per trade (USDT) | -0.08 | -0.05 |
| mean profit p-value | 2.994e-29 | 1.795e-09 |
| market change % (baseline) | -58.23 | 346.34 |
| strategy total % | -96.71 | -96.78 |
| Sharpe | -32.51 | -6.86 |
| Sortino | -26.04 | -4.92 |
| max drawdown % | 96.74 | 96.86 |
| profit factor | 0.59 | 0.79 |

**Retained out of sample: negative**

> **Read that number with care.** The author's window was a bear market (buy-and-hold −58%) and the out-of-sample window a bull market (+346%). For a long-biased strategy this ratio rewards having done *badly* in 2018–2020, so it measures regime luck as much as robustness. The regime-free comparison is the excess over buy-and-hold, below.

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free either. Cross-strategy comparisons in this repository use average profit per trade in percent.

**Excess over buy-and-hold** (regime-free): author's window **-38.5 pp**, out of sample **-443.1 pp**.

Baseline: buy-and-hold on the same pairs returned **-58.23%**; the strategy returned **-96.71%**.
Out of sample: buy-and-hold **346.34%** vs strategy **-96.78%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | clean | смещения не обнаружено |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | freqtrade ОТКАЗАЛСЯ анализировать: startup_candle_count=0, «приведёт к рекурсивным проблемам у части индикаторов» |
| прогрев не объявлен | **found** | самый длинный индикатор 20 свечей, startup_candle_count не задан (по умолчанию 0) |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **5m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `590bf74986c5` · strategy list `a039f448c17bed72`*
