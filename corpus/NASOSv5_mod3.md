# NASOSv5_mod3

Source: [`PeetCrypto/freqtrade-stuff`](https://github.com/PeetCrypto/freqtrade-stuff) · file `NASOSv5_mod3 (1).py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 81 | 522 |
| average profit per trade % | 2.28 | 2.1 |
| win rate % | 95.1 | 95.4 |
| average trade duration, minutes | 2282.0 | 1107.0 |
| duration measured in own candles | 456.4 | 221.4 |
| expectancy per trade (USDT) | 3.14 | 5.36 |
| mean profit p-value | 0.0006663 | 1.635e-08 |
| market change % (baseline) | -59.05 | 346.34 |
| strategy total % | 25.42 | 279.57 |
| Sharpe | 0.84 | 1.06 |
| Sortino | 0.44 | 0.55 |
| max drawdown % | 3.73 | 14.86 |
| profit factor | 3.26 | 2.54 |

**Retained out of sample: 171%**

> **Read that number with care.** The author's window was a bear market (buy-and-hold −58%) and the out-of-sample window a bull market (+346%). For a long-biased strategy this ratio rewards having done *badly* in 2018–2020, so it measures regime luck as much as robustness. The regime-free comparison is the excess over buy-and-hold, below.

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free either. Cross-strategy comparisons in this repository use average profit per trade in percent.

**Excess over buy-and-hold** (regime-free): author's window **+84.5 pp**, out of sample **-66.8 pp**.

Baseline: buy-and-hold on the same pairs returned **-59.05%**; the strategy returned **25.42%**.
Out of sample: buy-and-hold **346.34%** vs strategy **279.57%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | could not run | код 1 |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | индикаторы меняются от объёма истории: EWO -12.317%, rsi_slow 0.021% |
| прогрев объявлен | clean | 200 при потребности 200 |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **5m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `590bf74986c5` · strategy list `a039f448c17bed72`*
