# NWEv6_new

Source: [`anakein/beastbotXB`](https://github.com/anakein/beastbotXB) · file `NWEv6_new.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 1869 | 6239 |
| average profit per trade % | -0.51 | -0.38 |
| win rate % | 66.8 | 67.1 |
| average trade duration, minutes | 538.0 | 577.0 |
| duration measured in own candles | 179.33 | 192.33 |
| expectancy per trade (USDT) | -0.38 | -0.15 |
| mean profit p-value | 2.66e-16 | 2.109e-16 |
| market change % (baseline) | -56.37 | 347.44 |
| strategy total % | -70.27 | -95.02 |
| Sharpe | -9.35 | -5.26 |
| Sortino | -11.21 | -4.66 |
| max drawdown % | 70.66 | 95.13 |
| profit factor | 0.59 | 0.71 |

**Retained out of sample: negative**

> **Read that number with care.** The author's window was a bear market (buy-and-hold −58%) and the out-of-sample window a bull market (+346%). For a long-biased strategy this ratio rewards having done *badly* in 2018–2020, so it measures regime luck as much as robustness. The regime-free comparison is the excess over buy-and-hold, below.

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free either. Cross-strategy comparisons in this repository use average profit per trade in percent.

**Excess over buy-and-hold** (regime-free): author's window **-13.9 pp**, out of sample **-442.5 pp**.

Baseline: buy-and-hold on the same pairs returned **-56.37%**; the strategy returned **-70.27%**.
Out of sample: buy-and-hold **347.44%** vs strategy **-95.02%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | clean | смещения не обнаружено |
| indicator recursion (freqtrade's own `recursive-analysis`) | clean | рекурсивных отклонений не найдено |
| прогрев не объявлен | **found** | самый длинный индикатор 500 свечей, startup_candle_count не задан (по умолчанию 0) |
| мёртвые настройки трейлинга | **found** | trailing_stop=False, но trailing_stop_positive=0.005 задан — читается как работающая защита |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **3m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `590bf74986c5` · strategy list `a039f448c17bed72`*
