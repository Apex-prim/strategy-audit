# MACD_EMA

Source: [`PeetCrypto/freqtrade-stuff`](https://github.com/PeetCrypto/freqtrade-stuff) · file `MACD_EMA.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 10460 | 15195 |
| average profit per trade % | -0.23 | -0.17 |
| win rate % | 43.3 | 49.3 |
| average trade duration, minutes | 236.0 | 213.0 |
| duration measured in own candles | 47.2 | 42.6 |
| expectancy per trade (USDT) | -0.09 | -0.06 |
| mean profit p-value | 2.151e-27 | 5.342e-18 |
| market change % (baseline) | -58.23 | 346.34 |
| strategy total % | -95.03 | -96.58 |
| Sharpe | -29.07 | -8.63 |
| Sortino | -28.65 | -8.85 |
| max drawdown % | 95.04 | 96.68 |
| profit factor | 0.68 | 0.79 |

**Retained out of sample: negative**

> **Read that number with care.** The author's window was a bear market (buy-and-hold −58%) and the out-of-sample window a bull market (+346%). For a long-biased strategy this ratio rewards having done *badly* in 2018–2020, so it measures regime luck as much as robustness. The regime-free comparison is the excess over buy-and-hold, below.

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free either. Cross-strategy comparisons in this repository use average profit per trade in percent.

**Excess over buy-and-hold** (regime-free): author's window **-36.8 pp**, out of sample **-442.9 pp**.

Baseline: buy-and-hold on the same pairs returned **-58.23%**; the strategy returned **-95.03%**.
Out of sample: buy-and-hold **346.34%** vs strategy **-96.58%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | could not run | вывод не разобран |
| indicator recursion (freqtrade's own `recursive-analysis`) | clean | рекурсивных отклонений не найдено |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **5m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `590bf74986c5` · strategy list `a039f448c17bed72`*
