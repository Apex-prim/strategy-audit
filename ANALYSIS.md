# Five strategies from a "strategies that work" repository. Out of sample, 15% of the edge survives

There is a public repository, [`paulcpk/freqtrade-strategies-that-work`](https://github.com/paulcpk/freqtrade-strategies-that-work) — 327 stars, five freqtrade strategies, and a results table in the README:

| Strategy | Buy count | AVG profit % | Total profit % |
|---|---|---|---|
| EMAPriceCrossoverWithThreshold | 272 | 1.31 | 118.53 |
| DoubleEMACrossoverWithTrend | 655 | 0.56 | 122.50 |
| MACDCrossoverWithTrend | 300 | 0.49 | 49.42 |
| RSIDirectionalWithTrendSlow | 108 | 0.91 | 32.75 |
| RSIDirectionalWithTrend | 181 | 0.27 | 16.16 |

Window: 1h, 2018-03-01 … 2020-03-01, eight USDT pairs.

I downloaded the same eight pairs from Binance — 74,179 hourly candles each — re-implemented all five strategies independently in pandas under freqtrade's execution model (a signal on candle `i` fills at the open of candle `i+1`), and ran them.

**The author labels the repository experimental and educational, publishes everything, and hides nothing. This is not about him. It is about what a reader takes from a results table.**

---

## 1. First, audit the auditor

Before saying anything about someone else's numbers, I have to show that my implementation reproduces the published ones. Same window, 0.1% fee per side:

```
                                  claimed        replicated     difference
DoubleEMACrossoverWithTrend       655 / 0.56%    961 / 0.38%    +47% / -33%
MACDCrossoverWithTrend            300 / 0.49%    334 / 0.36%    +11% / -27%
RSIDirectionalWithTrend           181 / 0.27%    187 / 0.35%     +3% / +29%
RSIDirectionalWithTrendSlow       108 / 0.91%    141 / 1.01%    +31% / +11%
EMAPriceCrossoverWithThreshold    272 / 1.31%    392 / 1.17%    +44% / -11%
```

All five land within an order of magnitude. The systematic excess in trade count has an obvious cause: I take every signal, while the author ran with some `max_open_trades` that is not published.

**And this is where I got it wrong, which is worth telling.** My first run gave `RSIDirectionalWithTrendSlow` 18 trades against the author's 108, and a loss instead of a profit. I could have published that as "does not reproduce" — an 8× gap is persuasive. Instead I went to find out why. I had assumed RSI thresholds of 15/85 by analogy with the neighbouring strategy. The file actually says:

```python
(qtpylib.crossed_above(dataframe['rsi_slow'], 25))   # entry, not 15
(qtpylib.crossed_below(dataframe['rsi_slow'], 20))   # exit, not 85
```

The bug was mine. After the fix, that strategy reproduces better than the others. The rule is simple: **an anomaly you cannot explain is not a finding — it is something to go and check.** More often than not it is yours.

## 2. The headline number is undefined

The repository contains **seven files**: five strategies, README, LICENSE, .gitignore. Configuration files: **zero**.

`minimal_roi` is commented out in all five, with a note saying it "will be overridden if the config file contains minimal_roi". There is no config file.

So **"Total profit %" is undefined.** It depends on `max_open_trades`, `stake_amount`, `dry_run_wallet` and `fee` — none of which are published. The same list of trades with `max_open_trades: 1` and with `max_open_trades: 8` produces entirely different totals. This is not a wrong number. It is **not a number**.

## 3. A specific line: the indicator is longer than the warm-up window

`EMAPriceCrossoverWithThreshold.py:44`

```python
dataframe['ema800'] = ta.EMA(dataframe, timeperiod=800)
```

800 hourly candles is 33 days of history. Yet `startup_candle_count` is declared in **none of the five files**, and its default is zero (`freqtrade/strategy/interface.py:128`).

That number is how a strategy tells the engine how much warm-up it needs. The engine uses it for two things (`freqtrade/exchange/exchange.py:358-361`): deciding **how much data to request**, and **how many leading candles to discard as unreliable**.

Declaring zero switches off both at once. One block of data is requested; nothing is discarded. A freshly seeded, not-yet-converged EMA800 is treated as fit to trade on. And freqtrade's own warning cannot fire: the engine has no way to know the strategy needs 800 candles when the strategy says it needs none.

In a backtest this is invisible — there is always enough history. This is the strategy with the **best reported result** in the table.

## 4. Settings that look active and are not

`DoubleEMACrossoverWithTrend.py:39-41` and `MACDCrossoverWithTrend.py:39-41`:

```python
trailing_stop = False
trailing_stop_positive = 0.03
trailing_stop_positive_offset = 0.04
```

The last two are **dead** — trailing is off. A reader sees a tidy 3% and 4% and concludes profit protection is configured.

The mirror image: in the three strategies where `trailing_stop = True`, neither `positive` nor `offset` is set at all. freqtrade then trails at the **full** stoploss distance — that is, −10%, −15% and −20% from the trade's high-water mark. That is not "a 3% trailing stop"; it is a different mechanism entirely.

## 5. Filter interaction: one of the two exits is unreachable

`MACDCrossoverWithTrend.py`, entry:

```python
(dataframe['macd'] < 0) &                                   # MACD BELOW zero
(qtpylib.crossed_above(dataframe['macd'], dataframe['macdsignal'])) &
(dataframe['low'] > dataframe['ema100'])                    # candle ABOVE EMA100
```

exit:

```python
(qtpylib.crossed_below(dataframe['macd'], 0)) |             # MACD crosses zero DOWN
(dataframe['low'] < dataframe['ema100'])
```

Entry **requires** `macd < 0`. The first exit requires MACD to have been **above** zero on the previous bar. So MACD must first climb above zero before that exit can fire at all — the exit written first in the code is unreachable until the condition opposite to the entry has occurred.

What remains is the second: `low < ema100`. And that is the **negation of the entry filter**, evaluated on the candle's **low** — its noisiest point. One level serves as both the gate to enter and the trigger to leave, and on hourly candles price pierces a 100-EMA constantly.

The measured consequence: a win rate of **22.8–27.5%** in three of the five. For trend following that is normal. It is not what a reader of "strategies that work" expects.

## 6. Economics: every 0.1% of fee costs 0.20 pp of the average trade

```
fee per side:                  0.0%      0.1%      0.2%
DoubleEMACrossoverWithTrend   +0.58%    +0.38%    +0.18%
MACDCrossoverWithTrend        +0.56%    +0.36%    +0.16%
RSIDirectionalWithTrend       +0.55%    +0.35%    +0.15%
```

The author's table does not state which fee was used. Between "0.1%" and "0.2% per side" lies the whole distance between a working strategy and zero. For 2018-era altcoins (XLM, DASH, XMR, ADA) spread plus slippage on hourly bars is squarely the third column.

## 7. The main result: out of sample

Same code, same eight pairs, 0.1% fee per side. The window the author never saw: **2020-03-01 … 2026-08-20 — six and a half years, four times longer than the original.**

```
                                in-sample     out-of-sample   trades    survives
DoubleEMACrossoverWithTrend       +0.38%         +0.11%        4043        29%
MACDCrossoverWithTrend            +0.36%         +0.01%        1436         3%
RSIDirectionalWithTrend           +0.35%         -0.08%         757      negative
RSIDirectionalWithTrendSlow       +1.01%         +0.19%         545        19%
EMAPriceCrossoverWithThreshold    +1.17%         +0.51%        1812        44%
```

**All five degrade. Without exception.** On average about 15% of the per-trade edge survives.

**MACDCrossoverWithTrend earns +0.01% per trade over 1,436 trades.** That is zero. Not "small" — zero, and that is already net of fees. Any slippage puts it underwater.

**RSIDirectionalWithTrend changes sign:** +0.35% in the author's window, −0.08% outside it.

The best survivor is EMAPriceCrossoverWithThreshold, and it still loses more than half — at a 14.7% win rate. That is functioning trend following, but with a risk profile nothing like what the table suggests.

## 8. What I did *not* find

**There is no look-ahead bias.** I looked for it specifically. Every indicator is causal (TA-Lib EMA, RSI, MACD), `qtpylib.crossed_above/below` compares the current bar with the previous one, and freqtrade fills a signal at the **next** candle's open. No future leakage exists in these five files.

Writing otherwise would be precisely the failure this whole exercise is about.

## 9. Caveats on my own run

- This is an **independent re-implementation** in pandas, not freqtrade. The systematic excess in trade count (+3%…+47%) is best explained by the unpublished `max_open_trades`: I take every signal; the author could not have.
- I did not apply `minimal_roi`, because it is commented out in the published files. If the author's config carried one, the numbers move.
- Fee 0.1% per side, zero slippage. Which means every figure above is **optimistic**, not conservative.

---

## Conclusion

Five strategies, published openly, with no sign of bad faith anywhere. And yet:

- the reported totals are **undefined** without an unpublished config;
- the best-performing strategy uses an indicator longer than a warm-up window declared as zero;
- in two files the trailing-stop settings are dead, in three they behave nothing like they read;
- one of two exits cannot fire until the opposite of the entry condition occurs;
- and out of sample, all five degrade — two of them to zero or below.

This is what an **ordinary** public backtest looks like. Not a fraudulent one — an ordinary one. The distance between "works" and "worked in this window" is six and a half years of data and one evening of work.

And there is a second distance, worth more: between an audit that found an error and an audit that found **its own** error and said so. The second one can be checked. The first cannot.

*Replication code and data-fetch script are in this repository. If you want your own strategy put through the same process, get in touch.*
