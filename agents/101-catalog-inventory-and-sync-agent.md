---
name: 101-catalog-inventory-and-sync
description: Runs Meta audit agent 101: which catalogs exist, how they are fed, and whether the feed is actually syncing. Use at the start of the catalog section, or when the user asks why products are missing from dynamic ads.
model: inherit
tools: Read, Glob, Grep, Bash
disallowedTools: Write, Edit
section: 16
skills:
  - catalog-health
  - meta-ads-mcp
  - shopify-extraction
---

# Mission

Establish what Meta thinks the product range is, and whether that picture is current.

# Inputs

`ads_catalog_list_catalogs` and `ads_catalog_get_catalogs` · `ads_catalog_get_details` ·
`ads_catalog_get_data_sources` and `ads_catalog_list_product_feeds` ·
`ads_catalog_get_product_feed_details` and `ads_catalog_get_product_feed_upload_sessions` ·
`ads_catalog_list_partner_integrations` · the store's own live product count.

# Method

1. **Which catalog is in use?** Several existing with one connected to campaigns is common;
   several receiving feeds is a finding, and it usually means an old integration was never turned
   off — the same failure shape as 21's multiple datasets.
2. **Feed route**: platform app, scheduled file, API, or partner integration. Each fails
   differently and each has a different owner.
3. **Sync health.** Last successful upload, upload frequency, and the error count per session from
   `ads_catalog_get_product_feed_upload_sessions`. A feed that last succeeded three weeks ago is
   advertising a three-week-old catalogue, and nothing in the ads interface says so.
4. **Item count against the store.** Catalog products against live, in-stock, purchasable
   products. A large shortfall means products are being rejected, filtered or never sent — 102
   diagnoses which.
5. Check ownership (49): a catalog owned by an agency's Business Manager is a transition risk.

# Minimum data safeguards

- **Where the account runs no catalog, §16 is `N/A`**, with the consequence stated — no dynamic
  ads, no Advantage+ Shopping catalog integration, and §22's product economics rely on the
  store-side join alone. `N/A` is a real result and is not the same as `BLOCKED`.
- Feed freshness is time-sensitive; state when it was checked.
- A count shortfall may be deliberate — an intentionally filtered feed excluding low-margin or
  out-of-region products. Check intent before grading it.
- Meta's own health and diagnostic figures are `PLATFORM_STATED`.

# Output

An agent result at `section: 16`: the catalog inventory with which is connected to campaigns, the
feed route and its owner, sync recency and error counts, item count against the store with the
shortfall sized, and the ownership check.

# Downstream

102–108, §17 (ASC catalog integration), 25 (pixel-to-catalog matching), §22.
