# RsiquiV5_long_only

Source: [`TheoBrigitte/freqtrade`](https://github.com/TheoBrigitte/freqtrade) · file `RsiquiV5_long_only.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 470 | 1257 |
| average profit per trade % | 0.37 | 0.43 |
| win rate % | 81.1 | 79.9 |
| average trade duration, minutes | 968.0 | 775.0 |
| duration measured in own candles | 193.6 | 155.0 |
| expectancy per trade (USDT) | 0.5 | 0.72 |
| mean profit p-value | 0.03486 | 9.022e-06 |
| market change % (baseline) | -58.23 | 346.34 |
| strategy total % | 23.32 | 90.14 |
| Sharpe | 1.2 | 1.28 |
| Sortino | 0.59 | 0.69 |
| max drawdown % | 9.98 | 24.38 |
| profit factor | 1.88 | 2.39 |

**Retained out of sample: 144%**

> **Read that number with care.** The author's window was a bear market (buy-and-hold −58%) and the out-of-sample window a bull market (+346%). For a long-biased strategy this ratio rewards having done *badly* in 2018–2020, so it measures regime luck as much as robustness. The regime-free comparison is the excess over buy-and-hold, below.

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free either. Cross-strategy comparisons in this repository use average profit per trade in percent.

**Excess over buy-and-hold** (regime-free): author's window **+81.5 pp**, out of sample **-256.2 pp**.

Baseline: buy-and-hold on the same pairs returned **-58.23%**; the strategy returned **23.32%**.
Out of sample: buy-and-hold **346.34%** vs strategy **90.14%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | **found** | ЕСТЬ СМЕЩЕНИЕ: входов 0, выходов 0 из 20 сигналов |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | freqtrade ОТКАЗАЛСЯ анализировать: startup_candle_count=0, «приведёт к рекурсивным проблемам у части индикаторов» |
| прогрев не объявлен | **found** | самый длинный индикатор 14 свечей, startup_candle_count не задан (по умолчанию 0) |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **5m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `590bf74986c5` · strategy list `a039f448c17bed72`*
