# SMAOG

Source: [`Foxel05/freqtrade-stuff`](https://github.com/Foxel05/freqtrade-stuff) · file `SMAOG.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 105 | 433 |
| average profit per trade % | 0.74 | 0.61 |
| win rate % | 79.0 | 78.5 |
| average trade duration, minutes | 33.0 | 34.0 |
| duration measured in own candles | 6.6 | 6.8 |
| expectancy per trade (USDT) | 0.95 | 0.89 |
| mean profit p-value | 0.0001089 | 2.809e-10 |
| market change % (baseline) | -59.23 | 346.34 |
| strategy total % | 10.02 | 38.56 |
| Sharpe | 1.09 | 1.09 |
| Sortino | 0.86 | 0.79 |
| max drawdown % | 1.48 | 2.86 |
| profit factor | 2.88 | 2.45 |

**Retained out of sample: 94%**

> **Read that number with care.** The author's window was a bear market (buy-and-hold −58%) and the out-of-sample window a bull market (+346%). For a long-biased strategy this ratio rewards having done *badly* in 2018–2020, so it measures regime luck as much as robustness. The regime-free comparison is the excess over buy-and-hold, below.

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free either. Cross-strategy comparisons in this repository use average profit per trade in percent.

**Excess over buy-and-hold** (regime-free): author's window **+69.2 pp**, out of sample **-307.8 pp**.

Baseline: buy-and-hold on the same pairs returned **-59.23%**; the strategy returned **10.02%**.
Out of sample: buy-and-hold **346.34%** vs strategy **38.56%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | could not run | вывод не разобран |
| indicator recursion (freqtrade's own `recursive-analysis`) | clean | рекурсивных отклонений не найдено |
| прогрев объявлен | clean | 400 при потребности 200 |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **5m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `590bf74986c5` · strategy list `a039f448c17bed72`*
