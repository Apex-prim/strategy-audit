# KAMACCIRSI_new

Source: [`werkkrew/freqtrade-strategies`](https://github.com/werkkrew/freqtrade-strategies) · file `KAMACCIRSI.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 68 | 121 |
| average profit per trade % | -0.26 | -0.01 |
| win rate % | 55.9 | 57.9 |
| average trade duration, minutes | 257.0 | 258.0 |
| duration measured in own candles | 51.4 | 51.6 |
| expectancy per trade (USDT) | -0.32 | -0.02 |
| mean profit p-value | 0.3937 | 0.9342 |
| market change % (baseline) | -58.42 | 346.34 |
| strategy total % | -2.18 | -0.26 |
| Sharpe | -0.19 | -0.01 |
| Sortino | -0.19 | -0.01 |
| max drawdown % | 3.25 | 3.66 |
| profit factor | 0.71 | 0.98 |

**Retained out of sample: negative**

> **Read that number with care.** The author's window was a bear market (buy-and-hold −58%) and the out-of-sample window a bull market (+346%). For a long-biased strategy this ratio rewards having done *badly* in 2018–2020, so it measures regime luck as much as robustness. The regime-free comparison is the excess over buy-and-hold, below.

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free either. Cross-strategy comparisons in this repository use average profit per trade in percent.

**Excess over buy-and-hold** (regime-free): author's window **+56.2 pp**, out of sample **-346.6 pp**.

⚠ **Not statistically significant in its author's own window** (p = 0.3937 > 0.05): the average trade is not distinguishable from zero.

Baseline: buy-and-hold on the same pairs returned **-58.42%**; the strategy returned **-2.18%**.
Out of sample: buy-and-hold **346.34%** vs strategy **-0.26%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | clean | смещения не обнаружено |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | индикаторы меняются от объёма истории: rsi 0.110% |
| прогрев не объявлен | **found** | самый длинный индикатор 21 свечей, startup_candle_count не задан (по умолчанию 0) |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **5m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `590bf74986c5` · strategy list `a039f448c17bed72`*
