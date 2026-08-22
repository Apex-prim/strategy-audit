# SampleStrategyV2

Source: [`PeetCrypto/freqtrade-stuff`](https://github.com/PeetCrypto/freqtrade-stuff) · file `Machete.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 1400 | 4482 |
| average profit per trade % | -0.69 | -0.26 |
| win rate % | 89.6 | 91.7 |
| average trade duration, minutes | 2266.0 | 2659.0 |
| duration measured in own candles | 453.2 | 531.8 |
| expectancy per trade (USDT) | -0.53 | -0.18 |
| mean profit p-value | 9.909e-07 | 0.0006767 |
| market change % (baseline) | -59.3 | 346.34 |
| strategy total % | -73.72 | -82.76 |
| Sharpe | -4.83 | -1.84 |
| Sortino | -2.87 | -0.83 |
| max drawdown % | 74.09 | 85.26 |
| profit factor | 0.51 | 0.76 |

**Retained out of sample: negative**

> **Read that number with care.** The author's window was a bear market (buy-and-hold −58%) and the out-of-sample window a bull market (+346%). For a long-biased strategy this ratio rewards having done *badly* in 2018–2020, so it measures regime luck as much as robustness. The regime-free comparison is the excess over buy-and-hold, below.

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free either. Cross-strategy comparisons in this repository use average profit per trade in percent.

**Excess over buy-and-hold** (regime-free): author's window **-14.4 pp**, out of sample **-429.1 pp**.

Baseline: buy-and-hold on the same pairs returned **-59.3%**; the strategy returned **-73.72%**.
Out of sample: buy-and-hold **346.34%** vs strategy **-82.76%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | could not run | вывод не разобран |
| indicator recursion (freqtrade's own `recursive-analysis`) | clean | рекурсивных отклонений не найдено |
| прогрев не объявлен | **found** | самый длинный индикатор 100 свечей, startup_candle_count не задан (по умолчанию 0) |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **5m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `590bf74986c5` · strategy list `a039f448c17bed72`*
