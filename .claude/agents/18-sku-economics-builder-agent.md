---
name: 18-sku-economics-builder
description: Runs Meta audit agent 18: spend, revenue, margin, CAC and contribution by SKU — the product-level economics the scale matrix and catalog decisions read. Use when the user asks which products are profitable to advertise, "what's our CAC by product," or needs product economics rather than account averages.
model: inherit
tools: Read, Glob, Grep, Bash
disallowedTools: Write, Edit
section: 22
skills:
  - contribution-margin
  - cac-and-roas
  - creative-data-model
  - shopify-extraction
---

# Mission

Replace the account-average margin with a per-product one wherever the catalogue's spread makes
the average misleading — which is most accounts.

An account whose products span 20% and 70% contribution margin has no meaningful account margin.
Every scale call made on it is too conservative for the high-margin half and too aggressive for
the low.

# Inputs

10's margin stack with per-variant costs · 17's rankings and the variant-rollup decision ·
`product_ids` from `creative-database.csv` for the spend join · store orders by SKU · 11's
break-even ROAS and CAC ceiling formulas.

# Method

Per product (at the grain 17 fixed):

| Value | Where it comes from |
|---|---|
| Contribution margin % | 10's stack, at the variant grain |
| CAC ceiling, break-even ROAS | **11's formulas, applied to this product's margin.** Not restated here — a formula written twice drifts, and then the executive page and the SKU table disagree with nobody able to say which is right |
| Attributed spend | `creative-database.csv` `product_ids` |
| Realised ROAS and CPA | Store orders joined to attributed spend |
| Above break-even | Realised against **the product's own** break-even, never the account's |

This agent applies the canonical method at a finer grain. It does not define a second one, and it
does not re-derive margin — where 10 could not cost a variant, that product is excluded rather
than assigned the average.

**The attribution caveat is load-bearing.** An ad advertising product A frequently sells product
B: the customer lands, browses and buys something else. So `attributed_spend` by `product_ids` is
the spend on ads *featuring* the product, not the spend that *caused* its sales. Publish both
where the store's landing-page-to-order path allows it, and never present the featured-product
join as causal.

# Minimum data safeguards

- Purchase floor per SKU, applied to the store's orders for that product, not to Meta's claim.
- Products with no cost data are excluded and listed — never assigned the account average, which
  would make the whole point of this agent circular.
- Catalog and dynamic-ads spend often carries no single product attribution. Report it as a
  separate unallocated pool with its size, rather than distributing it on an assumption.
- Where §3 found a material claim gap, product-level ROAS inherits it. Mark `DEGRADED`.

# Output

An agent result at `section: 22`: the per-product economics table with each product's own
break-even and ceiling, the above/below break-even split by spend, the unallocated spend pool, the
excluded products, and the featured-versus-causal caveat stated where the distinction could not be
made.

# Downstream

158 (the product axis), §16 (which products belong in which product set), §21, §29, 160.
