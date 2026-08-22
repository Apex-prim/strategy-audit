# CMCWinner

Source: [`PeetCrypto/freqtrade-stuff`](https://github.com/PeetCrypto/freqtrade-stuff) · file `CMCWinner.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 1633 | 4999 |
| average profit per trade % | -0.37 | -0.21 |
| win rate % | 58.8 | 59.7 |
| average trade duration, minutes | 181.0 | 200.0 |
| duration measured in own candles | 12.07 | 13.33 |
| expectancy per trade (USDT) | -0.33 | -0.15 |
| mean profit p-value | 1.864e-14 | 2.712e-09 |
| market change % (baseline) | -58.11 | 345.85 |
| strategy total % | -53.35 | -73.87 |
| Sharpe | -8.17 | -3.41 |
| Sortino | -6.58 | -2.9 |
| max drawdown % | 53.73 | 76.23 |
| profit factor | 0.4 | 0.67 |

**Retained out of sample: negative**

> **Read that number with care.** The author's window was a bear market (buy-and-hold −58%) and the out-of-sample window a bull market (+346%). For a long-biased strategy this ratio rewards having done *badly* in 2018–2020, so it measures regime luck as much as robustness. The regime-free comparison is the excess over buy-and-hold, below.

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free either. Cross-strategy comparisons in this repository use average profit per trade in percent.

**Excess over buy-and-hold** (regime-free): author's window **+4.8 pp**, out of sample **-419.7 pp**.

Baseline: buy-and-hold on the same pairs returned **-58.11%**; the strategy returned **-53.35%**.
Out of sample: buy-and-hold **345.85%** vs strategy **-73.87%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | could not run | вывод не разобран |
| indicator recursion (freqtrade's own `recursive-analysis`) | clean | рекурсивных отклонений не найдено |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **15m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `590bf74986c5` · strategy list `a039f448c17bed72`*
