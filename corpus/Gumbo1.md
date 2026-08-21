# Gumbo1

Source: [`PeetCrypto/freqtrade-stuff`](https://github.com/PeetCrypto/freqtrade-stuff) · file `gumbo1.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 10024 | 13558 |
| expectancy per trade (USDT) | -0.1 | -0.07 |
| mean profit p-value | 3.633e-40 | 1.943e-16 |
| market change % (baseline) | -59.05 | 346.34 |
| strategy total % | -96.56 | -96.64 |
| Sharpe | -34.92 | -7.76 |
| Sortino | -28.27 | -5.37 |
| max drawdown % | 96.57 | 96.68 |
| profit factor | 0.48 | 0.59 |

**Retained out of sample: negative**

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free. Cross-strategy comparisons in this repository use average profit per trade in percent.

Baseline: buy-and-hold on the same pairs returned **-59.05%**; the strategy returned **-96.56%**.
Out of sample: buy-and-hold **346.34%** vs strategy **-96.64%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | could not run | вывод не разобран |
| indicator recursion (freqtrade's own `recursive-analysis`) | clean | рекурсивных отклонений не найдено |
| прогрев объявлен | clean | 200 при потребности 80 |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **5m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `4a7c7414af9b` · strategy list `dac6309df791d209`*
