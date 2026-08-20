# Nine questions to ask your own backtest

Every one of these is mechanical. None requires judgement, a guru, or a paid
course. Each is a question your own backtest can answer today, and each
corresponds to a defect actually found in public strategies audited here.

Commands assume freqtrade. The reasoning applies to any engine.

---

## 1. Is `startup_candle_count` declared, and is it big enough?

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

## 2. Does the engine's own bias detector clear you?

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

## 3. Is the result significant, or is it noise?

freqtrade prints `Mean profit p-value` in every backtest summary. Most people
scroll past it.

**A p-value above 0.05 means your average trade is statistically
indistinguishable from zero** — no matter how good the equity curve looks. One
of the strategies audited here shows p = 0.13 *in its own author's window*.

**Passing looks like:** p below 0.05, and a trade count large enough that the
test means something (a few dozen trades tells you almost nothing).

## 4. Did you beat buying and holding?

The same summary prints `Market change` — what the pairs themselves did over the
window. This is your baseline, and it is free.

A strategy returning +16% in a window where the market fell 58% is doing real
work. A strategy returning +50% where the market rose 400% is an expensive way
to underperform.

**Passing looks like:** you know both numbers and can say which one you beat.

## 5. Can every exit actually fire?

Read your entry and exit conditions side by side and ask whether each exit is
reachable from the state the entry creates.

Real example: an entry requiring `macd < 0` paired with an exit of
`crossed_below(macd, 0)` — which needs MACD to have been *above* zero on the
previous bar. That exit cannot fire until the opposite of the entry condition has
occurred first. The strategy has two exits on paper and one in practice.

**Passing looks like:** for each exit, a sentence describing a path from entry to
that exit.

## 6. Are your trailing-stop settings actually on?

```python
trailing_stop = False
trailing_stop_positive = 0.03   # inert — trailing is off
```

And the mirror image: `trailing_stop = True` with no `trailing_stop_positive`
means the stop trails at your **full** stoploss distance, not a few percent.

**Passing looks like:** the settings you read match the behaviour you get.

## 7. What happens when costs are 2× your assumption?

```bash
freqtrade backtesting --strategy YourStrategy --fee 0.001   # then 0.002
```

Fee is a proxy for total round-trip cost: exchange fee plus spread plus
slippage. Backtests fill at the candle open with none of the last two. On
illiquid pairs in volatile periods, doubling the assumed cost is not pessimism —
it is realism.

**Passing looks like:** your edge survives 2× cost. If it does not, you do not
have an edge, you have a fee arbitrage against your own optimism.

## 8. Does the result hold outside the window you developed in?

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

## 9. Can someone else reproduce your number?

If your headline is "Total profit %", it depends on `max_open_trades`,
`stake_amount` and `dry_run_wallet`. Without those published, the number is not
wrong — it is **undefined**. The same trade list under different settings gives
completely different totals.

**Passing looks like:** your config is in the repository, or your headline
metric is one that does not depend on it. Expectancy per trade does not.

---

## What this checklist cannot tell you

Whether your idea is any good. Every check above is about whether your
*measurement* is trustworthy. A perfectly measured strategy with no edge is
still a strategy with no edge — you will simply know it sooner and for less
money.

That is the whole value on offer here, and it is worth stating plainly rather
than dressed up.

---

*Want these nine run against your strategy? The harness in this repository does
it — `harness.py`. Or open an issue.*
