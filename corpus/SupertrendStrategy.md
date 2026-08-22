# SupertrendStrategy

Source: [`PeetCrypto/freqtrade-stuff`](https://github.com/PeetCrypto/freqtrade-stuff) · file `SupertrendStrategy.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 718 | 3102 |
| average profit per trade % | 0.83 | 0.7 |
| win rate % | 34.8 | 33.3 |
| average trade duration, minutes | 3876.0 | 3497.0 |
| duration measured in own candles | 64.6 | 58.28 |
| expectancy per trade (USDT) | 1.15 | 1.7 |
| mean profit p-value | 0.02502 | 0.1334 |
| market change % (baseline) | -59.54 | 348.67 |
| strategy total % | 82.54 | 527.28 |
| Sharpe | 1.58 | 0.68 |
| Sortino | 5.38 | 2.29 |
| max drawdown % | 27.06 | 56.13 |
| profit factor | 1.37 | 1.15 |

**Retained out of sample: 148%**

> **Read that number with care.** The author's window was a bear market (buy-and-hold −58%) and the out-of-sample window a bull market (+346%). For a long-biased strategy this ratio rewards having done *badly* in 2018–2020, so it measures regime luck as much as robustness. The regime-free comparison is the excess over buy-and-hold, below.

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free either. Cross-strategy comparisons in this repository use average profit per trade in percent.

**Excess over buy-and-hold** (regime-free): author's window **+142.1 pp**, out of sample **+178.6 pp**.

Baseline: buy-and-hold on the same pairs returned **-59.54%**; the strategy returned **82.54%**.
Out of sample: buy-and-hold **348.67%** vs strategy **527.28%** — **beats the baseline**.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | could not run | вывод не разобран |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | индикаторы меняются от объёма истории: ema90 0.130%, supertrend_1 0.045%, supertrend_3 0.065% |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **1h** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `590bf74986c5` · strategy list `a039f448c17bed72`*
