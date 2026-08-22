# ElliotV8HO

Source: [`davidzr/freqtrade-strategies`](https://github.com/davidzr/freqtrade-strategies) · file `ElliotV8HO.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 42 | 344 |
| average profit per trade % | 0.75 | 1.37 |
| win rate % | 95.2 | 97.1 |
| average trade duration, minutes | 927.0 | 217.0 |
| duration measured in own candles | 185.4 | 43.4 |
| expectancy per trade (USDT) | 0.93 | 2.28 |
| mean profit p-value | 0.3034 | 3.707e-10 |
| market change % (baseline) | -59.23 | 346.34 |
| strategy total % | 3.92 | 78.43 |
| Sharpe | 0.18 | 0.97 |
| Sortino | 1.81 | 1.0 |
| max drawdown % | 2.36 | 6.41 |
| profit factor | 1.8 | 3.38 |

**Retained out of sample: 245%**

> **Read that number with care.** The author's window was a bear market (buy-and-hold −58%) and the out-of-sample window a bull market (+346%). For a long-biased strategy this ratio rewards having done *badly* in 2018–2020, so it measures regime luck as much as robustness. The regime-free comparison is the excess over buy-and-hold, below.

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free either. Cross-strategy comparisons in this repository use average profit per trade in percent.

**Excess over buy-and-hold** (regime-free): author's window **+63.1 pp**, out of sample **-267.9 pp**.

⚠ **Not statistically significant in its author's own window** (p = 0.3034 > 0.05): the average trade is not distinguishable from zero.

Baseline: buy-and-hold on the same pairs returned **-59.23%**; the strategy returned **3.92%**.
Out of sample: buy-and-hold **346.34%** vs strategy **78.43%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | could not run | вывод не разобран |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | индикаторы меняются от объёма истории: EWO -12.317% |
| прогрев объявлен | clean | 400 при потребности 50 |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **5m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `590bf74986c5` · strategy list `a039f448c17bed72`*
