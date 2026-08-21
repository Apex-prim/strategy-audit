# E0V1E

Source: [`eovie/freqtrade_strs`](https://github.com/eovie/freqtrade_strs) · file `E0V1E.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 73 | 557 |
| expectancy per trade (USDT) | 0.99 | 1.24 |
| mean profit p-value | 0.07457 | 6.021e-05 |
| market change % (baseline) | -58.41 | 346.34 |
| strategy total % | 7.21 | 68.93 |
| Sharpe | 0.41 | 0.77 |
| Sortino | 0.22 | 0.44 |
| max drawdown % | 3.14 | 15.38 |
| profit factor | 2.33 | 1.89 |

**Retained out of sample: 125%**

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free. Cross-strategy comparisons in this repository use average profit per trade in percent.

⚠ **Not statistically significant in its author's own window** (p = 0.07457 > 0.05): the average trade is not distinguishable from zero.

Baseline: buy-and-hold on the same pairs returned **-58.41%**; the strategy returned **7.21%**.
Out of sample: buy-and-hold **346.34%** vs strategy **68.93%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | could not run | вывод не разобран |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | индикаторы меняются от объёма истории: rsi 12.447%, rsi_fast 0.045%, rsi_slow 12.811% |
| прогрев объявлен | clean | 20 при потребности 20 |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **5m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `4a7c7414af9b` · strategy list `dac6309df791d209`*
