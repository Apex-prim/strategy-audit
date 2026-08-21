# NASOSv4

Source: [`PeetCrypto/freqtrade-stuff`](https://github.com/PeetCrypto/freqtrade-stuff) · file `NASOSv4.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 259 | 1093 |
| expectancy per trade (USDT) | 1.83 | 2.15 |
| mean profit p-value | 1.338e-07 | 1.342e-06 |
| market change % (baseline) | -59.05 | 346.34 |
| strategy total % | 47.43 | 235.25 |
| Sharpe | 2.29 | 1.3 |
| Sortino | 6.57 | 0.56 |
| max drawdown % | 6.71 | 19.56 |
| profit factor | 2.85 | 1.84 |

**Retained out of sample: 117%**

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free. Cross-strategy comparisons in this repository use average profit per trade in percent.

Baseline: buy-and-hold on the same pairs returned **-59.05%**; the strategy returned **47.43%**.
Out of sample: buy-and-hold **346.34%** vs strategy **235.25%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | could not run | код 1 |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | индикаторы меняются от объёма истории: EWO -12.317% |
| прогрев объявлен | clean | 200 при потребности 200 |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **5m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `4a7c7414af9b` · strategy list `dac6309df791d209`*
