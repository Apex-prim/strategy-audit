# FrostAuraM31hStrategy

Source: [`PeetCrypto/freqtrade-stuff`](https://github.com/PeetCrypto/freqtrade-stuff) · file `FrostAuraM31hStrategy.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 533 | 1936 |
| average profit per trade % | -1.51 | -0.27 |
| win rate % | 59.1 | 62.5 |
| average trade duration, minutes | 5667.0 | 5343.0 |
| duration measured in own candles | 94.45 | 89.05 |
| expectancy per trade (USDT) | -1.29 | -0.32 |
| mean profit p-value | 1.195e-05 | 0.08998 |
| market change % (baseline) | -59.27 | 348.67 |
| strategy total % | -68.7 | -62.28 |
| Sharpe | -2.68 | -0.6 |
| Sortino | -2.01 | -0.46 |
| max drawdown % | 68.96 | 71.59 |
| profit factor | 0.39 | 0.84 |

**Retained out of sample: negative**

> **Read that number with care.** The author's window was a bear market (buy-and-hold −58%) and the out-of-sample window a bull market (+346%). For a long-biased strategy this ratio rewards having done *badly* in 2018–2020, so it measures regime luck as much as robustness. The regime-free comparison is the excess over buy-and-hold, below.

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free either. Cross-strategy comparisons in this repository use average profit per trade in percent.

**Excess over buy-and-hold** (regime-free): author's window **-9.4 pp**, out of sample **-411.0 pp**.

Baseline: buy-and-hold on the same pairs returned **-59.27%**; the strategy returned **-68.7%**.
Out of sample: buy-and-hold **348.67%** vs strategy **-62.28%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | could not run | вывод не разобран |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | индикаторы меняются от объёма истории: rsi 4.044% |
| прогрев не объявлен | **found** | самый длинный индикатор 20 свечей, startup_candle_count не задан (по умолчанию 0) |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **1h** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `590bf74986c5` · strategy list `a039f448c17bed72`*
