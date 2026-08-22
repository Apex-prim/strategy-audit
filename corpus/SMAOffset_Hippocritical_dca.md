# SMAOffset_Hippocritical_dca

Source: [`TheoBrigitte/freqtrade`](https://github.com/TheoBrigitte/freqtrade) · file `SMAOffset_Hippocritical_dca.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 27 | 191 |
| average profit per trade % | 1.61 | 1.68 |
| win rate % | 96.3 | 97.9 |
| average trade duration, minutes | 24.0 | 29.0 |
| duration measured in own candles | 4.8 | 5.8 |
| expectancy per trade (USDT) | 0.5 | 0.51 |
| mean profit p-value | 2.385e-10 | 8.432e-17 |
| market change % (baseline) | -59.3 | 346.34 |
| strategy total % | 1.35 | 9.72 |
| Sharpe | 1.38 | 1.03 |
| Sortino | -100.0 | 0.29 |
| max drawdown % | 0.03 | 0.63 |
| profit factor | 50.9 | 8.74 |

**Retained out of sample: 102%**

> **Read that number with care.** The author's window was a bear market (buy-and-hold −58%) and the out-of-sample window a bull market (+346%). For a long-biased strategy this ratio rewards having done *badly* in 2018–2020, so it measures regime luck as much as robustness. The regime-free comparison is the excess over buy-and-hold, below.

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free either. Cross-strategy comparisons in this repository use average profit per trade in percent.

**Excess over buy-and-hold** (regime-free): author's window **+60.6 pp**, out of sample **-336.6 pp**.

Baseline: buy-and-hold on the same pairs returned **-59.3%**; the strategy returned **1.35%**.
Out of sample: buy-and-hold **346.34%** vs strategy **9.72%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | could not run | вывод не разобран |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | индикаторы меняются от объёма истории: EWO -12.317% |
| прогрев не объявлен | **found** | самый длинный индикатор 14 свечей, startup_candle_count не задан (по умолчанию 0) |
| мёртвые настройки трейлинга | **found** | trailing_stop=False, но trailing_stop_positive=0.001 задан — читается как работающая защита |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **5m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `590bf74986c5` · strategy list `a039f448c17bed72`*
