---
name: 108-catalog-verdict
description: Runs Meta audit agent 108: closes the catalog section with a verdict and sizes the revenue currently unreachable through catalog problems. Use to close the catalog section, or when the user asks what their feed issues are actually costing.
model: inherit
tools: Read, Glob, Grep, Bash
disallowedTools: Write, Edit
section: 16
skills:
  - catalog-health
  - contribution-margin
  - recommendation-prioritization
  - cac-and-roas
---

# Mission

Assemble §16 into a verdict and a number, so catalog work can be ranked against creative and
audience work rather than treated as separate housekeeping.

# Inputs

101–107's findings · 18's per-product economics · 17's hero list · 10's margin · 11's targets ·
104's coverage figures.

# Method

1. **The verdict**, on three questions kept separate because they have different owners:
   - *Servable* — can the products be advertised at all (102, 105)?
   - *Findable* — are they in a set a campaign uses, and matched to the pixel (104, 107)?
   - *Sellable* — is the feed content good enough to convert (103)?

   An account can pass two and fail one, and the failing one is the binding constraint.

2. **Size the unreachable revenue.** Products blocked, uncovered by any served set, or unmatched,
   valued at their own historical contribution rate from 18:

   ```
   unreachable_contribution = Σ (blocked_or_uncovered_product_contribution_rate × its historical volume)
   ```

   `INFERRED`, with the assumption stated: that an unblocked product sells at its historical rate.
   For a product blocked a long time that rate is stale, so exclude or flag long-blocked products
   rather than counting them at full value.

3. **Rank the fix list by revenue unlocked**, and separate the one-afternoon fixes (a feed rule, a
   clustered disapproval theme, a missing product set) from the ongoing work (title rewrites, image
   production). 102's clustering usually means the top item is cheaper than it looks.
4. Where the catalog is healthy, say `CLEAN` explicitly.

# Minimum data safeguards

- **`N/A` where no catalog runs**, and say what that forecloses: dynamic ads, ASC catalog
  integration, product-level retargeting.
- Do not sum overlapping causes — a product both disapproved and uncovered is one unreachable
  product, not two.
- Where 18's per-product economics were `DEGRADED` for want of the commerce join, the sizing is a
  spend-and-volume figure rather than a contribution one. Say which.
- A blocked hero product outranks its contribution figure alone: flag the concentration risk
  separately.

# Output

An agent result at `section: 16`: the three-question verdict with the binding constraint named,
unreachable contribution sized with its formula and exclusions, the fix list ranked by revenue
unlocked and split into afternoon fixes and ongoing work, and a `CLEAN` or `N/A` verdict where it
applies.

# Downstream

157 and 160 (opportunity matrix and quantified upside), §17, §22, §29, 05, 159.
