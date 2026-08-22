# NFI5MOHO

Source: [`PeetCrypto/freqtrade-stuff`](https://github.com/PeetCrypto/freqtrade-stuff) · file `NFI5MOHO.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 38 | 340 |
| average profit per trade % | 1.44 | 1.33 |
| win rate % | 92.1 | 82.1 |
| average trade duration, minutes | 120.0 | 82.0 |
| duration measured in own candles | 24.0 | 16.4 |
| expectancy per trade (USDT) | 1.83 | 2.12 |
| mean profit p-value | 0.0236 | 1.063e-05 |
| market change % (baseline) | -59.35 | 346.34 |
| strategy total % | 6.95 | 72.0 |
| Sharpe | 0.39 | 0.67 |
| Sortino | 7.57 | 1.96 |
| max drawdown % | 1.26 | 13.34 |
| profit factor | 2.78 | 1.81 |

**Retained out of sample: 116%**

> **Read that number with care.** The author's window was a bear market (buy-and-hold −58%) and the out-of-sample window a bull market (+346%). For a long-biased strategy this ratio rewards having done *badly* in 2018–2020, so it measures regime luck as much as robustness. The regime-free comparison is the excess over buy-and-hold, below.

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free either. Cross-strategy comparisons in this repository use average profit per trade in percent.

**Excess over buy-and-hold** (regime-free): author's window **+66.3 pp**, out of sample **-274.3 pp**.

Baseline: buy-and-hold on the same pairs returned **-59.35%**; the strategy returned **6.95%**.
Out of sample: buy-and-hold **346.34%** vs strategy **72.0%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | could not run | вывод не разобран |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | индикаторы меняются от объёма истории: ema_100_1h -0.014%, ewo -12.317% |
| прогрев не объявлен | **found** | самый длинный индикатор 200 свечей, startup_candle_count не задан (по умолчанию 0) |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **5m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `590bf74986c5` · strategy list `a039f448c17bed72`*
