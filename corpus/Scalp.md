# Scalp

Source: [`PeetCrypto/freqtrade-stuff`](https://github.com/PeetCrypto/freqtrade-stuff) · file `Scalp.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 13597 | 14817 |
| average profit per trade % | -0.2 | -0.18 |
| win rate % | 22.9 | 18.8 |
| average trade duration, minutes | 6.0 | 5.0 |
| duration measured in own candles | 6.0 | 5.0 |
| expectancy per trade (USDT) | -0.07 | -0.07 |
| mean profit p-value | 7.549e-228 | 1.731e-149 |
| market change % (baseline) | -55.54 | 347.94 |
| strategy total % | -96.59 | -96.57 |
| Sharpe | -100.12 | -25.94 |
| Sortino | -98.06 | -25.36 |
| max drawdown % | 96.59 | 96.57 |
| profit factor | 0.22 | 0.23 |

**Retained out of sample: negative**

> **Read that number with care.** The author's window was a bear market (buy-and-hold −58%) and the out-of-sample window a bull market (+346%). For a long-biased strategy this ratio rewards having done *badly* in 2018–2020, so it measures regime luck as much as robustness. The regime-free comparison is the excess over buy-and-hold, below.

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free either. Cross-strategy comparisons in this repository use average profit per trade in percent.

**Excess over buy-and-hold** (regime-free): author's window **-41.1 pp**, out of sample **-444.5 pp**.

Baseline: buy-and-hold on the same pairs returned **-55.54%**; the strategy returned **-96.59%**.
Out of sample: buy-and-hold **347.94%** vs strategy **-96.57%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | could not run | вывод не разобран |
| indicator recursion (freqtrade's own `recursive-analysis`) | clean | рекурсивных отклонений не найдено |
| прогрев не объявлен | **found** | самый длинный индикатор 20 свечей, startup_candle_count не задан (по умолчанию 0) |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **1m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `590bf74986c5` · strategy list `a039f448c17bed72`*
