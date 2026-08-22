# CofiBitStrategy

Source: [`PeetCrypto/freqtrade-stuff`](https://github.com/PeetCrypto/freqtrade-stuff) · file `CofiBitStrategy.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 7429 | 20015 |
| average profit per trade % | -0.17 | -0.14 |
| win rate % | 41.0 | 42.0 |
| average trade duration, minutes | 30.0 | 28.0 |
| duration measured in own candles | 6.0 | 5.6 |
| expectancy per trade (USDT) | -0.11 | -0.05 |
| mean profit p-value | 1.463e-54 | 1.374e-21 |
| market change % (baseline) | -58.23 | 346.34 |
| strategy total % | -79.75 | -96.68 |
| Sharpe | -35.33 | -10.93 |
| Sortino | -33.49 | -10.67 |
| max drawdown % | 80.11 | 96.69 |
| profit factor | 0.47 | 0.7 |

**Retained out of sample: negative**

> **Read that number with care.** The author's window was a bear market (buy-and-hold −58%) and the out-of-sample window a bull market (+346%). For a long-biased strategy this ratio rewards having done *badly* in 2018–2020, so it measures regime luck as much as robustness. The regime-free comparison is the excess over buy-and-hold, below.

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free either. Cross-strategy comparisons in this repository use average profit per trade in percent.

**Excess over buy-and-hold** (regime-free): author's window **-21.5 pp**, out of sample **-443.0 pp**.

Baseline: buy-and-hold on the same pairs returned **-58.23%**; the strategy returned **-79.75%**.
Out of sample: buy-and-hold **346.34%** vs strategy **-96.68%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | could not run | вывод не разобран |
| indicator recursion (freqtrade's own `recursive-analysis`) | clean | рекурсивных отклонений не найдено |
| прогрев не объявлен | **found** | самый длинный индикатор 5 свечей, startup_candle_count не задан (по умолчанию 0) |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **5m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `590bf74986c5` · strategy list `a039f448c17bed72`*
