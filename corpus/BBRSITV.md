# BBRSITV

Source: [`PeetCrypto/freqtrade-stuff`](https://github.com/PeetCrypto/freqtrade-stuff) · file `BBRSITV.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 67 | 353 |
| average profit per trade % | 0.23 | 0.72 |
| win rate % | 64.2 | 59.5 |
| average trade duration, minutes | 377.0 | 402.0 |
| duration measured in own candles | 75.4 | 80.4 |
| expectancy per trade (USDT) | 0.26 | 1.0 |
| mean profit p-value | 0.7056 | 0.02531 |
| market change % (baseline) | -58.37 | 346.34 |
| strategy total % | 1.77 | 35.43 |
| Sharpe | 0.08 | 0.34 |
| Sortino | 0.1 | 0.43 |
| max drawdown % | 4.42 | 7.72 |
| profit factor | 1.13 | 1.37 |

**Retained out of sample: 385%**

> **Read that number with care.** The author's window was a bear market (buy-and-hold −58%) and the out-of-sample window a bull market (+346%). For a long-biased strategy this ratio rewards having done *badly* in 2018–2020, so it measures regime luck as much as robustness. The regime-free comparison is the excess over buy-and-hold, below.

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free either. Cross-strategy comparisons in this repository use average profit per trade in percent.

**Excess over buy-and-hold** (regime-free): author's window **+60.1 pp**, out of sample **-310.9 pp**.

⚠ **Not statistically significant in its author's own window** (p = 0.7056 > 0.05): the average trade is not distinguishable from zero.

Baseline: buy-and-hold on the same pairs returned **-58.37%**; the strategy returned **1.77%**.
Out of sample: buy-and-hold **346.34%** vs strategy **35.43%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | could not run | вывод не разобран |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | индикаторы меняются от объёма истории: rsi 0.935% |
| мёртвые настройки трейлинга | **found** | trailing_stop=False, но trailing_stop_positive=0.005 задан — читается как работающая защита |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **5m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `590bf74986c5` · strategy list `a039f448c17bed72`*
