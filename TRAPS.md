# Backtesting traps: a static screen that disqualifies one strategy in 895

When this audit was posted to the freqtrade Discord, `froggleston` said the bias
checks are not the only thing that flags a gamed strategy. He was right, and I
asked what else. The community answered with a link to their own document:

**<https://brookmiles.github.io/freqtrade-stuff/2021/04/12/backtesting-traps/>**

It describes six ways a backtest flatters a strategy. Four are checkable by
reading the code, and `traps.py` now checks them. **Nothing in this file is my
own idea** — including the 0.1–0.5% spread threshold, which is theirs.

## What a backtesting trap is — the community's definition, not mine

`Hippocritical`, freqtrade Discord, 2026-08-22:

> *"A backtesting trap is where you have a different result from backtest to dry
> run. Backtesting works on candles, where dry / live runs work on ticker data
> (which is not available, only max resolution of 1 minute via
> timeframe-detail)."*

**Divergence between backtest and live is the whole definition.** Applying it to
my own four checks disqualifies two of them:

| check | backtest vs live | verdict |
|---|---|---|
| trailing tighter than the spread | backtest fills inside the spread, live does not | **trap** |
| tight ROI on a long timeframe | the target is granted from the candle's range, not its path | **trap** |
| inert trailing setting | trailing is off in *both* — the engine does what the config says | not a trap |
| stoploss is not a stop | −0.99 behaves identically in both | not a trap |

The last two are real defects — one misleads the reader, the other is a risk
decision most people would not make knowingly — but they do not make a backtest
disagree with live, so they are recorded as notes and disqualify nobody.

I had already written that this question was *"the community's call, not mine"*.
It was answered, so it is applied rather than debated.

**Checked before it was applied.** Eight strategies were held at the traps gate
by those two flags alone. Carried forward through the remaining gates on their
own recorded numbers, **all eight fail G12** — none beats buy-and-hold on its
own pairs. The published endpoint does not move.

*(My first attempt at that check counted the eight as surviving everything
downstream, because it treated "never evaluated" as "passed" — the same defect
this audit had already fixed once, in `G9_candle`. It was caught by a
plausibility guard that refused a ladder starting at zero.)*

## What the corpus looks like after that

```
strategies checked                              895
of which pass every statistical gate             72      flagged  8
of which also clear both bias detectors          15      flagged  1

trailing tighter than the spread                 38
tight ROI on a long timeframe                     4
flagged                                          42 of 895   (5%)

DISQUALIFIED BY THIS LAYER                        1 of 895
   SMAIP3v2 — trailing tighter than the spread

notes, not disqualifications
   stoploss is not a stop                       263
   inert trailing setting                       177
   loose trailing (no trailing_stop_positive)    23
```

Before this correction the layer flagged 371 strategies (41%) and read as a
substantial filter. It is not one. **Stating it plainly: this layer costs one
strategy out of 895, and the previous 41% was mostly counting things that are
not backtesting traps.**

## What this screen is not

It reads declared configuration constants out of the source. That places a hard
ceiling on it, and two members of the community named the ceiling directly.

`froggleston`: *"any callback can add a backtesting trap — it can be very
subtle."* Correct, and fatal to any claim of completeness: a trap constructed
inside `custom_exit`, `confirm_trade_entry` or a custom stoploss is invisible to
a reader of constants. Nothing here counts those.

`Hippocritical`: *"it's simply impossible to catch all that — since the facts
there in traps, for example, are floating."* Also correct. The thresholds are
practitioner judgement, not physics, and a static screen cannot enumerate a set
whose members are invented per strategy.

**So this is a necessary condition on declared configuration, not a detector.**
Passing it means four specific documented mistakes are absent from the constants.
It means nothing about the callbacks, and it is not evidence of soundness.

## It is a different subject from lookahead-analysis

`Hippocritical` explained what `lookahead-analysis` actually does, and it is
worth stating because I had compared the two as though they were rivals:

> *"It does a full backtest and then n cut-off backtests with the same start but
> cut off where the trade would buy. If the trade buys at a different time, then
> something looked into the future. It doesn't look into the strategy at all, it
> just checks its behaviour."*

That is a **black-box behavioural test**. This file is a **white-box reading of
constants**. They have different subjects, so low overlap between them is the
expected result, not a shortfall in either. Measuring one against the other, as
an earlier version of [CORRECTIONS.md](CORRECTIONS.md) did, was a category
error — mine.

---

> **One flag was removed on 2026-08-22, and the removal was checked before it
> was made.** `trailing_stop = True` with no `trailing_stop_positive` was
> counted as a trap on the grounds that the stop then trails at the full
> stoploss distance. `Hippocritical`, in the freqtrade Discord: *"if you have
> loose trailing you wont have a trap; if you have things like 0.1% trailing
> then not."*
>
> He is right. A wide trailing stop is executable — it sits far from the spread
> and fills reliably. What makes a trailing stop a trap is **tightness**, not
> trailing. The check now records it as a note rather than a disqualification.
>
> Before changing it: of the nine strategies disqualified at the traps gate,
> **zero** were disqualified by that flag alone. The ladder is byte-identical
> after the change — 15 → 6 → 5 → 0. A rule can be corrected on its merits when
> no verdict depends on it, and that is checked rather than asserted.
>
> **And a second correction from the same conversation.** *"if you have 1%
> trailing and do 10x leverage then it essentially becomes 0.1% trailing."*
> True, and it is in the engine: `backtesting.py` computes the trailing distance
> as `trailing_stop_positive / leverage`. The check now compares the
> **effective** distance against the spread. One strategy changes hands — `WTX3`,
> 1% at 10× = 0.001 — and it never produced numbers, so again no verdict moves.
>
> ⚠ Leverage detection here reads only a literal `return <number>` inside
> `leverage()`. Leverage from the config, computed leverage, or per-pair
> leverage is invisible to it. The 36 strategies it finds are a **floor**, not
> a count.

*These counts are read from [LEDGER.csv](LEDGER.csv), not computed separately —
one source, so the two cannot drift apart. The corpus grew from 804 to 895 and
the survivor figure moved only from 71% to 69% — and that only because a flag
was withdrawn on its merits, not because the corpus changed under it.*

**Sixty-nine percent of the strategies that clear every statistical test carry
at least one of these.** Neither `lookahead-analysis` nor `recursive-analysis`
nor any p-value sees them, because they are properties of the strategy's
configuration rather than of its signal.

## The four that are checked

**`stoploss = -0.99` — 245 strategies.** A declared stop that is not a stop.
Losing positions are never cut, so the reported maximum drawdown is computed on
closed trades while the real risk sits in positions that stay open. This is the
single most common pattern in the corpus.

**Inert trailing settings — 164.** `trailing_stop_positive` is set while
`trailing_stop` is `False`. The value does nothing. Whoever tuned it was tuning
a number the engine ignores.

**Trailing tighter than the spread — 27.** The traps article explains the
mechanism: backtesting walks price to the candle high, adjusts the trailing
stop, then walks price down, which "gives you a perfect candle trade, selling
just below the high of the candle, almost every time." A trailing stop below the
0.1–0.5% spread cannot behave that way live.

**Trailing with no `trailing_stop_positive` — 22.** The stop trails at the full
`stoploss` distance rather than a few percent, which is usually not what the
author meant.

**Tight `minimal_roi` on long candles — 4.** Same mechanism as the trailing
trap: on hourly-plus candles the price is unlikely to reach a sub-1% ROI target
before the stop would have triggered in real conditions.

## The three that are NOT checked, and why

Stated because a check list with silent gaps is worse than a short one:

- **Unfilled limit orders.** Backtesting fills every order at the requested
  price. Live, they sit unfilled.
- **Slippage.** The market moves between decision and execution.
- **Many trades with sub-0.5% average profit.** The article is blunt: those
  profits "will become losses in live due to slippage." This one needs average
  profit per trade in percent and trade duration, which the cards do not yet
  carry.

The article's sharpest red flag is also not yet checked: **average trade
duration shorter than the candle timeframe** — a trade opening and closing
inside one candle, which backtesting permits and live trading mostly does not.
Adding duration to the cards is the next step, and until it is there, these
four checks are a floor rather than a ceiling.

## Reproduce

```bash
python traps.py
```

Pure static analysis of the strategy source. No backtests, no data, seconds to
run against the whole corpus.
