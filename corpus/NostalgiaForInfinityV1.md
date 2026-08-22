# NostalgiaForInfinityV1

Source: [`PeetCrypto/freqtrade-stuff`](https://github.com/PeetCrypto/freqtrade-stuff) · file `NostalgiaForInfinityV1.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 769 | 2688 |
| average profit per trade % | 0.33 | 0.3 |
| win rate % | 61.9 | 58.1 |
| average trade duration, minutes | 334.0 | 384.0 |
| duration measured in own candles | 66.8 | 76.8 |
| expectancy per trade (USDT) | 0.47 | 0.59 |
| mean profit p-value | 0.0002134 | 0.0001009 |
| market change % (baseline) | -59.05 | 346.34 |
| strategy total % | 36.15 | 159.61 |
| Sharpe | 2.7 | 1.63 |
| Sortino | 3.02 | 1.85 |
| max drawdown % | 7.61 | 15.66 |
| profit factor | 1.49 | 1.27 |

**Retained out of sample: 126%**

> **Read that number with care.** The author's window was a bear market (buy-and-hold −58%) and the out-of-sample window a bull market (+346%). For a long-biased strategy this ratio rewards having done *badly* in 2018–2020, so it measures regime luck as much as robustness. The regime-free comparison is the excess over buy-and-hold, below.

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free either. Cross-strategy comparisons in this repository use average profit per trade in percent.

**Excess over buy-and-hold** (regime-free): author's window **+95.2 pp**, out of sample **-186.7 pp**.

Baseline: buy-and-hold on the same pairs returned **-59.05%**; the strategy returned **36.15%**.
Out of sample: buy-and-hold **346.34%** vs strategy **159.61%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | could not run | вывод не разобран |
| indicator recursion (freqtrade's own `recursive-analysis`) | clean | рекурсивных отклонений не найдено |
| прогрев не объявлен | **found** | самый длинный индикатор 200 свечей, startup_candle_count не задан (по умолчанию 0) |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **5m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `590bf74986c5` · strategy list `a039f448c17bed72`*
