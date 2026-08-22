# NostalgiaForInfinityNextGen

Source: [`PeetCrypto/freqtrade-stuff`](https://github.com/PeetCrypto/freqtrade-stuff) · file `NostalgiaForInfinityNextGen.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 26 | 132 |
| average profit per trade % | 1.44 | 1.5 |
| win rate % | 92.3 | 91.7 |
| average trade duration, minutes | 957.0 | 678.0 |
| duration measured in own candles | 63.8 | 45.2 |
| expectancy per trade (USDT) | 1.82 | 2.07 |
| mean profit p-value | 0.01923 | 0.00124 |
| market change % (baseline) | -59.37 | 345.85 |
| strategy total % | 4.73 | 27.34 |
| Sharpe | 0.34 | 0.31 |
| Sortino | 1.21 | 0.22 |
| max drawdown % | 1.04 | 5.44 |
| profit factor | 3.41 | 2.31 |

**Retained out of sample: 114%**

> **Read that number with care.** The author's window was a bear market (buy-and-hold −58%) and the out-of-sample window a bull market (+346%). For a long-biased strategy this ratio rewards having done *badly* in 2018–2020, so it measures regime luck as much as robustness. The regime-free comparison is the excess over buy-and-hold, below.

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free either. Cross-strategy comparisons in this repository use average profit per trade in percent.

**Excess over buy-and-hold** (regime-free): author's window **+64.1 pp**, out of sample **-318.5 pp**.

Baseline: buy-and-hold on the same pairs returned **-59.37%**; the strategy returned **4.73%**.
Out of sample: buy-and-hold **345.85%** vs strategy **27.34%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | could not run | вывод не разобран |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | индикаторы меняются от объёма истории: ema_100_1h -0.014%, ema_100 0.019%, ema_200 0.123%, ema_vwma_osc_32 59.436%, ema_vwma_osc_64 1276.906% |
| прогрев не объявлен | **found** | самый длинный индикатор 200 свечей, startup_candle_count не задан (по умолчанию 0) |
| мёртвые настройки трейлинга | **found** | trailing_stop=False, но trailing_stop_positive=0.01 задан — читается как работающая защита |
| признак утечки будущего | **found** | центрированное окно center=True |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **15m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `590bf74986c5` · strategy list `a039f448c17bed72`*
