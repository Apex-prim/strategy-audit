# twinturboV8

Source: [`TheoBrigitte/freqtrade`](https://github.com/TheoBrigitte/freqtrade) · file `twinturboV8.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 24 | 107 |
| average profit per trade % | 1.21 | 0.93 |
| win rate % | 91.7 | 83.2 |
| average trade duration, minutes | 950.0 | 810.0 |
| duration measured in own candles | 190.0 | 162.0 |
| expectancy per trade (USDT) | 1.5 | 1.19 |
| mean profit p-value | 0.2921 | 0.1452 |
| market change % (baseline) | -58.3 | 346.34 |
| strategy total % | 3.59 | 12.69 |
| Sharpe | 0.14 | 0.12 |
| Sortino | 0.07 | 0.07 |
| max drawdown % | 2.83 | 5.9 |
| profit factor | 2.15 | 1.63 |

**Retained out of sample: 79%**

> **Read that number with care.** The author's window was a bear market (buy-and-hold −58%) and the out-of-sample window a bull market (+346%). For a long-biased strategy this ratio rewards having done *badly* in 2018–2020, so it measures regime luck as much as robustness. The regime-free comparison is the excess over buy-and-hold, below.

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free either. Cross-strategy comparisons in this repository use average profit per trade in percent.

**Excess over buy-and-hold** (regime-free): author's window **+61.9 pp**, out of sample **-333.6 pp**.

⚠ **Not statistically significant in its author's own window** (p = 0.2921 > 0.05): the average trade is not distinguishable from zero.

Baseline: buy-and-hold on the same pairs returned **-58.3%**; the strategy returned **3.59%**.
Out of sample: buy-and-hold **346.34%** vs strategy **12.69%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | could not run | вывод не разобран |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | индикаторы меняются от объёма истории: BTC_EWO_Fast_1h 13.218%, rsi -4.207%, rsi_slow -7.999% |
| прогрев занижен | **found** | объявлено 35, нужно не менее 200 |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **5m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `590bf74986c5` · strategy list `a039f448c17bed72`*
