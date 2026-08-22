# BBRSI4cust

Source: [`davidzr/freqtrade-strategies`](https://github.com/davidzr/freqtrade-strategies) · file `BBRSI4cust.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 7881 | 15005 |
| average profit per trade % | -0.2 | -0.18 |
| win rate % | 58.6 | 57.7 |
| average trade duration, minutes | 94.0 | 91.0 |
| duration measured in own candles | 6.27 | 6.07 |
| expectancy per trade (USDT) | -0.11 | -0.06 |
| mean profit p-value | 1.421e-42 | 2.749e-41 |
| market change % (baseline) | -58.53 | 345.85 |
| strategy total % | -85.4 | -96.56 |
| Sharpe | -31.97 | -13.38 |
| Sortino | -23.04 | -9.45 |
| max drawdown % | 85.42 | 96.58 |
| profit factor | 0.45 | 0.52 |

**Retained out of sample: negative**

> **Read that number with care.** The author's window was a bear market (buy-and-hold −58%) and the out-of-sample window a bull market (+346%). For a long-biased strategy this ratio rewards having done *badly* in 2018–2020, so it measures regime luck as much as robustness. The regime-free comparison is the excess over buy-and-hold, below.

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free either. Cross-strategy comparisons in this repository use average profit per trade in percent.

**Excess over buy-and-hold** (regime-free): author's window **-26.9 pp**, out of sample **-442.4 pp**.

Baseline: buy-and-hold on the same pairs returned **-58.53%**; the strategy returned **-85.4%**.
Out of sample: buy-and-hold **345.85%** vs strategy **-96.56%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | clean | смещения не обнаружено |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | индикаторы меняются от объёма истории: plus_di 2.181%, rsi -0.375% |
| прогрев не объявлен | **found** | самый длинный индикатор 20 свечей, startup_candle_count не задан (по умолчанию 0) |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **15m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `590bf74986c5` · strategy list `a039f448c17bed72`*
