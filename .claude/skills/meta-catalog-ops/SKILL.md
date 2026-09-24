---
name: meta-catalog-ops
description: When fixing a Meta product catalog on a live account under the execution protocol — feed rules, product updates, product sets and event-source connections. Use in an execution run when the user asks to "fix my catalog," "update product data," "create a product set," or "connect the pixel to the catalog." Execution lane only. For diagnosing what is wrong with the catalog, see the catalog section of full-audit.
lane: execution
---
# Catalog operations

Load `meta-execution-protocol` first.

Catalog work has a property the rest of the lane does not: **the catalog is usually downstream of
something else.** Fixing a product in Meta while the source feed keeps overwriting it produces a
fix that survives until the next sync, and an audit trail that says the problem was fixed.

## Fix the source, not the symptom

Before any catalog write, establish where the data comes from:

- A Shopify or platform sync → **fix it there.** A Meta-side product update will be overwritten.
- A scheduled feed file → fix the feed, or add a feed rule.
- Manual upload → the Meta-side fix is the real fix.

Where the source is not writable by this session, the deliverable is a recommendation for
whoever owns it — not a Meta-side patch that masks the problem for a day.

## Feed rules

`ads_catalog_create_feed_rule` transforms data at ingestion. Useful and quietly dangerous:

- A rule applies to **every** matching product, including ones nobody checked.
- Rules stack, and interactions are not obvious. Adding a second rule to fix the first one's side
  effect is how a feed becomes unmaintainable.
- Preview the affected product count before creating. A rule intended for 40 products that
  matches 4,000 is caught here or not at all.
- Log the rule id. `ads_catalog_product_feed_delete_rule` is the rollback, and it needs the id.

## Product updates

`ads_catalog_update_product` for individual corrections. Batch carefully:

- Capture before values per product. A bulk update with no before state has no rollback.
- Availability and price are the two fields most likely to be re-synced from source within hours.
- Title and description changes affect dynamic-ads relevance; they are creative changes wearing a
  data-field costume, and deserve the same review window.

## Product sets

`ads_catalog_create_product_set` is low-risk and high-value: it is how margin-aware segmentation
reaches Advantage+ Shopping and dynamic ads. A set built on the account's actual contribution
data (§22) rather than on category is one of the more useful changes this lane makes.

Check `ads_catalog_get_product_set_products` after creation. A set whose filter matched nothing
looks successful in the response.

## Deletions

`ads_catalog_delete_product` and `ads_catalog_product_set_delete` are last resorts with named
justification. A product deleted from the catalog loses its performance history and its
associations, and "tidying up" is not a justification.

Prefer excluding a product from a set over deleting it from the catalog.

## Event source connections

`ads_catalog_event_source_connect|disconnect` links the pixel to the catalog. Connecting is
usually correct and usually the fix for a dynamic-ads problem. **Disconnecting breaks dynamic
ads and retargeting immediately** — it is not a reversible experiment, because the matching
history does not come back with the connection.

## Rollback

Weaker here than elsewhere, and the plan must say so: feed rules can be deleted, product updates
can be reversed if before values were captured, and deletions and disconnections largely cannot.
That asymmetry is the reason for the fix-the-source rule at the top.
