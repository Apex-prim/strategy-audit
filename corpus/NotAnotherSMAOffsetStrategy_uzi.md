# NotAnotherSMAOffsetStrategy_uzi

Source: [`PeetCrypto/freqtrade-stuff`](https://github.com/PeetCrypto/freqtrade-stuff) · file `NotAnotherSMAOffsetStrategy_uzi.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 122 | 529 |
| expectancy per trade (USDT) | 0.71 | 0.61 |
| mean profit p-value | 0.02892 | 0.002739 |
| market change % (baseline) | -59.05 | 346.34 |
| strategy total % | 8.61 | 32.47 |
| Sharpe | 0.64 | 0.56 |
| Sortino | 0.59 | 0.65 |
| max drawdown % | 1.77 | 10.59 |
| profit factor | 1.7 | 1.38 |

**Retained out of sample: 86%**

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free. Cross-strategy comparisons in this repository use average profit per trade in percent.

Baseline: buy-and-hold on the same pairs returned **-59.05%**; the strategy returned **8.61%**.
Out of sample: buy-and-hold **346.34%** vs strategy **32.47%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | could not run | вывод не разобран |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | индикаторы меняются от объёма истории: EWO -12.317% |
| прогрев объявлен | clean | 200 при потребности 100 |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **5m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `4a7c7414af9b` · strategy list `dac6309df791d209`*
