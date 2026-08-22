# eltoro

Source: [`jaredrsommer/freqtradestrategies`](https://github.com/jaredrsommer/freqtradestrategies) · file `eltoro.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 777 | 2927 |
| average profit per trade % | -1.33 | -0.3 |
| win rate % | 86.9 | 90.6 |
| average trade duration, minutes | 5144.0 | 5009.0 |
| duration measured in own candles | 342.93 | 333.93 |
| expectancy per trade (USDT) | -1.01 | -0.28 |
| mean profit p-value | 2.866e-06 | 0.02858 |
| market change % (baseline) | -59.09 | 345.85 |
| strategy total % | -78.26 | -82.54 |
| Sharpe | -3.44 | -0.96 |
| Sortino | -2.88 | -0.54 |
| max drawdown % | 78.38 | 88.48 |
| profit factor | 0.48 | 0.83 |

**Retained out of sample: negative**

> **Read that number with care.** The author's window was a bear market (buy-and-hold −58%) and the out-of-sample window a bull market (+346%). For a long-biased strategy this ratio rewards having done *badly* in 2018–2020, so it measures regime luck as much as robustness. The regime-free comparison is the excess over buy-and-hold, below.

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free either. Cross-strategy comparisons in this repository use average profit per trade in percent.

**Excess over buy-and-hold** (regime-free): author's window **-19.2 pp**, out of sample **-428.4 pp**.

Baseline: buy-and-hold on the same pairs returned **-59.09%**; the strategy returned **-78.26%**.
Out of sample: buy-and-hold **345.85%** vs strategy **-82.54%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | clean | смещения не обнаружено |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | индикаторы меняются от объёма истории: BTC_EWO_Fast_1h 7.925%, ema_dif25 14.222%, rsi -0.238%, rsi_ma -0.280%, rsi_ma_pcnt -7.901% |
| прогрев занижен | **found** | объявлено 79, нужно не менее 200 |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **15m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `590bf74986c5` · strategy list `a039f448c17bed72`*
