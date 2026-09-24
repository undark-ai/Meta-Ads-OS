---
name: catalog-health
description: When auditing a Meta product catalog and dynamic ads — feed sync health, product diagnostics, disapprovals, item ID stability, price parity against the live site, and product-set coverage. Use when the user asks "audit my catalog," "why are my dynamic ads not delivering," "product feed errors," "DPA isn't working," or "catalog diagnostics." Only applies to accounts running a catalog; confirm one exists before starting.
---
# Catalog health

Catalog problems are invisible in standard ad metrics. An ad looks low-spend or "just not
delivering" when the real cause is a third of the catalog disapproved or a product set that has
quietly gone empty. The campaign keeps running and stops working.

**Confirm a catalog exists first.** If none does, §16 closes `N/A` — and whether the account
*should* have one is a separate finding, often a good one.

## The five checks, in order

1. **Catalog and ownership** — which catalog, which business owns it, and is it the one actually
   driving live ads. More than one is common after an agency handover; ask which is canonical
   rather than auditing the wrong one.
2. **Feed sync health** — last successful upload, error and warning counts on the most recent
   session.
3. **Product diagnostics** — disapproved and flagged products, missing required fields, by
   category.
4. **Dynamic ads health** — is the catalog correctly connected to the pixel/dataset and the event
   set driving it.
5. **Product set coverage** — are the sets actually in use non-empty and current.

## The three that break campaigns silently

These are worth more than the diagnostics dashboard, because none of them raises an error.

**Item ID stability across feed generations.** If item IDs change when the feed regenerates — a
platform migration, an app change, a SKU renumbering — Meta treats every product as new. Social
proof resets to zero and every dynamic retargeting audience keyed to those IDs empties. Nothing
errors. Compare item IDs across **two** feed generations, not within one.

**Price parity against the live site.** A feed price disagreeing with the site price is both a
conversion killer — the buyer sees a different number on arrival — and a policy risk. Spot-check a
sample against the live product page, not against the feed's own metadata, which will happily
agree with itself.

**Feed error trend, not snapshot.** Forty errors means nothing without direction. Forty that were
four last month is a broken sync. Forty that have been forty for a year is a stable set of
discontinued SKUs someone should tidy. Always report the trend.

## Quantify by share, not count

"340 of 1,200 products missing GTIN, concentrated in one category" is a finding. "Some products
have issues" is not. Report the count **and** the share of catalog affected per issue category —
and where possible, the share of *spend* flowing to affected products, since a disapproved product
nobody advertises costs nothing.

## Red flags worth naming

| Check | Flag |
|---|---|
| Last successful upload | Over 48 hours old for a feed expected to run daily |
| Upload sessions | A "succeeded" session with a high warning count nobody reviewed |
| Multiple active catalogs | Ambiguity about which drives live ads |
| Product sets | A set whose filter now matches nothing — it looks configured and delivers nothing |
| Out-of-stock | Products still receiving spend while unavailable (cross-check §16 against inventory) |
| Pixel↔catalog matching | `content_ids` in the purchase event not matching catalog item IDs — dynamic retargeting cannot work without it |

That last one bridges to §2: a catalog can be perfect and dynamic ads still fail because the pixel
sends a SKU where the catalog holds an item ID. Check both sides of the join, not just the catalog.

## Output

For §16: the five checks with their state, issues quantified as share of catalog and share of
spend, the three silent breakers explicitly checked and reported even when clean, and the
recommendation routed to wherever the data actually originates — usually the commerce platform,
not Meta. A Meta-side product edit that the next sync overwrites is not a fix.
