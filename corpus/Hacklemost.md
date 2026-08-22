# Hacklemost

Source: [`werkkrew/freqtrade-strategies`](https://github.com/werkkrew/freqtrade-strategies) · file `Hacklemost.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 10 | 158 |
| average profit per trade % | 1.88 | 1.06 |
| win rate % | 100.0 | 97.5 |
| average trade duration, minutes | 3920.0 | 281.0 |
| duration measured in own candles | 784.0 | 56.2 |
| expectancy per trade (USDT) | 2.35 | 1.39 |
| mean profit p-value | 0.009984 | 0.02344 |
| market change % (baseline) | -58.23 | 346.34 |
| strategy total % | 2.35 | 22.02 |
| Sharpe | 0.28 | 0.23 |
| Sortino | -100.0 | 2.79 |
| max drawdown % | 0.0 | 9.72 |
| profit factor | 0.0 | 2.25 |

**Retained out of sample: 59%**

> **Read that number with care.** The author's window was a bear market (buy-and-hold −58%) and the out-of-sample window a bull market (+346%). For a long-biased strategy this ratio rewards having done *badly* in 2018–2020, so it measures regime luck as much as robustness. The regime-free comparison is the excess over buy-and-hold, below.

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free either. Cross-strategy comparisons in this repository use average profit per trade in percent.

**Excess over buy-and-hold** (regime-free): author's window **+60.6 pp**, out of sample **-324.3 pp**.

Baseline: buy-and-hold on the same pairs returned **-58.23%**; the strategy returned **2.35%**.
Out of sample: buy-and-hold **346.34%** vs strategy **22.02%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | could not run | вывод не разобран |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | freqtrade ОТКАЗАЛСЯ анализировать: startup_candle_count=0, «приведёт к рекурсивным проблемам у части индикаторов» |
| прогрев не объявлен | **found** | самый длинный индикатор 48 свечей, startup_candle_count не задан (по умолчанию 0) |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **5m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `590bf74986c5` · strategy list `a039f448c17bed72`*
