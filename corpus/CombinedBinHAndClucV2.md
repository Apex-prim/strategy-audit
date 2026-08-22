# CombinedBinHAndClucV2

Source: [`PeetCrypto/freqtrade-stuff`](https://github.com/PeetCrypto/freqtrade-stuff) · file `CombinedBinHAndClucV2.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 207 | 521 |
| average profit per trade % | 0.08 | 0.5 |
| win rate % | 65.7 | 67.9 |
| average trade duration, minutes | 123.0 | 104.0 |
| duration measured in own candles | 24.6 | 20.8 |
| expectancy per trade (USDT) | 0.08 | 0.71 |
| mean profit p-value | 0.765 | 0.00276 |
| market change % (baseline) | -59.05 | 346.34 |
| strategy total % | 1.6 | 37.03 |
| Sharpe | 0.11 | 0.56 |
| Sortino | 0.16 | 1.11 |
| max drawdown % | 8.02 | 5.79 |
| profit factor | 1.05 | 1.36 |

**Retained out of sample: 888%**

> **Read that number with care.** The author's window was a bear market (buy-and-hold −58%) and the out-of-sample window a bull market (+346%). For a long-biased strategy this ratio rewards having done *badly* in 2018–2020, so it measures regime luck as much as robustness. The regime-free comparison is the excess over buy-and-hold, below.

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free either. Cross-strategy comparisons in this repository use average profit per trade in percent.

**Excess over buy-and-hold** (regime-free): author's window **+60.6 pp**, out of sample **-309.3 pp**.

⚠ **Not statistically significant in its author's own window** (p = 0.765 > 0.05): the average trade is not distinguishable from zero.

Baseline: buy-and-hold on the same pairs returned **-59.05%**; the strategy returned **1.6%**.
Out of sample: buy-and-hold **346.34%** vs strategy **37.03%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | could not run | вывод не разобран |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | индикаторы меняются от объёма истории: srsi_fk -0.144%, srsi_fd -0.134% |
| прогрев объявлен | clean | 200 при потребности 50 |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **5m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `590bf74986c5` · strategy list `a039f448c17bed72`*
