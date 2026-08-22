# LookaheadStrategy

Source: [`davidzr/freqtrade-strategies`](https://github.com/davidzr/freqtrade-strategies) · file `LookaheadStrategy.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 833 | 2791 |
| average profit per trade % | 2.97 | 2.99 |
| win rate % | 99.3 | 99.7 |
| average trade duration, minutes | 54.0 | 40.0 |
| duration measured in own candles | 10.8 | 8.0 |
| expectancy per trade (USDT) | 24.28 | 9237.33 |
| mean profit p-value | 6.513e-135 | 4.715e-126 |
| market change % (baseline) | -58.23 | 346.34 |
| strategy total % | 2022.28 | 2578139.95 |
| Sharpe | 22.68 | 10.75 |
| Sortino | 10.55 | 4278.62 |
| max drawdown % | 2.4 | 2.31 |
| profit factor | 151.34 | 69139.06 |

**Retained out of sample: 38045%**

> **Read that number with care.** The author's window was a bear market (buy-and-hold −58%) and the out-of-sample window a bull market (+346%). For a long-biased strategy this ratio rewards having done *badly* in 2018–2020, so it measures regime luck as much as robustness. The regime-free comparison is the excess over buy-and-hold, below.

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free either. Cross-strategy comparisons in this repository use average profit per trade in percent.

**Excess over buy-and-hold** (regime-free): author's window **+2080.5 pp**, out of sample **+2577793.6 pp**.

Baseline: buy-and-hold on the same pairs returned **-58.23%**; the strategy returned **2022.28%**.
Out of sample: buy-and-hold **346.34%** vs strategy **2578139.95%** — **beats the baseline**.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | **found** | ЕСТЬ СМЕЩЕНИЕ: входов 20, выходов 0 из 20 сигналов |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | freqtrade ОТКАЗАЛСЯ анализировать: startup_candle_count=0, «приведёт к рекурсивным проблемам у части индикаторов» |
| прогрев не объявлен | **found** | самый длинный индикатор 50 свечей, startup_candle_count не задан (по умолчанию 0) |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **5m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `590bf74986c5` · strategy list `a039f448c17bed72`*
