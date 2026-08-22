# SampleStrategy

Source: [`DutchCryptoDad/FreqtradeBotStrategyDevelopmentForBeginners`](https://github.com/DutchCryptoDad/FreqtradeBotStrategyDevelopmentForBeginners) · file `sample_strategy.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 3105 | 9619 |
| average profit per trade % | -0.34 | -0.25 |
| win rate % | 86.2 | 87.0 |
| average trade duration, minutes | 1200.0 | 1275.0 |
| duration measured in own candles | 240.0 | 255.0 |
| expectancy per trade (USDT) | -0.25 | -0.1 |
| mean profit p-value | 8.058e-09 | 1.498e-06 |
| market change % (baseline) | -58.37 | 346.34 |
| strategy total % | -76.96 | -96.76 |
| Sharpe | -8.44 | -3.82 |
| Sortino | -7.24 | -2.13 |
| max drawdown % | 78.6 | 96.94 |
| profit factor | 0.68 | 0.8 |

**Retained out of sample: negative**

> **Read that number with care.** The author's window was a bear market (buy-and-hold −58%) and the out-of-sample window a bull market (+346%). For a long-biased strategy this ratio rewards having done *badly* in 2018–2020, so it measures regime luck as much as robustness. The regime-free comparison is the excess over buy-and-hold, below.

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free either. Cross-strategy comparisons in this repository use average profit per trade in percent.

**Excess over buy-and-hold** (regime-free): author's window **-18.6 pp**, out of sample **-443.1 pp**.

Baseline: buy-and-hold on the same pairs returned **-58.37%**; the strategy returned **-76.96%**.
Out of sample: buy-and-hold **346.34%** vs strategy **-96.76%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | clean | смещения не обнаружено |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | индикаторы меняются от объёма истории: adx -27.315%, rsi 0.935% |
| прогрев не объявлен | **found** | самый длинный индикатор 100 свечей, startup_candle_count не задан (по умолчанию 0) |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **5m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `590bf74986c5` · strategy list `a039f448c17bed72`*
