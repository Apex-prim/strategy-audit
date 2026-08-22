# kalthetank

Source: [`jaredrsommer/freqtradestrategies`](https://github.com/jaredrsommer/freqtradestrategies) · file `kalthetank (2).py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 39 | — |
| average profit per trade % | -3.98 | — |
| win rate % | 82.1 | — |
| average trade duration, minutes | 148885.0 | — |
| duration measured in own candles | 2481.42 | — |
| expectancy per trade (USDT) | -9.13 | — |
| mean profit p-value | 0.1429 | — |
| market change % (baseline) | -54.03 | — |
| strategy total % | -35.59 | — |
| Sharpe | -0.25 | — |
| Sortino | -0.27 | — |
| max drawdown % | 47.13 | — |
| profit factor | 0.38 | — |

**Retained out of sample: —**

> **Read that number with care.** The author's window was a bear market (buy-and-hold −58%) and the out-of-sample window a bull market (+346%). For a long-biased strategy this ratio rewards having done *badly* in 2018–2020, so it measures regime luck as much as robustness. The regime-free comparison is the excess over buy-and-hold, below.

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free either. Cross-strategy comparisons in this repository use average profit per trade in percent.

**Excess over buy-and-hold** (regime-free): author's window **+18.4 pp**.

⚠ **Not statistically significant in its author's own window** (p = 0.1429 > 0.05): the average trade is not distinguishable from zero.

Baseline: buy-and-hold on the same pairs returned **-54.03%**; the strategy returned **-35.59%**.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | could not run | Fatal exception! |
| indicator recursion (freqtrade's own `recursive-analysis`) | could not run | Fatal exception! |
| прогрев объявлен | clean | 200 при потребности 21 |
| признак утечки будущего | **found** | центрированное окно center=True |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **1h** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `590bf74986c5` · strategy list `a039f448c17bed72`*
