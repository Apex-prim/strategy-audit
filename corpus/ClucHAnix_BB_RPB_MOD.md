# ClucHAnix_BB_RPB_MOD

Source: [`PeetCrypto/freqtrade-stuff`](https://github.com/PeetCrypto/freqtrade-stuff) · file `ClucHAnix_BB_RPB_MOD.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 826 | — |
| average profit per trade % | -0.07 | — |
| win rate % | 57.6 | — |
| average trade duration, minutes | 62.0 | — |
| duration measured in own candles | 62.0 | — |
| expectancy per trade (USDT) | -0.1 | — |
| mean profit p-value | 0.3139 | — |
| market change % (baseline) | -55.62 | — |
| strategy total % | -8.45 | — |
| Sharpe | -0.76 | — |
| Sortino | -0.84 | — |
| max drawdown % | 22.05 | — |
| profit factor | 0.91 | — |

**Retained out of sample: —**

> **Read that number with care.** The author's window was a bear market (buy-and-hold −58%) and the out-of-sample window a bull market (+346%). For a long-biased strategy this ratio rewards having done *badly* in 2018–2020, so it measures regime luck as much as robustness. The regime-free comparison is the excess over buy-and-hold, below.

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free either. Cross-strategy comparisons in this repository use average profit per trade in percent.

**Excess over buy-and-hold** (regime-free): author's window **+47.2 pp**.

⚠ **Not statistically significant in its author's own window** (p = 0.3139 > 0.05): the average trade is not distinguishable from zero.

Baseline: buy-and-hold on the same pairs returned **-55.62%**; the strategy returned **-8.45%**.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | could not run | вывод не разобран |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | индикаторы меняются от объёма истории: EWO 66.246% |
| прогрев объявлен | clean | 200 при потребности 168 |
| мёртвые настройки трейлинга | **found** | trailing_stop=False, но trailing_stop_positive=0.001 задан — читается как работающая защита |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **1m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `590bf74986c5` · strategy list `a039f448c17bed72`*
