# MiniLambo

Source: [`PeetCrypto/freqtrade-stuff`](https://github.com/PeetCrypto/freqtrade-stuff) · file `MiniLambo (2).py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 217 | 1252 |
| average profit per trade % | -0.01 | -0.32 |
| win rate % | 72.4 | 62.3 |
| average trade duration, minutes | 55.0 | 17.0 |
| duration measured in own candles | 55.0 | 17.0 |
| expectancy per trade (USDT) | -0.04 | -0.33 |
| mean profit p-value | 0.8702 | 0.001168 |
| market change % (baseline) | -55.62 | 347.94 |
| strategy total % | -0.85 | -41.8 |
| Sharpe | -0.06 | -0.93 |
| Sortino | -0.05 | -0.79 |
| max drawdown % | 7.44 | 44.77 |
| profit factor | 0.96 | 0.73 |

**Retained out of sample: negative**

> **Read that number with care.** The author's window was a bear market (buy-and-hold −58%) and the out-of-sample window a bull market (+346%). For a long-biased strategy this ratio rewards having done *badly* in 2018–2020, so it measures regime luck as much as robustness. The regime-free comparison is the excess over buy-and-hold, below.

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free either. Cross-strategy comparisons in this repository use average profit per trade in percent.

**Excess over buy-and-hold** (regime-free): author's window **+54.8 pp**, out of sample **-389.7 pp**.

⚠ **Not statistically significant in its author's own window** (p = 0.8702 > 0.05): the average trade is not distinguishable from zero.

Baseline: buy-and-hold on the same pairs returned **-55.62%**; the strategy returned **-0.85%**.
Out of sample: buy-and-hold **347.94%** vs strategy **-41.8%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | could not run | вывод не разобран |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | индикаторы меняются от объёма истории: rsi_100 -1.453%, ewo 66.246% |
| прогрев объявлен | clean | 200 при потребности 100 |
| мёртвые настройки трейлинга | **found** | trailing_stop=False, но trailing_stop_positive=0.3207 задан — читается как работающая защита |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **1m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `590bf74986c5` · strategy list `a039f448c17bed72`*
