# HurstCycle3

Source: [`jaredrsommer/freqtradestrategies`](https://github.com/jaredrsommer/freqtradestrategies) · file `HurstCycle3 (2).py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 10088 | 10019 |
| average profit per trade % | -0.27 | -0.27 |
| win rate % | 30.7 | 37.4 |
| average trade duration, minutes | 157.0 | 142.0 |
| duration measured in own candles | 10.47 | 9.47 |
| expectancy per trade (USDT) | -0.1 | -0.1 |
| mean profit p-value | 5.45e-53 | 8.501e-47 |
| market change % (baseline) | -58.11 | 345.85 |
| strategy total % | -96.57 | -96.6 |
| Sharpe | -40.46 | -11.69 |
| Sortino | -49.47 | -15.83 |
| max drawdown % | 96.57 | 96.6 |
| profit factor | 0.58 | 0.65 |

**Retained out of sample: negative**

> **Read that number with care.** The author's window was a bear market (buy-and-hold −58%) and the out-of-sample window a bull market (+346%). For a long-biased strategy this ratio rewards having done *badly* in 2018–2020, so it measures regime luck as much as robustness. The regime-free comparison is the excess over buy-and-hold, below.

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free either. Cross-strategy comparisons in this repository use average profit per trade in percent.

**Excess over buy-and-hold** (regime-free): author's window **-38.5 pp**, out of sample **-442.5 pp**.

Baseline: buy-and-hold on the same pairs returned **-58.11%**; the strategy returned **-96.57%**.
Out of sample: buy-and-hold **345.85%** vs strategy **-96.6%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | could not run | Fatal exception! |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | freqtrade ОТКАЗАЛСЯ анализировать: startup_candle_count=0, «приведёт к рекурсивным проблемам у части индикаторов» |
| признак утечки будущего | **found** | центрированное окно center=True |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **15m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `590bf74986c5` · strategy list `a039f448c17bed72`*
