# ASDTSRockwellTrading

Source: [`Foxel05/freqtrade-stuff`](https://github.com/Foxel05/freqtrade-stuff) · file `ASDTSRockwellTrading.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 16298 | 13654 |
| average profit per trade % | -0.16 | -0.2 |
| win rate % | 24.4 | 23.2 |
| average trade duration, minutes | 45.0 | 45.0 |
| duration measured in own candles | 9.0 | 9.0 |
| expectancy per trade (USDT) | -0.06 | -0.07 |
| mean profit p-value | 1.36e-65 | 1.255e-42 |
| market change % (baseline) | -58.23 | 346.34 |
| strategy total % | -96.57 | -96.57 |
| Sharpe | -57.33 | -12.98 |
| Sortino | -91.15 | -17.96 |
| max drawdown % | 96.59 | 96.57 |
| profit factor | 0.61 | 0.6 |

**Retained out of sample: negative**

> **Read that number with care.** The author's window was a bear market (buy-and-hold −58%) and the out-of-sample window a bull market (+346%). For a long-biased strategy this ratio rewards having done *badly* in 2018–2020, so it measures regime luck as much as robustness. The regime-free comparison is the excess over buy-and-hold, below.

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free either. Cross-strategy comparisons in this repository use average profit per trade in percent.

**Excess over buy-and-hold** (regime-free): author's window **-38.3 pp**, out of sample **-442.9 pp**.

Baseline: buy-and-hold on the same pairs returned **-58.23%**; the strategy returned **-96.57%**.
Out of sample: buy-and-hold **346.34%** vs strategy **-96.57%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | clean | смещения не обнаружено |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | freqtrade ОТКАЗАЛСЯ анализировать: startup_candle_count=0, «приведёт к рекурсивным проблемам у части индикаторов» |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **5m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `590bf74986c5` · strategy list `a039f448c17bed72`*
