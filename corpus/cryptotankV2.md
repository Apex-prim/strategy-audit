# cryptotankV2

Source: [`jaredrsommer/freqtradestrategies`](https://github.com/jaredrsommer/freqtradestrategies) · file `cryptotankV2.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 1279 | — |
| average profit per trade % | -0.41 | — |
| win rate % | 92.7 | — |
| average trade duration, minutes | 3262.0 | — |
| duration measured in own candles | 652.4 | — |
| expectancy per trade (USDT) | -0.45 | — |
| mean profit p-value | 0.002682 | — |
| market change % (baseline) | -58.37 | — |
| strategy total % | -57.06 | — |
| Sharpe | -2.82 | — |
| Sortino | -2.46 | — |
| max drawdown % | 60.22 | — |
| profit factor | 0.66 | — |

**Retained out of sample: —**

> **Read that number with care.** The author's window was a bear market (buy-and-hold −58%) and the out-of-sample window a bull market (+346%). For a long-biased strategy this ratio rewards having done *badly* in 2018–2020, so it measures regime luck as much as robustness. The regime-free comparison is the excess over buy-and-hold, below.

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free either. Cross-strategy comparisons in this repository use average profit per trade in percent.

**Excess over buy-and-hold** (regime-free): author's window **+1.3 pp**.

Baseline: buy-and-hold on the same pairs returned **-58.37%**; the strategy returned **-57.06%**.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | clean | смещения не обнаружено |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | индикаторы меняются от объёма истории: ema_124 -0.012%, buy_rsi_16 1.932%, buy_rsi_ma_14 3.839%, rsi_ma_slope 23.184% |
| прогрев не объявлен | **found** | самый длинный индикатор 50 свечей, startup_candle_count не задан (по умолчанию 0) |
| трейлинг на полном стопе | **found** | trailing_stop=True без trailing_stop_positive ⇒ стоп тащится на ВСЁ расстояние стоп-лосса |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **5m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `590bf74986c5` · strategy list `a039f448c17bed72`*
