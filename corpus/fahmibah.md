# fahmibah

Source: [`davidzr/freqtrade-strategies`](https://github.com/davidzr/freqtrade-strategies) · file `fahmibah.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 5242 | 15701 |
| average profit per trade % | -0.28 | -0.13 |
| win rate % | 86.8 | 87.1 |
| average trade duration, minutes | 1040.0 | 971.0 |
| duration measured in own candles | 208.0 | 194.2 |
| expectancy per trade (USDT) | -0.17 | -0.06 |
| mean profit p-value | 1.008e-09 | 0.002274 |
| market change % (baseline) | -59.11 | 346.34 |
| strategy total % | -87.38 | -96.66 |
| Sharpe | -11.6 | -3.09 |
| Sortino | -7.48 | -1.73 |
| max drawdown % | 89.35 | 97.4 |
| profit factor | 0.7 | 0.9 |

**Retained out of sample: negative**

> **Read that number with care.** The author's window was a bear market (buy-and-hold −58%) and the out-of-sample window a bull market (+346%). For a long-biased strategy this ratio rewards having done *badly* in 2018–2020, so it measures regime luck as much as robustness. The regime-free comparison is the excess over buy-and-hold, below.

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free either. Cross-strategy comparisons in this repository use average profit per trade in percent.

**Excess over buy-and-hold** (regime-free): author's window **-28.3 pp**, out of sample **-443.0 pp**.

Baseline: buy-and-hold on the same pairs returned **-59.11%**; the strategy returned **-87.38%**.
Out of sample: buy-and-hold **346.34%** vs strategy **-96.66%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | clean | смещения не обнаружено |
| indicator recursion (freqtrade's own `recursive-analysis`) | clean | рекурсивных отклонений не найдено |
| прогрев объявлен | clean | 168 при потребности 168 |
| мёртвые настройки трейлинга | **found** | trailing_stop=False, но trailing_stop_positive=0.001 задан — читается как работающая защита |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **5m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `590bf74986c5` · strategy list `a039f448c17bed72`*
