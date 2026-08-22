# NormalizerStrategy

Source: [`davidzr/freqtrade-strategies`](https://github.com/davidzr/freqtrade-strategies) · file `NormalizerStrategy.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 970 | 2777 |
| average profit per trade % | -0.82 | -0.73 |
| win rate % | 40.3 | 42.3 |
| average trade duration, minutes | 332.0 | 386.0 |
| duration measured in own candles | 5.53 | 6.43 |
| expectancy per trade (USDT) | -0.65 | -0.33 |
| mean profit p-value | 8.168e-18 | 4.409e-24 |
| market change % (baseline) | -51.25 | 348.67 |
| strategy total % | -63.39 | -92.16 |
| Sharpe | -7.4 | -4.35 |
| Sortino | -8.66 | -4.48 |
| max drawdown % | 63.66 | 92.25 |
| profit factor | 0.44 | 0.4 |

**Retained out of sample: negative**

> **Read that number with care.** The author's window was a bear market (buy-and-hold −58%) and the out-of-sample window a bull market (+346%). For a long-biased strategy this ratio rewards having done *badly* in 2018–2020, so it measures regime luck as much as robustness. The regime-free comparison is the excess over buy-and-hold, below.

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free either. Cross-strategy comparisons in this repository use average profit per trade in percent.

**Excess over buy-and-hold** (regime-free): author's window **-12.1 pp**, out of sample **-440.8 pp**.

Baseline: buy-and-hold on the same pairs returned **-51.25%**; the strategy returned **-63.39%**.
Out of sample: buy-and-hold **348.67%** vs strategy **-92.16%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | clean | смещения не обнаружено |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | индикаторы меняются от объёма истории: pct_sum -33.617% |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **1h** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `590bf74986c5` · strategy list `a039f448c17bed72`*
