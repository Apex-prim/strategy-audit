# STRATEGY_RSI_BB_BOUNDS_CROSS

Source: [`davidzr/freqtrade-strategies`](https://github.com/davidzr/freqtrade-strategies) · file `STRATEGY_RSI_BB_BOUNDS_CROSS.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 1762 | 5435 |
| average profit per trade % | -0.14 | -0.2 |
| win rate % | 26.2 | 19.1 |
| average trade duration, minutes | 13.0 | 12.0 |
| duration measured in own candles | 2.6 | 2.4 |
| expectancy per trade (USDT) | -0.15 | -0.14 |
| mean profit p-value | 3.643e-18 | 2.738e-113 |
| market change % (baseline) | -58.41 | 346.34 |
| strategy total % | -26.34 | -74.5 |
| Sharpe | -9.65 | -13.81 |
| Sortino | -18.11 | -24.99 |
| max drawdown % | 26.7 | 75.06 |
| profit factor | 0.52 | 0.35 |

**Retained out of sample: negative**

> **Read that number with care.** The author's window was a bear market (buy-and-hold −58%) and the out-of-sample window a bull market (+346%). For a long-biased strategy this ratio rewards having done *badly* in 2018–2020, so it measures regime luck as much as robustness. The regime-free comparison is the excess over buy-and-hold, below.

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free either. Cross-strategy comparisons in this repository use average profit per trade in percent.

**Excess over buy-and-hold** (regime-free): author's window **+32.1 pp**, out of sample **-420.8 pp**.

Baseline: buy-and-hold on the same pairs returned **-58.41%**; the strategy returned **-26.34%**.
Out of sample: buy-and-hold **346.34%** vs strategy **-74.5%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | clean | смещения не обнаружено |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | индикаторы меняются от объёма истории: rsi 12.447%, rsi_percent 63.577%, rsi_ub -0.454%, bb_minus_rsi_percent 21.303% |
| прогрев не объявлен | **found** | самый длинный индикатор 14 свечей, startup_candle_count не задан (по умолчанию 0) |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **5m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `590bf74986c5` · strategy list `a039f448c17bed72`*
