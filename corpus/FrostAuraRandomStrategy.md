# FrostAuraRandomStrategy

Source: [`davidzr/freqtrade-strategies`](https://github.com/davidzr/freqtrade-strategies) · file `FrostAuraRandomStrategy.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 1260 | 4561 |
| average profit per trade % | -0.58 | -0.05 |
| win rate % | 65.9 | 68.6 |
| average trade duration, minutes | 4903.0 | 4961.0 |
| duration measured in own candles | 81.72 | 82.68 |
| expectancy per trade (USDT) | -0.58 | -0.17 |
| mean profit p-value | 0.0002994 | 0.4394 |
| market change % (baseline) | -59.27 | 348.67 |
| strategy total % | -73.13 | -77.42 |
| Sharpe | -3.37 | -0.42 |
| Sortino | -2.49 | -0.3 |
| max drawdown % | 77.94 | 92.99 |
| profit factor | 0.65 | 0.95 |

**Retained out of sample: negative**

> **Read that number with care.** The author's window was a bear market (buy-and-hold −58%) and the out-of-sample window a bull market (+346%). For a long-biased strategy this ratio rewards having done *badly* in 2018–2020, so it measures regime luck as much as robustness. The regime-free comparison is the excess over buy-and-hold, below.

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free either. Cross-strategy comparisons in this repository use average profit per trade in percent.

**Excess over buy-and-hold** (regime-free): author's window **-13.9 pp**, out of sample **-426.1 pp**.

Baseline: buy-and-hold on the same pairs returned **-59.27%**; the strategy returned **-73.13%**.
Out of sample: buy-and-hold **348.67%** vs strategy **-77.42%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | **found** | ЕСТЬ СМЕЩЕНИЕ: входов 15, выходов 16 из 20 сигналов |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | индикаторы меняются от объёма истории: random_number 34.483% |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **1h** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `590bf74986c5` · strategy list `a039f448c17bed72`*
