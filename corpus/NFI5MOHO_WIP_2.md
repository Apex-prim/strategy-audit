# NFI5MOHO_WIP_2

Source: [`davidzr/freqtrade-strategies`](https://github.com/davidzr/freqtrade-strategies) · file `NFI5MOHO_WIP_2.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 210 | 778 |
| average profit per trade % | 0.44 | 1.33 |
| win rate % | 85.2 | 90.2 |
| average trade duration, minutes | 248.0 | 162.0 |
| duration measured in own candles | 49.6 | 32.4 |
| expectancy per trade (USDT) | 0.56 | 3.32 |
| mean profit p-value | 0.01928 | 2.972e-37 |
| market change % (baseline) | -59.35 | 346.34 |
| strategy total % | 11.7 | 257.96 |
| Sharpe | 0.9 | 3.04 |
| Sortino | 0.61 | 1.64 |
| max drawdown % | 6.75 | 4.66 |
| profit factor | 1.65 | 4.4 |

**Retained out of sample: 593%**

> **Read that number with care.** The author's window was a bear market (buy-and-hold −58%) and the out-of-sample window a bull market (+346%). For a long-biased strategy this ratio rewards having done *badly* in 2018–2020, so it measures regime luck as much as robustness. The regime-free comparison is the excess over buy-and-hold, below.

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free either. Cross-strategy comparisons in this repository use average profit per trade in percent.

**Excess over buy-and-hold** (regime-free): author's window **+71.0 pp**, out of sample **-88.4 pp**.

Baseline: buy-and-hold on the same pairs returned **-59.35%**; the strategy returned **11.7%**.
Out of sample: buy-and-hold **346.34%** vs strategy **257.96%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | clean | смещения не обнаружено |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | индикаторы меняются от объёма истории: ema_100_1h -0.014%, ewo -12.317% |
| прогрев не объявлен | **found** | самый длинный индикатор 200 свечей, startup_candle_count не задан (по умолчанию 0) |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **5m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `590bf74986c5` · strategy list `a039f448c17bed72`*
