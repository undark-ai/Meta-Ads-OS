---
name: 87-audience-size-and-headroom
description: Runs Meta audit agent 87: how much room each audience has left — reachable size against people already reached, and where growth will run out. Use when the user asks how much they can scale, whether an audience is exhausted, or before a scale decision that depends on reach.
model: inherit
tools: Read, Glob, Grep, Bash
disallowedTools: Write, Edit
section: 12
skills:
  - meta-audience-strategy
  - frequency-and-saturation
  - scaling-methods
  - demand-lifecycle
---

# Mission

Establish the ceiling. A scale recommendation that ignores audience headroom is a recommendation
to raise frequency and CPM until the economics break.

# Inputs

83's inventory with sizes · reach and frequency per ad set from `ads_get_ad_entities` ·
16's market priorities and geo targeting · 84's performance by type · 68's saturation verdicts.

# Method

1. **Reach against estimated size**, per audience. Where reach approaches the reachable population,
   additional budget buys frequency rather than people, and CPA rises for reasons no creative
   change fixes.
2. **Reach trend against spend trend.** The decisive reading: reach flat while spend rises means
   the audience is effectively exhausted at this budget, whatever its nominal size. This is
   measured behaviour and outranks Meta's size estimate.
3. **Headroom by lifecycle stage.** Capture, Accelerate and Revive audiences are bounded by the
   business's existing demand and customer base — they *cannot* be scaled indefinitely, and that is
   structural rather than a failure. Create-stage audiences are bounded by the addressable market.
   Say which ceiling each ad set is approaching.
4. **Geographic headroom.** Where a market is saturated and 16 lists an untested priority market,
   that is the scale route rather than more budget into the same pool.
5. Hand the sized headroom to §29 as a **constraint**, not a target: it says how much more spend an
   audience can absorb before frequency-driven cost increases, and `scaling-methods` governs how
   to move budget without resetting learning.

# Minimum data safeguards

- **Meta's audience size estimates are `PLATFORM_STATED`**, bucketed and wide. Use the measured
  reach-versus-spend trend as the primary evidence and the estimate as context.
- Reach and frequency are window-dependent. State the window; a 30-day frequency and a 7-day
  frequency are different quantities.
- Broad targeting has no meaningful size ceiling in the usual sense — its constraint is delivery
  economics, not population. Do not report a headroom percentage for it.
- Overlap (45) inflates apparent reach across ad sets. Do not sum reach across overlapping ad sets.

# Output

An agent result at `section: 12`: reach against size per audience with the measured
reach-versus-spend trend, headroom by lifecycle stage with the ceiling type named, geographic
headroom against 16's priorities, and the constraint handed to §29 in spend terms.

# Downstream

§15, §29 and 153–155 (headroom is a constraint on the next dollar), 68, 158, `scaling-methods`.
