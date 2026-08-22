# StrategyScalpingFast

Source: [`davidzr/freqtrade-strategies`](https://github.com/davidzr/freqtrade-strategies) · file `StrategyScalpingFast.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 1002 | 3828 |
| average profit per trade % | -0.48 | 0.12 |
| win rate % | 96.8 | 98.2 |
| average trade duration, minutes | 5828.0 | 5540.0 |
| duration measured in own candles | 5828.0 | 5540.0 |
| expectancy per trade (USDT) | -0.61 | -0.07 |
| mean profit p-value | 0.01405 | 0.8168 |
| market change % (baseline) | -55.53 | 347.94 |
| strategy total % | -60.81 | -24.97 |
| Sharpe | -2.04 | -0.12 |
| Sortino | -1.02 | -0.04 |
| max drawdown % | 62.08 | 79.67 |
| profit factor | 0.53 | 0.97 |

**Retained out of sample: negative**

> **Read that number with care.** The author's window was a bear market (buy-and-hold −58%) and the out-of-sample window a bull market (+346%). For a long-biased strategy this ratio rewards having done *badly* in 2018–2020, so it measures regime luck as much as robustness. The regime-free comparison is the excess over buy-and-hold, below.

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free either. Cross-strategy comparisons in this repository use average profit per trade in percent.

**Excess over buy-and-hold** (regime-free): author's window **-5.3 pp**, out of sample **-372.9 pp**.

Baseline: buy-and-hold on the same pairs returned **-55.53%**; the strategy returned **-60.81%**.
Out of sample: buy-and-hold **347.94%** vs strategy **-24.97%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | clean | смещения не обнаружено |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | индикаторы меняются от объёма истории: rsi -1.353% |
| прогрев не объявлен | **found** | самый длинный индикатор 20 свечей, startup_candle_count не задан (по умолчанию 0) |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **1m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `590bf74986c5` · strategy list `a039f448c17bed72`*
