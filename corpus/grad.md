# grad

Source: [`jaredrsommer/freqtradestrategies`](https://github.com/jaredrsommer/freqtradestrategies) · file `grad (copy).py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 6173 | 20915 |
| average profit per trade % | 0.5 | 0.53 |
| win rate % | 48.5 | 48.4 |
| average trade duration, minutes | 194.0 | 206.0 |
| duration measured in own candles | 3.23 | 3.43 |
| expectancy per trade (USDT) | 6.8 | 6091.9 |
| mean profit p-value | 3.022e-56 | 8.889e-78 |
| market change % (baseline) | -59.31 | 348.67 |
| strategy total % | 4197.88 | 12741211.14 |
| Sharpe | 32.83 | 21.92 |
| Sortino | 95.67 | 60.48 |
| max drawdown % | 2.27 | 1.18 |
| profit factor | 2.92 | 2.56 |

**Retained out of sample: 89587%**

> **Read that number with care.** The author's window was a bear market (buy-and-hold −58%) and the out-of-sample window a bull market (+346%). For a long-biased strategy this ratio rewards having done *badly* in 2018–2020, so it measures regime luck as much as robustness. The regime-free comparison is the excess over buy-and-hold, below.

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free either. Cross-strategy comparisons in this repository use average profit per trade in percent.

**Excess over buy-and-hold** (regime-free): author's window **+4257.2 pp**, out of sample **+12740862.5 pp**.

Baseline: buy-and-hold on the same pairs returned **-59.31%**; the strategy returned **4197.88%**.
Out of sample: buy-and-hold **348.67%** vs strategy **12741211.14%** — **beats the baseline**.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | **found** | ЕСТЬ СМЕЩЕНИЕ: входов 0, выходов 0 из 20 сигналов |
| indicator recursion (freqtrade's own `recursive-analysis`) | clean | рекурсивных отклонений не найдено |
| мёртвые настройки трейлинга | **found** | trailing_stop=False, но trailing_stop_positive=0.015 задан — читается как работающая защита |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **1h** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `590bf74986c5` · strategy list `a039f448c17bed72`*
