# SMAIP3v2

Source: [`PeetCrypto/freqtrade-stuff`](https://github.com/PeetCrypto/freqtrade-stuff) · file `SMAIP3v2.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 95 | 376 |
| average profit per trade % | 0.98 | 0.62 |
| win rate % | 84.2 | 79.5 |
| average trade duration, minutes | 22.0 | 25.0 |
| duration measured in own candles | 4.4 | 5.0 |
| expectancy per trade (USDT) | 1.28 | 0.89 |
| mean profit p-value | 1.814e-10 | 3.174e-16 |
| market change % (baseline) | -59.05 | 346.34 |
| strategy total % | 12.14 | 33.36 |
| Sharpe | 1.83 | 1.34 |
| Sortino | 2.13 | 1.48 |
| max drawdown % | 1.19 | 3.23 |
| profit factor | 5.32 | 2.86 |

**Retained out of sample: 70%**

> **Read that number with care.** The author's window was a bear market (buy-and-hold −58%) and the out-of-sample window a bull market (+346%). For a long-biased strategy this ratio rewards having done *badly* in 2018–2020, so it measures regime luck as much as robustness. The regime-free comparison is the excess over buy-and-hold, below.

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free either. Cross-strategy comparisons in this repository use average profit per trade in percent.

**Excess over buy-and-hold** (regime-free): author's window **+71.2 pp**, out of sample **-313.0 pp**.

Baseline: buy-and-hold on the same pairs returned **-59.05%**; the strategy returned **12.14%**.
Out of sample: buy-and-hold **346.34%** vs strategy **33.36%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | could not run | вывод не разобран |
| indicator recursion (freqtrade's own `recursive-analysis`) | clean | рекурсивных отклонений не найдено |
| прогрев объявлен | clean | 200 при потребности 200 |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **5m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `590bf74986c5` · strategy list `a039f448c17bed72`*
