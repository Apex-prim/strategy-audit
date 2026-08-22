# SMAOffsetV2

Source: [`PeetCrypto/freqtrade-stuff`](https://github.com/PeetCrypto/freqtrade-stuff) · file `SMAOffsetV2 (1).py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 187 | 607 |
| average profit per trade % | 0.43 | 1.32 |
| win rate % | 63.1 | 72.3 |
| average trade duration, minutes | 146.0 | 137.0 |
| duration measured in own candles | 29.2 | 27.4 |
| expectancy per trade (USDT) | 0.54 | 2.74 |
| mean profit p-value | 0.07142 | 3.202e-12 |
| market change % (baseline) | -59.05 | 346.34 |
| strategy total % | 10.1 | 166.4 |
| Sharpe | 0.65 | 1.42 |
| Sortino | 0.77 | 1.29 |
| max drawdown % | 10.07 | 8.04 |
| profit factor | 1.41 | 2.32 |

**Retained out of sample: 507%**

> **Read that number with care.** The author's window was a bear market (buy-and-hold −58%) and the out-of-sample window a bull market (+346%). For a long-biased strategy this ratio rewards having done *badly* in 2018–2020, so it measures regime luck as much as robustness. The regime-free comparison is the excess over buy-and-hold, below.

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free either. Cross-strategy comparisons in this repository use average profit per trade in percent.

**Excess over buy-and-hold** (regime-free): author's window **+69.1 pp**, out of sample **-179.9 pp**.

⚠ **Not statistically significant in its author's own window** (p = 0.07142 > 0.05): the average trade is not distinguishable from zero.

Baseline: buy-and-hold on the same pairs returned **-59.05%**; the strategy returned **10.1%**.
Out of sample: buy-and-hold **346.34%** vs strategy **166.4%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | could not run | вывод не разобран |
| indicator recursion (freqtrade's own `recursive-analysis`) | clean | рекурсивных отклонений не найдено |
| прогрев объявлен | clean | 200 при потребности 25 |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **5m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `590bf74986c5` · strategy list `a039f448c17bed72`*
