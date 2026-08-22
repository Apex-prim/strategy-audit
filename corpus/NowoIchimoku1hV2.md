# NowoIchimoku1hV2

Source: [`PeetCrypto/freqtrade-stuff`](https://github.com/PeetCrypto/freqtrade-stuff) · file `NowoIchimoku1hV2 (1).py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 745 | 2950 |
| average profit per trade % | 0.69 | 0.53 |
| win rate % | 71.9 | 72.8 |
| average trade duration, minutes | 2014.0 | 1983.0 |
| duration measured in own candles | 33.57 | 33.05 |
| expectancy per trade (USDT) | 1.14 | 1.84 |
| mean profit p-value | 1.232e-05 | 5.013e-06 |
| market change % (baseline) | -59.69 | 348.67 |
| strategy total % | 85.03 | 541.93 |
| Sharpe | 3.16 | 2.01 |
| Sortino | 3.36 | 1.88 |
| max drawdown % | 11.46 | 14.93 |
| profit factor | 1.55 | 1.31 |

**Retained out of sample: 161%**

> **Read that number with care.** The author's window was a bear market (buy-and-hold −58%) and the out-of-sample window a bull market (+346%). For a long-biased strategy this ratio rewards having done *badly* in 2018–2020, so it measures regime luck as much as robustness. The regime-free comparison is the excess over buy-and-hold, below.

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free either. Cross-strategy comparisons in this repository use average profit per trade in percent.

**Excess over buy-and-hold** (regime-free): author's window **+144.7 pp**, out of sample **+193.3 pp**.

Baseline: buy-and-hold on the same pairs returned **-59.69%**; the strategy returned **85.03%**.
Out of sample: buy-and-hold **348.67%** vs strategy **541.93%** — **beats the baseline**.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | could not run | вывод не разобран |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | индикаторы меняются от объёма истории: srsi_k 0.048%, srsi_d 0.082% |
| трейлинг на полном стопе | **found** | trailing_stop=True без trailing_stop_positive ⇒ стоп тащится на ВСЁ расстояние стоп-лосса |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **1h** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `590bf74986c5` · strategy list `a039f448c17bed72`*
