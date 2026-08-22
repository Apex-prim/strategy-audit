# NASOSv5_mod1_DanMod

Source: [`davidzr/freqtrade-strategies`](https://github.com/davidzr/freqtrade-strategies) · file `NASOSv5_mod1_DanMod.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 29 | 367 |
| average profit per trade % | 2.35 | 2.54 |
| win rate % | 96.6 | 96.2 |
| average trade duration, minutes | 1243.0 | 333.0 |
| duration measured in own candles | 248.6 | 66.6 |
| expectancy per trade (USDT) | 2.99 | 5.8 |
| mean profit p-value | 0.06708 | 1.396e-11 |
| market change % (baseline) | -59.05 | 346.34 |
| strategy total % | 8.68 | 212.81 |
| Sharpe | 0.27 | 1.08 |
| Sortino | -100.0 | 0.49 |
| max drawdown % | 3.73 | 11.09 |
| profit factor | 3.13 | 3.7 |

**Retained out of sample: 194%**

> **Read that number with care.** The author's window was a bear market (buy-and-hold −58%) and the out-of-sample window a bull market (+346%). For a long-biased strategy this ratio rewards having done *badly* in 2018–2020, so it measures regime luck as much as robustness. The regime-free comparison is the excess over buy-and-hold, below.

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free either. Cross-strategy comparisons in this repository use average profit per trade in percent.

**Excess over buy-and-hold** (regime-free): author's window **+67.7 pp**, out of sample **-133.5 pp**.

⚠ **Not statistically significant in its author's own window** (p = 0.06708 > 0.05): the average trade is not distinguishable from zero.

Baseline: buy-and-hold on the same pairs returned **-59.05%**; the strategy returned **8.68%**.
Out of sample: buy-and-hold **346.34%** vs strategy **212.81%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | could not run | Fatal exception! |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | индикаторы меняются от объёма истории: EWO -12.317%, rsi_slow 0.021% |
| прогрев объявлен | clean | 200 при потребности 100 |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **5m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `590bf74986c5` · strategy list `a039f448c17bed72`*
