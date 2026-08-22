# NotAnotherSMAOffsetStrategy

Source: [`Juusseli/Trade`](https://github.com/Juusseli/Trade) · file `NotAnotherSMAOffsetStrategy.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 215 | 683 |
| average profit per trade % | 0.69 | 1.04 |
| win rate % | 71.2 | 77.0 |
| average trade duration, minutes | 82.0 | 56.0 |
| duration measured in own candles | 16.4 | 11.2 |
| expectancy per trade (USDT) | 0.94 | 2.04 |
| mean profit p-value | 5.228e-06 | 8.496e-15 |
| market change % (baseline) | -59.05 | 346.34 |
| strategy total % | 20.16 | 139.57 |
| Sharpe | 1.8 | 1.68 |
| Sortino | 2.06 | 1.1 |
| max drawdown % | 5.66 | 4.57 |
| profit factor | 2.22 | 2.73 |

**Retained out of sample: 217%**

> **Read that number with care.** The author's window was a bear market (buy-and-hold −58%) and the out-of-sample window a bull market (+346%). For a long-biased strategy this ratio rewards having done *badly* in 2018–2020, so it measures regime luck as much as robustness. The regime-free comparison is the excess over buy-and-hold, below.

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free either. Cross-strategy comparisons in this repository use average profit per trade in percent.

**Excess over buy-and-hold** (regime-free): author's window **+79.2 pp**, out of sample **-206.8 pp**.

Baseline: buy-and-hold on the same pairs returned **-59.05%**; the strategy returned **20.16%**.
Out of sample: buy-and-hold **346.34%** vs strategy **139.57%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | could not run | Fatal exception! |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | индикаторы меняются от объёма истории: EWO -12.317% |
| прогрев объявлен | clean | 200 при потребности 100 |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **5m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `590bf74986c5` · strategy list `a039f448c17bed72`*
