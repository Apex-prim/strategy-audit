# ClucHAnix_5m_old

Source: [`TheoBrigitte/freqtrade`](https://github.com/TheoBrigitte/freqtrade) · file `ClucHAnix_5m_old.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 644 | 2190 |
| average profit per trade % | 0.21 | 0.29 |
| win rate % | 60.1 | 60.2 |
| average trade duration, minutes | 148.0 | 101.0 |
| duration measured in own candles | 29.6 | 20.2 |
| expectancy per trade (USDT) | 0.27 | 0.51 |
| mean profit p-value | 0.02739 | 6.489e-05 |
| market change % (baseline) | -59.11 | 346.34 |
| strategy total % | 17.48 | 111.99 |
| Sharpe | 1.47 | 1.52 |
| Sortino | 1.31 | 1.13 |
| max drawdown % | 7.64 | 20.52 |
| profit factor | 1.29 | 1.4 |

**Retained out of sample: 189%**

> **Read that number with care.** The author's window was a bear market (buy-and-hold −58%) and the out-of-sample window a bull market (+346%). For a long-biased strategy this ratio rewards having done *badly* in 2018–2020, so it measures regime luck as much as robustness. The regime-free comparison is the excess over buy-and-hold, below.

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free either. Cross-strategy comparisons in this repository use average profit per trade in percent.

**Excess over buy-and-hold** (regime-free): author's window **+76.6 pp**, out of sample **-234.3 pp**.

Baseline: buy-and-hold on the same pairs returned **-59.11%**; the strategy returned **17.48%**.
Out of sample: buy-and-hold **346.34%** vs strategy **111.99%** — loses to it.

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
