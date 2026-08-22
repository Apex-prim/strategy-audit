# Cluc7werk

Source: [`PeetCrypto/freqtrade-stuff`](https://github.com/PeetCrypto/freqtrade-stuff) · file `Cluc7werk.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 303 | — |
| average profit per trade % | -0.64 | — |
| win rate % | 32.0 | — |
| average trade duration, minutes | 13.0 | — |
| duration measured in own candles | 13.0 | — |
| expectancy per trade (USDT) | -0.71 | — |
| mean profit p-value | 5.648e-15 | — |
| market change % (baseline) | -55.61 | — |
| strategy total % | -21.39 | — |
| Sharpe | -3.76 | — |
| Sortino | -6.85 | — |
| max drawdown % | 21.81 | — |
| profit factor | 0.33 | — |

**Retained out of sample: —**

> **Read that number with care.** The author's window was a bear market (buy-and-hold −58%) and the out-of-sample window a bull market (+346%). For a long-biased strategy this ratio rewards having done *badly* in 2018–2020, so it measures regime luck as much as robustness. The regime-free comparison is the excess over buy-and-hold, below.

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free either. Cross-strategy comparisons in this repository use average profit per trade in percent.

**Excess over buy-and-hold** (regime-free): author's window **+34.2 pp**.

Baseline: buy-and-hold on the same pairs returned **-55.61%**; the strategy returned **-21.39%**.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | could not run | код 1 |
| indicator recursion (freqtrade's own `recursive-analysis`) | clean | рекурсивных отклонений не найдено |
| прогрев не объявлен | **found** | самый длинный индикатор 48 свечей, startup_candle_count не задан (по умолчанию 0) |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **1m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `590bf74986c5` · strategy list `a039f448c17bed72`*
