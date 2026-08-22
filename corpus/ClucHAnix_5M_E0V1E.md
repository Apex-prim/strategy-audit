# ClucHAnix_5M_E0V1E

Source: [`phuchust/freqtrade_strategy`](https://github.com/phuchust/freqtrade_strategy) · file `ClucHAnix_5M_E0V1E_DYNAMIC_TB.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 1232 | 4227 |
| average profit per trade % | 0.25 | 0.11 |
| win rate % | 68.1 | 68.9 |
| average trade duration, minutes | 228.0 | 182.0 |
| duration measured in own candles | 45.6 | 36.4 |
| expectancy per trade (USDT) | 0.36 | 0.11 |
| mean profit p-value | 0.003894 | 0.26 |
| market change % (baseline) | -59.11 | 346.34 |
| strategy total % | 44.25 | 46.54 |
| Sharpe | 2.66 | 0.59 |
| Sortino | 2.33 | 0.47 |
| max drawdown % | 7.71 | 46.12 |
| profit factor | 1.26 | 1.06 |

**Retained out of sample: 31%**

> **Read that number with care.** The author's window was a bear market (buy-and-hold −58%) and the out-of-sample window a bull market (+346%). For a long-biased strategy this ratio rewards having done *badly* in 2018–2020, so it measures regime luck as much as robustness. The regime-free comparison is the excess over buy-and-hold, below.

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free either. Cross-strategy comparisons in this repository use average profit per trade in percent.

**Excess over buy-and-hold** (regime-free): author's window **+103.4 pp**, out of sample **-299.8 pp**.

Baseline: buy-and-hold on the same pairs returned **-59.11%**; the strategy returned **44.25%**.
Out of sample: buy-and-hold **346.34%** vs strategy **46.54%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | clean | смещения не обнаружено |
| indicator recursion (freqtrade's own `recursive-analysis`) | clean | рекурсивных отклонений не найдено |
| прогрев объявлен | clean | 168 при потребности 168 |
| мёртвые настройки трейлинга | **found** | trailing_stop=False, но trailing_stop_positive=0.3207 задан — читается как работающая защита |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **5m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `590bf74986c5` · strategy list `a039f448c17bed72`*
