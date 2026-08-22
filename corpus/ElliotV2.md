# ElliotV2

Source: [`davidzr/freqtrade-strategies`](https://github.com/davidzr/freqtrade-strategies) · file `ElliotV2.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 43 | 359 |
| average profit per trade % | 1.76 | 1.74 |
| win rate % | 93.0 | 90.8 |
| average trade duration, minutes | 960.0 | 415.0 |
| duration measured in own candles | 192.0 | 83.0 |
| expectancy per trade (USDT) | 2.27 | 3.12 |
| mean profit p-value | 0.017 | 1.841e-06 |
| market change % (baseline) | -58.92 | 346.34 |
| strategy total % | 9.74 | 112.05 |
| Sharpe | 0.43 | 0.74 |
| Sortino | 0.23 | 0.7 |
| max drawdown % | 2.22 | 11.01 |
| profit factor | 3.04 | 2.08 |

**Retained out of sample: 137%**

> **Read that number with care.** The author's window was a bear market (buy-and-hold −58%) and the out-of-sample window a bull market (+346%). For a long-biased strategy this ratio rewards having done *badly* in 2018–2020, so it measures regime luck as much as robustness. The regime-free comparison is the excess over buy-and-hold, below.

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free either. Cross-strategy comparisons in this repository use average profit per trade in percent.

**Excess over buy-and-hold** (regime-free): author's window **+68.7 pp**, out of sample **-234.3 pp**.

Baseline: buy-and-hold on the same pairs returned **-58.92%**; the strategy returned **9.74%**.
Out of sample: buy-and-hold **346.34%** vs strategy **112.05%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | could not run | вывод не разобран |
| indicator recursion (freqtrade's own `recursive-analysis`) | clean | рекурсивных отклонений не найдено |
| прогрев объявлен | clean | 139 при потребности 100 |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **5m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `590bf74986c5` · strategy list `a039f448c17bed72`*
