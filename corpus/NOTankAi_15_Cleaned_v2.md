# NOTankAi_15_Cleaned_v2

Source: [`TheoBrigitte/freqtrade`](https://github.com/TheoBrigitte/freqtrade) · file `NOTankAi_15_Cleaned_v2.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 3528 | 11207 |
| average profit per trade % | 1.67 | 1.87 |
| win rate % | 95.3 | 94.9 |
| average trade duration, minutes | 148.0 | 174.0 |
| duration measured in own candles | 9.87 | 11.6 |
| expectancy per trade (USDT) | 345.76 | 56790.67 |
| mean profit p-value | 8.383e-92 | 0.0 |
| market change % (baseline) | -59.49 | 345.85 |
| strategy total % | 121982.94 | 63645298.3 |
| Sharpe | 32.63 | 49.3 |
| Sortino | 39.73 | 58.8 |
| max drawdown % | 0.98 | 0.27 |
| profit factor | 36.04 | 29.24 |

**Retained out of sample: 16425%**

> **Read that number with care.** The author's window was a bear market (buy-and-hold −58%) and the out-of-sample window a bull market (+346%). For a long-biased strategy this ratio rewards having done *badly* in 2018–2020, so it measures regime luck as much as robustness. The regime-free comparison is the excess over buy-and-hold, below.

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free either. Cross-strategy comparisons in this repository use average profit per trade in percent.

**Excess over buy-and-hold** (regime-free): author's window **+122042.4 pp**, out of sample **+63644952.4 pp**.

Baseline: buy-and-hold on the same pairs returned **-59.49%**; the strategy returned **121982.94%**.
Out of sample: buy-and-hold **345.85%** vs strategy **63645298.3%** — **beats the baseline**.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | clean | смещения не обнаружено |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | индикаторы меняются от объёма истории: min_threshold_mean 9.210%, max_threshold_mean 9.000% |
| прогрев не объявлен | **found** | самый длинный индикатор 20 свечей, startup_candle_count не задан (по умолчанию 0) |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **15m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `590bf74986c5` · strategy list `a039f448c17bed72`*
