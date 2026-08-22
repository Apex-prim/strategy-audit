# NotAnotherSMAOffsetStrategy_uzi3

Source: [`Foxel05/freqtrade-stuff`](https://github.com/Foxel05/freqtrade-stuff) · file `NotAnotherSMAOffsetStrategy_uzi3.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 217 | 954 |
| average profit per trade % | 0.45 | 0.75 |
| win rate % | 81.6 | 84.2 |
| average trade duration, minutes | 516.0 | 173.0 |
| duration measured in own candles | 103.2 | 34.6 |
| expectancy per trade (USDT) | 0.58 | 1.44 |
| mean profit p-value | 0.07369 | 1.396e-07 |
| market change % (baseline) | -59.23 | 346.34 |
| strategy total % | 12.67 | 137.43 |
| Sharpe | 0.7 | 1.33 |
| Sortino | 0.57 | 0.91 |
| max drawdown % | 3.83 | 7.64 |
| profit factor | 1.4 | 1.68 |

**Retained out of sample: 248%**

> **Read that number with care.** The author's window was a bear market (buy-and-hold −58%) and the out-of-sample window a bull market (+346%). For a long-biased strategy this ratio rewards having done *badly* in 2018–2020, so it measures regime luck as much as robustness. The regime-free comparison is the excess over buy-and-hold, below.

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free either. Cross-strategy comparisons in this repository use average profit per trade in percent.

**Excess over buy-and-hold** (regime-free): author's window **+71.9 pp**, out of sample **-208.9 pp**.

⚠ **Not statistically significant in its author's own window** (p = 0.07369 > 0.05): the average trade is not distinguishable from zero.

Baseline: buy-and-hold on the same pairs returned **-59.23%**; the strategy returned **12.67%**.
Out of sample: buy-and-hold **346.34%** vs strategy **137.43%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | could not run | Fatal exception! |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | индикаторы меняются от объёма истории: EWO -12.317% |
| прогрев объявлен | clean | 400 при потребности 100 |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **5m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `590bf74986c5` · strategy list `a039f448c17bed72`*
