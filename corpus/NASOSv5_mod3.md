# NASOSv5_mod3

Source: [`PeetCrypto/freqtrade-stuff`](https://github.com/PeetCrypto/freqtrade-stuff) · file `NASOSv5_mod3 (1).py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 81 | 522 |
| expectancy per trade (USDT) | 3.14 | 5.36 |
| mean profit p-value | 0.0006663 | 1.635e-08 |
| market change % (baseline) | -59.05 | 346.34 |
| strategy total % | 25.42 | 279.57 |
| Sharpe | 0.84 | 1.06 |
| Sortino | 0.44 | 0.55 |
| max drawdown % | 3.73 | 14.86 |
| profit factor | 3.26 | 2.54 |

**Retained out of sample: 171%**

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free. Cross-strategy comparisons in this repository use average profit per trade in percent.

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

*Code fingerprint `4a7c7414af9b` · strategy list `dac6309df791d209`*
