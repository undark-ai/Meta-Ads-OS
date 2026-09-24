---
name: shopify-extraction
description: When pulling revenue truth from the commerce platform for a Meta audit — orders, line items, margin inputs, new-vs-returning customer status, refunds and inventory. Use whenever a section needs banked revenue, contribution margin, new-customer CAC or SKU economics. This is the authoritative source for everything Meta can only claim.
---
# Commerce platform extraction

Meta is authoritative for media delivery. The commerce platform is authoritative for **money**.
Every economic conclusion in the audit resolves here, and three things exist nowhere else: banked
revenue, margin, and who was already a customer.

Written for Shopify; the same fields exist under different names in WooCommerce, BigCommerce and
the rest. Discover the actual schema rather than assuming.

## What to pull

| Data | Used by |
|---|---|
| Orders: id, created_at, total, subtotal, discounts, tax, shipping, currency | §3 reconciliation, §1 economics |
| Line items: SKU, variant, quantity, price, **unit cost** | §22 SKU economics, §1 margin |
| Customer id and **first-order flag** | §24 new vs returning, new-customer CAC |
| Refunds and returns, with dates | §1 return-adjusted margin |
| Landing site and referring site, or the UTM capture | §3, §2 link tracking |
| Discount codes applied per order | §21 realised discounting |
| Inventory levels | §16 out-of-stock exposure |
| Product catalog: titles, images, prices, availability | §16 feed inputs where the catalog is unreachable |

## Alignment for §3

Reconciliation fails on definitions far more often than on tracking. Before comparing to Meta:

- **Date basis.** Orders are dated when placed. Meta dates conversions and credits back to the
 click, up to the window length earlier.
- **Timezone.** The store's is frequently not the ad account's.
- **Gross vs net.** Decide whether tax, shipping and discounts are in, and apply the same choice
 to both sides.
- **Refunds.** The store nets them; Meta does not.
- **Order types.** POS, draft, subscription renewals and manual orders may be in the store total
 and not in anything Meta could have caused. Exclude them explicitly, and say what was excluded.
- **Population.** Meta's implied AOV compares against **Meta-attributed** orders, not all store
 orders. This is a common and wrong comparison.

## New vs returning

The single most valuable thing this source provides, and the one Meta cannot supply at all.

`new_customer_share` and `new_customer_cac` are null without this join — **never estimated**.
Every scale recommendation that depends on them says so.

The gap between blended CAC and new-customer CAC tells you how much of the account's "acquisition"
is buying back its own customers.

## Margin coverage

Unit cost is set per variant and is frequently incomplete. Report **coverage** — "cost set on 71%
of variants, representing 88% of revenue" — rather than silently averaging over the gaps. A margin
computed over 60% of revenue and presented as the account margin is an assumption wearing a
measurement's clothes.

## Returns lag

A 30-day window understates the return rate under a 60-day policy, which overstates margin on
recent cohorts — including exactly the cohorts a scale decision is being made on. Use a
completed-cohort return rate, by product, not the account average over the window.

## Where the platform is unreachable

Walk the ladder (`mcp-discovery`) before declaring it. Then:

- §3 cannot run, and every ROAS in the audit stays a platform claim. Say this at the top of the
 executive page, not in a data-limitations appendix.
- §1 margin falls to the user, or to a labelled assumption with sensitivity published.
- §24 new-vs-returning closes `BLOCKED`, and every new-customer figure is null.

The audit continues. Most of its findings never needed this source — but the ones that did must
say so rather than quietly substituting Meta's numbers.
