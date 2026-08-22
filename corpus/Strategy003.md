# Strategy003

Source: [`TheoBrigitte/freqtrade`](https://github.com/TheoBrigitte/freqtrade) · file `Strategy003.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 768 | 2730 |
| average profit per trade % | -0.26 | -0.2 |
| win rate % | 90.1 | 91.4 |
| average trade duration, minutes | 998.0 | 1109.0 |
| duration measured in own candles | 199.6 | 221.8 |
| expectancy per trade (USDT) | -0.3 | -0.19 |
| mean profit p-value | 0.02293 | 0.0003887 |
| market change % (baseline) | -58.23 | 346.34 |
| strategy total % | -23.11 | -51.76 |
| Sharpe | -1.65 | -1.5 |
| Sortino | -7.37 | -2.1 |
| max drawdown % | 27.3 | 53.67 |
| profit factor | 0.73 | 0.75 |

**Retained out of sample: negative**

> **Read that number with care.** The author's window was a bear market (buy-and-hold −58%) and the out-of-sample window a bull market (+346%). For a long-biased strategy this ratio rewards having done *badly* in 2018–2020, so it measures regime luck as much as robustness. The regime-free comparison is the excess over buy-and-hold, below.

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free either. Cross-strategy comparisons in this repository use average profit per trade in percent.

**Excess over buy-and-hold** (regime-free): author's window **+35.1 pp**, out of sample **-398.1 pp**.

Baseline: buy-and-hold on the same pairs returned **-58.23%**; the strategy returned **-23.11%**.
Out of sample: buy-and-hold **346.34%** vs strategy **-51.76%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | clean | смещения не обнаружено |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | freqtrade ОТКАЗАЛСЯ анализировать: startup_candle_count=0, «приведёт к рекурсивным проблемам у части индикаторов» |
| прогрев не объявлен | **found** | самый длинный индикатор 100 свечей, startup_candle_count не задан (по умолчанию 0) |
| мёртвые настройки трейлинга | **found** | trailing_stop=False, но trailing_stop_positive=0.01 задан — читается как работающая защита |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **5m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `590bf74986c5` · strategy list `a039f448c17bed72`*
