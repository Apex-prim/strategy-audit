# cryptotank

Source: [`jaredrsommer/freqtradestrategies`](https://github.com/jaredrsommer/freqtradestrategies) · file `cryptotank.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 510 | 1802 |
| average profit per trade % | 0.2 | 0.38 |
| win rate % | 80.0 | 75.9 |
| average trade duration, minutes | 3876.0 | 2455.0 |
| duration measured in own candles | 64.6 | 40.92 |
| expectancy per trade (USDT) | -1.32 | -0.52 |
| mean profit p-value | 0.008512 | 0.001626 |
| market change % (baseline) | -59.27 | 348.67 |
| strategy total % | -67.44 | -93.47 |
| Sharpe | -1.56 | -1.08 |
| Sortino | -0.94 | -0.63 |
| max drawdown % | 68.15 | 93.47 |
| profit factor | 0.59 | 0.67 |

**Retained out of sample: negative**

> **Read that number with care.** The author's window was a bear market (buy-and-hold −58%) and the out-of-sample window a bull market (+346%). For a long-biased strategy this ratio rewards having done *badly* in 2018–2020, so it measures regime luck as much as robustness. The regime-free comparison is the excess over buy-and-hold, below.

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free either. Cross-strategy comparisons in this repository use average profit per trade in percent.

**Excess over buy-and-hold** (regime-free): author's window **-8.2 pp**, out of sample **-442.1 pp**.

Baseline: buy-and-hold on the same pairs returned **-59.27%**; the strategy returned **-67.44%**.
Out of sample: buy-and-hold **348.67%** vs strategy **-93.47%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | clean | смещения не обнаружено |
| indicator recursion (freqtrade's own `recursive-analysis`) | clean | рекурсивных отклонений не найдено |
| трейлинг на полном стопе | **found** | trailing_stop=True без trailing_stop_positive ⇒ стоп тащится на ВСЁ расстояние стоп-лосса |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **1h** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `590bf74986c5` · strategy list `a039f448c17bed72`*
