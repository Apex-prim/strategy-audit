# NASOSv5_mod1

Source: [`PeetCrypto/freqtrade-stuff`](https://github.com/PeetCrypto/freqtrade-stuff) · file `NASOSv5_mod1 (1).py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 50 | 472 |
| average profit per trade % | 2.13 | 2.35 |
| win rate % | 96.0 | 95.8 |
| average trade duration, minutes | 2515.0 | 996.0 |
| duration measured in own candles | 503.0 | 199.2 |
| expectancy per trade (USDT) | 2.75 | 6.14 |
| mean profit p-value | 0.04952 | 4.448e-11 |
| market change % (baseline) | -59.05 | 346.34 |
| strategy total % | 13.76 | 289.68 |
| Sharpe | 0.38 | 1.19 |
| Sortino | 12.65 | 0.53 |
| max drawdown % | 7.41 | 11.08 |
| profit factor | 2.57 | 3.16 |

**Retained out of sample: 223%**

> **Read that number with care.** The author's window was a bear market (buy-and-hold −58%) and the out-of-sample window a bull market (+346%). For a long-biased strategy this ratio rewards having done *badly* in 2018–2020, so it measures regime luck as much as robustness. The regime-free comparison is the excess over buy-and-hold, below.

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free either. Cross-strategy comparisons in this repository use average profit per trade in percent.

**Excess over buy-and-hold** (regime-free): author's window **+72.8 pp**, out of sample **-56.7 pp**.

Baseline: buy-and-hold on the same pairs returned **-59.05%**; the strategy returned **13.76%**.
Out of sample: buy-and-hold **346.34%** vs strategy **289.68%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | could not run | код 1 |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | индикаторы меняются от объёма истории: EWO -12.317%, rsi_slow 0.021% |
| прогрев объявлен | clean | 200 при потребности 200 |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **5m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `590bf74986c5` · strategy list `a039f448c17bed72`*
