---
name: scaling-methods
description: When executing a scale decision on Meta — the readiness checklist that gates it, the four scaling methods with their day-by-day budget steps, and how to tell a campaign has hit its ceiling. Use when the user asks "how do I scale this," "how fast can I increase budget," "vertical or horizontal scaling," "should I duplicate the ad set," or "how do I scale Advantage+." The scale matrix decides WHICH combination to scale; this covers how to actually do it without breaking the read.
---
# Scaling methods

`scale-matrix` decides *which* combination deserves more budget and how much headroom the evidence
supports. This covers *how* to move the money without destroying the thing you are scaling.

## Readiness — all must be true

If any fails, fix it first. Scaling amplifies whatever is currently true, including a fluke.

- [ ] The ad set has **exited learning** (~50 optimisation events in 7 days)
- [ ] ROAS stable within roughly ±15% for **at least two weeks**
- [ ] Frequency below the threshold for its campaign type (`frequency-and-saturation`)
- [ ] Creative fresh — the account's own median creative lifespan not yet elapsed
- [ ] **No pending change that would itself reset learning** — bid strategy, audience, optimisation event
- [ ] The §2 measurement verdict is not `RED`, and the ROAS is reconciled (§3)
- [ ] Above the purchase floor (`learning-phase-and-significance`)

The last two are this repository's additions and they are not optional: scaling against conversion
values the audit has just shown to be unreliable is the specific mistake the system exists to
prevent.

## The four methods

### 1. Vertical — same audience, more budget

For proven ROAS at low frequency.

| Day | Action |
|---|---|
| 1 | Increase budget **15–20%**. Never more than ~20% in 24 hours — above that resets learning |
| 2–3 | Monitor. **No changes** |
| 4 | Compare ROAS against the pre-scale baseline. Within 15% → continue. Dropped more than 15% → revert and wait 48h before reassessing |
| 5 | If stable, increase again |

On CBO, raise the campaign budget and let Meta redistribute. On ABO, raise each ad set
individually, weighted toward the ones that earned it.

### 2. Horizontal — new audience, same creative

For a campaign approaching frequency saturation rather than one that is budget-limited.

1. Take the winning creative on 14-day performance.
2. New ad set: different audience, same creative, budget at ~50% of the original's.
3. Run **untouched for 7 days**.
4. New ad set above ~50% of the original's ROAS → keep, then scale it vertically. Below → pause and
   try a different audience.

### 3. Duplicate and scale — the risk-averse route

1. Duplicate the winning ad set.
2. Set the duplicate's budget 50–100% higher.
3. Run both in parallel for 7 days.
4. Duplicate within ~20% of the original → pause the original, keep the duplicate. Underperforms →
   pause the duplicate, keep the original.

Costs more (you fund both) and buys a reversible test. Worth it on the account's largest spender.

### 4. Advantage+ Shopping

ASC does not support ad-set duplication or manual audience adjustment.

1. Add **new asset groups** — new creative themes, not duplicates of existing ones.
2. Raise the campaign budget 15–20% at a time.
3. Add audience signals: fresh customer-list uploads, additional interest signals.
4. Expand country targeting where applicable.
5. **Do not edit existing asset groups while scaling** — that resets learning for the *whole*
   campaign, not just the group you touched.

## Choosing the lever: budget against effort

Where several routes are open, the constraint decides:

| | Low effort | High effort |
|---|---|---|
| **Budget available** | **Audiences** — expand segments, add lookalike tiers. Fastest reach gain, reuses existing assets | **Geography** — new countries or regions. Check shipping economics (§23) before assuming a market is profitable |
| **Budget constrained** | **Ads** — better creative frees budget by converting more of the same spend | **Objectives and bids** — a more efficient objective or bid strategy frees budget. Slowest, resets learning |

With no spare budget, the bottom row is the only real option, and better creative is the cheaper
of the two. With budget and no time, the top row scales reach with the least campaign work.

## The ceiling

Signs a campaign has stopped absorbing money:

- Frequency rising while reach is flat
- CPM climbing at each budget step
- Purchases per additional dollar falling — the marginal figure, not the average
- Delivery drifting toward cheaper placements as the good inventory exhausts

At the ceiling, further vertical scaling buys worse traffic. The move is horizontal, geographic, or
accepting the ceiling and reporting it as one — `scale-matrix` records this as
`observed_ceiling` so the next run does not re-litigate it.

## Applying any of this

Every step here is a mutation. It goes through `workflows/08-execution-run` under
`EXECUTION-PROTOCOL.md`, with the budget sanity-checked against **account history** rather than
against the plan — an entity scaled to 10× the intended budget is the common failure, and one
look catches it.
