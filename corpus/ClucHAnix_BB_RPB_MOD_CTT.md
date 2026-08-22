# ClucHAnix_BB_RPB_MOD_CTT

Source: [`davidzr/freqtrade-strategies`](https://github.com/davidzr/freqtrade-strategies) · file `ClucHAnix_BB_RPB_MOD_CTT.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 1555 | 4941 |
| average profit per trade % | 0.06 | 0.19 |
| win rate % | 69.1 | 72.1 |
| average trade duration, minutes | 138.0 | 120.0 |
| duration measured in own candles | 27.6 | 24.0 |
| expectancy per trade (USDT) | 0.07 | 0.35 |
| mean profit p-value | 0.3974 | 0.005958 |
| market change % (baseline) | -59.05 | 346.34 |
| strategy total % | 10.23 | 175.34 |
| Sharpe | 0.87 | 1.56 |
| Sortino | 0.95 | 1.16 |
| max drawdown % | 13.46 | 36.89 |
| profit factor | 1.06 | 1.14 |

**Retained out of sample: 500%**

> **Read that number with care.** The author's window was a bear market (buy-and-hold −58%) and the out-of-sample window a bull market (+346%). For a long-biased strategy this ratio rewards having done *badly* in 2018–2020, so it measures regime luck as much as robustness. The regime-free comparison is the excess over buy-and-hold, below.

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free either. Cross-strategy comparisons in this repository use average profit per trade in percent.

**Excess over buy-and-hold** (regime-free): author's window **+69.3 pp**, out of sample **-171.0 pp**.

⚠ **Not statistically significant in its author's own window** (p = 0.3974 > 0.05): the average trade is not distinguishable from zero.

Baseline: buy-and-hold on the same pairs returned **-59.05%**; the strategy returned **10.23%**.
Out of sample: buy-and-hold **346.34%** vs strategy **175.34%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | clean | смещения не обнаружено |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | индикаторы меняются от объёма истории: EWO -12.317%, btc_1m 13.935% |
| прогрев объявлен | clean | 200 при потребности 200 |
| мёртвые настройки трейлинга | **found** | trailing_stop=False, но trailing_stop_positive=0.001 задан — читается как работающая защита |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **5m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `590bf74986c5` · strategy list `a039f448c17bed72`*
