# BinHV45HO

Source: [`TheoBrigitte/freqtrade`](https://github.com/TheoBrigitte/freqtrade) · file `BinHV45HO.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 32 | 357 |
| average profit per trade % | 1.25 | -0.06 |
| win rate % | 100.0 | 93.6 |
| average trade duration, minutes | 2225.0 | 7.0 |
| duration measured in own candles | 2225.0 | 7.0 |
| expectancy per trade (USDT) | 1.58 | -0.14 |
| mean profit p-value | 4.195e-58 | 0.7039 |
| market change % (baseline) | -55.54 | 347.94 |
| strategy total % | 5.07 | -5.08 |
| Sharpe | 55.7 | -0.06 |
| Sortino | -100.0 | -0.19 |
| max drawdown % | 0.0 | 24.36 |
| profit factor | 0.0 | 0.92 |

**Retained out of sample: negative**

> **Read that number with care.** The author's window was a bear market (buy-and-hold −58%) and the out-of-sample window a bull market (+346%). For a long-biased strategy this ratio rewards having done *badly* in 2018–2020, so it measures regime luck as much as robustness. The regime-free comparison is the excess over buy-and-hold, below.

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free either. Cross-strategy comparisons in this repository use average profit per trade in percent.

**Excess over buy-and-hold** (regime-free): author's window **+60.6 pp**, out of sample **-353.0 pp**.

Baseline: buy-and-hold on the same pairs returned **-55.54%**; the strategy returned **5.07%**.
Out of sample: buy-and-hold **347.94%** vs strategy **-5.08%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | could not run | вывод не разобран |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | freqtrade ОТКАЗАЛСЯ анализировать: startup_candle_count=0, «приведёт к рекурсивным проблемам у части индикаторов» |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **1m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `590bf74986c5` · strategy list `a039f448c17bed72`*
