# ElliotV5HOMod3

Source: [`davidzr/freqtrade-strategies`](https://github.com/davidzr/freqtrade-strategies) · file `ElliotV5HOMod3.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 88 | 459 |
| average profit per trade % | -0.04 | 1.48 |
| win rate % | 46.6 | 56.2 |
| average trade duration, minutes | 1224.0 | 465.0 |
| duration measured in own candles | 244.8 | 93.0 |
| expectancy per trade (USDT) | -0.11 | 2.68 |
| mean profit p-value | 0.9003 | 3.493e-05 |
| market change % (baseline) | -58.45 | 346.34 |
| strategy total % | -0.95 | 123.16 |
| Sharpe | -0.03 | 0.73 |
| Sortino | -1.48 | 3.12 |
| max drawdown % | 7.96 | 9.75 |
| profit factor | 0.97 | 1.53 |

**Retained out of sample: n/a**

> **Read that number with care.** The author's window was a bear market (buy-and-hold −58%) and the out-of-sample window a bull market (+346%). For a long-biased strategy this ratio rewards having done *badly* in 2018–2020, so it measures regime luck as much as robustness. The regime-free comparison is the excess over buy-and-hold, below.

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free either. Cross-strategy comparisons in this repository use average profit per trade in percent.

**Excess over buy-and-hold** (regime-free): author's window **+57.5 pp**, out of sample **-223.2 pp**.

⚠ **Not statistically significant in its author's own window** (p = 0.9003 > 0.05): the average trade is not distinguishable from zero.

Baseline: buy-and-hold on the same pairs returned **-58.45%**; the strategy returned **-0.95%**.
Out of sample: buy-and-hold **346.34%** vs strategy **123.16%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | could not run | вывод не разобран |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | индикаторы меняются от объёма истории: rsi 0.205% |
| прогрев объявлен | clean | 79 при потребности 14 |
| мёртвые настройки трейлинга | **found** | trailing_stop=False, но trailing_stop_positive=0.005 задан — читается как работающая защита |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **5m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `590bf74986c5` · strategy list `a039f448c17bed72`*
