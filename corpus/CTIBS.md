# CTIBS

Source: [`jaredrsommer/freqtradestrategies`](https://github.com/jaredrsommer/freqtradestrategies) · file `CTIBS.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 1106 | 4447 |
| average profit per trade % | -0.58 | -0.37 |
| win rate % | 85.1 | 83.6 |
| average trade duration, minutes | 3785.0 | 3229.0 |
| duration measured in own candles | 252.33 | 215.27 |
| expectancy per trade (USDT) | -0.56 | -0.21 |
| mean profit p-value | 0.002067 | 0.0008994 |
| market change % (baseline) | -59.17 | 345.85 |
| strategy total % | -62.23 | -92.77 |
| Sharpe | -2.69 | -1.79 |
| Sortino | -2.36 | -1.01 |
| max drawdown % | 65.53 | 92.98 |
| profit factor | 0.72 | 0.8 |

**Retained out of sample: negative**

> **Read that number with care.** The author's window was a bear market (buy-and-hold −58%) and the out-of-sample window a bull market (+346%). For a long-biased strategy this ratio rewards having done *badly* in 2018–2020, so it measures regime luck as much as robustness. The regime-free comparison is the excess over buy-and-hold, below.

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free either. Cross-strategy comparisons in this repository use average profit per trade in percent.

**Excess over buy-and-hold** (regime-free): author's window **-3.1 pp**, out of sample **-438.6 pp**.

Baseline: buy-and-hold on the same pairs returned **-59.17%**; the strategy returned **-62.23%**.
Out of sample: buy-and-hold **345.85%** vs strategy **-92.77%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | clean | смещения не обнаружено |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | индикаторы меняются от объёма истории: ema_dif35 -2.866% |
| прогрев не объявлен | **found** | самый длинный индикатор 32 свечей, startup_candle_count не задан (по умолчанию 0) |
| трейлинг на полном стопе | **found** | trailing_stop=True без trailing_stop_positive ⇒ стоп тащится на ВСЁ расстояние стоп-лосса |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **15m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `590bf74986c5` · strategy list `a039f448c17bed72`*
