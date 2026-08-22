# Uptrend

Source: [`PeetCrypto/freqtrade-stuff`](https://github.com/PeetCrypto/freqtrade-stuff) · file `Uptrend.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 74 | 397 |
| average profit per trade % | -0.71 | -1.04 |
| win rate % | 44.6 | 42.1 |
| average trade duration, minutes | 35.0 | 28.0 |
| duration measured in own candles | 7.0 | 5.6 |
| expectancy per trade (USDT) | -0.86 | -1.02 |
| mean profit p-value | 0.06664 | 7.663e-08 |
| market change % (baseline) | -58.37 | 346.34 |
| strategy total % | -6.38 | -40.55 |
| Sharpe | -0.42 | -0.88 |
| Sortino | -0.47 | -0.98 |
| max drawdown % | 7.34 | 41.55 |
| profit factor | 0.54 | 0.45 |

**Retained out of sample: negative**

> **Read that number with care.** The author's window was a bear market (buy-and-hold −58%) and the out-of-sample window a bull market (+346%). For a long-biased strategy this ratio rewards having done *badly* in 2018–2020, so it measures regime luck as much as robustness. The regime-free comparison is the excess over buy-and-hold, below.

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free either. Cross-strategy comparisons in this repository use average profit per trade in percent.

**Excess over buy-and-hold** (regime-free): author's window **+52.0 pp**, out of sample **-386.9 pp**.

⚠ **Not statistically significant in its author's own window** (p = 0.06664 > 0.05): the average trade is not distinguishable from zero.

Baseline: buy-and-hold on the same pairs returned **-58.37%**; the strategy returned **-6.38%**.
Out of sample: buy-and-hold **346.34%** vs strategy **-40.55%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | could not run | вывод не разобран |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | индикаторы меняются от объёма истории: rsi 0.935% |
| прогрев не объявлен | **found** | самый длинный индикатор 200 свечей, startup_candle_count не задан (по умолчанию 0) |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **5m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `590bf74986c5` · strategy list `a039f448c17bed72`*
