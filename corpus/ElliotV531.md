# ElliotV531

Source: [`davidzr/freqtrade-strategies`](https://github.com/davidzr/freqtrade-strategies) · file `ElliotV531.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 164 | 723 |
| average profit per trade % | 0.69 | 0.25 |
| win rate % | 78.0 | 67.5 |
| average trade duration, minutes | 130.0 | 103.0 |
| duration measured in own candles | 26.0 | 20.6 |
| expectancy per trade (USDT) | 0.92 | 0.33 |
| mean profit p-value | 2.72e-05 | 0.03872 |
| market change % (baseline) | -59.05 | 346.34 |
| strategy total % | 15.01 | 24.12 |
| Sharpe | 1.45 | 0.45 |
| Sortino | 1.07 | 0.36 |
| max drawdown % | 2.15 | 5.57 |
| profit factor | 2.5 | 1.3 |

**Retained out of sample: 36%**

> **Read that number with care.** The author's window was a bear market (buy-and-hold −58%) and the out-of-sample window a bull market (+346%). For a long-biased strategy this ratio rewards having done *badly* in 2018–2020, so it measures regime luck as much as robustness. The regime-free comparison is the excess over buy-and-hold, below.

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free either. Cross-strategy comparisons in this repository use average profit per trade in percent.

**Excess over buy-and-hold** (regime-free): author's window **+74.1 pp**, out of sample **-322.2 pp**.

Baseline: buy-and-hold on the same pairs returned **-59.05%**; the strategy returned **15.01%**.
Out of sample: buy-and-hold **346.34%** vs strategy **24.12%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | could not run | вывод не разобран |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | индикаторы меняются от объёма истории: EWO -12.317% |
| прогрев объявлен | clean | 200 при потребности 100 |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **5m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `590bf74986c5` · strategy list `a039f448c17bed72`*
