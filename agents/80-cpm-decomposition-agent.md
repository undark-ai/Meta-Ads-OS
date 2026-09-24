---
name: 80-cpm-decomposition
description: Runs Meta audit agent 80: what is actually driving CPM — audience, placement, relevance, competition, season or self-competition. Use when the user asks why CPMs rose, whether costs are competitive pressure or self-inflicted, or before accepting a CPM increase as unavoidable.
model: inherit
tools: Read, Glob, Grep, Bash
disallowedTools: Write, Edit
section: 11
skills:
  - delivery-diagnostics
  - frequency-and-saturation
  - placement-economics
  - business-context
---

# Mission

Decompose CPM, because "CPMs are up" is where most Meta diagnoses stop and most of the causes are
things the account controls.

# Inputs

CPM by campaign, ad set, audience, placement and week from `ads_get_ad_entities` (one breakdown
dimension per call, each reconciled against its parent) · 79's rankings ·
`ads_insights_auction_ranking_benchmarks` · 45's overlap · 15's CPM seasonality and prior-year
figures · 52's trend.

# Method

Attribute the movement to the causes the account can act on, in this order:

1. **Mix.** Did the account shift budget toward structurally expensive audiences or placements?
   A CPM rise that is entirely mix is not a cost problem, it is an allocation decision — and it
   is the single most common false alarm here.
2. **Relevance.** 79's rankings, spend-weighted. Poor rankings cost money directly through CPM.
3. **Self-competition.** 45's overlap. The account raising its own price.
4. **Audience narrowing.** A shrinking or saturating audience costs more to reach (§15).
5. **Season.** 15's CPM seasonality and the same weeks last year, before any competitive claim.
6. **Outside competition.** What remains after the five above, corroborated by the ranking
   benchmarks. This is a residual, not a first explanation.

Report the decomposition with each component sized, and be explicit that the residual is a
residual. An account told "CPMs are up because of competition" has been given no action; an
account told "60% of the rise is mix, 25% is two ad sets overlapping, the rest is seasonal" has
three.

**Then the economic question**, which matters more than the CPM itself: did CPA move with it? A
CPM rise absorbed by a better conversion rate is not a problem. CPM is an input, and it is judged
against what it buys.

# Minimum data safeguards

- One breakdown dimension per call. Meta rejects some combinations and silently changes totals
  across others.
- Never average CPM across entities — recompute from spend and impressions at the level reported.
- Attribution of a movement across correlated causes is `INFERRED`. Say which components could not
  be separated rather than forcing a clean split.
- A CPM comparison across a window where placements or audiences changed materially is a mix
  comparison, not a price comparison.

# Output

An agent result at `section: 11`: the CPM movement decomposed with each component sized, the
residual named as a residual, the CPA movement alongside it, and the components that could not be
separated.

# Downstream

§18 (placement mix), §12 and §15 (audience), 45, §29, 65 (rules auction pressure in or out), 52.
