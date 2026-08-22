# SRsi

Source: [`davidzr/freqtrade-strategies`](https://github.com/davidzr/freqtrade-strategies) · file `SRsi.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 11981 | 11787 |
| average profit per trade % | -0.22 | -0.23 |
| win rate % | 34.3 | 34.7 |
| average trade duration, minutes | 25.0 | 22.0 |
| duration measured in own candles | 25.0 | 22.0 |
| expectancy per trade (USDT) | -0.08 | -0.08 |
| mean profit p-value | 5.055e-125 | 1.51e-80 |
| market change % (baseline) | -55.73 | 347.94 |
| strategy total % | -96.58 | -96.58 |
| Sharpe | -68.95 | -16.82 |
| Sortino | -66.71 | -14.76 |
| max drawdown % | 96.58 | 96.58 |
| profit factor | 0.37 | 0.34 |

**Retained out of sample: negative**

> **Read that number with care.** The author's window was a bear market (buy-and-hold −58%) and the out-of-sample window a bull market (+346%). For a long-biased strategy this ratio rewards having done *badly* in 2018–2020, so it measures regime luck as much as robustness. The regime-free comparison is the excess over buy-and-hold, below.

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free either. Cross-strategy comparisons in this repository use average profit per trade in percent.

**Excess over buy-and-hold** (regime-free): author's window **-40.9 pp**, out of sample **-444.5 pp**.

Baseline: buy-and-hold on the same pairs returned **-55.73%**; the strategy returned **-96.58%**.
Out of sample: buy-and-hold **347.94%** vs strategy **-96.58%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | clean | смещения не обнаружено |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | индикаторы меняются от объёма истории: rsi -0.380%, d 1.409% |
| прогрев не объявлен | **found** | самый длинный индикатор 30 свечей, startup_candle_count не задан (по умолчанию 0) |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **1m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `590bf74986c5` · strategy list `a039f448c17bed72`*
