# PowerTower

Source: [`freqtrade/freqtrade-strategies`](https://github.com/freqtrade/freqtrade-strategies) · file `PowerTower.py`

## Result

| metric | author's window | out of sample |
|---|---|---|
| trades | 1232 | 3769 |
| expectancy per trade (USDT) | -0.44 | 0.04 |
| mean profit p-value | 0.007949 | 0.815 |
| market change % (baseline) | -58.37 | 346.34 |
| strategy total % | -53.74 | 13.42 |
| Sharpe | -2.44 | 0.12 |
| Sortino | -1.57 | 0.07 |
| max drawdown % | 55.58 | 46.68 |
| profit factor | 0.62 | 1.02 |

**Retained out of sample: n/a**

> Expectancy above is in USDT and the backtests run with `stake_amount: "unlimited"`, which compounds — so it is **not** scale-free. Cross-strategy comparisons in this repository use average profit per trade in percent.

Baseline: buy-and-hold on the same pairs returned **-58.37%**; the strategy returned **-53.74%**.
Out of sample: buy-and-hold **346.34%** vs strategy **13.42%** — loses to it.

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | clean | смещения не обнаружено |
| indicator recursion (freqtrade's own `recursive-analysis`) | clean | рекурсивных отклонений не найдено |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **5m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `4a7c7414af9b` · strategy list `dac6309df791d209`*
