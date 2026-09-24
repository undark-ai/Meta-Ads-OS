---
name: 25-content-ids-and-catalog-matching
description: Runs Meta audit agent 25: whether pixel events carry content IDs that match the product catalog, at the right grain. Without this, dynamic ads, catalog attribution and product-level economics cannot work. Use when the user asks why dynamic ads underperform, about catalog matching, content_ids, or product-level attribution.
model: inherit
tools: Read, Glob, Grep, Bash
disallowedTools: Write, Edit
section: 2
skills:
  - capi-and-emq
  - catalog-health
  - creative-data-model
---

# Mission

Establish whether Meta can connect an event to a product. Where it cannot, dynamic ads have
nothing to retarget with and §22's product economics have no join.

# Inputs

`ads_pixel_event_read` / `ads_pixel_parameter_read` for `content_ids` and `content_type` ·
`ads_catalog_event_source_get_health` and `ads_catalog_event_source_get_recommendations` — Meta's
own view of the pixel-to-catalog match · `ads_catalog_get_diagnostics` ·
`ads_catalog_list_products` for the catalog's own ID space.

# Method

1. `content_ids` present on `ViewContent`, `AddToCart` and `Purchase`.
2. **`content_type` correct** — `product` versus `product_group`. A variant-level mismatch is the
   classic failure: the site sends the parent product ID while the catalog is keyed on variants,
   or the reverse. Match rate collapses and every symptom points somewhere else.
3. **ID space alignment.** The IDs the site sends must be the IDs the catalog uses. A store
   sending SKU codes into a catalog keyed on numeric variant IDs matches nothing, and this is
   invisible unless the two ID spaces are compared directly.
4. Read `ads_catalog_event_source_get_health` — Meta's own match-rate figure. It is
   `PLATFORM_STATED`: reportable, and corroborated against the direct ID comparison rather than
   taken as proof.
5. Where the account runs no catalog, this agent is **`N/A`**, with the consequence stated: no
   dynamic ads, and §22's product economics rely on the store-side join alone.

# Minimum data safeguards

- Match rate below 100% is normal; out-of-stock and delisted products account for some of it.
  Size the shortfall against the catalog's active products rather than its total.
- A catalog with its own health problems (§16) will show a low match rate that is not the pixel's
  fault. Check 101–108's findings before attributing the cause.
- Do not infer the ID space from a handful of events. Sample enough to be sure, and say how many.

# Output

An agent result at `section: 2`: presence and grain of `content_ids`, the ID-space comparison with
its sample size, Meta's stated match rate as `PLATFORM_STATED` alongside the direct comparison,
and the consequence for dynamic ads and product-level economics.

# Downstream

§16 (catalog), §17 (Advantage+ Shopping depends on matching), 18 and 158 (the product axis), 36.
