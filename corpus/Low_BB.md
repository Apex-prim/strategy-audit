# Low_BB

Source: [`PeetCrypto/freqtrade-stuff`](https://github.com/PeetCrypto/freqtrade-stuff) · file `Low_BB.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 61 | 588 |
| average profit per trade % | -0.75 | 0.25 |
| win rate % | 14.8 | 24.1 |
| average trade duration, minutes | 187.0 | 1007.0 |
| duration measured in own candles | 187.0 | 1007.0 |
| expectancy per trade (USDT) | -0.9 | 0.31 |
| mean profit p-value | 0.01086 | 0.2557 |
| market change % (baseline) | -55.54 | 347.94 |
| strategy total % | -5.51 | 18.12 |
| Sharpe | -0.54 | 0.22 |
| Sortino | -33.9 | 9.21 |
| max drawdown % | 6.89 | 9.36 |
| profit factor | 0.47 | 1.18 |

**Retained out of sample: n/a**

> **Read that number with care.** The author's window was a bear market (buy-and-hold −58%) and the out-of-sample window a bull market (+346%). For a long-biased strategy this ratio rewards having done *badly* in 2018–2020, so it measures regime luck as much as robustness. The regime-free comparison is the excess over buy-and-hold, below.

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free either. Cross-strategy comparisons in this repository use average profit per trade in percent.

**Excess over buy-and-hold** (regime-free): author's window **+50.0 pp**, out of sample **-329.8 pp**.

Baseline: buy-and-hold on the same pairs returned **-55.54%**; the strategy returned **-5.51%**.
Out of sample: buy-and-hold **347.94%** vs strategy **18.12%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | could not run | вывод не разобран |
| indicator recursion (freqtrade's own `recursive-analysis`) | clean | рекурсивных отклонений не найдено |
| прогрев не объявлен | **found** | самый длинный индикатор 20 свечей, startup_candle_count не задан (по умолчанию 0) |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **1m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `590bf74986c5` · strategy list `a039f448c17bed72`*
