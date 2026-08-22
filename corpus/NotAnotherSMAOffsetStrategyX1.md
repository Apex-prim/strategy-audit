# NotAnotherSMAOffsetStrategyX1

Source: [`PeetCrypto/freqtrade-stuff`](https://github.com/PeetCrypto/freqtrade-stuff) · file `NotAnotherSMAOffsetStrategyX1.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 116 | 481 |
| average profit per trade % | 0.67 | 0.62 |
| win rate % | 69.0 | 67.8 |
| average trade duration, minutes | 64.0 | 54.0 |
| duration measured in own candles | 12.8 | 10.8 |
| expectancy per trade (USDT) | 0.87 | 0.91 |
| mean profit p-value | 1.005e-05 | 4.64e-07 |
| market change % (baseline) | -59.23 | 346.34 |
| strategy total % | 10.14 | 43.9 |
| Sharpe | 1.31 | 0.91 |
| Sortino | 1.74 | 0.71 |
| max drawdown % | 1.02 | 5.79 |
| profit factor | 2.82 | 2.07 |

**Retained out of sample: 105%**

> **Read that number with care.** The author's window was a bear market (buy-and-hold −58%) and the out-of-sample window a bull market (+346%). For a long-biased strategy this ratio rewards having done *badly* in 2018–2020, so it measures regime luck as much as robustness. The regime-free comparison is the excess over buy-and-hold, below.

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free either. Cross-strategy comparisons in this repository use average profit per trade in percent.

**Excess over buy-and-hold** (regime-free): author's window **+69.4 pp**, out of sample **-302.4 pp**.

Baseline: buy-and-hold on the same pairs returned **-59.23%**; the strategy returned **10.14%**.
Out of sample: buy-and-hold **346.34%** vs strategy **43.9%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | could not run | код 1 |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | индикаторы меняются от объёма истории: EWO -12.317% |
| прогрев объявлен | clean | 400 при потребности 100 |
| мёртвые настройки трейлинга | **found** | trailing_stop=False, но trailing_stop_positive=0.005 задан — читается как работающая защита |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **5m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `590bf74986c5` · strategy list `a039f448c17bed72`*
