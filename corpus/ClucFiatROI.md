# ClucFiatROI

Source: [`PeetCrypto/freqtrade-stuff`](https://github.com/PeetCrypto/freqtrade-stuff) · file `ClucFiatROI.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 1292 | 4734 |
| average profit per trade % | -0.16 | 0.27 |
| win rate % | 82.0 | 85.6 |
| average trade duration, minutes | 2765.0 | 2211.0 |
| duration measured in own candles | 553.0 | 442.2 |
| expectancy per trade (USDT) | -0.26 | 0.44 |
| mean profit p-value | 0.1486 | 0.08502 |
| market change % (baseline) | -58.41 | 346.34 |
| strategy total % | -33.61 | 206.7 |
| Sharpe | -1.36 | 0.96 |
| Sortino | -0.65 | 0.4 |
| max drawdown % | 38.26 | 60.85 |
| profit factor | 0.77 | 1.19 |

**Retained out of sample: n/a**

> **Read that number with care.** The author's window was a bear market (buy-and-hold −58%) and the out-of-sample window a bull market (+346%). For a long-biased strategy this ratio rewards having done *badly* in 2018–2020, so it measures regime luck as much as robustness. The regime-free comparison is the excess over buy-and-hold, below.

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free either. Cross-strategy comparisons in this repository use average profit per trade in percent.

**Excess over buy-and-hold** (regime-free): author's window **+24.8 pp**, out of sample **-139.6 pp**.

⚠ **Not statistically significant in its author's own window** (p = 0.1486 > 0.05): the average trade is not distinguishable from zero.

Baseline: buy-and-hold on the same pairs returned **-58.41%**; the strategy returned **-33.61%**.
Out of sample: buy-and-hold **346.34%** vs strategy **206.7%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | could not run | вывод не разобран |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | индикаторы меняются от объёма истории: ema_slow 0.012%, rsi 0.110% |
| прогрев не объявлен | **found** | самый длинный индикатор 48 свечей, startup_candle_count не задан (по умолчанию 0) |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **5m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `590bf74986c5` · strategy list `a039f448c17bed72`*
