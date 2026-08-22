# CombinedBinHAndClucV7

Source: [`PeetCrypto/freqtrade-stuff`](https://github.com/PeetCrypto/freqtrade-stuff) · file `CombinedBinHAndClucV7.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 211 | 678 |
| average profit per trade % | 0.61 | 0.57 |
| win rate % | 74.9 | 71.8 |
| average trade duration, minutes | 185.0 | 203.0 |
| duration measured in own candles | 37.0 | 40.6 |
| expectancy per trade (USDT) | 0.81 | 0.89 |
| mean profit p-value | 0.0003524 | 7.477e-09 |
| market change % (baseline) | -59.05 | 346.34 |
| strategy total % | 17.18 | 60.21 |
| Sharpe | 1.38 | 1.23 |
| Sortino | 1.38 | 1.38 |
| max drawdown % | 4.73 | 3.72 |
| profit factor | 1.84 | 1.72 |

**Retained out of sample: 110%**

> **Read that number with care.** The author's window was a bear market (buy-and-hold −58%) and the out-of-sample window a bull market (+346%). For a long-biased strategy this ratio rewards having done *badly* in 2018–2020, so it measures regime luck as much as robustness. The regime-free comparison is the excess over buy-and-hold, below.

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free either. Cross-strategy comparisons in this repository use average profit per trade in percent.

**Excess over buy-and-hold** (regime-free): author's window **+76.2 pp**, out of sample **-286.1 pp**.

Baseline: buy-and-hold on the same pairs returned **-59.05%**; the strategy returned **17.18%**.
Out of sample: buy-and-hold **346.34%** vs strategy **60.21%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | could not run | вывод не разобран |
| indicator recursion (freqtrade's own `recursive-analysis`) | clean | рекурсивных отклонений не найдено |
| прогрев не объявлен | **found** | самый длинный индикатор 200 свечей, startup_candle_count не задан (по умолчанию 0) |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **5m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `590bf74986c5` · strategy list `a039f448c17bed72`*
