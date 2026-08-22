# CustomStoplossWithPSAR

Source: [`PeetCrypto/freqtrade-stuff`](https://github.com/PeetCrypto/freqtrade-stuff) · file `custom_stoploss_with_psar.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 62 | 78 |
| average profit per trade % | -7.43 | 85.53 |
| win rate % | 12.9 | 23.1 |
| average trade duration, minutes | 104799.0 | 305270.0 |
| duration measured in own candles | 1746.65 | 5087.83 |
| expectancy per trade (USDT) | -8.78 | 55.86 |
| mean profit p-value | 0.0002515 | 0.1366 |
| market change % (baseline) | -58.4 | 348.67 |
| strategy total % | -54.41 | 435.73 |
| Sharpe | -0.81 | 0.11 |
| Sortino | -2.42 | 1.16 |
| max drawdown % | 76.2 | 23.46 |
| profit factor | 0.3 | 2.37 |

**Retained out of sample: n/a**

> **Read that number with care.** The author's window was a bear market (buy-and-hold −58%) and the out-of-sample window a bull market (+346%). For a long-biased strategy this ratio rewards having done *badly* in 2018–2020, so it measures regime luck as much as robustness. The regime-free comparison is the excess over buy-and-hold, below.

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free either. Cross-strategy comparisons in this repository use average profit per trade in percent.

**Excess over buy-and-hold** (regime-free): author's window **+4.0 pp**, out of sample **+87.1 pp**.

Baseline: buy-and-hold on the same pairs returned **-58.4%**; the strategy returned **-54.41%**.
Out of sample: buy-and-hold **348.67%** vs strategy **435.73%** — **beats the baseline**.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | could not run | вывод не разобран |
| indicator recursion (freqtrade's own `recursive-analysis`) | clean | рекурсивных отклонений не найдено |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **1h** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `590bf74986c5` · strategy list `a039f448c17bed72`*
