# HyperStra_GSN_SMAOnly

Source: [`PeetCrypto/freqtrade-stuff`](https://github.com/PeetCrypto/freqtrade-stuff) · file `HyperStra_GSN_SMAOnly.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 8 | 9 |
| average profit per trade % | 4.95 | 18.53 |
| win rate % | 87.5 | 77.8 |
| average trade duration, minutes | 322.0 | 73.0 |
| duration measured in own candles | 64.4 | 14.6 |
| expectancy per trade (USDT) | 6.24 | 22.9 |
| mean profit p-value | 0.00668 | 0.007036 |
| market change % (baseline) | -59.17 | 346.34 |
| strategy total % | 4.99 | 20.61 |
| Sharpe | 0.3 | 0.09 |
| Sortino | -100.0 | 37.77 |
| max drawdown % | 0.0 | 1.28 |
| profit factor | 754923.68 | 17.15 |

**Retained out of sample: 367%**

> **Read that number with care.** The author's window was a bear market (buy-and-hold −58%) and the out-of-sample window a bull market (+346%). For a long-biased strategy this ratio rewards having done *badly* in 2018–2020, so it measures regime luck as much as robustness. The regime-free comparison is the excess over buy-and-hold, below.

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free either. Cross-strategy comparisons in this repository use average profit per trade in percent.

**Excess over buy-and-hold** (regime-free): author's window **+64.2 pp**, out of sample **-325.7 pp**.

Baseline: buy-and-hold on the same pairs returned **-59.17%**; the strategy returned **4.99%**.
Out of sample: buy-and-hold **346.34%** vs strategy **20.61%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | could not run | вывод не разобран |
| indicator recursion (freqtrade's own `recursive-analysis`) | clean | рекурсивных отклонений не найдено |
| мёртвые настройки трейлинга | **found** | trailing_stop=False, но trailing_stop_positive=0.005 задан — читается как работающая защита |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **5m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `590bf74986c5` · strategy list `a039f448c17bed72`*
