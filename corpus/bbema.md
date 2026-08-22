# bbema

Source: [`davidzr/freqtrade-strategies`](https://github.com/davidzr/freqtrade-strategies) · file `bbema.py`

## Could not be measured

```
Timeframe needs to be set in either configuration or as cli argument `--timeframe 5m`
```

Declared timeframe: `none declared`. This is a named cause, not a verdict on the strategy — see the note on buckets in [../BASELINE.md](../BASELINE.md).

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | could not run | Timeframe needs to be set in either configuration or as cli argument `--timeframe 5m` |
| indicator recursion (freqtrade's own `recursive-analysis`) | could not run | Timeframe needs to be set in either configuration or as cli argument `--timeframe 5m` |
| прогрев не объявлен | **found** | самый длинный индикатор 50 свечей, startup_candle_count не задан (по умолчанию 0) |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **undetermined** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `590bf74986c5` · strategy list `a039f448c17bed72`*
