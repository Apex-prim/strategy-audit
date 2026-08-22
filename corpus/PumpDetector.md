# PumpDetector

Source: [`davidzr/freqtrade-strategies`](https://github.com/davidzr/freqtrade-strategies) · file `PumpDetector.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 13347 | 18911 |
| average profit per trade % | -0.2 | -0.14 |
| win rate % | 52.0 | 56.5 |
| average trade duration, minutes | 131.0 | 116.0 |
| duration measured in own candles | 26.2 | 23.2 |
| expectancy per trade (USDT) | -0.07 | -0.05 |
| mean profit p-value | 2.106e-31 | 3.294e-22 |
| market change % (baseline) | -58.37 | 346.34 |
| strategy total % | -96.58 | -96.75 |
| Sharpe | -35.34 | -10.79 |
| Sortino | -29.68 | -8.11 |
| max drawdown % | 96.6 | 96.76 |
| profit factor | 0.6 | 0.67 |

**Retained out of sample: negative**

> **Read that number with care.** The author's window was a bear market (buy-and-hold −58%) and the out-of-sample window a bull market (+346%). For a long-biased strategy this ratio rewards having done *badly* in 2018–2020, so it measures regime luck as much as robustness. The regime-free comparison is the excess over buy-and-hold, below.

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free either. Cross-strategy comparisons in this repository use average profit per trade in percent.

**Excess over buy-and-hold** (regime-free): author's window **-38.2 pp**, out of sample **-443.1 pp**.

Baseline: buy-and-hold on the same pairs returned **-58.37%**; the strategy returned **-96.58%**.
Out of sample: buy-and-hold **346.34%** vs strategy **-96.75%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | clean | смещения не обнаружено |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | индикаторы меняются от объёма истории: k -1.582%, d -5.693%, j 17.992% |
| прогрев не объявлен | **found** | самый длинный индикатор 3 свечей, startup_candle_count не задан (по умолчанию 0) |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **5m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `590bf74986c5` · strategy list `a039f448c17bed72`*
