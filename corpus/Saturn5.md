# Saturn5

Source: [`PeetCrypto/freqtrade-stuff`](https://github.com/PeetCrypto/freqtrade-stuff) · file `Saturn5.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 761 | 2595 |
| average profit per trade % | -0.58 | 0.05 |
| win rate % | 77.4 | 80.3 |
| average trade duration, minutes | 7894.0 | 8505.0 |
| duration measured in own candles | 526.27 | 567.0 |
| expectancy per trade (USDT) | -0.77 | -0.23 |
| mean profit p-value | 0.008394 | 0.5661 |
| market change % (baseline) | -59.37 | 345.85 |
| strategy total % | -58.58 | -59.66 |
| Sharpe | -1.92 | -0.24 |
| Sortino | -3.23 | -0.26 |
| max drawdown % | 67.39 | 89.46 |
| profit factor | 0.77 | 0.97 |

**Retained out of sample: negative**

> **Read that number with care.** The author's window was a bear market (buy-and-hold −58%) and the out-of-sample window a bull market (+346%). For a long-biased strategy this ratio rewards having done *badly* in 2018–2020, so it measures regime luck as much as robustness. The regime-free comparison is the excess over buy-and-hold, below.

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free either. Cross-strategy comparisons in this repository use average profit per trade in percent.

**Excess over buy-and-hold** (regime-free): author's window **+0.8 pp**, out of sample **-405.5 pp**.

Baseline: buy-and-hold on the same pairs returned **-59.37%**; the strategy returned **-58.58%**.
Out of sample: buy-and-hold **345.85%** vs strategy **-59.66%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | could not run | код 1 |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | индикаторы меняются от объёма истории: s2_ema_xxl_off 0.123%, s2_ema_xxl 0.123%, vwmacd 0.030%, signal -0.033% |
| прогрев не объявлен | **found** | самый длинный индикатор 200 свечей, startup_candle_count не задан (по умолчанию 0) |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **15m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `590bf74986c5` · strategy list `a039f448c17bed72`*
