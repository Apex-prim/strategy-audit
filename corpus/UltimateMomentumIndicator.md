# UltimateMomentumIndicator

Source: [`PeetCrypto/freqtrade-stuff`](https://github.com/PeetCrypto/freqtrade-stuff) · file `UltimateMomentumIndicator.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 1765 | 6382 |
| average profit per trade % | -0.38 | 0.14 |
| win rate % | 48.2 | 50.0 |
| average trade duration, minutes | 3462.0 | 3508.0 |
| duration measured in own candles | 692.4 | 701.6 |
| expectancy per trade (USDT) | -0.39 | -0.01 |
| mean profit p-value | 0.0002804 | 0.9665 |
| market change % (baseline) | -58.37 | 346.34 |
| strategy total % | -69.69 | -8.43 |
| Sharpe | -4.0 | -0.03 |
| Sortino | -4.73 | -0.04 |
| max drawdown % | 78.83 | 86.37 |
| profit factor | 0.76 | 1.0 |

**Retained out of sample: negative**

> **Read that number with care.** The author's window was a bear market (buy-and-hold −58%) and the out-of-sample window a bull market (+346%). For a long-biased strategy this ratio rewards having done *badly* in 2018–2020, so it measures regime luck as much as robustness. The regime-free comparison is the excess over buy-and-hold, below.

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free either. Cross-strategy comparisons in this repository use average profit per trade in percent.

**Excess over buy-and-hold** (regime-free): author's window **-11.3 pp**, out of sample **-354.8 pp**.

Baseline: buy-and-hold on the same pairs returned **-58.37%**; the strategy returned **-69.69%**.
Out of sample: buy-and-hold **346.34%** vs strategy **-8.43%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | could not run | вывод не разобран |
| indicator recursion (freqtrade's own `recursive-analysis`) | clean | рекурсивных отклонений не найдено |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **5m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `590bf74986c5` · strategy list `a039f448c17bed72`*
