# Frozen decision rule for the next corpus

**Frozen 2026-08-22, before the next corpus exists.**

The published result for the current corpus is *repair-adjusted*: both bias
detectors ran from the first commit, but which of them disqualifies a strategy
was settled after seeing the data. That is stated in [LEDGER.md](LEDGER.md) and
both figures are published, so nobody has to take my word for the order.

Transparency about a post-hoc decision does not convert it into a
pre-registered one. The only thing that does is fixing the rule **before** the
next set of numbers exists. This file is that fix.

---

## The rule, in full, with no free parameters

A strategy in the **next** corpus is called a survivor if and only if it passes
all of the following, evaluated in this order:

| # | gate | threshold | source |
|---|---|---|---|
| 1 | both windows produced a summary | numbers present, not exit code 0 | `harness.py` |
| 2 | trades in the author's window | ≥ 30 | frozen here |
| 3 | expectancy in the author's window | > 0 | frozen here |
| 4 | mean-profit p-value, author's window | < 0.05 | freqtrade output |
| 5 | expectancy out of sample | > 0 | frozen here |
| 6 | mean-profit p-value, out of sample | < 0.05 | freqtrade output |
| 7 | `lookahead-analysis` | no bias found | freqtrade |
| 8 | `recursive-analysis` | no finding, **including a refusal to run** | freqtrade |
| 9 | community backtesting traps | zero flags | `traps.py`, thresholds theirs |
| 10 | trade duration | **measured**, and ≥ 1 own candle | `harness.py` |
| 11 | multiplicity | p out of sample ≤ Benjamini-Hochberg threshold | `ledger_block.py` |

The **primary endpoint** is the count of survivors that beat `Market change`
(buy-and-hold on the same pairs over the same window) out of sample.

The **secondary endpoint**, reported alongside and never instead, is the same
count under Benjamini-Yekutieli, which controls FDR under arbitrary dependence.

## What is fixed and what is not

**Fixed.** Every threshold above. The order. The primary endpoint. The
cost assumption (0.1% per side, with 0.2% and 0.3% reported as sensitivity).
The out-of-sample window boundary: the corpus is split at the date the
strategy's own repository last touched it, or 2020-03-01 where that is unknown.

**Not fixed, and declared as such.** Which repositories enter the next corpus —
it is a census of what can be found, not a sample I choose. The number of
strategies. The market regime in either window.

**Explicitly forbidden.** Adding a gate after seeing the next result. If a new
disqualifier is discovered, it is reported as a *separate exploratory finding*
with its own epoch label, and the primary endpoint stays computed under the
rule above. That is the entire point of this file.

## How a reader checks that I kept it

This file is committed before the next corpus is swept. Its commit date is in
`git log`, and so is the first result file of that corpus. If the second
predates the first, the freeze was not a freeze.

`ledger.py` records `code_md5` and `plan_md5` on every card, so the pipeline
that produced a number can be identified from the number itself. The gates above
are the ones in `ledger_block.LADDER`; if that list changes, the diff is in the
history and this file is invalidated rather than quietly re-interpreted.

## What this file does not claim

It does not make the *current* result confirmatory. That result stays
repair-adjusted and is labelled as such wherever it appears. This freeze applies
to the next corpus and to nothing that already exists.

It also does not promise the next result will be interesting. A frozen rule that
yields a boring number is the normal case, and publishing it is the price of the
rule meaning anything.
