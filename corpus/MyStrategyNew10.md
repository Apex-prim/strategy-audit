# MyStrategyNew10

Source: [`PeetCrypto/freqtrade-stuff`](https://github.com/PeetCrypto/freqtrade-stuff) · file `MyStrategyNew10.py`

## Could not be measured

```
TypeError: attribute name must be string, not 'NoneType'
```

Declared timeframe: `none declared`. This is a named cause, not a verdict on the strategy — see the note on buckets in [../BASELINE.md](../BASELINE.md).

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | could not run | вывод не разобран |
| indicator recursion (freqtrade's own `recursive-analysis`) | **found** | индикаторы меняются от объёма истории: EMA_96_15m 0.017%, EMA_71_4h -0.012%, EMA_83_4h -0.017%, EMA_96_4h -0.019%, EMA_71_1d 0.084% |
| мёртвые настройки трейлинга | **found** | trailing_stop=False, но trailing_stop_positive=0.03 задан — читается как работающая защита |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **undetermined** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `590bf74986c5` · strategy list `a039f448c17bed72`*
