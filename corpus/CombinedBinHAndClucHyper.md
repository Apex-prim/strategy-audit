# CombinedBinHAndClucHyper

Source: [`TheoBrigitte/freqtrade`](https://github.com/TheoBrigitte/freqtrade) · file `CombinedBinHAndClucHyper.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 653 | 3164 |
| average profit per trade % | 0.07 | 0.24 |
| win rate % | 69.2 | 63.5 |
| average trade duration, minutes | 2671.0 | 559.0 |
| duration measured in own candles | 2671.0 | 559.0 |
| expectancy per trade (USDT) | 0.1 | 0.48 |
| mean profit p-value | 0.5822 | 1.373e-14 |
| market change % (baseline) | -55.69 | 347.94 |
| strategy total % | 6.41 | 152.66 |
| Sharpe | 0.37 | 3.52 |
| Sortino | 0.21 | 2.25 |
| max drawdown % | 8.73 | 6.87 |
| profit factor | 1.33 | 8.85 |

**Retained out of sample: 480%**

> **Read that number with care.** The author's window was a bear market (buy-and-hold −58%) and the out-of-sample window a bull market (+346%). For a long-biased strategy this ratio rewards having done *badly* in 2018–2020, so it measures regime luck as much as robustness. The regime-free comparison is the excess over buy-and-hold, below.

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free either. Cross-strategy comparisons in this repository use average profit per trade in percent.

**Excess over buy-and-hold** (regime-free): author's window **+62.1 pp**, out of sample **-195.3 pp**.

⚠ **Not statistically significant in its author's own window** (p = 0.5822 > 0.05): the average trade is not distinguishable from zero.

Baseline: buy-and-hold on the same pairs returned **-55.69%**; the strategy returned **6.41%**.
Out of sample: buy-and-hold **347.94%** vs strategy **152.66%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | clean | смещения не обнаружено |
| indicator recursion (freqtrade's own `recursive-analysis`) | clean | рекурсивных отклонений не найдено |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **1m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `590bf74986c5` · strategy list `a039f448c17bed72`*
