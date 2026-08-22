# NOTankAi_15

Source: [`TheoBrigitte/freqtrade`](https://github.com/TheoBrigitte/freqtrade) · file `NOTankAi_15.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 2859 | — |
| average profit per trade % | 1.78 | — |
| win rate % | 100.0 | — |
| average trade duration, minutes | 541.0 | — |
| duration measured in own candles | 36.07 | — |
| expectancy per trade (USDT) | 175.8 | — |
| mean profit p-value | 1.03e-54 | — |
| market change % (baseline) | -58.11 | — |
| strategy total % | 50262.5 | — |
| Sharpe | 22.25 | — |
| Sortino | -100.0 | — |
| max drawdown % | 4.0 | — |
| profit factor | 24.98 | — |

**Retained out of sample: —**

> **Read that number with care.** The author's window was a bear market (buy-and-hold −58%) and the out-of-sample window a bull market (+346%). For a long-biased strategy this ratio rewards having done *badly* in 2018–2020, so it measures regime luck as much as robustness. The regime-free comparison is the excess over buy-and-hold, below.

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free either. Cross-strategy comparisons in this repository use average profit per trade in percent.

**Excess over buy-and-hold** (regime-free): author's window **+50320.6 pp**.

Baseline: buy-and-hold on the same pairs returned **-58.11%**; the strategy returned **50262.5%**.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | clean | смещения не обнаружено |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | freqtrade ОТКАЗАЛСЯ анализировать: startup_candle_count=0, «приведёт к рекурсивным проблемам у части индикаторов» |
| прогрев не объявлен | **found** | самый длинный индикатор 200 свечей, startup_candle_count не задан (по умолчанию 0) |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **15m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `590bf74986c5` · strategy list `a039f448c17bed72`*
