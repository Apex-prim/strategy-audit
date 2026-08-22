# CrossEMAStrategy

Source: [`PeetCrypto/freqtrade-stuff`](https://github.com/PeetCrypto/freqtrade-stuff) · file `CrossEMAStrategy.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 828 | 3235 |
| average profit per trade % | 0.52 | 0.73 |
| win rate % | 28.4 | 28.3 |
| average trade duration, minutes | 3586.0 | 3632.0 |
| duration measured in own candles | 59.77 | 60.53 |
| expectancy per trade (USDT) | 0.61 | 2.05 |
| mean profit p-value | 0.09905 | 0.1126 |
| market change % (baseline) | -59.51 | 348.67 |
| strategy total % | 50.16 | 662.4 |
| Sharpe | 1.25 | 0.73 |
| Sortino | 4.21 | 2.72 |
| max drawdown % | 23.21 | 55.1 |
| profit factor | 1.24 | 1.16 |

**Retained out of sample: 336%**

> **Read that number with care.** The author's window was a bear market (buy-and-hold −58%) and the out-of-sample window a bull market (+346%). For a long-biased strategy this ratio rewards having done *badly* in 2018–2020, so it measures regime luck as much as robustness. The regime-free comparison is the excess over buy-and-hold, below.

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free either. Cross-strategy comparisons in this repository use average profit per trade in percent.

**Excess over buy-and-hold** (regime-free): author's window **+109.7 pp**, out of sample **+313.7 pp**.

⚠ **Not statistically significant in its author's own window** (p = 0.09905 > 0.05): the average trade is not distinguishable from zero.

Baseline: buy-and-hold on the same pairs returned **-59.51%**; the strategy returned **50.16%**.
Out of sample: buy-and-hold **348.67%** vs strategy **662.4%** — **beats the baseline**.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | could not run | вывод не разобран |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | индикаторы меняются от объёма истории: ema28 0.016%, ema48 0.124% |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **1h** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `590bf74986c5` · strategy list `a039f448c17bed72`*
