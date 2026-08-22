# MACD_TRIPLE_MA

Source: [`PeetCrypto/freqtrade-stuff`](https://github.com/PeetCrypto/freqtrade-stuff) · file `MACD_TRIPLE_MA.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 4251 | 10594 |
| average profit per trade % | -0.19 | -0.25 |
| win rate % | 52.8 | 52.3 |
| average trade duration, minutes | 206.0 | 206.0 |
| duration measured in own candles | 41.2 | 41.2 |
| expectancy per trade (USDT) | -0.15 | -0.09 |
| mean profit p-value | 3.588e-14 | 7.4e-37 |
| market change % (baseline) | -58.46 | 346.34 |
| strategy total % | -63.53 | -96.57 |
| Sharpe | -12.97 | -10.6 |
| Sortino | -13.97 | -10.07 |
| max drawdown % | 64.62 | 96.58 |
| profit factor | 0.66 | 0.58 |

**Retained out of sample: negative**

> **Read that number with care.** The author's window was a bear market (buy-and-hold −58%) and the out-of-sample window a bull market (+346%). For a long-biased strategy this ratio rewards having done *badly* in 2018–2020, so it measures regime luck as much as robustness. The regime-free comparison is the excess over buy-and-hold, below.

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free either. Cross-strategy comparisons in this repository use average profit per trade in percent.

**Excess over buy-and-hold** (regime-free): author's window **-5.1 pp**, out of sample **-442.9 pp**.

Baseline: buy-and-hold on the same pairs returned **-58.46%**; the strategy returned **-63.53%**.
Out of sample: buy-and-hold **346.34%** vs strategy **-96.57%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | could not run | вывод не разобран |
| indicator recursion (freqtrade's own `recursive-analysis`) | clean | рекурсивных отклонений не найдено |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **5m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `590bf74986c5` · strategy list `a039f448c17bed72`*
