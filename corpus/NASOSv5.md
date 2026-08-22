# NASOSv5

Source: [`PeetCrypto/freqtrade-stuff`](https://github.com/PeetCrypto/freqtrade-stuff) · file `NASOSv5.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 117 | 684 |
| average profit per trade % | 0.67 | 0.2 |
| win rate % | 72.6 | 59.2 |
| average trade duration, minutes | 510.0 | 105.0 |
| duration measured in own candles | 102.0 | 21.0 |
| expectancy per trade (USDT) | 0.87 | 0.21 |
| mean profit p-value | 0.033 | 0.4225 |
| market change % (baseline) | -59.05 | 346.34 |
| strategy total % | 10.13 | 14.56 |
| Sharpe | 0.61 | 0.17 |
| Sortino | 0.42 | 0.13 |
| max drawdown % | 1.87 | 19.41 |
| profit factor | 1.93 | 1.14 |

**Retained out of sample: 24%**

> **Read that number with care.** The author's window was a bear market (buy-and-hold −58%) and the out-of-sample window a bull market (+346%). For a long-biased strategy this ratio rewards having done *badly* in 2018–2020, so it measures regime luck as much as robustness. The regime-free comparison is the excess over buy-and-hold, below.

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free either. Cross-strategy comparisons in this repository use average profit per trade in percent.

**Excess over buy-and-hold** (regime-free): author's window **+69.2 pp**, out of sample **-331.8 pp**.

Baseline: buy-and-hold on the same pairs returned **-59.05%**; the strategy returned **10.13%**.
Out of sample: buy-and-hold **346.34%** vs strategy **14.56%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | could not run | код 1 |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | индикаторы меняются от объёма истории: EWO -12.317% |
| прогрев объявлен | clean | 200 при потребности 200 |
| мёртвые настройки трейлинга | **found** | trailing_stop=False, но trailing_stop_positive=0.001 задан — читается как работающая защита |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **5m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `590bf74986c5` · strategy list `a039f448c17bed72`*
