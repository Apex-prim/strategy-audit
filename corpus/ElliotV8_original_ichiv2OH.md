# ElliotV8_original_ichiv2OH

Source: [`TheoBrigitte/freqtrade`](https://github.com/TheoBrigitte/freqtrade) · file `ElliotV8_original_ichiv2OH.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 60 | 455 |
| average profit per trade % | 0.82 | 0.72 |
| win rate % | 80.0 | 83.3 |
| average trade duration, minutes | 72.0 | 64.0 |
| duration measured in own candles | 14.4 | 12.8 |
| expectancy per trade (USDT) | 1.04 | 1.06 |
| mean profit p-value | 0.06613 | 9.719e-05 |
| market change % (baseline) | -59.23 | 346.34 |
| strategy total % | 6.24 | 48.25 |
| Sharpe | 0.38 | 0.68 |
| Sortino | 0.27 | 0.65 |
| max drawdown % | 1.39 | 8.86 |
| profit factor | 2.01 | 1.67 |

**Retained out of sample: 102%**

> **Read that number with care.** The author's window was a bear market (buy-and-hold −58%) and the out-of-sample window a bull market (+346%). For a long-biased strategy this ratio rewards having done *badly* in 2018–2020, so it measures regime luck as much as robustness. The regime-free comparison is the excess over buy-and-hold, below.

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free either. Cross-strategy comparisons in this repository use average profit per trade in percent.

**Excess over buy-and-hold** (regime-free): author's window **+65.5 pp**, out of sample **-298.1 pp**.

⚠ **Not statistically significant in its author's own window** (p = 0.06613 > 0.05): the average trade is not distinguishable from zero.

Baseline: buy-and-hold on the same pairs returned **-59.23%**; the strategy returned **6.24%**.
Out of sample: buy-and-hold **346.34%** vs strategy **48.25%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | could not run | вывод не разобран |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | индикаторы меняются от объёма истории: EWO -12.317% |
| прогрев объявлен | clean | 400 при потребности 50 |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **5m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `590bf74986c5` · strategy list `a039f448c17bed72`*
