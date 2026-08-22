# SMAOffset

Source: [`PeetCrypto/freqtrade-stuff`](https://github.com/PeetCrypto/freqtrade-stuff) · file `SMAOffset.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 483 | 1625 |
| average profit per trade % | 0.11 | 0.86 |
| win rate % | 57.6 | 67.6 |
| average trade duration, minutes | 689.0 | 704.0 |
| duration measured in own candles | 137.8 | 140.8 |
| expectancy per trade (USDT) | 0.1 | 2.45 |
| mean profit p-value | 0.6463 | 6.825e-06 |
| market change % (baseline) | -58.37 | 346.34 |
| strategy total % | 4.77 | 398.09 |
| Sharpe | 0.26 | 1.47 |
| Sortino | 0.33 | 1.35 |
| max drawdown % | 13.03 | 19.27 |
| profit factor | 1.05 | 1.48 |

**Retained out of sample: 2450%**

> **Read that number with care.** The author's window was a bear market (buy-and-hold −58%) and the out-of-sample window a bull market (+346%). For a long-biased strategy this ratio rewards having done *badly* in 2018–2020, so it measures regime luck as much as robustness. The regime-free comparison is the excess over buy-and-hold, below.

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free either. Cross-strategy comparisons in this repository use average profit per trade in percent.

**Excess over buy-and-hold** (regime-free): author's window **+63.1 pp**, out of sample **+51.8 pp**.

⚠ **Not statistically significant in its author's own window** (p = 0.6463 > 0.05): the average trade is not distinguishable from zero.

Baseline: buy-and-hold on the same pairs returned **-58.37%**; the strategy returned **4.77%**.
Out of sample: buy-and-hold **346.34%** vs strategy **398.09%** — **beats the baseline**.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | could not run | вывод не разобран |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | индикаторы меняются от объёма истории: ma_offset_sell -0.020% |
| мёртвые настройки трейлинга | **found** | trailing_stop=False, но trailing_stop_positive=0.0001 задан — читается как работающая защита |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **5m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `590bf74986c5` · strategy list `a039f448c17bed72`*
