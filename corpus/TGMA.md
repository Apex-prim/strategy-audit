# TGMA

Source: [`jaredrsommer/freqtradestrategies`](https://github.com/jaredrsommer/freqtradestrategies) · file `TGMA.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 1766 | 6907 |
| average profit per trade % | -0.25 | -0.33 |
| win rate % | 35.5 | 34.2 |
| average trade duration, minutes | 270.0 | 251.0 |
| duration measured in own candles | 4.5 | 4.18 |
| expectancy per trade (USDT) | -0.24 | -0.14 |
| mean profit p-value | 2.334e-08 | 2.536e-19 |
| market change % (baseline) | -59.31 | 348.67 |
| strategy total % | -42.39 | -94.09 |
| Sharpe | -6.17 | -6.06 |
| Sortino | -8.91 | -8.06 |
| max drawdown % | 42.39 | 94.13 |
| profit factor | 0.65 | 0.66 |

**Retained out of sample: negative**

> **Read that number with care.** The author's window was a bear market (buy-and-hold −58%) and the out-of-sample window a bull market (+346%). For a long-biased strategy this ratio rewards having done *badly* in 2018–2020, so it measures regime luck as much as robustness. The regime-free comparison is the excess over buy-and-hold, below.

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free either. Cross-strategy comparisons in this repository use average profit per trade in percent.

**Excess over buy-and-hold** (regime-free): author's window **+16.9 pp**, out of sample **-442.8 pp**.

Baseline: buy-and-hold on the same pairs returned **-59.31%**; the strategy returned **-42.39%**.
Out of sample: buy-and-hold **348.67%** vs strategy **-94.09%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | could not run | Fatal exception! |
| indicator recursion (freqtrade's own `recursive-analysis`) | could not run | Fatal exception! |
| прогрев объявлен | clean | 20 при потребности 3 |
| мёртвые настройки трейлинга | **found** | trailing_stop=False, но trailing_stop_positive=0.035 задан — читается как работающая защита |
| признак утечки будущего | **found** | центрированное окно center=True |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **1h** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `590bf74986c5` · strategy list `a039f448c17bed72`*
