# NotAnotherSMAOffsetStrategyModHO_LamineDz_20210901

Source: [`davidzr/freqtrade-strategies`](https://github.com/davidzr/freqtrade-strategies) · file `NotAnotherSMAOffsetStrategyModHO_LamineDz_20210901.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 159 | 984 |
| average profit per trade % | 0.1 | 0.34 |
| win rate % | 62.9 | 64.3 |
| average trade duration, minutes | 37.0 | 34.0 |
| duration measured in own candles | 7.4 | 6.8 |
| expectancy per trade (USDT) | 0.12 | 0.51 |
| mean profit p-value | 0.5183 | 6.353e-06 |
| market change % (baseline) | -59.05 | 346.34 |
| strategy total % | 1.98 | 50.06 |
| Sharpe | 0.21 | 1.15 |
| Sortino | 0.21 | 1.16 |
| max drawdown % | 5.77 | 7.86 |
| profit factor | 1.15 | 1.5 |

**Retained out of sample: 425%**

> **Read that number with care.** The author's window was a bear market (buy-and-hold −58%) and the out-of-sample window a bull market (+346%). For a long-biased strategy this ratio rewards having done *badly* in 2018–2020, so it measures regime luck as much as robustness. The regime-free comparison is the excess over buy-and-hold, below.

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free either. Cross-strategy comparisons in this repository use average profit per trade in percent.

**Excess over buy-and-hold** (regime-free): author's window **+61.0 pp**, out of sample **-296.3 pp**.

⚠ **Not statistically significant in its author's own window** (p = 0.5183 > 0.05): the average trade is not distinguishable from zero.

Baseline: buy-and-hold on the same pairs returned **-59.05%**; the strategy returned **1.98%**.
Out of sample: buy-and-hold **346.34%** vs strategy **50.06%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | could not run | вывод не разобран |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | индикаторы меняются от объёма истории: EWO -12.317% |
| прогрев объявлен | clean | 200 при потребности 100 |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **5m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `590bf74986c5` · strategy list `a039f448c17bed72`*
