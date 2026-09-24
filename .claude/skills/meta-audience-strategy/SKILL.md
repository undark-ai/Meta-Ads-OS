---
name: meta-audience-strategy
description: "When the user wants to build audiences for e-commerce or D2C Meta ads — customer-list lookalikes, value-based seeds, pixel and engagement audiences, broad targeting, exclusions, and audience quality validation. Also use when the user mentions 'lookalike audience,' 'custom audience,' 'seed audience,' 'value-based lookalike,' 'broad targeting,' 'audience exclusions,' or 'who should I target on Facebook.' For the e-commerce Meta hub, see meta-ads. For high-LTV and VIP segment plays, see meta-high-value-audiences. For Meta audience strategy, see meta-audience-strategy."
metadata:
 version: 1.1.0
---

<!-- execution-boundary: documents-writes -->
<!-- Names write tools without calling them: describes how audiences get built, applied by the execution lane.
     Calling them is the execution lane's, under EXECUTION-PROTOCOL.md. -->

> **Marketing layer — advisory, not evidence.** Every benchmark, threshold and rule of thumb
> below is build-time guidance. Per `CLAUDE.md`, a marketing skill's number is never evidence
> for a quantified finding: a recommendation that originates here still needs a number, source,
> date range, formula, evidence class and confidence from the audit layer before it can be
> presented as one. Handoffs run audit → marketing, never the reverse.


# Audience Strategy for D2C Meta Ads

Meta's algorithm is powerful at finding buyers — but only if you feed it high-quality seed data and clean purchase signals. Your data quality determines everything; your creative does the rest of the targeting work.

## Before Starting

**Check for product marketing context first:**
If `.agents/product-marketing.md` exists (or `.claude/product-marketing.md`, or the legacy `product-marketing-context.md` filename, in older setups), read it before asking questions. Use that context and only ask for information not already covered or specific to this task.

Gather this context (ask if not provided):
- Customer base size and whether order history is exportable (with LTV per customer)
- Pixel maturity — weekly purchase volume and how long it has been collecting data

## Start With Customer Intelligence (Before Touching Ads Manager)

**Survey and interview existing customers:** why they bought (trigger, problem, occasion), what made them hesitate (address it in ad copy and landing pages), where they discovered you (validates channel mix). Post-purchase surveys are the cheapest, highest-signal research tool in ecom.

**Segment your best customers.** Build seed audiences from customers who:
1. **Spent the most** (highest AOV / total revenue)
2. **Bought again fastest** (shortest time to second purchase)
3. **Stayed longest** (highest LTV, most orders)

These three signals identify your top ~5% of buyers. Your targeting strategy should start with finding more of THESE people, not more people in general. Land the most in-market segment first; expand to colder tiers once it's saturated (typically after ~12 months of focused prospecting).

**The other 5%: only a fraction of your market is in-market right now.** At any given moment roughly 5% of the people who could buy your product are actually shopping for it. Early prospecting is efficient because you are harvesting that band. It is also why efficiency degrades as you scale — around the 12-month mark you have worked through the in-market share of your addressable audience, and further growth means paying to reach people who are not shopping yet. That is a *creative* problem (demand creation, see `ads/references/d2c-paid-playbook.md`), not an audience problem, and no lookalike percentage solves it. Plan for the transition rather than discovering it as a CAC cliff.

**Build audiences from what the platform actually offers.** Before writing an audience spec, open Ads Manager and draft a campaign. Write down only the attributes you can genuinely target, not the ones your persona document describes. A persona built from customer research and an audience built from available targeting options are two different artifacts, and conflating them produces specs nobody can implement.

## The Data Hierarchy

### Tier 1: First-Party Customer Data (Start Here)

Your order history is your highest-quality data source.

**How to build customer-list lookalikes:**
1. Export best customers using the segmentation above (include email, phone, name, zip — more identifiers = higher match rate)
2. Upload as a Custom Audience with **customer value** (LTV column) so Meta can build value-based lookalikes (via the Meta Ads MCP: `ads_create_custom_audience`, then `ads_update_custom_audience_users` to add members)
3. Build a 1% value-based lookalike from that seed
4. Validate quality (below), then expand to 2–3%

Rules for seed lists: feed Meta the cream of the crop — better data in = better lookalikes out. If the list is large enough (1,000+), segment by product line, AOV tier, or repeat status. Don't dilute the seed with one-time discount buyers. Refresh monthly (check size and freshness with `ads_get_custom_audience`).

**Sizing and match rate.** 1,000+ matched records is the practical floor for a usable lookalike seed; 100 is Meta's hard minimum and produces a lookalike not worth running. Match rate rises sharply with identifier count — email plus phone plus name matches far better than email alone, and every D2C checkout already captures all three.

**Static seeds decay; rolling seeds don't.** This distinction decides your maintenance workload:

| Seed type | Refresh |
|---|---|
| Uploaded customer file | **Rebuild every 60–90 days.** The list is a snapshot; it ages out of relevance as the customer base changes |
| Pixel/CAPI-sourced rule ("purchasers, last 180 days") | Self-refreshing. No manual rebuild — the rule re-evaluates continuously |

Prefer rolling sources where the rule can express what you want. Reserve uploaded files for what the pixel can't see: LTV tiers, subscription status, wholesale flags, survey-attributed cohorts.

**Rebuild when the business changes, not on a calendar.** A new product line, a price repositioning, or a shift in the conversion mix invalidates a seed faster than any elapsed-time rule. A quarterly refresh with no thought behind it is a ritual.

**Engagement audiences are not bottom-funnel.** Video viewers and page engagers are early- to mid-funnel pools. Treating them as retargeting audiences — same urgency, same offer as a cart abandoner — burns budget on people who have shown interest in content, not in buying.

### Tier 2: Pixel and Engagement Audiences

When the customer list is small or new: purchasers (pixel, 180d) as seed; add-to-cart and checkout initiators for retargeting; Instagram/Facebook engagers and 50%+ video viewers as cheap warm pools. These are weaker seeds than paid customers but useful for young brands and for retargeting structure.

### Tier 3: Broad Targeting

Broad lets the algorithm find your buyer from creative signals and pixel history rather than explicit targeting. Post-Andromeda (2024–2025), broad is the end state for most ecom accounts — but earn it:

**Broad works when:** the product has mass-market appeal, the pixel is seasoned (50+ purchases/week), and the creative is highly specific about who it's for ("For side sleepers who wake up with neck pain" filters better than any interest). The creative acts as repellent for non-buyers.

**Broad struggles when:** very niche or very high-priced products, cold pixel, or thin creative volume. There, Tier 1/2 seeds still outperform on new-customer CAC.

## Audience Validation

Before scaling any audience, validate it — in your order data, not Ads Manager.

**Setup:** one ABO campaign, Sales objective, one ad set per audience source (1% value lookalike / engagement / broad), the SAME 3–4 ads in every ad set, equal budgets, 2–4 weeks.

**What to check per ad set:**
- New-customer rate (post-purchase survey: "Is this your first purchase?")
- AOV and contribution margin per order (is one audience full of sale-item hunters?)
- Discount-code usage rate
- Early repeat signal / 60-day LTV by acquisition audience

Kill ad sets that deliver cheap-but-worthless orders. Take the winner into CBO creative scaling (see meta-campaign-structure).

## Exclusion Hygiene

Always exclude, everywhere it applies:
- **Recent purchasers** (30–60 day suppression) from prospecting and retargeting
- **Existing customers** from any campaign judged on new-customer CAC
- **Subscribers/members** from acquisition offers they already have
- Refresh synced lists at least weekly

Dirty exclusions inflate ROAS, waste budget, and serve intro offers to loyal customers.

### The Five Exclusion Layers

| Exclusion audience | Built from | Applied to |
|---|---|---|
| Existing customers | Uploaded customer file plus pixel purchasers | All prospecting, and anything judged on new-customer CAC |
| Subscribers and members | Email/SMS list, membership flag | Acquisition offers they already qualify for |
| Same-SKU purchasers | Pixel Purchase with `content_ids` | Dynamic and catalog retargeting for that SKU |
| Lookalike source members | The seed audience itself | The lookalike built from it |
| Negative placements | Placement performance data | Ad sets where a placement is sustainedly above campaign-average CPA |

**Match the exclusion window to the repurchase cycle, not to a round number.** For a consumable on a 45-day cycle, an all-time purchaser exclusion permanently removes your best repeat buyers from every campaign; a rolling 30–45 day exclusion suppresses them while they still have product and re-includes them exactly when they're ready to reorder. All-time exclusions are right for durables and wrong for consumables and subscriptions, and most accounts use the same setting for both.

**Cross-sell into a different category is fine. The same SKU is not.** Excluding purchasers from the *product* they bought is essential; excluding them from the whole catalog throws away the cheapest revenue you have.

### Exclusion Audit

Five checks, in this order:

1. Does **every** prospecting campaign carry a customer exclusion? One missing ad set is enough to distort account-level new-customer CAC.
2. When was each exclusion audience **last updated**? A customer list that stopped syncing three months ago reads as present and is functionally absent. This is the check nobody runs.
3. Are purchase exclusions applied at **product level**, not only account level, wherever dynamic retargeting runs?
4. Are any **placements** running sustainedly above 2× campaign-average CPA?
5. Is the refresh **automated**? A manual weekly sync is a manual weekly failure.

### Audience Overlap

Overlap is the Meta equivalent of keyword cannibalization: your own ad sets bidding against each other, raising your CPMs with your own budget.

| Overlap | Read |
|---|---|
| Under 10% | Negligible. Ignore |
| 10–20% | Watch. Note it, don't restructure |
| 20–30% | Consolidate or add exclusions |
| Over 30% | Severe. Actively wasting budget |

**The tool has a blind spot.** Meta's overlap comparison only works across *saved* audiences, so on broad targeting and Advantage+ campaigns — where most modern D2C spend lives — it can tell you nothing. There you read overlap from proxy signals:

- Frequency rising across several ad sets at the same time
- CPM climbing broadly with no seasonal or competitive explanation
- Several ad sets simultaneously under-delivering relative to their budgets

**Costing it.** Compare a suspect ad set's CPM against a comparable non-overlapping ad set — same objective, similar audience size, same period. The CPM delta multiplied by impressions approximates the wasted spend, which is the number that gets a restructure approved.

**When overlap is fine:** sequential funnel stages targeting the same people deliberately at different depths; cells of a running Experiments test; and a short-lived 1%/2%/5% lookalike ladder built on purpose to find the efficiency edge. Overlap is only a problem when it's unintentional.

## Offer Strategy for Cold Audiences

The offer affects both volume and quality of the signal:
- **Good for cold traffic:** hero product at full price with strong creative, best-seller bundles, sitewide-relevant first-order offer
- **Risky for cold traffic:** deep discounts (train the algorithm to find deal-seekers; watch repeat rate), niche SKUs with tiny appeal (too few purchases to validate statistically)
- Match the landing page to the ad's promise — the audience the algorithm learns from is the audience that converts on that page.

## Related Skills

- **meta-ads**: The e-commerce Meta hub — campaign strategy, structure, and optimization across the full account.
- **meta-high-value-audiences**: High-LTV, VIP, and best-customer segment plays with value lookalikes and incrementality measurement.
- **meta-campaign-structure**: Where validated audiences slot into account architecture, budgets, and the scaling roadmap.
- **full-audit**: The evidence-graded audit lane — 30 sections against live account data, where these benchmarks get tested rather than assumed.
- **ads**: Platform-agnostic paid strategy, including audience targeting across Google, LinkedIn, and other channels, and the D2C paid playbook reference.
- **meta-advantage-plus**: Advantage Custom and Advantage Lookalike behaviour when Meta is allowed to expand past your audience.
- **meta-attribution**: Measuring whether an audience is incremental rather than just cheap.
