# KAMACCIRSI

Source: [`PeetCrypto/freqtrade-stuff`](https://github.com/PeetCrypto/freqtrade-stuff) · file `KAMACCIRSI.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 2220 | 8049 |
| average profit per trade % | -0.54 | -0.16 |
| win rate % | 69.3 | 68.6 |
| average trade duration, minutes | 2652.0 | 2634.0 |
| duration measured in own candles | 530.4 | 526.8 |
| expectancy per trade (USDT) | -0.39 | -0.11 |
| mean profit p-value | 1.281e-05 | 0.08124 |
| market change % (baseline) | -58.42 | 346.34 |
| strategy total % | -85.99 | -92.32 |
| Sharpe | -5.39 | -1.27 |
| Sortino | -3.16 | -0.75 |
| max drawdown % | 86.05 | 96.07 |
| profit factor | 0.44 | 0.83 |

**Retained out of sample: negative**

> **Read that number with care.** The author's window was a bear market (buy-and-hold −58%) and the out-of-sample window a bull market (+346%). For a long-biased strategy this ratio rewards having done *badly* in 2018–2020, so it measures regime luck as much as robustness. The regime-free comparison is the excess over buy-and-hold, below.

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free either. Cross-strategy comparisons in this repository use average profit per trade in percent.

**Excess over buy-and-hold** (regime-free): author's window **-27.6 pp**, out of sample **-438.7 pp**.

Baseline: buy-and-hold on the same pairs returned **-58.42%**; the strategy returned **-85.99%**.
Out of sample: buy-and-hold **346.34%** vs strategy **-92.32%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | could not run | вывод не разобран |
| indicator recursion (freqtrade's own `recursive-analysis`) | clean | рекурсивных отклонений не найдено |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **5m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `590bf74986c5` · strategy list `a039f448c17bed72`*
