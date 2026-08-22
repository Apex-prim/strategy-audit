# StrategyTestV3

Source: [`markdregan/FreqAI-Marcos-Lopez-De-Prado`](https://github.com/markdregan/FreqAI-Marcos-Lopez-De-Prado) · file `strategy_test_v3.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 9893 | 23422 |
| average profit per trade % | -0.17 | -0.11 |
| win rate % | 50.0 | 52.5 |
| average trade duration, minutes | 45.0 | 42.0 |
| duration measured in own candles | 9.0 | 8.4 |
| expectancy per trade (USDT) | -0.09 | -0.04 |
| mean profit p-value | 4.566e-38 | 5.678e-09 |
| market change % (baseline) | -58.41 | 346.34 |
| strategy total % | -88.14 | -96.78 |
| Sharpe | -33.72 | -7.21 |
| Sortino | -28.91 | -6.04 |
| max drawdown % | 88.52 | 96.82 |
| profit factor | 0.54 | 0.82 |

**Retained out of sample: negative**

> **Read that number with care.** The author's window was a bear market (buy-and-hold −58%) and the out-of-sample window a bull market (+346%). For a long-biased strategy this ratio rewards having done *badly* in 2018–2020, so it measures regime luck as much as robustness. The regime-free comparison is the excess over buy-and-hold, below.

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free either. Cross-strategy comparisons in this repository use average profit per trade in percent.

**Excess over buy-and-hold** (regime-free): author's window **-29.7 pp**, out of sample **-443.1 pp**.

Baseline: buy-and-hold on the same pairs returned **-58.41%**; the strategy returned **-88.14%**.
Out of sample: buy-and-hold **346.34%** vs strategy **-96.78%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | clean | смещения не обнаружено |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | индикаторы меняются от объёма истории: minus_di -4.063%, plus_di 29.287%, rsi 12.447% |
| прогрев не объявлен | **found** | самый длинный индикатор 20 свечей, startup_candle_count не задан (по умолчанию 0) |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **5m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `590bf74986c5` · strategy list `a039f448c17bed72`*
