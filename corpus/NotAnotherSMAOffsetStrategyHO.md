# NotAnotherSMAOffsetStrategyHO

Source: [`MMR-19/freqtrade-strategies`](https://github.com/MMR-19/freqtrade-strategies) · file `NotAnotherSMAOffSetStrategyHO.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 185 | 720 |
| average profit per trade % | 1.33 | 1.49 |
| win rate % | 80.5 | 84.4 |
| average trade duration, minutes | 87.0 | 52.0 |
| duration measured in own candles | 17.4 | 10.4 |
| expectancy per trade (USDT) | 1.91 | 3.74 |
| mean profit p-value | 1.079e-11 | 1.069e-11 |
| market change % (baseline) | -59.05 | 346.34 |
| strategy total % | 35.4 | 269.2 |
| Sharpe | 2.59 | 1.5 |
| Sortino | 3.33 | 0.73 |
| max drawdown % | 5.04 | 12.8 |
| profit factor | 3.36 | 2.67 |

**Retained out of sample: 196%**

> **Read that number with care.** The author's window was a bear market (buy-and-hold −58%) and the out-of-sample window a bull market (+346%). For a long-biased strategy this ratio rewards having done *badly* in 2018–2020, so it measures regime luck as much as robustness. The regime-free comparison is the excess over buy-and-hold, below.

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free either. Cross-strategy comparisons in this repository use average profit per trade in percent.

**Excess over buy-and-hold** (regime-free): author's window **+94.4 pp**, out of sample **-77.1 pp**.

Baseline: buy-and-hold on the same pairs returned **-59.05%**; the strategy returned **35.4%**.
Out of sample: buy-and-hold **346.34%** vs strategy **269.2%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | could not run | Fatal exception! |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | индикаторы меняются от объёма истории: EWO -12.317% |
| прогрев объявлен | clean | 200 при потребности 100 |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **5m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `590bf74986c5` · strategy list `a039f448c17bed72`*
