# LuxOSC

Source: [`PeetCrypto/freqtrade-stuff`](https://github.com/PeetCrypto/freqtrade-stuff) · file `LuxOSC.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 3207 | 11370 |
| average profit per trade % | -0.28 | -0.13 |
| win rate % | 60.4 | 61.5 |
| average trade duration, minutes | 1056.0 | 1102.0 |
| duration measured in own candles | 211.2 | 220.4 |
| expectancy per trade (USDT) | -0.23 | -0.08 |
| mean profit p-value | 4.531e-07 | 0.05759 |
| market change % (baseline) | -58.37 | 346.34 |
| strategy total % | -72.27 | -90.44 |
| Sharpe | -7.49 | -1.64 |
| Sortino | -6.56 | -1.32 |
| max drawdown % | 76.24 | 95.91 |
| profit factor | 0.73 | 0.92 |

**Retained out of sample: negative**

> **Read that number with care.** The author's window was a bear market (buy-and-hold −58%) and the out-of-sample window a bull market (+346%). For a long-biased strategy this ratio rewards having done *badly* in 2018–2020, so it measures regime luck as much as robustness. The regime-free comparison is the excess over buy-and-hold, below.

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free either. Cross-strategy comparisons in this repository use average profit per trade in percent.

**Excess over buy-and-hold** (regime-free): author's window **-13.9 pp**, out of sample **-436.8 pp**.

Baseline: buy-and-hold on the same pairs returned **-58.37%**; the strategy returned **-72.27%**.
Out of sample: buy-and-hold **346.34%** vs strategy **-90.44%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | could not run | вывод не разобран |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | индикаторы меняются от объёма истории: osc 16.276%, signal 19.689%, supertrend -0.118% |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **5m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `590bf74986c5` · strategy list `a039f448c17bed72`*
