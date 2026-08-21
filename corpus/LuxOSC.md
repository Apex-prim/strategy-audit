# LuxOSC

Source: [`PeetCrypto/freqtrade-stuff`](https://github.com/PeetCrypto/freqtrade-stuff) · file `LuxOSC.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 3207 | 11370 |
| expectancy per trade (USDT) | -0.23 | -0.08 |
| mean profit p-value | 4.531e-07 | 0.05759 |
| market change % (baseline) | -58.37 | 346.34 |
| strategy total % | -72.27 | -90.44 |
| Sharpe | -7.49 | -1.64 |
| Sortino | -6.56 | -1.32 |
| max drawdown % | 76.24 | 95.91 |
| profit factor | 0.73 | 0.92 |

**Retained out of sample: negative**

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free. Cross-strategy comparisons in this repository use average profit per trade in percent.

Baseline: buy-and-hold on the same pairs returned **-58.37%**; the strategy returned **-72.27%**.
Out of sample: buy-and-hold **346.34%** vs strategy **-90.44%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | could not run | вывод не разобран |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | индикаторы меняются от объёма истории: osc 16.276%, signal 19.689%, supertrend -0.118% |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **5m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `4a7c7414af9b` · strategy list `dac6309df791d209`*
