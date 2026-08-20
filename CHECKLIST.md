# Ten questions to ask your own backtest

Each corresponds to a defect actually found in the public strategies audited
here. None requires judgement, a guru, or a paid course.

**Five are a single command. Five are a careful read of your own code.** They
are marked, because claiming all ten are one-liners would be the same kind of
overstatement this repository exists to catch.

    ⌨  one command      1, 2, 3, 4, 7, 10
    👁  read your code   5, 6, 8, 9

Nine come from defects found in the public strategies audited here. **Number 10
comes from a defect found in this project's own pipeline** — which is exactly
why it is in the list.

Commands assume freqtrade. The reasoning applies to any engine.

---

## ⌨ 1. Is `startup_candle_count` declared, and is it big enough?

```bash
freqtrade recursive-analysis --strategy YourStrategy --timerange 20220101-20220401
```

If it prints *"invalid startup candle count of 0"* and refuses to run, your
strategy has told the engine it needs no warm-up. The engine then requests one
block of candles and discards none — so an indicator that needs 800 bars gets
used before it has converged. Backtests hide this completely: history is always
available there. Live runs are not so generous.

**Passing looks like:** a declared count at least as large as your longest
indicator period, and a table of indicators with near-zero variation.

*Found in 5 of the first 5 strategies audited.*

## ⌨ 2. Does the engine's own bias detector clear you?

```bash
freqtrade lookahead-analysis --strategy YourStrategy --timerange 20220101-20220401
```

Look-ahead bias is when a signal uses information that did not exist yet. It is
the single most common way a backtest becomes fiction, and freqtrade ships a
detector for it that almost nobody runs.

**Passing looks like:** `no bias detected`.

*Note: the first five strategies audited here all passed this. It is worth
saying when a check comes back clean — an audit that only ever reports problems
is not measuring, it is campaigning.*

## ⌨ 3. Is the result significant, or is it noise?

freqtrade prints `Mean profit p-value` in every backtest summary. Most people
scroll past it.

**A p-value above 0.05 means your average trade is statistically
indistinguishable from zero** — no matter how good the equity curve looks. One
of the strategies audited here shows p = 0.13 *in its own author's window*.

**Passing looks like:** p below 0.05, and a trade count large enough that the
test means something (a few dozen trades tells you almost nothing).

## ⌨ 4. Did you beat buying and holding?

The same summary prints `Market change` — what the pairs themselves did over the
window. This is your baseline, and it is free.

A strategy returning +16% in a window where the market fell 58% is doing real
work. A strategy returning +50% where the market rose 400% is an expensive way
to underperform.

**Passing looks like:** you know both numbers and can say which one you beat.

## 👁 5. Can every exit actually fire?

Read your entry and exit conditions side by side and ask whether each exit is
reachable from the state the entry creates.

Real example: an entry requiring `macd < 0` paired with an exit of
`crossed_below(macd, 0)` — which needs MACD to have been *above* zero on the
previous bar. That exit cannot fire until the opposite of the entry condition has
occurred first. The strategy has two exits on paper and one in practice.

**Passing looks like:** for each exit, a sentence describing a path from entry to
that exit.

## 👁 6. Are your trailing-stop settings actually on?

```python
trailing_stop = False
trailing_stop_positive = 0.03   # inert — trailing is off
```

And the mirror image: `trailing_stop = True` with no `trailing_stop_positive`
means the stop trails at your **full** stoploss distance, not a few percent.

**Passing looks like:** the settings you read match the behaviour you get.

## ⌨ 7. What happens when costs are 2× your assumption?

```bash
freqtrade backtesting --strategy YourStrategy --fee 0.001   # then 0.002
```

Fee is a proxy for total round-trip cost: exchange fee plus spread plus
slippage. Backtests fill at the candle open with none of the last two. On
illiquid pairs in volatile periods, doubling the assumed cost is not pessimism —
it is realism.

**Passing looks like:** your edge survives 2-3× your assumed cost. If it does
not, you do not have an edge — you have a fee arbitrage against your own
optimism.

Measured on the five strategies audited here, raising cost from 0.1% to 0.3%
per side turns **three of them negative inside their own author's window**:

```
                                0.1%     0.2%     0.3%  per side
EMAPriceCrossoverWithThreshold  1.63     1.26     0.93
RSIDirectionalWithTrendSlow     1.13     0.86     0.59
MACDCrossoverWithTrend          0.53     0.25    -0.01
DoubleEMACrossoverWithTrend     0.49     0.18    -0.08
RSIDirectionalWithTrend         0.42     0.16    -0.09
```

## 👁 8. Does the result hold outside the window you developed in?

Split your data. Develop on the first part; never look at the second until you
are done. Then run once.

Of the first five strategies audited here, all five degraded out of sample; two
retained under 10% of their per-trade edge, and one turned negative.

**Passing looks like:** an out-of-sample expectancy that is a meaningful
fraction of the in-sample one — and you decided what "meaningful" was before you
looked.

*This is an out-of-sample test, not a walk-forward analysis. Walk-forward means
rolling or anchored windows with re-fitting at each step. Calling one the other
is a terminology error worth avoiding — including by us: an earlier version of
this repository used the wrong word.*

## 👁 9. Can someone else reproduce your number?

If your headline is "Total profit %", it depends on `max_open_trades`,
`stake_amount` and `dry_run_wallet`. Without those published, the number is not
wrong — it is **undefined**. The same trade list under different settings gives
completely different totals.

**Passing looks like:** your config is in the repository, or your headline
metric is one that does not depend on it. Expectancy per trade does not.

## ⌨ 10. Did the engine run the timeframe you think it ran?

```bash
freqtrade backtesting --strategy YourStrategy ... 2>&1 | grep "Strategy using timeframe"
```

A `timeframe` key in your **config** silently overrides the one your strategy
declares in its own source. There is no warning. A 5-minute strategy will run on
hourly candles and return a complete, plausible result — thousands of trades, a
respectable equity curve, nothing amiss in the output.

This is not hypothetical: it happened here, to this pipeline, across a
corpus sweep, and was caught only by counting how many strategies declared which
timeframe. The published audits were unaffected because those strategies happen
to declare `1h`; everything else was invalid.

While you are reading that log, also check for:

```
WARNING - No history for DASH/USDT, spot, 1h found
```

The engine warns and **keeps going on the remaining pairs**. Your result is then
computed over fewer instruments than you think, and is not comparable to one that
was not.

**Passing looks like:** the timeframe in the engine's log matches the one in your
strategy file, and there are no missing-history warnings — or you know exactly
which pairs are missing and say so alongside the number.


---

## What this checklist cannot tell you

Whether your idea is any good. Every check above is about whether your
*measurement* is trustworthy. A perfectly measured strategy with no edge is
still a strategy with no edge — you will simply know it sooner and for less
money.

That is the whole value on offer here, and it is worth stating plainly rather
than dressed up.

---

*Want these ten run against your strategy?*

**📧 faxesuxan24@gmail.com** for a private audit, or open an issue to do it in
the open. The harness in this repository — `harness.py` — is the same pipeline,
so you can also just run it yourself and never talk to anyone.
