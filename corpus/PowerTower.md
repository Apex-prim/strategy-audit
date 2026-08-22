# PowerTower

Source: [`TheoBrigitte/freqtrade`](https://github.com/TheoBrigitte/freqtrade) · file `PowerTower.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 1232 | 3769 |
| average profit per trade % | -0.43 | 0.07 |
| win rate % | 66.6 | 69.7 |
| average trade duration, minutes | 2321.0 | 2244.0 |
| duration measured in own candles | 464.2 | 448.8 |
| expectancy per trade (USDT) | -0.44 | 0.04 |
| mean profit p-value | 0.007949 | 0.815 |
| market change % (baseline) | -58.37 | 346.34 |
| strategy total % | -53.74 | 13.42 |
| Sharpe | -2.44 | 0.12 |
| Sortino | -1.57 | 0.07 |
| max drawdown % | 55.58 | 46.68 |
| profit factor | 0.62 | 1.02 |

**Retained out of sample: n/a**

> **Read that number with care.** The author's window was a bear market (buy-and-hold −58%) and the out-of-sample window a bull market (+346%). For a long-biased strategy this ratio rewards having done *badly* in 2018–2020, so it measures regime luck as much as robustness. The regime-free comparison is the excess over buy-and-hold, below.

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free either. Cross-strategy comparisons in this repository use average profit per trade in percent.

**Excess over buy-and-hold** (regime-free): author's window **+4.6 pp**, out of sample **-332.9 pp**.

Baseline: buy-and-hold on the same pairs returned **-58.37%**; the strategy returned **-53.74%**.
Out of sample: buy-and-hold **346.34%** vs strategy **13.42%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | clean | смещения не обнаружено |
| indicator recursion (freqtrade's own `recursive-analysis`) | clean | рекурсивных отклонений не найдено |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **5m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `590bf74986c5` · strategy list `a039f448c17bed72`*
