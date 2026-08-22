# ActionZone

Source: [`PeetCrypto/freqtrade-stuff`](https://github.com/PeetCrypto/freqtrade-stuff) · file `ActionZone.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 97 | 464 |
| average profit per trade % | 4.02 | 4.31 |
| win rate % | 26.8 | 26.3 |
| average trade duration, minutes | 19833.0 | 18407.0 |
| duration measured in own candles | 13.77 | 12.78 |
| expectancy per trade (USDT) | 6.11 | 4.39 |
| mean profit p-value | 0.1086 | 0.02769 |
| market change % (baseline) | -45.75 | 352.61 |
| strategy total % | 59.3 | 203.8 |
| Sharpe | 0.44 | 0.39 |
| Sortino | 4.33 | 4.3 |
| max drawdown % | 20.2 | 15.35 |
| profit factor | 2.24 | 1.83 |

**Retained out of sample: 72%**

> **Read that number with care.** The author's window was a bear market (buy-and-hold −58%) and the out-of-sample window a bull market (+346%). For a long-biased strategy this ratio rewards having done *badly* in 2018–2020, so it measures regime luck as much as robustness. The regime-free comparison is the excess over buy-and-hold, below.

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free either. Cross-strategy comparisons in this repository use average profit per trade in percent.

**Excess over buy-and-hold** (regime-free): author's window **+105.0 pp**, out of sample **-148.8 pp**.

⚠ **Not statistically significant in its author's own window** (p = 0.1086 > 0.05): the average trade is not distinguishable from zero.

Baseline: buy-and-hold on the same pairs returned **-45.75%**; the strategy returned **59.3%**.
Out of sample: buy-and-hold **352.61%** vs strategy **203.8%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | could not run | вывод не разобран |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | индикаторы меняются от объёма истории: fastMA -0.011%, slowMA -0.082% |
| прогрев не объявлен | **found** | самый длинный индикатор 26 свечей, startup_candle_count не задан (по умолчанию 0) |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **1d** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `590bf74986c5` · strategy list `a039f448c17bed72`*
