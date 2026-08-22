# NormalizerStrategyHO2

Source: [`PeetCrypto/freqtrade-stuff`](https://github.com/PeetCrypto/freqtrade-stuff) · file `NormalizerStrategyHO2 (1).py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 819 | 2330 |
| average profit per trade % | -0.45 | -0.11 |
| win rate % | 33.0 | 37.0 |
| average trade duration, minutes | 872.0 | 935.0 |
| duration measured in own candles | 14.53 | 15.58 |
| expectancy per trade (USDT) | -0.48 | -0.15 |
| mean profit p-value | 0.0008315 | 0.1775 |
| market change % (baseline) | -51.25 | 348.67 |
| strategy total % | -39.02 | -35.85 |
| Sharpe | -2.6 | -0.53 |
| Sortino | -4.94 | -0.99 |
| max drawdown % | 43.14 | 54.68 |
| profit factor | 0.73 | 0.92 |

**Retained out of sample: negative**

> **Read that number with care.** The author's window was a bear market (buy-and-hold −58%) and the out-of-sample window a bull market (+346%). For a long-biased strategy this ratio rewards having done *badly* in 2018–2020, so it measures regime luck as much as robustness. The regime-free comparison is the excess over buy-and-hold, below.

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free either. Cross-strategy comparisons in this repository use average profit per trade in percent.

**Excess over buy-and-hold** (regime-free): author's window **+12.2 pp**, out of sample **-384.5 pp**.

Baseline: buy-and-hold on the same pairs returned **-51.25%**; the strategy returned **-39.02%**.
Out of sample: buy-and-hold **348.67%** vs strategy **-35.85%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | could not run | вывод не разобран |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | индикаторы меняются от объёма истории: pct_sum -33.617% |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **1h** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `590bf74986c5` · strategy list `a039f448c17bed72`*
