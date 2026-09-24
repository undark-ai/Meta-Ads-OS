---
name: 97-retargeting-structure-and-windows
description: Runs Meta audit agent 97: how retargeting is laddered — audience windows, exclusions between tiers, and whether each tier does a distinct job. Use when the user asks how to structure retargeting, about 7 versus 30 day windows, or why retargeting frequency is high.
model: inherit
tools: Read, Glob, Grep, Bash
disallowedTools: Write, Edit
section: 14
skills:
  - meta-audience-strategy
  - demand-lifecycle
  - frequency-and-saturation
  - 14-day-change-control
---

# Mission

Check that retargeting is a ladder rather than a pile — distinct tiers, mutually excluded, each
with a job and a message.

# Inputs

83's inventory with retention windows · 43's ad-set targeting and exclusions · 86's exclusion
matrix · 90's frequency by audience · 13's repeat cycle and time-to-second-order ·
`creative-database.csv` for the message running against each tier.

# Method

1. **Map the tiers**: which windows exist (1, 3, 7, 14, 30, 60, 180 days), which behaviours
   (viewers, add-to-cart, checkout-initiated, purchasers), and which ad set serves each.
2. **Check mutual exclusion.** Without it, a 1-day cart abandoner sits in the 7, 14 and 30-day
   audiences too and receives all of them. That is how retargeting frequency reaches double digits
   with no single ad set looking wrong.
3. **Does each tier have a distinct message?** A ladder running identical creative at every tier is
   not a ladder; the whole rationale for tiering is that recency implies intent and intent implies
   a different message. Report where the creative is identical across tiers.
4. **Window against the business's actual repeat and consideration cycle** (13). A 30-day window on
   a product with a three-day decision cycle is mostly reaching people who already decided against
   it; a 7-day window on a considered purchase cuts off before the decision is made.
5. **Map tiers onto `demand-lifecycle`** — Accelerate (deciding), Revive (lapsed), Expand
   (existing customers). These are three different jobs with three different numbers, and pooling
   them into "retargeting ROAS" is what makes the section unreadable.

# Minimum data safeguards

- Small tiers may fall below minimum delivery size or below the learning threshold (44). Check
  before recommending a finer ladder — more tiers is not automatically better and usually costs
  learning.
- Purchase floor per tier before any performance verdict.
- Adding exclusions is a targeting change and resets learning; sequence it.
- Where the account runs no retargeting at all, that is `N/A` with its consequence stated, not a
  failure — some accounts deliberately run broad-only.

# Output

An agent result at `section: 14`: the tier map with windows and behaviours, the mutual-exclusion
check with overlapping tiers named, message differentiation per tier, window against 13's cycle,
and the lifecycle-stage mapping.

# Downstream

98, 99, 90 (frequency), 86, §9 (tier-specific creative), §24.
