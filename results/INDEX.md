# Указатель разборов

Мера — **ожидание на сделку**, а не итоговый процент: итог зависит от `max_open_trades` и размера ставки, то есть от конфигурации, а не от стратегии.

| стратегия | источник | ТФ | в выборке | вне выборки | осталось | утечка | рекурсия |
|---|---|---|---|---|---|---|---|
| [DoubleEMACrossoverWithTrend](DoubleEMACrossoverWithTrend.md) | `paulcpk` | 1h | 0.49 | 0.22 | **45%** | ✅ | ⚠ |
| [EMAPriceCrossoverWithThreshold](EMAPriceCrossoverWithThreshold.md) | `paulcpk` | 1h | 1.63 | 0.9 | **55%** | ✅ | ⚠ |
| [MACDCrossoverWithTrend](MACDCrossoverWithTrend.md) | `paulcpk` | 1h | 0.53 | 0.03 | **6%** | ✅ | ⚠ |
| [RSIDirectionalWithTrend](RSIDirectionalWithTrend.md) | `paulcpk` | 1h | 0.42 | -0.09 | **отрицательное** | ✅ | ⚠ |
| [RSIDirectionalWithTrendSlow](RSIDirectionalWithTrendSlow.md) | `paulcpk` | 1h | 1.13 | 0.06 | **5%** | ✅ | ⚠ |

✅ проверка пройдена · ⚠ найден дефект · · проверить не удалось
