# ElliotV8_original

Source: [`davidzr/freqtrade-strategies`](https://github.com/davidzr/freqtrade-strategies) · file `ElliotV8_original.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 118 | 478 |
| average profit per trade % | 1.28 | 1.47 |
| win rate % | 90.7 | 93.1 |
| average trade duration, minutes | 311.0 | 516.0 |
| duration measured in own candles | 62.2 | 103.2 |
| expectancy per trade (USDT) | 1.74 | 2.89 |
| mean profit p-value | 0.0001429 | 2.707e-15 |
| market change % (baseline) | -59.23 | 346.34 |
| strategy total % | 20.49 | 137.9 |
| Sharpe | 1.12 | 1.45 |
| Sortino | 0.39 | 0.45 |
| max drawdown % | 3.98 | 3.98 |
| profit factor | 5.29 | 5.72 |

**Retained out of sample: 166%**

> **Read that number with care.** The author's window was a bear market (buy-and-hold −58%) and the out-of-sample window a bull market (+346%). For a long-biased strategy this ratio rewards having done *badly* in 2018–2020, so it measures regime luck as much as robustness. The regime-free comparison is the excess over buy-and-hold, below.

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free either. Cross-strategy comparisons in this repository use average profit per trade in percent.

**Excess over buy-and-hold** (regime-free): author's window **+79.7 pp**, out of sample **-208.4 pp**.

Baseline: buy-and-hold on the same pairs returned **-59.23%**; the strategy returned **20.49%**.
Out of sample: buy-and-hold **346.34%** vs strategy **137.9%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | could not run | вывод не разобран |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | индикаторы меняются от объёма истории: EWO -12.317% |
| прогрев объявлен | clean | 400 при потребности 50 |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **5m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `590bf74986c5` · strategy list `a039f448c17bed72`*
