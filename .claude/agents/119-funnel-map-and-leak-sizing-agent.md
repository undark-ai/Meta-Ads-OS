---
name: 119-funnel-map-and-leak-sizing
description: Runs Meta audit agent 119: the post-click funnel from impression to purchase, with leaks ranked by absolute lost orders rather than by rate. Use when the user asks where they are losing people, about funnel drop-off, or which conversion step to fix first.
model: inherit
tools: Read, Glob, Grep, Bash
disallowedTools: Write, Edit
section: 19
skills:
  - funnel-analysis
  - meta-post-click-funnel
  - creative-data-model
  - cac-and-roas
---

# Mission

Size the leaks, and rank them by orders rather than by percentage — because the worst-looking rate
is rarely the biggest opportunity.

# Inputs

`creative-database.csv` funnel columns · 51's campaign figures · 22's event-coverage findings,
which decide which steps are measurable at all · 11's break-even chain · 36's verdict.

# Method

1. Build the funnel: impression → 3-second view → outbound click → landing-page view → content
   view → add to cart → initiate checkout → purchase. Recompute every step rate from component
   sums.
2. **Rank by absolute lost orders**, not by rate:

   ```
   lost_orders_at_step = visitors_entering_step × (benchmark_rate − actual_rate)
   ```

   where the benchmark is the account's **own** best-performing comparable segment, not a published
   figure. A 20-point drop at a step 300 people reach is worth less than a 3-point drop at a step
   40,000 reach, and a rate-ranked funnel puts them the wrong way round every time.
3. **Value each leak** at 10's contribution per order, so §30 can rank funnel work against creative
   and catalog work in the same units.
4. **Attribute each leak to a layer**: click-to-LPV is speed, redirects or a dead destination (48);
   LPV-to-ATC is the page and the offer (§20, §21); ATC-to-checkout is cart friction; checkout-to-
   purchase is payment, shipping cost or trust (§20's checkout work).
5. **Segment the funnel** by device, placement, creative angle and product where volume allows —
   an account-level funnel averages a working desktop path with a broken mobile one.

# Minimum data safeguards

- **A step that is not measured is not a leak.** Where 22 found a missing event, that step is
  `BLOCKED`, not zero — and a funnel that silently treats an unfired event as a drop-off invents
  the largest leak in the report.
- Benchmarks are the account's own segments. A published funnel benchmark is not evidence for this
  account and is never used to size a leak.
- Purchase floor per segment before segmenting.
- Where §2's verdict is not `GREEN`, funnel rates inherit that; publish the map and mark the
  valuations `DEGRADED`.

# Output

An agent result at `section: 19`: the funnel with every rate recomputed from sums, leaks ranked by
absolute lost orders with the comparison segment named, each valued in contribution, each attributed
to a layer with its owner, and the segmented views the data supported.

# Downstream

120–128, §20, §21, 157 and 160, 05.
