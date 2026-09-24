# Weekly operating cycle

The recurring cadence between audits. Diagnosis, not a full sweep — and it inherits the audit's
canonical economics rather than recomputing them.

## Monday — read

| Step | What | Skills |
|---|---|---|
| 1 | Delivery blockers. A blocked ad is not an underperforming ad | 03 |
| 2 | Pull the last 7, 14 and 30 days. **Exclude the trailing conversion-lag window** or state that it is included | `meta-ads-data-validation` |
| 3 | Check the activity log for learning resets before attributing any movement to creative | `learning-phase-and-significance` |
| 4 | Performance against the canonical break-even ROAS and CAC ceiling from §1 | `cac-and-roas` |
| 5 | Fatigue check on ads above their campaign-type frequency threshold | `frequency-and-saturation` |

## Wednesday — act

| Step | What |
|---|---|
| 6 | Kill and graduate decisions, **each above the purchase floor** |
| 7 | Launch this week's tests, with their kill numbers agreed in advance |
| 8 | Stage-1 check on last week's launches: is Meta delivering them at all? |

## Friday — allocate

| Step | What |
|---|---|
| 9 | Budget adjustments on evidence of headroom, not on reported ROAS |
| 10 | Record what was learned, in the creative learning document |

## The rules that make this a cycle rather than fiddling

- **Do not read the last 3 days.** Under a 7-day-click window they are incomplete, and a
  week-over-week comparison including them always shows a decline. This manufactures fatigue
  findings that do not exist and is the single most common cause of a good ad being killed.
- **Do not act below the floor.** `learning-phase-and-significance`. An ad with four purchases
  has not told you anything.
- **One material change at a time** on any entity where a causal read is intended.
- **Check learning phase first.** An ad set that reset four days ago is reporting the edit.
- **Write down what was learned.** A cycle that produces decisions but no record re-learns the
  same thing next quarter.

## What this cycle does not do

Reconciliation, incrementality, catalog, structure. Those are audit work. If the weekly read
keeps surfacing the same unanswerable question — "is this ROAS real" — that is the signal to run
`02-full-account-audit`, not to keep reading harder.

## Changes

This workflow **diagnoses**. Applying its decisions is `08-execution-run`, or a human in Ads
Manager.
