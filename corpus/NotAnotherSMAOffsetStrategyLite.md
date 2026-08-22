# NotAnotherSMAOffsetStrategyLite

Source: [`Foxel05/freqtrade-stuff`](https://github.com/Foxel05/freqtrade-stuff) · file `NotAnotherSMAOffsetStrategyLite.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 321 | 1094 |
| average profit per trade % | 0.32 | 0.51 |
| win rate % | 68.5 | 73.6 |
| average trade duration, minutes | 56.0 | 44.0 |
| duration measured in own candles | 11.2 | 8.8 |
| expectancy per trade (USDT) | 0.42 | 0.89 |
| mean profit p-value | 0.007172 | 6.768e-12 |
| market change % (baseline) | -59.05 | 346.34 |
| strategy total % | 13.54 | 96.95 |
| Sharpe | 1.27 | 1.86 |
| Sortino | 1.22 | 1.52 |
| max drawdown % | 4.9 | 10.0 |
| profit factor | 1.5 | 1.81 |

**Retained out of sample: 212%**

> **Read that number with care.** The author's window was a bear market (buy-and-hold −58%) and the out-of-sample window a bull market (+346%). For a long-biased strategy this ratio rewards having done *badly* in 2018–2020, so it measures regime luck as much as robustness. The regime-free comparison is the excess over buy-and-hold, below.

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free either. Cross-strategy comparisons in this repository use average profit per trade in percent.

**Excess over buy-and-hold** (regime-free): author's window **+72.6 pp**, out of sample **-249.4 pp**.

Baseline: buy-and-hold on the same pairs returned **-59.05%**; the strategy returned **13.54%**.
Out of sample: buy-and-hold **346.34%** vs strategy **96.95%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | clean | смещения не обнаружено |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | индикаторы меняются от объёма истории: ewo -12.317% |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **5m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `590bf74986c5` · strategy list `a039f448c17bed72`*
