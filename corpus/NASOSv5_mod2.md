# NASOSv5_mod2

Source: [`PeetCrypto/freqtrade-stuff`](https://github.com/PeetCrypto/freqtrade-stuff) · file `NASOSv5_mod2 (1).py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 26 | 293 |
| average profit per trade % | 1.95 | 2.39 |
| win rate % | 96.2 | 95.6 |
| average trade duration, minutes | 1185.0 | 173.0 |
| duration measured in own candles | 237.0 | 34.6 |
| expectancy per trade (USDT) | 2.45 | 4.58 |
| mean profit p-value | 0.1673 | 9.317e-10 |
| market change % (baseline) | -59.05 | 346.34 |
| strategy total % | 6.37 | 134.23 |
| Sharpe | 0.19 | 0.88 |
| Sortino | -100.0 | 0.57 |
| max drawdown % | 3.73 | 14.85 |
| profit factor | 2.57 | 3.44 |

**Retained out of sample: 187%**

> **Read that number with care.** The author's window was a bear market (buy-and-hold −58%) and the out-of-sample window a bull market (+346%). For a long-biased strategy this ratio rewards having done *badly* in 2018–2020, so it measures regime luck as much as robustness. The regime-free comparison is the excess over buy-and-hold, below.

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free either. Cross-strategy comparisons in this repository use average profit per trade in percent.

**Excess over buy-and-hold** (regime-free): author's window **+65.4 pp**, out of sample **-212.1 pp**.

⚠ **Not statistically significant in its author's own window** (p = 0.1673 > 0.05): the average trade is not distinguishable from zero.

Baseline: buy-and-hold on the same pairs returned **-59.05%**; the strategy returned **6.37%**.
Out of sample: buy-and-hold **346.34%** vs strategy **134.23%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | could not run | код 1 |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | индикаторы меняются от объёма истории: EWO -12.317%, rsi_slow 0.021% |
| прогрев объявлен | clean | 200 при потребности 200 |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **5m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `590bf74986c5` · strategy list `a039f448c17bed72`*
