# NASOSv5_mod2

Source: [`PeetCrypto/freqtrade-stuff`](https://github.com/PeetCrypto/freqtrade-stuff) · file `NASOSv5_mod2 (1).py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 26 | 293 |
| expectancy per trade (USDT) | 2.45 | 4.58 |
| mean profit p-value | 0.1673 | 9.317e-10 |
| market change % (baseline) | -59.05 | 346.34 |
| strategy total % | 6.37 | 134.23 |
| Sharpe | 0.19 | 0.88 |
| Sortino | -100.0 | 0.57 |
| max drawdown % | 3.73 | 14.85 |
| profit factor | 2.57 | 3.44 |

**Retained out of sample: 187%**

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free. Cross-strategy comparisons in this repository use average profit per trade in percent.

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

*Code fingerprint `4a7c7414af9b` · strategy list `dac6309df791d209`*
