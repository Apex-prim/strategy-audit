# bbrsi

Source: [`davidzr/freqtrade-strategies`](https://github.com/davidzr/freqtrade-strategies) · file `BBRSI.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 1201 | 4306 |
| average profit per trade % | -1.17 | -0.54 |
| win rate % | 57.9 | 60.5 |
| average trade duration, minutes | 2918.0 | 3013.0 |
| duration measured in own candles | 12.16 | 12.55 |
| expectancy per trade (USDT) | -0.73 | -0.22 |
| mean profit p-value | 1.533e-07 | 1.093e-06 |
| market change % (baseline) | -58.5 | 340.8 |
| strategy total % | -87.36 | -96.8 |
| Sharpe | -4.82 | -2.59 |
| Sortino | -3.21 | -1.68 |
| max drawdown % | 87.36 | 96.81 |
| profit factor | 0.11 | 0.33 |

**Retained out of sample: negative**

> **Read that number with care.** The author's window was a bear market (buy-and-hold −58%) and the out-of-sample window a bull market (+346%). For a long-biased strategy this ratio rewards having done *badly* in 2018–2020, so it measures regime luck as much as robustness. The regime-free comparison is the excess over buy-and-hold, below.

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free either. Cross-strategy comparisons in this repository use average profit per trade in percent.

**Excess over buy-and-hold** (regime-free): author's window **-28.9 pp**, out of sample **-437.6 pp**.

Baseline: buy-and-hold on the same pairs returned **-58.5%**; the strategy returned **-87.36%**.
Out of sample: buy-and-hold **340.8%** vs strategy **-96.8%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | clean | смещения не обнаружено |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | индикаторы меняются от объёма истории: rsi 4.632% |
| прогрев не объявлен | **found** | самый длинный индикатор 20 свечей, startup_candle_count не задан (по умолчанию 0) |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **4h** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `590bf74986c5` · strategy list `a039f448c17bed72`*
