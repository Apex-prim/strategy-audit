# TestStrategyLegacyV1

Source: [`markdregan/FreqAI-Marcos-Lopez-De-Prado`](https://github.com/markdregan/FreqAI-Marcos-Lopez-De-Prado) · file `legacy_strategy_v1.py`

## Could not be measured

```
Strategy Interface v1 is no longer supported. Please update your strategy to implement `populate_indicators`, `populate_entry_trend` and
```

Declared timeframe: `5m`. This is a named cause, not a verdict on the strategy — see the note on buckets in [../BASELINE.md](../BASELINE.md).

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | could not run | Strategy Interface v1 is no longer supported. Please update your strategy to implement `populate_indicators`, `populate_entry_trend` and  |
| indicator recursion (freqtrade's own `recursive-analysis`) | could not run | Strategy Interface v1 is no longer supported. Please update your strategy to implement `populate_indicators`, `populate_entry_trend` and  |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **5m** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `590bf74986c5` · strategy list `a039f448c17bed72`*
