# SmartMoneyStrategy

Source: [`mikedigriz/freqtrade-strategy-mikedigriz`](https://github.com/mikedigriz/freqtrade-strategy-mikedigriz) · file `smart_money_strategy.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 23 | 262 |
| average profit per trade % | -16.26 | 3.65 |
| win rate % | 69.6 | 97.3 |
| average trade duration, minutes | 277979.0 | 85741.0 |
| duration measured in own candles | 9265.97 | 2858.03 |
| expectancy per trade (USDT) | -20.68 | 7.39 |
| mean profit p-value | 0.03823 | 0.1117 |
| market change % (baseline) | -57.83 | 343.26 |
| strategy total % | -47.56 | 193.69 |
| Sharpe | -0.28 | 0.21 |
| Sortino | -0.52 | 0.25 |
| max drawdown % | 52.86 | 49.24 |
| profit factor | 0.19 | 1.68 |

**Retained out of sample: n/a**

> **Read that number with care.** The author's window was a bear market (buy-and-hold −58%) and the out-of-sample window a bull market (+346%). For a long-biased strategy this ratio rewards having done *badly* in 2018–2020, so it measures regime luck as much as robustness. The regime-free comparison is the excess over buy-and-hold, below.

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free either. Cross-strategy comparisons in this repository use average profit per trade in percent.

**Excess over buy-and-hold** (regime-free): author's window **+10.3 pp**, out of sample **-149.6 pp**.

Baseline: buy-and-hold on the same pairs returned **-57.83%**; the strategy returned **-47.56%**.
Out of sample: buy-and-hold **343.26%** vs strategy **193.69%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | clean | смещения не обнаружено |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | freqtrade ОТКАЗАЛСЯ анализировать: startup_candle_count=0, «приведёт к рекурсивным проблемам у части индикаторов» |
| прогрев не объявлен | **found** | самый длинный индикатор 200 свечей, startup_candle_count не задан (по умолчанию 0) |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **30m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `590bf74986c5` · strategy list `a039f448c17bed72`*
