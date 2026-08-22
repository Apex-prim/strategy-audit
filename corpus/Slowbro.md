# Slowbro

Source: [`PeetCrypto/freqtrade-stuff`](https://github.com/PeetCrypto/freqtrade-stuff) · file `Slowbro.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 21 | 74 |
| average profit per trade % | -6.71 | 4.84 |
| win rate % | 66.7 | 90.5 |
| average trade duration, minutes | 253534.0 | 263223.0 |
| duration measured in own candles | 4225.57 | 4387.05 |
| expectancy per trade (USDT) | -11.63 | 5.24 |
| mean profit p-value | 0.3226 | 0.4581 |
| market change % (baseline) | -59.27 | 348.67 |
| strategy total % | -24.43 | 38.78 |
| Sharpe | -0.12 | 0.05 |
| Sortino | -0.18 | 0.1 |
| max drawdown % | 41.1 | 45.97 |
| profit factor | 0.54 | 1.33 |

**Retained out of sample: n/a**

> **Read that number with care.** The author's window was a bear market (buy-and-hold −58%) and the out-of-sample window a bull market (+346%). For a long-biased strategy this ratio rewards having done *badly* in 2018–2020, so it measures regime luck as much as robustness. The regime-free comparison is the excess over buy-and-hold, below.

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free either. Cross-strategy comparisons in this repository use average profit per trade in percent.

**Excess over buy-and-hold** (regime-free): author's window **+34.8 pp**, out of sample **-309.9 pp**.

⚠ **Not statistically significant in its author's own window** (p = 0.3226 > 0.05): the average trade is not distinguishable from zero.

Baseline: buy-and-hold on the same pairs returned **-59.27%**; the strategy returned **-24.43%**.
Out of sample: buy-and-hold **348.67%** vs strategy **38.78%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | could not run | вывод не разобран |
| indicator recursion (freqtrade's own `recursive-analysis`) | clean | рекурсивных отклонений не найдено |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **1h** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `590bf74986c5` · strategy list `a039f448c17bed72`*
