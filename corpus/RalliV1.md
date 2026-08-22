# RalliV1

Source: [`Foxel05/freqtrade-stuff`](https://github.com/Foxel05/freqtrade-stuff) · file `RalliV1.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 146 | 511 |
| average profit per trade % | 0.76 | 1.05 |
| win rate % | 70.5 | 74.8 |
| average trade duration, minutes | 66.0 | 53.0 |
| duration measured in own candles | 13.2 | 10.6 |
| expectancy per trade (USDT) | 1.0 | 1.83 |
| mean profit p-value | 8.89e-05 | 2.532e-17 |
| market change % (baseline) | -59.05 | 346.34 |
| strategy total % | 14.54 | 93.38 |
| Sharpe | 1.28 | 1.61 |
| Sortino | 1.57 | 1.42 |
| max drawdown % | 4.64 | 4.75 |
| profit factor | 2.32 | 2.83 |

**Retained out of sample: 183%**

> **Read that number with care.** The author's window was a bear market (buy-and-hold −58%) and the out-of-sample window a bull market (+346%). For a long-biased strategy this ratio rewards having done *badly* in 2018–2020, so it measures regime luck as much as robustness. The regime-free comparison is the excess over buy-and-hold, below.

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free either. Cross-strategy comparisons in this repository use average profit per trade in percent.

**Excess over buy-and-hold** (regime-free): author's window **+73.6 pp**, out of sample **-253.0 pp**.

Baseline: buy-and-hold on the same pairs returned **-59.05%**; the strategy returned **14.54%**.
Out of sample: buy-and-hold **346.34%** vs strategy **93.38%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | could not run | вывод не разобран |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | индикаторы меняются от объёма истории: EWO -12.317% |
| прогрев объявлен | clean | 200 при потребности 100 |
| мёртвые настройки трейлинга | **found** | trailing_stop=False, но trailing_stop_positive=0.005 задан — читается как работающая защита |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **5m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `590bf74986c5` · strategy list `a039f448c17bed72`*
