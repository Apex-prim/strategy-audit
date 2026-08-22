# Ichimoku_v31

Source: [`PeetCrypto/freqtrade-stuff`](https://github.com/PeetCrypto/freqtrade-stuff) · file `Ichimoku_v31_Heikin.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 238 | 1326 |
| average profit per trade % | 2.44 | 1.74 |
| win rate % | 26.9 | 23.0 |
| average trade duration, minutes | 6896.0 | 6014.0 |
| duration measured in own candles | 114.93 | 100.23 |
| expectancy per trade (USDT) | 3.68 | 4.26 |
| mean profit p-value | 0.0115 | 0.07244 |
| market change % (baseline) | -57.84 | 348.67 |
| strategy total % | 87.57 | 564.95 |
| Sharpe | 1.04 | 0.53 |
| Sortino | 6.65 | 2.87 |
| max drawdown % | 14.48 | 26.11 |
| profit factor | 2.16 | 1.36 |

**Retained out of sample: 116%**

> **Read that number with care.** The author's window was a bear market (buy-and-hold −58%) and the out-of-sample window a bull market (+346%). For a long-biased strategy this ratio rewards having done *badly* in 2018–2020, so it measures regime luck as much as robustness. The regime-free comparison is the excess over buy-and-hold, below.

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free either. Cross-strategy comparisons in this repository use average profit per trade in percent.

**Excess over buy-and-hold** (regime-free): author's window **+145.4 pp**, out of sample **+216.3 pp**.

Baseline: buy-and-hold on the same pairs returned **-57.84%**; the strategy returned **87.57%**.
Out of sample: buy-and-hold **348.67%** vs strategy **564.95%** — **beats the baseline**.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | could not run | вывод не разобран |
| indicator recursion (freqtrade's own `recursive-analysis`) | clean | рекурсивных отклонений не найдено |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **1h** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `590bf74986c5` · strategy list `a039f448c17bed72`*
