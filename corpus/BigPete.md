# BigPete

Source: [`davidzr/freqtrade-strategies`](https://github.com/davidzr/freqtrade-strategies) · file `BigPete.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 4439 | 13236 |
| average profit per trade % | -0.24 | -0.17 |
| win rate % | 78.8 | 78.8 |
| average trade duration, minutes | 1253.0 | 1178.0 |
| duration measured in own candles | 250.6 | 235.6 |
| expectancy per trade (USDT) | -0.18 | -0.07 |
| mean profit p-value | 2.996e-08 | 0.0004976 |
| market change % (baseline) | -59.05 | 346.34 |
| strategy total % | -79.34 | -96.63 |
| Sharpe | -9.68 | -3.24 |
| Sortino | -9.67 | -2.37 |
| max drawdown % | 83.61 | 96.78 |
| profit factor | 0.78 | 0.9 |

**Retained out of sample: negative**

> **Read that number with care.** The author's window was a bear market (buy-and-hold −58%) and the out-of-sample window a bull market (+346%). For a long-biased strategy this ratio rewards having done *badly* in 2018–2020, so it measures regime luck as much as robustness. The regime-free comparison is the excess over buy-and-hold, below.

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free either. Cross-strategy comparisons in this repository use average profit per trade in percent.

**Excess over buy-and-hold** (regime-free): author's window **-20.3 pp**, out of sample **-443.0 pp**.

Baseline: buy-and-hold on the same pairs returned **-59.05%**; the strategy returned **-79.34%**.
Out of sample: buy-and-hold **346.34%** vs strategy **-96.63%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | clean | смещения не обнаружено |
| indicator recursion (freqtrade's own `recursive-analysis`) | clean | рекурсивных отклонений не найдено |
| прогрев не объявлен | **found** | самый длинный индикатор 200 свечей, startup_candle_count не задан (по умолчанию 0) |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **5m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `590bf74986c5` · strategy list `a039f448c17bed72`*
