# SlowPotato

Source: [`davidzr/freqtrade-strategies`](https://github.com/davidzr/freqtrade-strategies) · file `SlowPotato.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 104 | — |
| average profit per trade % | -3.76 | — |
| win rate % | 93.3 | — |
| average trade duration, minutes | 61247.0 | — |
| duration measured in own candles | 12249.4 | — |
| expectancy per trade (USDT) | -4.76 | — |
| mean profit p-value | 0.03195 | — |
| market change % (baseline) | -58.23 | — |
| strategy total % | -49.55 | — |
| Sharpe | -0.58 | — |
| Sortino | -0.55 | — |
| max drawdown % | 53.89 | — |
| profit factor | 0.16 | — |

**Retained out of sample: —**

> **Read that number with care.** The author's window was a bear market (buy-and-hold −58%) and the out-of-sample window a bull market (+346%). For a long-biased strategy this ratio rewards having done *badly* in 2018–2020, so it measures regime luck as much as robustness. The regime-free comparison is the excess over buy-and-hold, below.

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free either. Cross-strategy comparisons in this repository use average profit per trade in percent.

**Excess over buy-and-hold** (regime-free): author's window **+8.7 pp**.

Baseline: buy-and-hold on the same pairs returned **-58.23%**; the strategy returned **-49.55%**.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | clean | смещения не обнаружено |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | freqtrade ОТКАЗАЛСЯ анализировать: startup_candle_count=0, «приведёт к рекурсивным проблемам у части индикаторов» |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **5m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `590bf74986c5` · strategy list `a039f448c17bed72`*
