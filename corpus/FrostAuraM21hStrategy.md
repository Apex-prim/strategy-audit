# FrostAuraM21hStrategy

Source: [`PeetCrypto/freqtrade-stuff`](https://github.com/PeetCrypto/freqtrade-stuff) · file `FrostAuraM21hStrategy.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 8809 | 11071 |
| average profit per trade % | -0.26 | -0.24 |
| win rate % | 20.2 | 22.3 |
| average trade duration, minutes | 235.0 | 242.0 |
| duration measured in own candles | 15.67 | 16.13 |
| expectancy per trade (USDT) | -0.11 | -0.09 |
| mean profit p-value | 1.723e-29 | 1.761e-14 |
| market change % (baseline) | -58.53 | 345.85 |
| strategy total % | -94.75 | -96.57 |
| Sharpe | -27.8 | -6.53 |
| Sortino | -53.3 | -12.73 |
| max drawdown % | 94.77 | 96.57 |
| profit factor | 0.59 | 0.72 |

**Retained out of sample: negative**

> **Read that number with care.** The author's window was a bear market (buy-and-hold −58%) and the out-of-sample window a bull market (+346%). For a long-biased strategy this ratio rewards having done *badly* in 2018–2020, so it measures regime luck as much as robustness. The regime-free comparison is the excess over buy-and-hold, below.

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free either. Cross-strategy comparisons in this repository use average profit per trade in percent.

**Excess over buy-and-hold** (regime-free): author's window **-36.2 pp**, out of sample **-442.4 pp**.

Baseline: buy-and-hold on the same pairs returned **-58.53%**; the strategy returned **-94.75%**.
Out of sample: buy-and-hold **345.85%** vs strategy **-96.57%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | could not run | вывод не разобран |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | индикаторы меняются от объёма истории: rsi -0.375% |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **15m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `590bf74986c5` · strategy list `a039f448c17bed72`*
