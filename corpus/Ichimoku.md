# Ichimoku

Source: [`PeetCrypto/freqtrade-stuff`](https://github.com/PeetCrypto/freqtrade-stuff) · file `Ichimoku.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 2434 | 6175 |
| average profit per trade % | -0.62 | -0.38 |
| win rate % | 79.8 | 82.2 |
| average trade duration, minutes | 2099.0 | 2063.0 |
| duration measured in own candles | 419.8 | 412.6 |
| expectancy per trade (USDT) | -0.36 | -0.16 |
| mean profit p-value | 4.715e-12 | 5.941e-06 |
| market change % (baseline) | -58.23 | 346.34 |
| strategy total % | -87.67 | -96.57 |
| Sharpe | -8.96 | -2.88 |
| Sortino | -7.88 | -1.97 |
| max drawdown % | 88.31 | 96.9 |
| profit factor | 0.61 | 0.8 |

**Retained out of sample: negative**

> **Read that number with care.** The author's window was a bear market (buy-and-hold −58%) and the out-of-sample window a bull market (+346%). For a long-biased strategy this ratio rewards having done *badly* in 2018–2020, so it measures regime luck as much as robustness. The regime-free comparison is the excess over buy-and-hold, below.

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free either. Cross-strategy comparisons in this repository use average profit per trade in percent.

**Excess over buy-and-hold** (regime-free): author's window **-29.4 pp**, out of sample **-442.9 pp**.

Baseline: buy-and-hold on the same pairs returned **-58.23%**; the strategy returned **-87.67%**.
Out of sample: buy-and-hold **346.34%** vs strategy **-96.57%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | could not run | вывод не разобран |
| indicator recursion (freqtrade's own `recursive-analysis`) | clean | рекурсивных отклонений не найдено |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **5m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `590bf74986c5` · strategy list `a039f448c17bed72`*
