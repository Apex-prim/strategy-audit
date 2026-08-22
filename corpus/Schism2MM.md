# Schism2MM

Source: [`PeetCrypto/freqtrade-stuff`](https://github.com/PeetCrypto/freqtrade-stuff) · file `Schism2MM.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 6 | 11 |
| average profit per trade % | 0.51 | 0.88 |
| win rate % | 83.3 | 100.0 |
| average trade duration, minutes | 68.0 | 39.0 |
| duration measured in own candles | 13.6 | 7.8 |
| expectancy per trade (USDT) | 0.63 | 1.09 |
| mean profit p-value | 0.01252 | 7.736e-05 |
| market change % (baseline) | -58.42 | 346.34 |
| strategy total % | 0.38 | 1.2 |
| Sharpe | 0.27 | 0.18 |
| Sortino | -100.0 | -100.0 |
| max drawdown % | 0.0 | 0.0 |
| profit factor | 3739.98 | 0.0 |

**Retained out of sample: 173%**

> **Read that number with care.** The author's window was a bear market (buy-and-hold −58%) and the out-of-sample window a bull market (+346%). For a long-biased strategy this ratio rewards having done *badly* in 2018–2020, so it measures regime luck as much as robustness. The regime-free comparison is the excess over buy-and-hold, below.

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free either. Cross-strategy comparisons in this repository use average profit per trade in percent.

**Excess over buy-and-hold** (regime-free): author's window **+58.8 pp**, out of sample **-345.1 pp**.

Baseline: buy-and-hold on the same pairs returned **-58.42%**; the strategy returned **0.38%**.
Out of sample: buy-and-hold **346.34%** vs strategy **1.2%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | could not run | код 1 |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | индикаторы меняются от объёма истории: rsi_1h 0.367% |
| прогрев не объявлен | **found** | самый длинный индикатор 14 свечей, startup_candle_count не задан (по умолчанию 0) |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **5m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `590bf74986c5` · strategy list `a039f448c17bed72`*
