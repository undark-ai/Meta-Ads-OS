---
name: learning-phase-and-significance
description: When deciding whether a Meta ad, ad set or angle has produced enough data to judge — the purchase floors below which a kill or scale call is variance, Meta's learning-phase mechanics, and which edits reset learning. Use when the user asks "is this ad dead," "can I kill this yet," "why did performance change after I edited it," "how long should I run a test," or when any agent is about to issue a kill or scale recommendation. This is the gate every creative and budget verdict passes through.
---
# Learning phase and significance

Two separate things, both of which invalidate a verdict, and both of which are ignored constantly:

1. **Learning phase** — the ad set is not delivering stably, so its numbers describe the
 algorithm's search, not the creative.
2. **Volume** — there are not enough purchases to distinguish the result from noise.

An ad killed at four purchases was not killed on evidence. It was killed on a coin flip that the
operator felt confident about.

## Meta's learning phase

An ad set enters learning at creation and after significant edits, and exits at roughly **50
optimisation events in a 7-day rolling window**. Below that, Meta is exploring: CPA is volatile,
delivery is uneven, and per-ad comparisons inside the ad set are close to meaningless.

`LEARNING LIMITED` is a different state: the ad set cannot reach 50 events per week at its
current budget and audience size, so it never stabilises. This is a **structural** finding —
consolidate, widen, or raise budget — not a creative one, and treating it as creative
underperformance is a diagnosis that leads to replacing ads that were never given a fair read.

### Edits that reset learning

Check `ads_account_get_activity_logs` before attributing any performance movement to creative:

| Resets learning | Usually does not |
|---|---|
| Targeting change | Budget change under ~20% |
| Optimisation event change | Ad status toggles within an existing set |
| Bid strategy or bid amount change | Name changes |
| Adding or removing ads | Schedule adjustments (small) |
| Placement change | |
| Large budget change (~20%+) | |
| Creative change on an existing ad | |

The percentages are Meta's stated behaviour, not a measured constant; they move. Treat them as a
prompt to check the activity log rather than a rule to compute against.

**The practical consequence:** a performance drop the day after an edit is the edit. An ad
"failing" inside an ad set that reset four days ago has not failed. Any agent about to
recommend a kill checks the learning state first, and says what it found.

## Purchase floors

The floors below which this system will not issue a verdict. They are deliberately conservative
because the cost of a wrong kill — losing a winner and the production spend behind it — is
higher than the cost of running a loser two more weeks.

| Decision | Floor | Rationale |
|---|---|---|
| Kill an ad | **≥ 15 purchases** on the ad, or spend ≥ 3× target CPA with **0** purchases | Zero-conversion at 3× CPA is a real signal; 2 purchases at 1× CPA is not |
| Scale an ad | **≥ 25 purchases** and stable for ≥ 7 days post-learning | Scaling amplifies whatever is true, including a fluke |
| Call an angle a winner | **≥ 30 purchases aggregated across the angle**, ≥ 3 distinct ads | Aggregation is why classification is worth doing |
| Call a test | Per `cro-experiment-design` / the test's pre-agreed kill number | Agreed before the test, never after |
| Compare two ad sets | Both out of learning, both ≥ 50 events/week | Otherwise you are comparing two searches |

Where the account's whole purchase volume sits below these floors, say so as a **structural**
finding in §10: the account cannot run a creative testing program at this volume, and the fix
is fewer, larger tests rather than more, smaller ones.

## Zero-conversion is not automatically waste

An ad with 30 clicks and no purchases at a €60 target CPA has spent maybe €25. That is normal
variance, not evidence of failure. Calling it waste and bulk-pausing on that basis is how
accounts lose the long tail that was about to work.

Two buckets:

- **`CONFIDENT_WASTE`** — spend ≥ 3× target CPA with zero purchases, conversion lag elapsed
- **`WATCH`** — everything below that

Report them separately. Never sum the watch bucket into a "recoverable spend" headline.

## Conversion lag

Meta credits a purchase to the click, which may have been up to 7 days earlier. **The last 7
days of any window are incomplete**, and the last 1–2 days are severely so.

- Exclude the trailing lag period from any "is this working" read, or state that it is included
 and what that does to the number.
- A week-over-week comparison where the current week includes incomplete days will always show a
 decline. This manufactures fatigue findings that do not exist.
- For a 7-day-click window, judge on data at least 7 days old.

## Practical significance beats statistical significance

A p-value on a 20-purchase sample is a formality. More useful questions:

1. **Would the decision change across the plausible range?** Compute the result at the low and
 high end of the confidence interval. If the action is the same at both ends, the uncertainty
 does not matter and you can act.
2. **Does a second signal agree?** A weak purchase signal plus a below-median hold rate plus a
 rising CPM is a stronger case than any one at higher volume.
3. **What does being wrong cost?** Pausing a €12/day ad is cheap and reversible. Cutting a
 €4,000/day campaign is not. Set the evidence bar by the cost of the mistake, not by a
 uniform threshold.

## What to return below the floor

`INSUFFICIENT_DATA`, with:

- the actual counts, so the reader can judge
- **how much more data is needed**, and how long that takes at current spend
- what to do meanwhile — usually "leave it running and check on <date>", occasionally
 "concentrate budget so this becomes readable"

Never force a recommendation to avoid an empty section. "We cannot tell yet, here is when we
can" is a finding. A confident verdict on four purchases is a liability, and it is the specific
liability that makes people distrust automated audits.

## Where this gates

- `scale-matrix.yaml` — the volume gate blocks `SCALE` and `KILL` verdicts
- `creative-record.yaml` — `volume_sufficient: false` blocks a kill recommendation for that ad
- §8 fatigue — a decay signal below the floor is `WATCH`, not `FATIGUED`
- §9 angle analysis — aggregated angle floors
- `EXECUTION-PROTOCOL.md` — the execution lane will not act below the floor
