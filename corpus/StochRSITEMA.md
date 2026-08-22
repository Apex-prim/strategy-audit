# StochRSITEMA

Source: [`PeetCrypto/freqtrade-stuff`](https://github.com/PeetCrypto/freqtrade-stuff) · file `StochRSITEMA.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 1004 | 3538 |
| average profit per trade % | -0.21 | -0.29 |
| win rate % | 54.7 | 52.2 |
| average trade duration, minutes | 157.0 | 171.0 |
| duration measured in own candles | 31.4 | 34.2 |
| expectancy per trade (USDT) | -0.23 | -0.2 |
| mean profit p-value | 1.51e-10 | 6.446e-49 |
| market change % (baseline) | -58.48 | 346.34 |
| strategy total % | -23.4 | -71.49 |
| Sharpe | -5.37 | -7.18 |
| Sortino | -5.27 | -6.88 |
| max drawdown % | 23.64 | 71.67 |
| profit factor | 0.48 | 0.37 |

**Retained out of sample: negative**

> **Read that number with care.** The author's window was a bear market (buy-and-hold −58%) and the out-of-sample window a bull market (+346%). For a long-biased strategy this ratio rewards having done *badly* in 2018–2020, so it measures regime luck as much as robustness. The regime-free comparison is the excess over buy-and-hold, below.

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free either. Cross-strategy comparisons in this repository use average profit per trade in percent.

**Excess over buy-and-hold** (regime-free): author's window **+35.1 pp**, out of sample **-417.8 pp**.

Baseline: buy-and-hold on the same pairs returned **-58.48%**; the strategy returned **-23.4%**.
Out of sample: buy-and-hold **346.34%** vs strategy **-71.49%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | could not run | вывод не разобран |
| indicator recursion (freqtrade's own `recursive-analysis`) | clean | рекурсивных отклонений не найдено |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **5m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `590bf74986c5` · strategy list `a039f448c17bed72`*
