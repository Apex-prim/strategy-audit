# VolumeBreakoutStrategy

Source: [`mlsys-io/PortfolioBench`](https://github.com/mlsys-io/PortfolioBench) · file `VolumeBreakoutStrategy.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 7556 | 9008 |
| average profit per trade % | -0.25 | -0.3 |
| win rate % | 30.0 | 31.6 |
| average trade duration, minutes | 179.0 | 168.0 |
| duration measured in own candles | 35.8 | 33.6 |
| expectancy per trade (USDT) | -0.12 | -0.11 |
| mean profit p-value | 9.619e-37 | 9.159e-39 |
| market change % (baseline) | -58.48 | 346.34 |
| strategy total % | -90.85 | -96.59 |
| Sharpe | -28.96 | -10.04 |
| Sortino | -44.2 | -15.07 |
| max drawdown % | 90.91 | 96.59 |
| profit factor | 0.63 | 0.64 |

**Retained out of sample: negative**

> **Read that number with care.** The author's window was a bear market (buy-and-hold −58%) and the out-of-sample window a bull market (+346%). For a long-biased strategy this ratio rewards having done *badly* in 2018–2020, so it measures regime luck as much as robustness. The regime-free comparison is the excess over buy-and-hold, below.

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free either. Cross-strategy comparisons in this repository use average profit per trade in percent.

**Excess over buy-and-hold** (regime-free): author's window **-32.4 pp**, out of sample **-442.9 pp**.

Baseline: buy-and-hold on the same pairs returned **-58.48%**; the strategy returned **-90.85%**.
Out of sample: buy-and-hold **346.34%** vs strategy **-96.59%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | clean | смещения не обнаружено |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | индикаторы меняются от объёма истории: rsi 0.765%, atr -0.109% |
| прогрев объявлен | clean | 50 при потребности 14 |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **5m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `590bf74986c5` · strategy list `a039f448c17bed72`*
