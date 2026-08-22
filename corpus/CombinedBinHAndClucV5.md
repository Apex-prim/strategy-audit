# CombinedBinHAndClucV5

Source: [`PeetCrypto/freqtrade-stuff`](https://github.com/PeetCrypto/freqtrade-stuff) · file `CombinedBinHAndClucV5.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 797 | 2188 |
| average profit per trade % | -0.09 | 0.31 |
| win rate % | 64.6 | 73.5 |
| average trade duration, minutes | 182.0 | 130.0 |
| duration measured in own candles | 36.4 | 26.0 |
| expectancy per trade (USDT) | -0.12 | 0.56 |
| mean profit p-value | 0.2603 | 3.397e-06 |
| market change % (baseline) | -58.48 | 346.34 |
| strategy total % | -9.49 | 121.65 |
| Sharpe | -0.83 | 1.76 |
| Sortino | -0.91 | 1.47 |
| max drawdown % | 25.67 | 22.75 |
| profit factor | 0.9 | 1.32 |

**Retained out of sample: n/a**

> **Read that number with care.** The author's window was a bear market (buy-and-hold −58%) and the out-of-sample window a bull market (+346%). For a long-biased strategy this ratio rewards having done *badly* in 2018–2020, so it measures regime luck as much as robustness. The regime-free comparison is the excess over buy-and-hold, below.

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free either. Cross-strategy comparisons in this repository use average profit per trade in percent.

**Excess over buy-and-hold** (regime-free): author's window **+49.0 pp**, out of sample **-224.7 pp**.

⚠ **Not statistically significant in its author's own window** (p = 0.2603 > 0.05): the average trade is not distinguishable from zero.

Baseline: buy-and-hold on the same pairs returned **-58.48%**; the strategy returned **-9.49%**.
Out of sample: buy-and-hold **346.34%** vs strategy **121.65%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | could not run | вывод не разобран |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | индикаторы меняются от объёма истории: ema_slow 0.013% |
| прогрев не объявлен | **found** | самый длинный индикатор 50 свечей, startup_candle_count не задан (по умолчанию 0) |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **5m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `590bf74986c5` · strategy list `a039f448c17bed72`*
