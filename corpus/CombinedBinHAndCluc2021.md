# CombinedBinHAndCluc2021

Source: [`PeetCrypto/freqtrade-stuff`](https://github.com/PeetCrypto/freqtrade-stuff) · file `CombinedBinHAndCluc2021.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 852 | 2445 |
| average profit per trade % | -0.03 | 0.37 |
| win rate % | 57.4 | 67.4 |
| average trade duration, minutes | 82.0 | 65.0 |
| duration measured in own candles | 16.4 | 13.0 |
| expectancy per trade (USDT) | -0.06 | 0.73 |
| mean profit p-value | 0.6192 | 0.0001065 |
| market change % (baseline) | -58.23 | 346.34 |
| strategy total % | -4.81 | 177.94 |
| Sharpe | -0.38 | 1.55 |
| Sortino | -0.41 | 1.59 |
| max drawdown % | 18.54 | 25.11 |
| profit factor | 0.95 | 1.26 |

**Retained out of sample: n/a**

> **Read that number with care.** The author's window was a bear market (buy-and-hold −58%) and the out-of-sample window a bull market (+346%). For a long-biased strategy this ratio rewards having done *badly* in 2018–2020, so it measures regime luck as much as robustness. The regime-free comparison is the excess over buy-and-hold, below.

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free either. Cross-strategy comparisons in this repository use average profit per trade in percent.

**Excess over buy-and-hold** (regime-free): author's window **+53.4 pp**, out of sample **-168.4 pp**.

⚠ **Not statistically significant in its author's own window** (p = 0.6192 > 0.05): the average trade is not distinguishable from zero.

Baseline: buy-and-hold on the same pairs returned **-58.23%**; the strategy returned **-4.81%**.
Out of sample: buy-and-hold **346.34%** vs strategy **177.94%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | could not run | вывод не разобран |
| indicator recursion (freqtrade's own `recursive-analysis`) | clean | рекурсивных отклонений не найдено |
| прогрев не объявлен | **found** | самый длинный индикатор 50 свечей, startup_candle_count не задан (по умолчанию 0) |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **5m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `590bf74986c5` · strategy list `a039f448c17bed72`*
