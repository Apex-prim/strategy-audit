# Tank1Modulus

Source: [`TheoBrigitte/freqtrade`](https://github.com/TheoBrigitte/freqtrade) · file `Tank1Modulus.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 94 | 506 |
| average profit per trade % | -2.27 | 0.61 |
| win rate % | 92.6 | 98.6 |
| average trade duration, minutes | 60708.0 | 39464.0 |
| duration measured in own candles | 1011.8 | 657.73 |
| expectancy per trade (USDT) | -1.73 | 0.4 |
| mean profit p-value | 0.1719 | 0.351 |
| market change % (baseline) | -54.03 | 348.67 |
| strategy total % | -16.3 | 20.16 |
| Sharpe | -0.36 | 0.17 |
| Sortino | -0.23 | 0.08 |
| max drawdown % | 25.13 | 30.98 |
| profit factor | 0.42 | 1.37 |

**Retained out of sample: n/a**

> **Read that number with care.** The author's window was a bear market (buy-and-hold −58%) and the out-of-sample window a bull market (+346%). For a long-biased strategy this ratio rewards having done *badly* in 2018–2020, so it measures regime luck as much as robustness. The regime-free comparison is the excess over buy-and-hold, below.

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free either. Cross-strategy comparisons in this repository use average profit per trade in percent.

**Excess over buy-and-hold** (regime-free): author's window **+37.7 pp**, out of sample **-328.5 pp**.

⚠ **Not statistically significant in its author's own window** (p = 0.1719 > 0.05): the average trade is not distinguishable from zero.

Baseline: buy-and-hold on the same pairs returned **-54.03%**; the strategy returned **-16.3%**.
Out of sample: buy-and-hold **348.67%** vs strategy **20.16%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | **found** | ЕСТЬ СМЕЩЕНИЕ: входов 15, выходов 19 из 20 сигналов |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | индикаторы меняются от объёма истории: obv -54.929%, wave_t1_MEAN_UP 17.038%, wave_t1_MEAN_DN 36.405%, wave_t1_UP_FIB 17.038%, wave_t1_DN_FIB 36.405% |
| прогрев не объявлен | **found** | самый длинный индикатор 200 свечей, startup_candle_count не задан (по умолчанию 0) |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **1h** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `590bf74986c5` · strategy list `a039f448c17bed72`*
