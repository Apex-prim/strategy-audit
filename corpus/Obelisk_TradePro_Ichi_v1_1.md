# Obelisk_TradePro_Ichi_v1_1

Source: [`PeetCrypto/freqtrade-stuff`](https://github.com/PeetCrypto/freqtrade-stuff) · file `Obelisk_TradePro_Ichi_v1_1.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 992 | 4067 |
| average profit per trade % | 0.19 | 0.08 |
| win rate % | 26.4 | 23.9 |
| average trade duration, minutes | 1077.0 | 1136.0 |
| duration measured in own candles | 17.95 | 18.93 |
| expectancy per trade (USDT) | 0.23 | 0.07 |
| mean profit p-value | 0.232 | 0.5473 |
| market change % (baseline) | -59.31 | 348.67 |
| strategy total % | 22.6 | 28.57 |
| Sharpe | 0.99 | 0.31 |
| Sortino | 9.21 | 2.82 |
| max drawdown % | 12.42 | 42.7 |
| profit factor | 1.17 | 1.05 |

**Retained out of sample: 30%**

> **Read that number with care.** The author's window was a bear market (buy-and-hold −58%) and the out-of-sample window a bull market (+346%). For a long-biased strategy this ratio rewards having done *badly* in 2018–2020, so it measures regime luck as much as robustness. The regime-free comparison is the excess over buy-and-hold, below.

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free either. Cross-strategy comparisons in this repository use average profit per trade in percent.

**Excess over buy-and-hold** (regime-free): author's window **+81.9 pp**, out of sample **-320.1 pp**.

⚠ **Not statistically significant in its author's own window** (p = 0.232 > 0.05): the average trade is not distinguishable from zero.

Baseline: buy-and-hold on the same pairs returned **-59.31%**; the strategy returned **22.6%**.
Out of sample: buy-and-hold **348.67%** vs strategy **28.57%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | **found** | ЕСТЬ СМЕЩЕНИЕ: входов 0, выходов 0 из 20 сигналов |
| indicator recursion (freqtrade's own `recursive-analysis`) | clean | рекурсивных отклонений не найдено |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **1h** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `590bf74986c5` · strategy list `a039f448c17bed72`*
