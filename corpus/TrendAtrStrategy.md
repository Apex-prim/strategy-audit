# TrendAtrStrategy

Source: [`mlsys-io/PortfolioBench`](https://github.com/mlsys-io/PortfolioBench) · file `TrendAtrStrategy.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 613 | 2454 |
| average profit per trade % | 0.21 | -0.04 |
| win rate % | 31.6 | 29.3 |
| average trade duration, minutes | 1229.0 | 1307.0 |
| duration measured in own candles | 5.12 | 5.45 |
| expectancy per trade (USDT) | 0.25 | -0.07 |
| mean profit p-value | 0.2945 | 0.5518 |
| market change % (baseline) | -53.45 | 340.8 |
| strategy total % | 15.15 | -17.47 |
| Sharpe | 0.69 | -0.24 |
| Sortino | 1.56 | -0.51 |
| max drawdown % | 18.23 | 39.72 |
| profit factor | 1.11 | 0.97 |

**Retained out of sample: negative**

> **Read that number with care.** The author's window was a bear market (buy-and-hold −58%) and the out-of-sample window a bull market (+346%). For a long-biased strategy this ratio rewards having done *badly* in 2018–2020, so it measures regime luck as much as robustness. The regime-free comparison is the excess over buy-and-hold, below.

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free either. Cross-strategy comparisons in this repository use average profit per trade in percent.

**Excess over buy-and-hold** (regime-free): author's window **+68.6 pp**, out of sample **-358.3 pp**.

⚠ **Not statistically significant in its author's own window** (p = 0.2945 > 0.05): the average trade is not distinguishable from zero.

Baseline: buy-and-hold on the same pairs returned **-53.45%**; the strategy returned **15.15%**.
Out of sample: buy-and-hold **340.8%** vs strategy **-17.47%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | clean | смещения не обнаружено |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | индикаторы меняются от объёма истории: ema_slow -0.169%, atr -0.563%, adx 6.235%, rsi 0.271%, dist_to_mid 0.647% |
| прогрев объявлен | clean | 60 при потребности 14 |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **4h** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `590bf74986c5` · strategy list `a039f448c17bed72`*
