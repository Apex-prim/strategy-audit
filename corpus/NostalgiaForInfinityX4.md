# NostalgiaForInfinityX4

Source: [`iterativv/NostalgiaForInfinity`](https://github.com/iterativv/NostalgiaForInfinity) · file `NostalgiaForInfinityX4.py`

## Could not be measured

```
ПРЕВЫШЕНО ВРЕМЯ
```

Declared timeframe: `5m`. This is a named cause, not a verdict on the strategy — see the note on buckets in [../BASELINE.md](../BASELINE.md).

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | could not run | вывод не разобран |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | индикаторы меняются от объёма истории: r_480_1h 357.101%, r_480_4h 350.867%, ewo_50_200 -12.317% |
| прогрев не объявлен | **found** | самый длинный индикатор 288 свечей, startup_candle_count не задан (по умолчанию 0) |
| мёртвые настройки трейлинга | **found** | trailing_stop=False, но trailing_stop_positive=0.01 задан — читается как работающая защита |
| признак утечки будущего | **found** | центрированное окно center=True |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **5m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `590bf74986c5` · strategy list `a039f448c17bed72`*
