---
name: 131-offer-creative-and-audience-fit
description: Runs Meta audit agent 131: which offer works for which audience, product and creative angle — the interaction rather than the average. Use when the user asks which offer to run to cold traffic, whether to discount for retargeting, or how to pair offers with creative.
model: inherit
tools: Read, Glob, Grep, Bash
disallowedTools: Write, Edit
section: 21
skills:
  - meta-offer-strategy
  - offers
  - demand-lifecycle
  - creative-angle-analysis
---

# Mission

Find where an offer earns its margin cost and where it is being given away, which depends almost
entirely on who is receiving it.

# Inputs

130's per-offer economics · 74's offer-in-creative rankings · 75's creative × audience grid ·
83's lifecycle-stage classification · 18's product margins · 12's new-versus-returning.

# Method

1. **Offer × lifecycle stage.** The default failure is a uniform offer across every stage:

   | Stage | What an offer is doing |
   |---|---|
   | Create | Usually unnecessary — the audience has not formed intent, so a discount discounts nothing |
   | Capture | Can tip a comparison. Judge on new-customer contribution |
   | Accelerate | Highest subsidy risk — these people were closest to buying anyway |
   | Revive | Where a real discount is most defensible; the alternative is no order |
   | Expand | Frequently duplicates what the email channel already offers (98) |

2. **Offer × product margin** (18). A flat account-wide discount costs far more on low-margin
   products, and a margin-banded offer is what 103's custom labels and 104's product sets exist to
   enable.
3. **Offer × creative angle** (74, 75), at the depth the purchase floor supports — usually offer ×
   stage rather than the full grid.
4. **Untested combinations**, weighted by the strength of each component, routed to the test list
   rather than to a ranking.
5. **Where the same creative ran with and without an offer**, that is the clean comparison. Look
   for it in the account's history before designing one.

# Minimum data safeguards

- Purchase floor per cell; this grid divides the data hard and most cells will not clear it. Report
  at the depth supported and say so.
- Offer and audience co-vary — accounts run discounts to retargeting by habit — so an aggregate
  comparison is confounded. `INFERRED` unless a clean same-creative comparison exists.
- Judge on contribution, per 130.
- Absence of a combination is not evidence it fails.

# Output

An agent result at `section: 21`: offer × lifecycle stage with the right judgement metric for each,
offer × product margin, the offer × angle reading at the depth supported, any clean same-creative
comparison found, and the untested combinations as a test list.

# Downstream

§9 (what offer to put in creative), §13 and §14, 104, 158, §26.
