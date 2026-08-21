# ASDTSRockwellTrading

Source: [`PeetCrypto/freqtrade-stuff`](https://github.com/PeetCrypto/freqtrade-stuff) · file `ASDTSRockwellTrading.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 16298 | 13654 |
| expectancy per trade (USDT) | -0.06 | -0.07 |
| mean profit p-value | 1.36e-65 | 1.255e-42 |
| market change % (baseline) | -58.23 | 346.34 |
| strategy total % | -96.57 | -96.57 |
| Sharpe | -57.33 | -12.98 |
| Sortino | -91.15 | -17.96 |
| max drawdown % | 96.59 | 96.57 |
| profit factor | 0.61 | 0.6 |

**Retained out of sample: negative**

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free. Cross-strategy comparisons in this repository use average profit per trade in percent.

Baseline: buy-and-hold on the same pairs returned **-58.23%**; the strategy returned **-96.57%**.
Out of sample: buy-and-hold **346.34%** vs strategy **-96.57%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | could not run | вывод не разобран |
| indicator recursion (freqtrade's own `recursive-analysis`) | clean | рекурсивных отклонений не найдено |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **5m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `4a7c7414af9b` · strategy list `dac6309df791d209`*
