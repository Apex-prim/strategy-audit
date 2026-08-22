# BBRSI2

Source: [`davidzr/freqtrade-strategies`](https://github.com/davidzr/freqtrade-strategies) · file `BBRSI2.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 6919 | 17503 |
| average profit per trade % | -0.38 | -0.13 |
| win rate % | 53.7 | 59.7 |
| average trade duration, minutes | 299.0 | 274.0 |
| duration measured in own candles | 299.0 | 274.0 |
| expectancy per trade (USDT) | -0.14 | -0.06 |
| mean profit p-value | 2.144e-29 | 2.788e-13 |
| market change % (baseline) | -55.54 | 347.94 |
| strategy total % | -96.64 | -96.8 |
| Sharpe | -24.59 | -7.82 |
| Sortino | -20.37 | -5.9 |
| max drawdown % | 96.68 | 96.9 |
| profit factor | 0.54 | 0.76 |

**Retained out of sample: negative**

> **Read that number with care.** The author's window was a bear market (buy-and-hold −58%) and the out-of-sample window a bull market (+346%). For a long-biased strategy this ratio rewards having done *badly* in 2018–2020, so it measures regime luck as much as robustness. The regime-free comparison is the excess over buy-and-hold, below.

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free either. Cross-strategy comparisons in this repository use average profit per trade in percent.

**Excess over buy-and-hold** (regime-free): author's window **-41.1 pp**, out of sample **-444.7 pp**.

Baseline: buy-and-hold on the same pairs returned **-55.54%**; the strategy returned **-96.64%**.
Out of sample: buy-and-hold **347.94%** vs strategy **-96.8%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | clean | смещения не обнаружено |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | freqtrade ОТКАЗАЛСЯ анализировать: startup_candle_count=0, «приведёт к рекурсивным проблемам у части индикаторов» |
| прогрев не объявлен | **found** | самый длинный индикатор 20 свечей, startup_candle_count не задан (по умолчанию 0) |
| трейлинг на полном стопе | **found** | trailing_stop=True без trailing_stop_positive ⇒ стоп тащится на ВСЁ расстояние стоп-лосса |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **1m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `590bf74986c5` · strategy list `a039f448c17bed72`*
