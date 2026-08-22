# CombinedBinHAndCluc

Source: [`PeetCrypto/freqtrade-stuff`](https://github.com/PeetCrypto/freqtrade-stuff) · file `CombinedBinHAndCluc.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 865 | 2675 |
| average profit per trade % | -0.01 | 0.17 |
| win rate % | 76.6 | 71.5 |
| average trade duration, minutes | 175.0 | 87.0 |
| duration measured in own candles | 35.0 | 17.4 |
| expectancy per trade (USDT) | -0.03 | 0.24 |
| mean profit p-value | 0.8143 | 0.02054 |
| market change % (baseline) | -58.23 | 346.34 |
| strategy total % | -2.54 | 65.05 |
| Sharpe | -0.18 | 0.97 |
| Sortino | -2.99 | 3.87 |
| max drawdown % | 17.19 | 32.69 |
| profit factor | 0.98 | 1.11 |

**Retained out of sample: n/a**

> **Read that number with care.** The author's window was a bear market (buy-and-hold −58%) and the out-of-sample window a bull market (+346%). For a long-biased strategy this ratio rewards having done *badly* in 2018–2020, so it measures regime luck as much as robustness. The regime-free comparison is the excess over buy-and-hold, below.

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free either. Cross-strategy comparisons in this repository use average profit per trade in percent.

**Excess over buy-and-hold** (regime-free): author's window **+55.7 pp**, out of sample **-281.3 pp**.

⚠ **Not statistically significant in its author's own window** (p = 0.8143 > 0.05): the average trade is not distinguishable from zero.

Baseline: buy-and-hold on the same pairs returned **-58.23%**; the strategy returned **-2.54%**.
Out of sample: buy-and-hold **346.34%** vs strategy **65.05%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | could not run | вывод не разобран |
| indicator recursion (freqtrade's own `recursive-analysis`) | clean | рекурсивных отклонений не найдено |
| прогрев не объявлен | **found** | самый длинный индикатор 50 свечей, startup_candle_count не задан (по умолчанию 0) |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **5m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `590bf74986c5` · strategy list `a039f448c17bed72`*
