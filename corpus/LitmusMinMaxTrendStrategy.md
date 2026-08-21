# LitmusMinMaxTrendStrategy

Source: [`markdregan/FreqAI-Marcos-Lopez-De-Prado`](https://github.com/markdregan/FreqAI-Marcos-Lopez-De-Prado) · file `LitmusMinMaxTrendStrategy.py`

## Could not be measured

```
Impossible to load Strategy 'LitmusMinMaxTrendStrategy'. This class does not exist or contains Python code errors.
```

Declared timeframe: `none declared`. This is a named cause, not a verdict on the strategy — see the note on buckets in [../BASELINE.md](../BASELINE.md).

## Checks

| check | result | detail |
|---|---|---|
| look-ahead bias (freqtrade's own `lookahead-analysis`) | could not run | вывод не разобран |
| indicator recursion (freqtrade's own `recursive-analysis`) | clean | рекурсивных отклонений не найдено |
| мёртвые настройки трейлинга | **found** | trailing_stop=False, но trailing_stop_positive=0.02 задан — читается как работающая защита |
| признак утечки будущего | **found** | сдвиг в будущее .shift(-N) |

---

*Run by freqtrade itself. Fee 0.1% per side, 8 USDT pairs, timeframe **undetermined** (the strategy's own — never overridden by config). Author's window 2018-03-01…2020-03-01, out of sample 2020-03-01…2026-08-19. "Could not check" is never printed as "clean".*

*Code fingerprint `8d9b3a08743f` · strategy list `a039f448c17bed72`*
