# NostalgiaForInfinityV4HO

Source: [`PeetCrypto/freqtrade-stuff`](https://github.com/PeetCrypto/freqtrade-stuff) · file `NostalgiaForInfinityV4HO (1).py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 78 | 301 |
| average profit per trade % | 0.93 | 1.32 |
| win rate % | 80.8 | 89.7 |
| average trade duration, minutes | 132.0 | 113.0 |
| duration measured in own candles | 26.4 | 22.6 |
| expectancy per trade (USDT) | 1.2 | 2.1 |
| mean profit p-value | 0.0004817 | 9.126e-12 |
| market change % (baseline) | -59.23 | 346.34 |
| strategy total % | 9.36 | 63.18 |
| Sharpe | 0.85 | 1.0 |
| Sortino | 0.68 | 0.46 |
| max drawdown % | 2.5 | 5.07 |
| profit factor | 2.88 | 3.99 |

**Retained out of sample: 175%**

> **Read that number with care.** The author's window was a bear market (buy-and-hold −58%) and the out-of-sample window a bull market (+346%). For a long-biased strategy this ratio rewards having done *badly* in 2018–2020, so it measures regime luck as much as robustness. The regime-free comparison is the excess over buy-and-hold, below.

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free either. Cross-strategy comparisons in this repository use average profit per trade in percent.

**Excess over buy-and-hold** (regime-free): author's window **+68.6 pp**, out of sample **-283.2 pp**.

Baseline: buy-and-hold on the same pairs returned **-59.23%**; the strategy returned **9.36%**.
Out of sample: buy-and-hold **346.34%** vs strategy **63.18%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | could not run | вывод не разобран |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | индикаторы меняются от объёма истории: ema_100_1h -0.014%, ewo -12.317% |
| прогрев не объявлен | **found** | самый длинный индикатор 200 свечей, startup_candle_count не задан (по умолчанию 0) |
| мёртвые настройки трейлинга | **found** | trailing_stop=False, но trailing_stop_positive=0.01 задан — читается как работающая защита |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **5m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `590bf74986c5` · strategy list `a039f448c17bed72`*
