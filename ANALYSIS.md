# Five strategies from a "strategies that work" repository. Out of sample, none is significant and one turns negative

There is a public repository,
[`paulcpk/freqtrade-strategies-that-work`](https://github.com/paulcpk/freqtrade-strategies-that-work)
— 327 stars, five freqtrade strategies, and a results table in the README:

| Strategy | Buy count | AVG profit % | Total profit % |
|---|---|---|---|
| EMAPriceCrossoverWithThreshold | 272 | 1.31 | 118.53 |
| DoubleEMACrossoverWithTrend | 655 | 0.56 | 122.50 |
| MACDCrossoverWithTrend | 300 | 0.49 | 49.42 |
| RSIDirectionalWithTrendSlow | 108 | 0.91 | 32.75 |
| RSIDirectionalWithTrend | 181 | 0.27 | 16.16 |

Window: 1h, 2018-03-01 … 2020-03-01, eight USDT pairs.

I downloaded the same eight pairs from Binance's public archives and ran the
authors' own `.py` files **through freqtrade itself** — same engine, same
execution semantics, no interpretation on my part.

> **This document was rewritten on 2026-08-21.** Its first version measured the
> strategies with a pandas re-implementation and reported per-trade results in
> USDT. Both were wrong choices and both have been replaced: a re-implementation
> invites the fair reply *"you rewrote my logic wrong"*, and a currency figure is
> not scale-free under `stake_amount: "unlimited"`, which compounds. Every number
> below now comes from the engine, in percent per trade. The old headline —
> *"15% of the edge survives"* — was an artifact of the discarded metric and is
> withdrawn rather than quietly edited.

**The author labels the repository experimental and educational, publishes
everything, and hides nothing. This is not about him. It is about what a reader
takes from a results table.**

---

## 1. First, audit the auditor

Before saying anything about someone else's numbers, the measurement has to
reproduce theirs. Same window, 0.1% fee per side, run by freqtrade:

```
                                  claimed        measured       difference
MACDCrossoverWithTrend            300 / 0.49%    303 / 0.42%     +1% / -14%
RSIDirectionalWithTrend           181 / 0.27%    167 / 0.34%     -8% / +26%
RSIDirectionalWithTrendSlow       108 / 0.91%    132 / 1.03%    +22% / +13%
EMAPriceCrossoverWithThreshold    272 / 1.31%    368 / 1.39%    +35% / +6%
DoubleEMACrossoverWithTrend       655 / 0.56%    861 / 0.38%    +31% / -32%
```

`MACDCrossoverWithTrend` lands at 303 trades against a claimed 300. The
remaining gaps have an obvious cause: `max_open_trades` is not published, so the
engine here takes signals the author's run could not have taken.

**And this is where I got it wrong, which is worth telling.** When this audit
still used a re-implementation, my first run gave `RSIDirectionalWithTrendSlow`
18 trades against the author's 108, and a loss instead of a profit. I could have
published that as "does not reproduce" — an 8× gap is persuasive. Instead I went
to find out why. I had assumed RSI thresholds of 15/85 by analogy with the
neighbouring strategy. The file actually says:

```python
(qtpylib.crossed_above(dataframe['rsi_slow'], 25))   # entry, not 15
(qtpylib.crossed_below(dataframe['rsi_slow'], 20))   # exit, not 85
```

The bug was mine. The rule is simple: **an anomaly you cannot explain is not a
finding — it is something to go and check.** More often than not it is yours.
That episode is also the reason the re-implementation is gone: the engine cannot
misread the author's thresholds, and I can.

## 2. The headline number is undefined

The repository contains **seven files**: five strategies, README, LICENSE,
.gitignore. Configuration files: **zero**.

`minimal_roi` is commented out in all five, with a note saying it "will be
overridden if the config file contains minimal_roi". There is no config file.

So **"Total profit %" is undefined.** It depends on `max_open_trades`,
`stake_amount`, `dry_run_wallet` and `fee` — none of which are published. The
same list of trades with `max_open_trades: 1` and with `max_open_trades: 8`
produces entirely different totals. This is not a wrong number. It is **not a
number**.

The same trap caught this repository, one level down. An early version reported
freqtrade's `Expectancy` in USDT and called it configuration-independent. Under
`stake_amount: "unlimited"` freqtrade divides the wallet across open slots and
compounds, so a currency expectancy grows with the account rather than with the
edge. The scale-free quantity is **average profit per trade in percent**, and
correcting it moved one strategy's retained edge from 5% to 26%.

## 3. A specific line: the indicator is longer than the warm-up window

`EMAPriceCrossoverWithThreshold.py:44`

```python
dataframe['ema800'] = ta.EMA(dataframe, timeperiod=800)
```

800 hourly candles is 33 days of history. Yet `startup_candle_count` is declared
in **none of the five files**, and its default is zero
(`freqtrade/strategy/interface.py:128`).

That number is how a strategy tells the engine how much warm-up it needs. The
engine uses it for two things (`freqtrade/exchange/exchange.py:358-361`):
deciding **how much data to request**, and **how many leading candles to discard
as unreliable**.

Declaring zero switches off both at once. One block of data is requested;
nothing is discarded. A freshly seeded, not-yet-converged EMA800 is treated as
fit to trade on. And freqtrade's own warning cannot fire: the engine has no way
to know the strategy needs 800 candles when the strategy says it needs none.

In a backtest this is invisible — there is always enough history. This is the
strategy with the **best reported result** in the table.

It is also why `recursive-analysis` returns a finding on all five: the engine
refuses to run the check at all, saying a startup count of 0 *"will lead to
recursive problems for some indicators"*. That is a finding about a
**declaration**, not a measurement of drift — a distinction this repository now
records per strategy rather than folding both into one label.

## 4. Settings that look active and are not

`DoubleEMACrossoverWithTrend.py:39-41` and `MACDCrossoverWithTrend.py:39-41`:

```python
trailing_stop = False
trailing_stop_positive = 0.03
trailing_stop_positive_offset = 0.04
```

The last two are **dead** — trailing is off. A reader sees a tidy 3% and 4% and
concludes profit protection is configured.

The mirror image: in the three strategies where `trailing_stop = True`, neither
`positive` nor `offset` is set at all. freqtrade then trails at the **full**
stoploss distance — that is, −10%, −15% and −20% from the trade's high-water
mark. That is not "a 3% trailing stop"; it is a different mechanism entirely.

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

Entry **requires** `macd < 0`. The first exit requires MACD to have been
**above** zero on the previous bar. So MACD must first climb above zero before
that exit can fire at all — the exit written first in the code is unreachable
until the condition opposite to the entry has occurred.

What remains is the second: `low < ema100`. And that is the **negation of the
entry filter**, evaluated on the candle's **low** — its noisiest point. One level
serves as both the gate to enter and the trigger to leave, and on hourly candles
price pierces a 100-EMA constantly.

The measured consequence: a win rate of **22.1–24.7%** in three of the five, and
**14.9%** in the best-performing one. For trend following that is normal. It is
not what a reader of "strategies that work" expects.

## 6. Economics: every 0.1% of fee costs about 0.20 pp of the average trade

```
avg trade %, fee per side:      0.1%     0.2%     0.3%
EMAPriceCrossoverWithThreshold  1.39     1.19     0.99
RSIDirectionalWithTrendSlow     1.03     0.82     0.62
MACDCrossoverWithTrend          0.42     0.21     0.01   <- zero
DoubleEMACrossoverWithTrend     0.38     0.18    -0.02   <- negative
RSIDirectionalWithTrend         0.34     0.14    -0.06   <- negative
```

The author's table does not state which fee was used. Between "0.1%" and "0.3%
per side" lies the whole distance between a working strategy and zero, and 0.3%
is not pessimism for 2018-era altcoins — XLM, DASH, XMR and ADA routinely showed
hourly spreads of 0.3–0.5%, which a backtest filling at the candle open does not
charge you.

**Three of the five have nothing left inside their own author's window** once
execution is priced that way: two negative, one at +0.01% per trade, which is
zero wearing a plus sign.

## 7. The main result: out of sample

Same files, same eight pairs, 0.1% fee per side. The window the author never
saw: **2020-03-01 … 2026-08-20 — six and a half years, more than three times
longer than the original.**

```
                                in-sample    p        out-of-sample   p        retained
EMAPriceCrossoverWithThreshold    +1.39%   0.113        +0.65%      0.161        47%
DoubleEMACrossoverWithTrend       +0.38%   0.049        +0.19%      0.290        50%
RSIDirectionalWithTrendSlow       +1.03%   0.381        +0.27%      0.924        26%
MACDCrossoverWithTrend            +0.42%   0.128        +0.05%      0.883        12%
RSIDirectionalWithTrend           +0.34%   0.238        -0.07%      0.556     negative
```

**All five degrade. Without exception.** But the more important column is the
one next to the returns.

**Four of the five were never statistically significant in their author's own
window, and none of the five is significant out of sample.** Only
`DoubleEMACrossoverWithTrend` clears p < 0.05 in-sample, and only just, at 0.049.
The strongest performer of the set — `EMAPriceCrossoverWithThreshold`, 1.39% per
trade — sits at p = 0.113: its average trade cannot be told apart from zero in
the window it was developed in.

For most of these strategies the out-of-sample collapse is almost beside the
point. The in-sample result was never established in the first place.

**MACDCrossoverWithTrend earns +0.05% per trade over 1,288 trades.** That is
zero, and it is already net of the assumed fee. Any slippage puts it underwater.

**RSIDirectionalWithTrend changes sign:** +0.34% in the author's window, −0.07%
outside it.

And the baseline nobody prints: over the out-of-sample window the eight pairs
themselves returned **+348.7%**. The best of the five returned +146.8% in total.
Every one of them underperformed doing nothing.

## 8. What I did *not* find

**There is no look-ahead bias.** freqtrade's own `lookahead-analysis` clears all
five, and reading the code agrees: every indicator is causal (TA-Lib EMA, RSI,
MACD), `qtpylib.crossed_above/below` compares the current bar with the previous
one, and freqtrade fills a signal at the **next** candle's open.

**Trades are not intra-candle artifacts either.** Average holding time runs from
14 candles to 104, so none of these results depends on the engine guessing
whether a candle's high or its low came first.

Saying so matters. An audit that only ever reports problems is not measuring, it
is campaigning.

## 9. Caveats on my own run

- `minimal_roi` is not applied, because it is commented out in the published
  files. If the author's config carried one, the numbers move.
- Fee is a proxy for total round-trip cost. freqtrade fills at the candle open
  with no spread and no slippage, so **every figure above is optimistic**, which
  is what section 6 exists to bound.
- Trade counts differ from the author's because `max_open_trades` is not
  published. That is a property of the repository, not of the measurement.
- **"Eight pairs" is the request list, not what traded throughout.** Three of the
  eight span the author's window; DASH was not listed on Binance until it was
  more than half over, and XMR was delisted on 2024-02-20. The engine correctly
  does not trade an unlisted pair, but a reader who sees "8 pairs" will assume
  eight throughout.

---

## Conclusion

Five strategies, published openly, with no sign of bad faith anywhere. And yet:

- the reported totals are **undefined** without an unpublished config;
- the best-performing strategy uses an indicator longer than a warm-up window
  declared as zero;
- in two files the trailing-stop settings are dead, in three they behave nothing
  like they read;
- one of two exits cannot fire until the opposite of the entry condition occurs;
- four of five are **not statistically significant in their own author's
  window**, and none is out of sample;
- and every one of them underperformed simply holding the same coins.

This is what an **ordinary** public backtest looks like. Not a fraudulent one —
an ordinary one. The distance between "works" and "worked in this window" is six
and a half years of data and one evening of work.

And there is a second distance, worth more: between an audit that found an error
and an audit that found **its own** errors and said so. This document has now
recorded three of them — a misread RSI threshold, a metric that was not
scale-free, and a headline built on the wrong one. The second kind of audit can
be checked. The first cannot.

*The pipeline that produced every number here is in this repository:
`harness.py` to measure, `ledger.py` to account for it. If you want your own
strategy put through the same process, get in touch.*
