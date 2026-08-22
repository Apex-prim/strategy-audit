# Renko

Source: [`PeetCrypto/freqtrade-stuff`](https://github.com/PeetCrypto/freqtrade-stuff) · file `Renko.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 11 | 113 |
| average profit per trade % | -2.65 | 15.32 |
| win rate % | 81.8 | 97.3 |
| average trade duration, minutes | 253954.0 | 152269.0 |
| duration measured in own candles | 16930.27 | 10151.27 |
| expectancy per trade (USDT) | -3.09 | 50.17 |
| mean profit p-value | 0.8385 | 3.329e-05 |
| market change % (baseline) | -58.11 | 345.85 |
| strategy total % | -3.4 | 566.89 |
| Sharpe | -0.02 | 0.37 |
| Sortino | -0.1 | 0.37 |
| max drawdown % | 17.34 | 21.9 |
| profit factor | 0.83 | 4.03 |

**Retained out of sample: n/a**

> **Read that number with care.** The author's window was a bear market (buy-and-hold −58%) and the out-of-sample window a bull market (+346%). For a long-biased strategy this ratio rewards having done *badly* in 2018–2020, so it measures regime luck as much as robustness. The regime-free comparison is the excess over buy-and-hold, below.

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free either. Cross-strategy comparisons in this repository use average profit per trade in percent.

**Excess over buy-and-hold** (regime-free): author's window **+54.7 pp**, out of sample **+221.0 pp**.

⚠ **Not statistically significant in its author's own window** (p = 0.8385 > 0.05): the average trade is not distinguishable from zero.

Baseline: buy-and-hold on the same pairs returned **-58.11%**; the strategy returned **-3.4%**.
Out of sample: buy-and-hold **345.85%** vs strategy **566.89%** — **beats the baseline**.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | **found** | ЕСТЬ СМЕЩЕНИЕ: входов 13, выходов 0 из 13 сигналов |
| indicator recursion (freqtrade's own `recursive-analysis`) | clean | рекурсивных отклонений не найдено |
| прогрев не объявлен | **found** | самый длинный индикатор 5 свечей, startup_candle_count не задан (по умолчанию 0) |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **15m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `590bf74986c5` · strategy list `a039f448c17bed72`*
