---
name: recommendation-prioritization
description: When merging findings from across an audit into one ranked, de-duplicated opportunity matrix and sequencing them into a 30/60/90 plan. Use when the user asks "what should I fix first," "prioritise these," "action plan," or when section 30 needs to close. Handles the double-counting problem that makes most audit totals wrong. For where to put more budget instead, see scale-matrix.
---
# Recommendation prioritisation

Thirty sections produce overlapping findings. The opportunity matrix is where they become one
ranked list, and the ranking is where most audits quietly go wrong.

## De-duplicate before ranking

The same money is found several times. A search for waste, a placement analysis and a creative
fatigue pass will all point at the same underperforming ad set, and summing their impacts
produces an account-level upside figure that is simply false.

- Merge findings that share a **spend base** into one canonical opportunity with contributing
 evidence from each source.
- Record `overlaps_with` on rows that touch the same spend without being the same finding.
- **Do not sum mutually exclusive scenarios.** "Fix the checkout" and "reallocate away from this
 campaign" cannot both realise their full stated value.
- The account-level total is not the sum of the column. Compute it from the de-duplicated set and
 say what was excluded.

## Rank on expected contribution, not ROAS

Four inputs, in this order:

1. **Expected contribution impact** — currency, or a range where uncertainty is material
2. **Confidence** — a high-confidence €20k beats a low-confidence €60k
3. **Effort** — implementation cost, including whose time
4. **Time to read** — how long before the change can be judged. This drives sequencing more than
 people expect

Where impact cannot be defensibly quantified, the finding is a `FLAG` with **no** currency
value. Never invent one to make it rank.

## The P0–P3 order

Priority is not the same as impact. It encodes dependency:

| Priority | Contains | Why here |
|---|---|---|
| **P0** | Tracking and measurement fixes | Everything downstream is judged on numbers these produce. Fixing them first makes every later change readable |
| **P1** | Obvious waste, structure, creative strategy | Large, fast, low-risk |
| **P2** | Catalog, product segmentation, landing pages, the creative testing engine | Real value, longer to build |
| **P3** | Incrementality testing, scaling winners, optimising toward profit and LTV | Depends on P0–P2 being true |

A P0 with modest currency impact still comes first. Fixing attribution is rarely the biggest
number in the matrix and is almost always the right first move, because it changes what every
other number means.

## Sequencing, not just ordering

The action plan is constrained by readability, not only by value:

- **One material change at a time** where a causal read is intended. Two simultaneous changes
 produce a result nobody can attribute, and the account has paid for a test it cannot learn
 from.
- **14-day read windows.** Changes stacked inside one window are unreadable.
- **Learning-phase cost.** A change that resets learning costs roughly a week of stable delivery.
 Say so in the plan rather than discovering it in the review.
- **Batch genuinely independent changes.** Pausing twelve unrelated fatigued ads is one decision,
 not twelve. Say which it is.

## The five buckets

`action-plan.md` splits into:

- **DO THIS WEEK** — high confidence, low effort, fast read
- **DO THIS MONTH** — high value, more effort or a longer read
- **TEST / LEARN** — needs an experiment before it is a decision
- **MONITOR** — real but not yet actionable; name the trigger that would make it so
- **DATA REQUIRED** — blocked on a measurement or a connector; name what unblocks it

`DATA REQUIRED` is not a failure bucket. It is frequently where the highest-value items sit, and
listing them keeps the reason for a `BLOCKED` section visible.

## Quantified upside

`quantified-upside.md` states current versus achievable for spend, revenue, ROAS, CAC and
conversion rate, with incremental revenue and contribution.

Every figure states its assumption. Anything that cannot be defended is a `FLAG`, not a number.
Close by naming **what could not be sized and why** — that paragraph is usually more useful than
the total, because it tells the account what to fix so the next audit can size it.
