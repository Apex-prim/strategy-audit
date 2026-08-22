# Quickie

Source: [`PeetCrypto/freqtrade-stuff`](https://github.com/PeetCrypto/freqtrade-stuff) · file `Quickie.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 1780 | 5896 |
| average profit per trade % | -0.46 | -0.13 |
| win rate % | 92.8 | 93.7 |
| average trade duration, minutes | 2794.0 | 3144.0 |
| duration measured in own candles | 558.8 | 628.8 |
| expectancy per trade (USDT) | -0.41 | -0.14 |
| mean profit p-value | 0.0001029 | 0.09337 |
| market change % (baseline) | -58.23 | 346.34 |
| strategy total % | -73.81 | -83.74 |
| Sharpe | -4.29 | -1.04 |
| Sortino | -2.43 | -0.44 |
| max drawdown % | 75.21 | 91.87 |
| profit factor | 0.6 | 0.89 |

**Retained out of sample: negative**

> **Read that number with care.** The author's window was a bear market (buy-and-hold −58%) and the out-of-sample window a bull market (+346%). For a long-biased strategy this ratio rewards having done *badly* in 2018–2020, so it measures regime luck as much as robustness. The regime-free comparison is the excess over buy-and-hold, below.

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free either. Cross-strategy comparisons in this repository use average profit per trade in percent.

**Excess over buy-and-hold** (regime-free): author's window **-15.6 pp**, out of sample **-430.1 pp**.

Baseline: buy-and-hold on the same pairs returned **-58.23%**; the strategy returned **-73.81%**.
Out of sample: buy-and-hold **346.34%** vs strategy **-83.74%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | could not run | вывод не разобран |
| indicator recursion (freqtrade's own `recursive-analysis`) | clean | рекурсивных отклонений не найдено |
| прогрев не объявлен | **found** | самый длинный индикатор 200 свечей, startup_candle_count не задан (по умолчанию 0) |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **5m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `590bf74986c5` · strategy list `a039f448c17bed72`*
