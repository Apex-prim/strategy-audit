# Maro4hMacdSd

Source: [`davidzr/freqtrade-strategies`](https://github.com/davidzr/freqtrade-strategies) · file `Maro4hMacdSd.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 13548 | 16944 |
| average profit per trade % | -0.19 | -0.16 |
| win rate % | 46.0 | 49.8 |
| average trade duration, minutes | 152.0 | 147.0 |
| duration measured in own candles | 30.4 | 29.4 |
| expectancy per trade (USDT) | -0.07 | -0.06 |
| mean profit p-value | 5.081e-26 | 5.457e-18 |
| market change % (baseline) | -58.23 | 346.34 |
| strategy total % | -96.31 | -96.73 |
| Sharpe | -32.16 | -9.11 |
| Sortino | -30.66 | -8.9 |
| max drawdown % | 96.34 | 96.75 |
| profit factor | 0.65 | 0.75 |

**Retained out of sample: negative**

> **Read that number with care.** The author's window was a bear market (buy-and-hold −58%) and the out-of-sample window a bull market (+346%). For a long-biased strategy this ratio rewards having done *badly* in 2018–2020, so it measures regime luck as much as robustness. The regime-free comparison is the excess over buy-and-hold, below.

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free either. Cross-strategy comparisons in this repository use average profit per trade in percent.

**Excess over buy-and-hold** (regime-free): author's window **-38.1 pp**, out of sample **-443.1 pp**.

Baseline: buy-and-hold on the same pairs returned **-58.23%**; the strategy returned **-96.31%**.
Out of sample: buy-and-hold **346.34%** vs strategy **-96.73%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | clean | смещения не обнаружено |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | freqtrade ОТКАЗАЛСЯ анализировать: startup_candle_count=0, «приведёт к рекурсивным проблемам у части индикаторов» |
| прогрев не объявлен | **found** | самый длинный индикатор 28 свечей, startup_candle_count не задан (по умолчанию 0) |
| мёртвые настройки трейлинга | **found** | trailing_stop=False, но trailing_stop_positive=0.1 задан — читается как работающая защита |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **5m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `590bf74986c5` · strategy list `a039f448c17bed72`*
