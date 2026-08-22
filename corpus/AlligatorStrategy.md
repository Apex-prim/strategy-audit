# AlligatorStrategy

Source: [`PeetCrypto/freqtrade-stuff`](https://github.com/PeetCrypto/freqtrade-stuff) · file `AlligatorStrategy.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 344 | 1495 |
| average profit per trade % | 1.83 | 1.46 |
| win rate % | 32.8 | 30.7 |
| average trade duration, minutes | 5319.0 | 5029.0 |
| duration measured in own candles | 88.65 | 83.82 |
| expectancy per trade (USDT) | 2.91 | 4.21 |
| mean profit p-value | 0.002122 | 0.06972 |
| market change % (baseline) | -54.03 | 348.67 |
| strategy total % | 100.04 | 629.58 |
| Sharpe | 1.52 | 0.57 |
| Sortino | 7.19 | 2.15 |
| max drawdown % | 7.22 | 33.63 |
| profit factor | 1.96 | 1.27 |

**Retained out of sample: 145%**

> **Read that number with care.** The author's window was a bear market (buy-and-hold −58%) and the out-of-sample window a bull market (+346%). For a long-biased strategy this ratio rewards having done *badly* in 2018–2020, so it measures regime luck as much as robustness. The regime-free comparison is the excess over buy-and-hold, below.

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free either. Cross-strategy comparisons in this repository use average profit per trade in percent.

**Excess over buy-and-hold** (regime-free): author's window **+154.1 pp**, out of sample **+280.9 pp**.

Baseline: buy-and-hold on the same pairs returned **-54.03%**; the strategy returned **100.04%**.
Out of sample: buy-and-hold **348.67%** vs strategy **629.58%** — **beats the baseline**.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | could not run | вывод не разобран |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | индикаторы меняются от объёма истории: ema200 0.039% |
| прогрев объявлен | clean | 200 при потребности 200 |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **1h** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `590bf74986c5` · strategy list `a039f448c17bed72`*
