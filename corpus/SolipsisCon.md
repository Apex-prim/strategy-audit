# SolipsisCon

Source: [`PeetCrypto/freqtrade-stuff`](https://github.com/PeetCrypto/freqtrade-stuff) · file `Solipsis-Con-v1.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 1959 | — |
| average profit per trade % | -0.3 | — |
| win rate % | 85.9 | — |
| average trade duration, minutes | 2974.0 | — |
| duration measured in own candles | 594.8 | — |
| expectancy per trade (USDT) | -0.35 | — |
| mean profit p-value | 0.001797 | — |
| market change % (baseline) | -58.42 | — |
| strategy total % | -67.98 | — |
| Sharpe | -3.62 | — |
| Sortino | -1.63 | — |
| max drawdown % | 72.72 | — |
| profit factor | 0.64 | — |

**Retained out of sample: —**

> **Read that number with care.** The author's window was a bear market (buy-and-hold −58%) and the out-of-sample window a bull market (+346%). For a long-biased strategy this ratio rewards having done *badly* in 2018–2020, so it measures regime luck as much as robustness. The regime-free comparison is the excess over buy-and-hold, below.

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free either. Cross-strategy comparisons in this repository use average profit per trade in percent.

**Excess over buy-and-hold** (regime-free): author's window **-9.6 pp**.

Baseline: buy-and-hold on the same pairs returned **-58.42%**; the strategy returned **-67.98%**.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | could not run | код 1 |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | индикаторы меняются от объёма истории: consensus_buy -14.286%, consensus_sell -20.000% |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **5m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `590bf74986c5` · strategy list `a039f448c17bed72`*
