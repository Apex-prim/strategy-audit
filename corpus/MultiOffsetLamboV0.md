# MultiOffsetLamboV0

Source: [`Foxel05/freqtrade-stuff`](https://github.com/Foxel05/freqtrade-stuff) · file `MultiOffsetLamboV0.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 26 | 174 |
| average profit per trade % | 0.8 | 1.38 |
| win rate % | 92.3 | 93.7 |
| average trade duration, minutes | 49.0 | 49.0 |
| duration measured in own candles | 9.8 | 9.8 |
| expectancy per trade (USDT) | 1.01 | 1.95 |
| mean profit p-value | 0.0135 | 0.0003129 |
| market change % (baseline) | -58.37 | 346.34 |
| strategy total % | 2.62 | 33.84 |
| Sharpe | 0.36 | 0.39 |
| Sortino | 0.3 | 0.21 |
| max drawdown % | 0.68 | 4.32 |
| profit factor | 3.83 | 3.96 |

**Retained out of sample: 193%**

> **Read that number with care.** The author's window was a bear market (buy-and-hold −58%) and the out-of-sample window a bull market (+346%). For a long-biased strategy this ratio rewards having done *badly* in 2018–2020, so it measures regime luck as much as robustness. The regime-free comparison is the excess over buy-and-hold, below.

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free either. Cross-strategy comparisons in this repository use average profit per trade in percent.

**Excess over buy-and-hold** (regime-free): author's window **+61.0 pp**, out of sample **-312.5 pp**.

Baseline: buy-and-hold on the same pairs returned **-58.37%**; the strategy returned **2.62%**.
Out of sample: buy-and-hold **346.34%** vs strategy **33.84%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | could not run | вывод не разобран |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | индикаторы меняются от объёма истории: kama_offset_buy 0.037% |
| мёртвые настройки трейлинга | **found** | trailing_stop=False, но trailing_stop_positive=0.001 задан — читается как работающая защита |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **5m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `590bf74986c5` · strategy list `a039f448c17bed72`*
