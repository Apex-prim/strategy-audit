# BB_RPB_TSL_RNG_VWAP

Source: [`davidzr/freqtrade-strategies`](https://github.com/davidzr/freqtrade-strategies) · file `BB_RPB_TSL_RNG_VWAP.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 244 | 1045 |
| average profit per trade % | 1.13 | 0.56 |
| win rate % | 64.8 | 51.0 |
| average trade duration, minutes | 57.0 | 38.0 |
| duration measured in own candles | 11.4 | 7.6 |
| expectancy per trade (USDT) | 1.66 | 0.95 |
| mean profit p-value | 7.62e-16 | 0.0002899 |
| market change % (baseline) | -58.87 | 346.34 |
| strategy total % | 40.39 | 99.52 |
| Sharpe | 3.54 | 0.95 |
| Sortino | 4.63 | 0.81 |
| max drawdown % | 2.35 | 19.23 |
| profit factor | 3.99 | 1.57 |

**Retained out of sample: 57%**

> **Read that number with care.** The author's window was a bear market (buy-and-hold −58%) and the out-of-sample window a bull market (+346%). For a long-biased strategy this ratio rewards having done *badly* in 2018–2020, so it measures regime luck as much as robustness. The regime-free comparison is the excess over buy-and-hold, below.

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free either. Cross-strategy comparisons in this repository use average profit per trade in percent.

**Excess over buy-and-hold** (regime-free): author's window **+99.3 pp**, out of sample **-246.8 pp**.

Baseline: buy-and-hold on the same pairs returned **-58.87%**; the strategy returned **40.39%**.
Out of sample: buy-and-hold **346.34%** vs strategy **99.52%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | clean | смещения не обнаружено |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | индикаторы меняются от объёма истории: srsi_fk 0.167%, srsi_fd 0.077%, ema_100 0.011%, rsi_slow -0.034%, rsi_84 -2.915% |
| прогрев объявлен | clean | 120 при потребности 112 |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **5m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `590bf74986c5` · strategy list `a039f448c17bed72`*
