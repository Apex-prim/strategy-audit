# RobotradingBody

Source: [`davidzr/freqtrade-strategies`](https://github.com/davidzr/freqtrade-strategies) · file `RobotradingBody.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 620 | 2275 |
| average profit per trade % | -0.2 | -0.04 |
| win rate % | 60.6 | 61.2 |
| average trade duration, minutes | 468.0 | 424.0 |
| duration measured in own candles | 1.95 | 1.77 |
| expectancy per trade (USDT) | -0.25 | -0.08 |
| mean profit p-value | 0.1131 | 0.4163 |
| market change % (baseline) | -50.13 | 340.8 |
| strategy total % | -15.71 | -17.44 |
| Sharpe | -1.06 | -0.31 |
| Sortino | -1.09 | -0.3 |
| max drawdown % | 25.62 | 43.02 |
| profit factor | 0.81 | 0.94 |

**Retained out of sample: negative**

> **Read that number with care.** The author's window was a bear market (buy-and-hold −58%) and the out-of-sample window a bull market (+346%). For a long-biased strategy this ratio rewards having done *badly* in 2018–2020, so it measures regime luck as much as robustness. The regime-free comparison is the excess over buy-and-hold, below.

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free either. Cross-strategy comparisons in this repository use average profit per trade in percent.

**Excess over buy-and-hold** (regime-free): author's window **+34.4 pp**, out of sample **-358.2 pp**.

⚠ **Not statistically significant in its author's own window** (p = 0.1131 > 0.05): the average trade is not distinguishable from zero.

Baseline: buy-and-hold on the same pairs returned **-50.13%**; the strategy returned **-15.71%**.
Out of sample: buy-and-hold **340.8%** vs strategy **-17.44%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | clean | смещения не обнаружено |
| indicator recursion (freqtrade's own `recursive-analysis`) | clean | рекурсивных отклонений не найдено |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **4h** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `590bf74986c5` · strategy list `a039f448c17bed72`*
