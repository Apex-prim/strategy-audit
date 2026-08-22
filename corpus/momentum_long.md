# momentum_long

Source: [`TheoBrigitte/freqtrade`](https://github.com/TheoBrigitte/freqtrade) · file `momentum_long.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 3865 | 12102 |
| average profit per trade % | -0.36 | -0.16 |
| win rate % | 80.6 | 82.3 |
| average trade duration, minutes | 1634.0 | 1503.0 |
| duration measured in own candles | 326.8 | 300.6 |
| expectancy per trade (USDT) | -0.23 | -0.08 |
| mean profit p-value | 3.005e-08 | 0.007536 |
| market change % (baseline) | -58.35 | 346.34 |
| strategy total % | -87.06 | -96.76 |
| Sharpe | -9.04 | -2.38 |
| Sortino | -8.45 | -1.67 |
| max drawdown % | 88.53 | 97.22 |
| profit factor | 0.75 | 0.92 |

**Retained out of sample: negative**

> **Read that number with care.** The author's window was a bear market (buy-and-hold −58%) and the out-of-sample window a bull market (+346%). For a long-biased strategy this ratio rewards having done *badly* in 2018–2020, so it measures regime luck as much as robustness. The regime-free comparison is the excess over buy-and-hold, below.

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free either. Cross-strategy comparisons in this repository use average profit per trade in percent.

**Excess over buy-and-hold** (regime-free): author's window **-28.7 pp**, out of sample **-443.1 pp**.

Baseline: buy-and-hold on the same pairs returned **-58.35%**; the strategy returned **-87.06%**.
Out of sample: buy-and-hold **346.34%** vs strategy **-96.76%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | clean | смещения не обнаружено |
| indicator recursion (freqtrade's own `recursive-analysis`) | clean | рекурсивных отклонений не найдено |
| мёртвые настройки трейлинга | **found** | trailing_stop=False, но trailing_stop_positive=0.01 задан — читается как работающая защита |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **5m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `590bf74986c5` · strategy list `a039f448c17bed72`*
