# CombinedBinHAndClucV8XHO

Source: [`davidzr/freqtrade-strategies`](https://github.com/davidzr/freqtrade-strategies) · file `CombinedBinHAndClucV8XHO.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 203 | 648 |
| average profit per trade % | 0.62 | 0.63 |
| win rate % | 83.7 | 81.6 |
| average trade duration, minutes | 127.0 | 132.0 |
| duration measured in own candles | 25.4 | 26.4 |
| expectancy per trade (USDT) | 0.82 | 1.0 |
| mean profit p-value | 8.527e-05 | 2.167e-13 |
| market change % (baseline) | -59.05 | 346.34 |
| strategy total % | 16.66 | 64.81 |
| Sharpe | 1.5 | 1.54 |
| Sortino | 1.27 | 1.39 |
| max drawdown % | 3.51 | 5.27 |
| profit factor | 2.15 | 2.15 |

**Retained out of sample: 122%**

> **Read that number with care.** The author's window was a bear market (buy-and-hold −58%) and the out-of-sample window a bull market (+346%). For a long-biased strategy this ratio rewards having done *badly* in 2018–2020, so it measures regime luck as much as robustness. The regime-free comparison is the excess over buy-and-hold, below.

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free either. Cross-strategy comparisons in this repository use average profit per trade in percent.

**Excess over buy-and-hold** (regime-free): author's window **+75.7 pp**, out of sample **-281.5 pp**.

Baseline: buy-and-hold on the same pairs returned **-59.05%**; the strategy returned **16.66%**.
Out of sample: buy-and-hold **346.34%** vs strategy **64.81%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | clean | смещения не обнаружено |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | индикаторы меняются от объёма истории: ema_100_1h -0.014% |
| прогрев не объявлен | **found** | самый длинный индикатор 200 свечей, startup_candle_count не задан (по умолчанию 0) |
| мёртвые настройки трейлинга | **found** | trailing_stop=False, но trailing_stop_positive=0.01 задан — читается как работающая защита |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **5m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `590bf74986c5` · strategy list `a039f448c17bed72`*
