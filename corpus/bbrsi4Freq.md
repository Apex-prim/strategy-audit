# bbrsi4Freq

Source: [`davidzr/freqtrade-strategies`](https://github.com/davidzr/freqtrade-strategies) · file `bbrsi4Freq.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 1067 | 3724 |
| average profit per trade % | -0.45 | -0.18 |
| win rate % | 56.3 | 60.6 |
| average trade duration, minutes | 334.0 | 302.0 |
| duration measured in own candles | 5.57 | 5.03 |
| expectancy per trade (USDT) | -0.43 | -0.16 |
| mean profit p-value | 5.296e-09 | 0.0006309 |
| market change % (baseline) | -59.27 | 348.67 |
| strategy total % | -45.93 | -58.63 |
| Sharpe | -5.04 | -1.69 |
| Sortino | -4.46 | -1.34 |
| max drawdown % | 46.11 | 64.91 |
| profit factor | 0.48 | 0.77 |

**Retained out of sample: negative**

> **Read that number with care.** The author's window was a bear market (buy-and-hold −58%) and the out-of-sample window a bull market (+346%). For a long-biased strategy this ratio rewards having done *badly* in 2018–2020, so it measures regime luck as much as robustness. The regime-free comparison is the excess over buy-and-hold, below.

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free either. Cross-strategy comparisons in this repository use average profit per trade in percent.

**Excess over buy-and-hold** (regime-free): author's window **+13.3 pp**, out of sample **-407.3 pp**.

Baseline: buy-and-hold on the same pairs returned **-59.27%**; the strategy returned **-45.93%**.
Out of sample: buy-and-hold **348.67%** vs strategy **-58.63%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | clean | смещения не обнаружено |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | индикаторы меняются от объёма истории: rsi 4.044% |
| прогрев не объявлен | **found** | самый длинный индикатор 20 свечей, startup_candle_count не задан (по умолчанию 0) |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **1h** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `590bf74986c5` · strategy list `a039f448c17bed72`*
