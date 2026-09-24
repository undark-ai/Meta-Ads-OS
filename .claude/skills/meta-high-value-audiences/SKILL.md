---
name: meta-high-value-audiences
description: "When the user wants to target high-LTV, VIP, or best-customer segments on Meta for an e-commerce or D2C brand — value-based customer-list seeds, value lookalikes, exclusion hygiene, tailored offers for top buyers, and incrementality measurement. Also use when the user mentions 'VIP audience,' 'high-LTV customers,' 'value-based lookalike,' 'best customers,' 'win-back campaign,' or 'targeting our top spenders.' For general audience building and validation, see meta-audience-strategy. For why Advantage+ can't lock to a VIP list, see meta-advantage-plus. For the e-commerce Meta hub, see meta-ads."
metadata:
 version: 1.1.0
---

<!-- execution-boundary: documents-writes -->
<!-- Names write tools without calling them: describes value-based audience builds, applied by the execution lane.
     Calling them is the execution lane's, under EXECUTION-PROTOCOL.md. -->

> **Marketing layer — advisory, not evidence.** Every benchmark, threshold and rule of thumb
> below is build-time guidance. Per `CLAUDE.md`, a marketing skill's number is never evidence
> for a quantified finding: a recommendation that originates here still needs a number, source,
> date range, formula, evidence class and confidence from the audit layer before it can be
> presented as one. Handoffs run audit → marketing, never the reverse.


# High-Value Audiences on Meta — D2C Playbook

Most prospecting chases any purchase. This playbook applies narrow, high-value targeting logic to e-commerce: identify your best-customer profile, find more of them, and run tailored campaigns for VIP acquisition, retention, and win-back — measured on LTV, not first-order ROAS.

## Before Starting

**Check for product marketing context first:**
If `.agents/product-marketing.md` exists (or `.claude/product-marketing.md`, or the legacy `product-marketing-context.md` filename, in older setups), read it before asking questions. Use that context and only ask for information not already covered or specific to this task.

Gather this context (ask if not provided):
- Customer count, LTV distribution (how concentrated is revenue in the top 10–20%?), and whether per-customer LTV is exportable
- Monthly Meta budget and whether purchase values flow back via CAPI

## When High-Value Targeting Makes Sense

**Use it when:**
- You have 1,000+ identifiable high-value customers (Meta needs seed volume; below ~500 matched, lookalikes get noisy)
- LTV is concentrated — top 10–20% of customers drive an outsized share of revenue (subscriptions, replenishment, high-AOV categories)
- You can pass **customer value** into Meta (LTV column on the list, or purchase values via CAPI)
- Repeat purchase or subscription behavior gives ads time to influence

**Skip it when:**
- Fewer than 500 matched high-value customers — the seed is too small; run broad and revisit later
- One-and-done product with flat LTV — plain acquisition is simpler and cheaper
- Budget < ~$3,000/month — you can't fund a segment layer and still exit learning on core prospecting

## Building the Seed: Define "High-Value"

Segment your customer base on three signals:
1. **Total spend / LTV** (top 10–20%)
2. **Repeat velocity** (bought again fastest)
3. **Retention** (still active; for subscriptions, longest tenure without churn)

Export with maximum identifiers (email, phone, name, zip, country) plus an LTV value column. Match rates on consumer emails are decent (30–60%); more identifiers → higher match. Refresh monthly — a stale VIP list decays fast. (Upload and maintain via the Meta Ads MCP: `ads_create_custom_audience`, `ads_update_custom_audience_users`, and `ads_get_custom_audience` to check match size.)

**Tiering:** if the base is large, split Tier A (top 5%, e.g. subscribers with 4+ orders) and Tier B (next 15%). Keep tiers in separate ad sets (ABO) so you control spend per tier and can compare quality.

## The Audience Plays

### 1. Value-based lookalikes (VIP acquisition)
Upload the high-LTV seed with the value column → build a 1% **value-based lookalike** → prospect against it with your premium positioning (hero bundles, full-price, quality-led creative — not discount hooks). Judge on 60/90-day LTV of acquired cohorts vs. broad-acquired cohorts, not first-order CAC alone. Expand to 2–3% once quality is proven.

### 2. VIP retention / cross-sell (targeting the list directly)
Target the high-value list itself for launches, replenishment reminders, limited editions, and loyalty perks. Objective: Sales, small budget, frequency-capped. Only fund this where email/SMS can't reach (unsubscribed, low open rates) — don't pay Meta for orders your owned channels get free.

### 3. High-value win-back
Seed: lapsed high-LTV customers (no order in 90–180 days, historical LTV in top tier). Tailored creative: what's new since they left, their category's best-sellers, a considered offer. Measure reactivation rate against a holdout — lapsed VIPs often return anyway.

### 4. High-AOV cart recovery
Retarget abandoned carts above a value threshold (e.g. cart value > 2× AOV) in their own ad set with stronger reassurance creative (reviews, guarantees, shipping/returns) — these carts justify dedicated spend that generic DPA underinvests in.

## Campaign Structure Rules

- **Keep high-value campaigns separate from broad prospecting.** Never mix — different logic, different KPIs, different offers.
- Use **manual campaigns with Advantage+ audience expansion OFF** for plays 2–4. Advantage+ treats every list as a suggestion and will expand beyond your segment; that defeats the point. Use Advantage+ only for play 1 at scale, with the list as a suggestion you accept expansion on (see meta-advantage-plus).
- ABO per tier for controlled spend; modest budgets ($50–150/day per segment is typical).

## Exclusion Hygiene (Non-Negotiable)

- Exclude **current VIPs** from acquisition and intro-offer campaigns — never show your best customers the new-customer discount
- Exclude **recent purchasers** (30–60 days) from win-back and retention pushes
- Exclude **active subscribers** from subscription-offer ads
- Sync suppression lists at least weekly; dirty exclusions burn budget, inflate ROAS, and erode trust with exactly the customers you can least afford to annoy

## Budget Priority by Customer-Value Tier

When you do split by value tier, weight the budget rather than dividing it evenly:

| Tier | Share of prospecting-adjacent budget | Why |
|---|---|---|
| VIP / high-LTV lookalike acquisition | 40–50% | The highest-return segment; more of these customers is the whole point |
| Mid-value acquisition | 20–30% | Volume, and the pool VIPs are eventually promoted from |
| One-time buyers (win-back, cross-sell) | 15–20% | Cheap incremental revenue, capped by list size |
| Prospect-only / cold non-buyers | 5–10% | Necessary for pipeline, lowest immediate return |

**Below a spend floor, don't split at all.** Splitting an account across four value tiers means four ad sets each fighting for 50 weekly conversions. Under roughly $10K/month on Meta, differentiate through **creative and offer** aimed at the high-value segment while keeping one consolidated ad set — the algorithm handles the allocation better than your structure will at that volume.

## Measurement

High-value plays need different KPIs than standard acquisition:

| Metric | What it measures | How |
|--------|-----------------|-----|
| Cohort LTV (60/90/365d) | Are VIP-lookalike customers actually worth more? | Compare vs. broad-acquired cohorts |
| Repeat rate by acquisition source | Quality of the lookalike | Order data, post-purchase survey |
| Reactivation lift | Win-back incrementality | 80/20 holdout, evaluate after 21+ days |
| New-vs-returning mix | Is spend acquiring or just harvesting? | Post-purchase survey + exclusion audit |

**Always run holdouts on retention and win-back** — a chunk of those purchases happen without ads. Send purchase values back via CAPI so the algorithm learns what a high-value conversion looks like, and don't trust last-click: retargeting your own VIPs will always look great in Ads Manager.

## Related Skills

- **meta-audience-strategy**: General audience building for e-commerce Meta — data hierarchy, seed rules, validation, and exclusions.
- **meta-advantage-plus**: Why Advantage+ expands beyond any list, and when automation beats manual for the acquisition play.
- **meta-ads**: The e-commerce Meta hub — campaign strategy, structure, and optimization across the full account.
- **meta-capi-and-events**: Wiring purchase values back to Meta so value-based optimization has real signal.
- **full-audit**: The evidence-graded audit lane — 30 sections against live account data, where these benchmarks get tested rather than assumed.
