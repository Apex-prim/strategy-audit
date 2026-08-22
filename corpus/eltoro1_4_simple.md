# eltoro1_4_simple

Source: [`jaredrsommer/freqtradestrategies`](https://github.com/jaredrsommer/freqtradestrategies) · file `eltoro1_4_simple.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 496 | 1921 |
| average profit per trade % | -1.28 | 0.03 |
| win rate % | 79.2 | 82.4 |
| average trade duration, minutes | 8096.0 | 7577.0 |
| duration measured in own candles | 539.73 | 505.13 |
| expectancy per trade (USDT) | -1.29 | -0.27 |
| mean profit p-value | 0.0006008 | 0.2491 |
| market change % (baseline) | -59.09 | 345.85 |
| strategy total % | -64.13 | -51.7 |
| Sharpe | -2.01 | -0.41 |
| Sortino | -2.62 | -0.47 |
| max drawdown % | 64.45 | 63.65 |
| profit factor | 0.62 | 0.92 |

**Retained out of sample: negative**

> **Read that number with care.** The author's window was a bear market (buy-and-hold −58%) and the out-of-sample window a bull market (+346%). For a long-biased strategy this ratio rewards having done *badly* in 2018–2020, so it measures regime luck as much as robustness. The regime-free comparison is the excess over buy-and-hold, below.

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free either. Cross-strategy comparisons in this repository use average profit per trade in percent.

**Excess over buy-and-hold** (regime-free): author's window **-5.0 pp**, out of sample **-397.6 pp**.

Baseline: buy-and-hold on the same pairs returned **-59.09%**; the strategy returned **-64.13%**.
Out of sample: buy-and-hold **345.85%** vs strategy **-51.7%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | clean | смещения не обнаружено |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | индикаторы меняются от объёма истории: INFEWO_4h -1.742%, BTC_EWO_Fast_4h -1.742%, rsi -0.238%, rsi_ma -0.280%, rsi_ma_pcnt -7.901% |
| прогрев занижен | **found** | объявлено 79, нужно не менее 200 |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **15m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `590bf74986c5` · strategy list `a039f448c17bed72`*
