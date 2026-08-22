# TDSequentialStrategy

Source: [`PeetCrypto/freqtrade-stuff`](https://github.com/PeetCrypto/freqtrade-stuff) · file `TDSequentialStrategy.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 1017 | 3570 |
| average profit per trade % | -0.73 | -0.42 |
| win rate % | 43.5 | 48.0 |
| average trade duration, minutes | 2180.0 | 2102.0 |
| duration measured in own candles | 36.33 | 35.03 |
| expectancy per trade (USDT) | -0.62 | -0.24 |
| mean profit p-value | 2.41e-07 | 4.076e-05 |
| market change % (baseline) | -59.27 | 348.67 |
| strategy total % | -63.06 | -87.44 |
| Sharpe | -4.35 | -1.98 |
| Sortino | -11.91 | -4.17 |
| max drawdown % | 66.0 | 88.16 |
| profit factor | 0.67 | 0.83 |

**Retained out of sample: negative**

> **Read that number with care.** The author's window was a bear market (buy-and-hold −58%) and the out-of-sample window a bull market (+346%). For a long-biased strategy this ratio rewards having done *badly* in 2018–2020, so it measures regime luck as much as robustness. The regime-free comparison is the excess over buy-and-hold, below.

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free either. Cross-strategy comparisons in this repository use average profit per trade in percent.

**Excess over buy-and-hold** (regime-free): author's window **-3.8 pp**, out of sample **-436.1 pp**.

Baseline: buy-and-hold on the same pairs returned **-59.27%**; the strategy returned **-63.06%**.
Out of sample: buy-and-hold **348.67%** vs strategy **-87.44%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | could not run | вывод не разобран |
| indicator recursion (freqtrade's own `recursive-analysis`) | clean | рекурсивных отклонений не найдено |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **1h** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `590bf74986c5` · strategy list `a039f448c17bed72`*
