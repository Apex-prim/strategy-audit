# MACDStrategy_crossed

Source: [`PeetCrypto/freqtrade-stuff`](https://github.com/PeetCrypto/freqtrade-stuff) · file `MACDStrategy_crossed.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 1075 | 3990 |
| average profit per trade % | -0.52 | -0.3 |
| win rate % | 88.8 | 88.1 |
| average trade duration, minutes | 2568.0 | 2602.0 |
| duration measured in own candles | 513.6 | 520.4 |
| expectancy per trade (USDT) | -0.51 | -0.21 |
| mean profit p-value | 0.001216 | 0.0006579 |
| market change % (baseline) | -58.23 | 346.34 |
| strategy total % | -55.1 | -83.98 |
| Sharpe | -2.78 | -1.74 |
| Sortino | -1.42 | -0.75 |
| max drawdown % | 58.12 | 86.59 |
| profit factor | 0.6 | 0.72 |

**Retained out of sample: negative**

> **Read that number with care.** The author's window was a bear market (buy-and-hold −58%) and the out-of-sample window a bull market (+346%). For a long-biased strategy this ratio rewards having done *badly* in 2018–2020, so it measures regime luck as much as robustness. The regime-free comparison is the excess over buy-and-hold, below.

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free either. Cross-strategy comparisons in this repository use average profit per trade in percent.

**Excess over buy-and-hold** (regime-free): author's window **+3.1 pp**, out of sample **-430.3 pp**.

Baseline: buy-and-hold on the same pairs returned **-58.23%**; the strategy returned **-55.1%**.
Out of sample: buy-and-hold **346.34%** vs strategy **-83.98%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | could not run | вывод не разобран |
| indicator recursion (freqtrade's own `recursive-analysis`) | clean | рекурсивных отклонений не найдено |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **5m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `590bf74986c5` · strategy list `a039f448c17bed72`*
