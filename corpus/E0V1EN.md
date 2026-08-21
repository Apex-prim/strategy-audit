# E0V1EN

Source: [`eovie/freqtrade_strs`](https://github.com/eovie/freqtrade_strs) · file `E0V1EN.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 71 | 438 |
| expectancy per trade (USDT) | 1.27 | 2.2 |
| mean profit p-value | 0.0006574 | 5.945e-12 |
| market change % (baseline) | -58.41 | 346.34 |
| strategy total % | 8.99 | 96.24 |
| Sharpe | 0.79 | 1.2 |
| Sortino | 0.83 | 0.83 |
| max drawdown % | 1.23 | 6.83 |
| profit factor | 3.06 | 2.76 |

**Retained out of sample: 173%**

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free. Cross-strategy comparisons in this repository use average profit per trade in percent.

Baseline: buy-and-hold on the same pairs returned **-58.41%**; the strategy returned **8.99%**.
Out of sample: buy-and-hold **346.34%** vs strategy **96.24%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | could not run | вывод не разобран |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | индикаторы меняются от объёма истории: rsi 12.447%, rsi_fast 0.045%, rsi_slow 12.811% |
| прогрев объявлен | clean | 20 при потребности 20 |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **5m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `4a7c7414af9b` · strategy list `dac6309df791d209`*
