# BBRSIOptimStrategy

Source: [`davidzr/freqtrade-strategies`](https://github.com/davidzr/freqtrade-strategies) · file `BBRSIOptimStrategy.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 2425 | 8272 |
| average profit per trade % | -0.28 | 0.07 |
| win rate % | 68.7 | 71.1 |
| average trade duration, minutes | 2491.0 | 2693.0 |
| duration measured in own candles | 498.2 | 538.6 |
| expectancy per trade (USDT) | -0.29 | -0.05 |
| mean profit p-value | 0.001221 | 0.8198 |
| market change % (baseline) | -58.37 | 346.34 |
| strategy total % | -71.51 | -37.99 |
| Sharpe | -4.17 | -0.17 |
| Sortino | -2.5 | -0.1 |
| max drawdown % | 75.59 | 88.71 |
| profit factor | 0.59 | 0.98 |

**Retained out of sample: negative**

> **Read that number with care.** The author's window was a bear market (buy-and-hold −58%) and the out-of-sample window a bull market (+346%). For a long-biased strategy this ratio rewards having done *badly* in 2018–2020, so it measures regime luck as much as robustness. The regime-free comparison is the excess over buy-and-hold, below.

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free either. Cross-strategy comparisons in this repository use average profit per trade in percent.

**Excess over buy-and-hold** (regime-free): author's window **-13.1 pp**, out of sample **-384.3 pp**.

Baseline: buy-and-hold on the same pairs returned **-58.37%**; the strategy returned **-71.51%**.
Out of sample: buy-and-hold **346.34%** vs strategy **-37.99%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | clean | смещения не обнаружено |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | индикаторы меняются от объёма истории: rsi 0.935% |
| прогрев не объявлен | **found** | самый длинный индикатор 20 свечей, startup_candle_count не задан (по умолчанию 0) |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **5m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `590bf74986c5` · strategy list `a039f448c17bed72`*
