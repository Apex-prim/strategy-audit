# NotAnotherSMAOffsetStrategy

Source: [`PeetCrypto/freqtrade-stuff`](https://github.com/PeetCrypto/freqtrade-stuff) · file `NotAnotherSMAOffsetStrategy.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 215 | 683 |
| expectancy per trade (USDT) | 0.94 | 2.04 |
| mean profit p-value | 5.228e-06 | 8.496e-15 |
| market change % (baseline) | -59.05 | 346.34 |
| strategy total % | 20.16 | 139.57 |
| Sharpe | 1.8 | 1.68 |
| Sortino | 2.06 | 1.1 |
| max drawdown % | 5.66 | 4.57 |
| profit factor | 2.22 | 2.73 |

**Retained out of sample: 217%**

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free. Cross-strategy comparisons in this repository use average profit per trade in percent.

Baseline: buy-and-hold on the same pairs returned **-59.05%**; the strategy returned **20.16%**.
Out of sample: buy-and-hold **346.34%** vs strategy **139.57%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | could not run | код 1 |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | индикаторы меняются от объёма истории: EWO -12.317% |
| прогрев объявлен | clean | 200 при потребности 100 |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **5m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `4a7c7414af9b` · strategy list `dac6309df791d209`*
