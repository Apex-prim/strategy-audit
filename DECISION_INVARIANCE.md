# A rule that was not changed when the result invited it

On 2026-08-22 a gate was added, produced a verdict, and within hours the data
offered a reason to modify that gate. The modification would have been
defensible, would have explained the data better, and was not made.

This file records that, because the whole difficulty of pre-registration is not
writing the rule down — it is leaving it alone once the numbers arrive.

---

## 1. The gate

`G12_economic`: a strategy passes if its total return out of sample exceeds
`Market change` — buy-and-hold on the same pairs over the same window.

## 2. When it was created

Commit `5091379`, 2026-08-22 10:59 UTC. Added after an outside reader pointed
out that the ladder demanded statistical significance and never demanded
economic significance.

Note the date against the corpus: the first result card of this corpus is
2026-08-21 19:58 UTC. **The gate is 15 hours younger than the data**, which is
exactly why the current result is labelled repair-adjusted and not confirmatory.
`freeze_guard.py` derives that from `git log` and `CORPUS_RUN.json` rather than
taking anyone's word.

## 3. The result it produced

Six strategies reached the gate. Five cleared the effect-size gate before it.
**None cleared `G12`.** Over the full window they return +38.6% to +159.6%
against buy-and-hold's +346.3% — a shortfall of 187 to 308 percentage points of
cumulative return.

## 4. When the regime dependence was found

Same day, hours later. The out-of-sample window is a bull market, so the gate
was suspected of measuring the window rather than the strategies. The test was
declared before it ran and deliberately neutral — calendar years, not periods
chosen by their shape.

```
year    market        survivors beating buy-and-hold
2020   +143.04%       0 of 5
2021   +218.33%       0 of 5
2022    -66.70%       5 of 5
2023    +76.37%       0 of 5
2024    +95.90%       0 of 5
2025    -20.89%       5 of 5
2026    -29.65%       5 of 5
```

Seven years, seven correct classifications by the sign of the market. The
survivors beat buy-and-hold in every falling year and in no rising year.

## 5. The modification that was proposed and refused

Two obvious repairs presented themselves:

- make `G12` regime-conditional — require the strategy to beat buy-and-hold in
  at least one declared regime rather than over the whole window;
- replace the benchmark with an exposure-matched one, since in 2022 the market
  fell 66.7% while these strategies returned between −5.9% and +3.5%, meaning
  they were barely in the market at all.

Both are reasonable. The second is arguably more correct as a matter of
finance. Neither was applied to `G12`.

## 6. The exploratory finding, kept separate

The regime split is published as an **exploratory** result with its own epoch.
It does not enter the primary endpoint. It is a hypothesis for the next corpus,
not a correction to this one.

It also does not say the survivors are useful. Sitting out a falling market is
something cash does without any strategy, and the correct benchmark for a
low-exposure strategy is an exposure-matched one — which is precisely the change
that was refused here, and which the next corpus can test under a rule fixed in
advance.

## 7. Why the change was refused

Because the result asked for it.

A rule adjusted after seeing what it produced cannot support the claim it is
used to make, however good the adjustment is. The repair would have been made on
the same data, on the same day, in response to the same numbers it was meant to
judge. That is the definition of the failure this repository exists to detect,
and finding it in someone else's work while performing it in one's own would
make the whole exercise worthless.

The gate stays. The finding is published beside it. The next corpus decides.

## 8. Where to check this

| what | where |
|---|---|
| gate introduced | commit `5091379` |
| ladder definition | `ledger_block.py`, `LADDER` |
| corpus start | `CORPUS_RUN.json`, `first_card_epoch` |
| status derived, not asserted | `freeze_guard.py` |
| frozen rule for the next corpus | `PREREGISTRATION.md` |
| the epoch table | `LEDGER.md`, `CLAIMS.csv` |

---

A certificate cannot be issued to oneself. It can only be earned by refusal —
and a refusal is only evidence if the temptation is documented alongside it.
