# Ichimoku_v37

Source: [`PeetCrypto/freqtrade-stuff`](https://github.com/PeetCrypto/freqtrade-stuff) · file `Ichimoku_v37_HeikinAshi.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 57 | 450 |
| average profit per trade % | 4.19 | 6.72 |
| win rate % | 21.1 | 17.3 |
| average trade duration, minutes | 20189.0 | 17287.0 |
| duration measured in own candles | 84.12 | 72.03 |
| expectancy per trade (USDT) | 4.96 | 15.5 |
| mean profit p-value | 0.1946 | 0.03365 |
| market change % (baseline) | -51.25 | 340.8 |
| strategy total % | 28.27 | 697.65 |
| Sharpe | 0.27 | 0.37 |
| Sortino | 2.42 | 2.35 |
| max drawdown % | 6.26 | 28.22 |
| profit factor | 2.57 | 1.95 |

**Retained out of sample: 312%**

> **Read that number with care.** The author's window was a bear market (buy-and-hold −58%) and the out-of-sample window a bull market (+346%). For a long-biased strategy this ratio rewards having done *badly* in 2018–2020, so it measures regime luck as much as robustness. The regime-free comparison is the excess over buy-and-hold, below.

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free either. Cross-strategy comparisons in this repository use average profit per trade in percent.

**Excess over buy-and-hold** (regime-free): author's window **+79.5 pp**, out of sample **+356.8 pp**.

⚠ **Not statistically significant in its author's own window** (p = 0.1946 > 0.05): the average trade is not distinguishable from zero.

Baseline: buy-and-hold on the same pairs returned **-51.25%**; the strategy returned **28.27%**.
Out of sample: buy-and-hold **340.8%** vs strategy **697.65%** — **beats the baseline**.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | could not run | вывод не разобран |
| indicator recursion (freqtrade's own `recursive-analysis`) | clean | рекурсивных отклонений не найдено |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **4h** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `590bf74986c5` · strategy list `a039f448c17bed72`*
