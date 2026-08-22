# SMAOffsetProtectOptV1

Source: [`Foxel05/freqtrade-stuff`](https://github.com/Foxel05/freqtrade-stuff) · file `SMAOffsetProtectOptV1.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 22 | 181 |
| average profit per trade % | -1.34 | 2.42 |
| win rate % | 54.5 | 77.3 |
| average trade duration, minutes | 131.0 | 112.0 |
| duration measured in own candles | 26.2 | 22.4 |
| expectancy per trade (USDT) | -1.67 | 3.81 |
| mean profit p-value | 0.3603 | 4.841e-06 |
| market change % (baseline) | -58.37 | 346.34 |
| strategy total % | -3.66 | 69.04 |
| Sharpe | -0.12 | 0.51 |
| Sortino | -0.13 | 0.68 |
| max drawdown % | 5.06 | 3.93 |
| profit factor | 0.57 | 3.26 |

**Retained out of sample: n/a**

> **Read that number with care.** The author's window was a bear market (buy-and-hold −58%) and the out-of-sample window a bull market (+346%). For a long-biased strategy this ratio rewards having done *badly* in 2018–2020, so it measures regime luck as much as robustness. The regime-free comparison is the excess over buy-and-hold, below.

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free either. Cross-strategy comparisons in this repository use average profit per trade in percent.

**Excess over buy-and-hold** (regime-free): author's window **+54.7 pp**, out of sample **-277.3 pp**.

⚠ **Not statistically significant in its author's own window** (p = 0.3603 > 0.05): the average trade is not distinguishable from zero.

Baseline: buy-and-hold on the same pairs returned **-58.37%**; the strategy returned **-3.66%**.
Out of sample: buy-and-hold **346.34%** vs strategy **69.04%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | could not run | вывод не разобран |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | индикаторы меняются от объёма истории: rsi 0.935% |
| прогрев объявлен | clean | 30 при потребности 14 |
| мёртвые настройки трейлинга | **found** | trailing_stop=False, но trailing_stop_positive=0.001 задан — читается как работающая защита |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **5m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `590bf74986c5` · strategy list `a039f448c17bed72`*
