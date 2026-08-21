# RLStrategy

Source: [`Mohamed-sm/Freqtrade-RLStrategy-IA`](https://github.com/Mohamed-sm/Freqtrade-RLStrategy-IA) · file `RLStrategy.py`

## Could not be measured

```
freqAI is not enabled. Please enable it in your config to use this strategy.
```

Declared timeframe: `1h`. This is a named cause, not a verdict on the strategy — see the note on buckets in [../BASELINE.md](../BASELINE.md).

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | could not run | freqAI is not enabled. Please enable it in your config to use this strategy. |
| indicator recursion (freqtrade's own `recursive-analysis`) | could not run | freqAI is not enabled. Please enable it in your config to use this strategy. |
| прогрев не объявлен | **found** | самый длинный индикатор 20 свечей, startup_candle_count не задан (по умолчанию 0) |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **1h** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `8d9b3a08743f` · strategy list `d43e19f4fcbe76b6`*
