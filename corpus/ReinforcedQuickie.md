# ReinforcedQuickie

Source: [`PeetCrypto/freqtrade-stuff`](https://github.com/PeetCrypto/freqtrade-stuff) · file `ReinforcedQuickie.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 5080 | 18998 |
| average profit per trade % | -0.2 | -0.13 |
| win rate % | 67.9 | 69.1 |
| average trade duration, minutes | 427.0 | 441.0 |
| duration measured in own candles | 85.4 | 88.2 |
| expectancy per trade (USDT) | -0.15 | -0.05 |
| mean profit p-value | 3.172e-14 | 3.331e-09 |
| market change % (baseline) | -58.23 | 346.34 |
| strategy total % | -73.77 | -95.91 |
| Sharpe | -14.18 | -6.6 |
| Sortino | -11.86 | -4.8 |
| max drawdown % | 74.7 | 96.25 |
| profit factor | 0.71 | 0.85 |

**Retained out of sample: negative**

> **Read that number with care.** The author's window was a bear market (buy-and-hold −58%) and the out-of-sample window a bull market (+346%). For a long-biased strategy this ratio rewards having done *badly* in 2018–2020, so it measures regime luck as much as robustness. The regime-free comparison is the excess over buy-and-hold, below.

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free either. Cross-strategy comparisons in this repository use average profit per trade in percent.

**Excess over buy-and-hold** (regime-free): author's window **-15.5 pp**, out of sample **-442.2 pp**.

Baseline: buy-and-hold on the same pairs returned **-58.23%**; the strategy returned **-73.77%**.
Out of sample: buy-and-hold **346.34%** vs strategy **-95.91%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | **found** | ЕСТЬ СМЕЩЕНИЕ: входов 0, выходов 0 из 20 сигналов |
| indicator recursion (freqtrade's own `recursive-analysis`) | clean | рекурсивных отклонений не найдено |
| прогрев не объявлен | **found** | самый длинный индикатор 30 свечей, startup_candle_count не задан (по умолчанию 0) |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **5m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `590bf74986c5` · strategy list `a039f448c17bed72`*
