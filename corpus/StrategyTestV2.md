# StrategyTestV2

Source: [`markdregan/FreqAI-Marcos-Lopez-De-Prado`](https://github.com/markdregan/FreqAI-Marcos-Lopez-De-Prado) · file `strategy_test_v2.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 6303 | 19767 |
| average profit per trade % | -0.18 | -0.12 |
| win rate % | 69.5 | 70.0 |
| average trade duration, minutes | 341.0 | 378.0 |
| duration measured in own candles | 68.2 | 75.6 |
| expectancy per trade (USDT) | -0.12 | -0.05 |
| mean profit p-value | 7.396e-12 | 0.0004201 |
| market change % (baseline) | -58.41 | 346.34 |
| strategy total % | -77.37 | -96.59 |
| Sharpe | -14.26 | -4.01 |
| Sortino | -8.64 | -2.5 |
| max drawdown % | 79.59 | 97.65 |
| profit factor | 0.54 | 0.84 |

**Retained out of sample: negative**

> **Read that number with care.** The author's window was a bear market (buy-and-hold −58%) and the out-of-sample window a bull market (+346%). For a long-biased strategy this ratio rewards having done *badly* in 2018–2020, so it measures regime luck as much as robustness. The regime-free comparison is the excess over buy-and-hold, below.

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free either. Cross-strategy comparisons in this repository use average profit per trade in percent.

**Excess over buy-and-hold** (regime-free): author's window **-19.0 pp**, out of sample **-442.9 pp**.

Baseline: buy-and-hold on the same pairs returned **-58.41%**; the strategy returned **-77.37%**.
Out of sample: buy-and-hold **346.34%** vs strategy **-96.59%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | clean | смещения не обнаружено |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | индикаторы меняются от объёма истории: minus_di -4.063%, plus_di 29.287%, rsi 12.447% |
| прогрев не объявлен | **found** | самый длинный индикатор 20 свечей, startup_candle_count не задан (по умолчанию 0) |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **5m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `590bf74986c5` · strategy list `a039f448c17bed72`*
