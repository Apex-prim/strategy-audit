# Elliotv8

Source: [`Foxel05/freqtrade-stuff`](https://github.com/Foxel05/freqtrade-stuff) · file `ElliotV8.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 120 | 500 |
| average profit per trade % | 0.91 | 0.96 |
| win rate % | 75.8 | 78.0 |
| average trade duration, minutes | 45.0 | 41.0 |
| duration measured in own candles | 9.0 | 8.2 |
| expectancy per trade (USDT) | 1.2 | 1.6 |
| mean profit p-value | 9.06e-08 | 2.228e-15 |
| market change % (baseline) | -59.23 | 346.34 |
| strategy total % | 14.46 | 80.17 |
| Sharpe | 1.64 | 1.48 |
| Sortino | 1.97 | 1.07 |
| max drawdown % | 1.13 | 5.18 |
| profit factor | 3.62 | 3.02 |

**Retained out of sample: 133%**

> **Read that number with care.** The author's window was a bear market (buy-and-hold −58%) and the out-of-sample window a bull market (+346%). For a long-biased strategy this ratio rewards having done *badly* in 2018–2020, so it measures regime luck as much as robustness. The regime-free comparison is the excess over buy-and-hold, below.

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free either. Cross-strategy comparisons in this repository use average profit per trade in percent.

**Excess over buy-and-hold** (regime-free): author's window **+73.7 pp**, out of sample **-266.2 pp**.

Baseline: buy-and-hold on the same pairs returned **-59.23%**; the strategy returned **14.46%**.
Out of sample: buy-and-hold **346.34%** vs strategy **80.17%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | could not run | вывод не разобран |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | индикаторы меняются от объёма истории: EWO -12.317% |
| прогрев объявлен | clean | 400 при потребности 50 |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **5m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `590bf74986c5` · strategy list `a039f448c17bed72`*
