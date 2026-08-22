# IchimokuCloudStrategy

Source: [`mlsys-io/PortfolioBench`](https://github.com/mlsys-io/PortfolioBench) · file `IchimokuCloudStrategy.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 145 | 651 |
| average profit per trade % | 1.62 | 2.41 |
| win rate % | 37.9 | 37.2 |
| average trade duration, minutes | 5417.0 | 5423.0 |
| duration measured in own candles | 22.57 | 22.6 |
| expectancy per trade (USDT) | 2.07 | 6.98 |
| mean profit p-value | 0.04935 | 0.001231 |
| market change % (baseline) | -53.45 | 340.8 |
| strategy total % | 29.97 | 454.67 |
| Sharpe | 0.63 | 0.67 |
| Sortino | 2.1 | 2.38 |
| max drawdown % | 10.62 | 11.59 |
| profit factor | 1.68 | 1.77 |

**Retained out of sample: 337%**

> **Read that number with care.** The author's window was a bear market (buy-and-hold −58%) and the out-of-sample window a bull market (+346%). For a long-biased strategy this ratio rewards having done *badly* in 2018–2020, so it measures regime luck as much as robustness. The regime-free comparison is the excess over buy-and-hold, below.

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free either. Cross-strategy comparisons in this repository use average profit per trade in percent.

**Excess over buy-and-hold** (regime-free): author's window **+83.4 pp**, out of sample **+113.9 pp**.

Baseline: buy-and-hold on the same pairs returned **-53.45%**; the strategy returned **29.97%**.
Out of sample: buy-and-hold **340.8%** vs strategy **454.67%** — **beats the baseline**.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | **found** | ЕСТЬ СМЕЩЕНИЕ: входов 0, выходов 0 из 20 сигналов |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | индикаторы меняются от объёма истории: cloud_top -0.222% |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **4h** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `590bf74986c5` · strategy list `a039f448c17bed72`*
