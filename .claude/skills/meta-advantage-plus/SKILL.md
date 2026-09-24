---
name: meta-advantage-plus
description: "When the user is deciding whether and how to use Advantage+ shopping campaigns for an e-commerce or D2C brand — what to let Meta automate, what to constrain, existing-customer budget caps, and when manual campaigns beat automation. Also use when the user mentions 'Advantage+,' 'ASC,' 'Advantage Plus shopping,' 'automated campaigns,' 'should I let Meta automate,' or 'manual vs automated targeting.' For the e-commerce Meta hub, see meta-ads. For locked VIP-segment targeting that Advantage+ cannot do, see meta-high-value-audiences. For building the audiences you feed it, see meta-audience-strategy."
metadata:
 version: 1.1.0
---

<!-- execution-boundary: documents-writes -->
<!-- Names write tools without calling them: describes the audience and campaign builds an ASC transition needs.
     Calling them is the execution lane's, under EXECUTION-PROTOCOL.md. -->

> **Marketing layer — advisory, not evidence.** Every benchmark, threshold and rule of thumb
> below is build-time guidance. Per `CLAUDE.md`, a marketing skill's number is never evidence
> for a quantified finding: a recommendation that originates here still needs a number, source,
> date range, formula, evidence class and confidence from the audit layer before it can be
> presented as one. Handoffs run audit → marketing, never the reverse.


# Advantage+ for D2C E-commerce on Meta

How to use Meta's Advantage+ automation for e-commerce sales. Covers when to use Advantage+ shopping vs. manual campaigns, setup, budget requirements, and how it interacts with new-customer goals.

## Before Starting

**Check for product marketing context first:**
If `.agents/product-marketing.md` exists (or `.claude/product-marketing.md`, or the legacy `product-marketing-context.md` filename, in older setups), read it before asking questions. Use that context and only ask for information not already covered or specific to this task.

Gather this context (ask if not provided):
- Weekly purchase volume, monthly Meta budget, and target CPA / break-even CAC
- Tracking state: Pixel + CAPI firing on Purchase with values, and whether a product catalog exists

## What Changed: Andromeda to Advantage+

Meta's Andromeda algorithm (2024–2025) changed how ads are delivered. Before, manual targeting (interests, demographics, stacked lookalikes) was the primary lever. After, creative quality and conversion signals matter more than targeting — the algorithm finds your buyer if your creative resonates and your tracking is clean.

**The game shifted from "who do I target" to "what creative do I feed the algorithm, and what purchase data do I send back."** Advantage+ is Meta's product layer on Andromeda: it automates targeting, placements, creative optimization, and budget allocation.

## The Four Layers

1. **Advantage+ Audience** — your custom audiences and lookalikes become suggestions, not hard limits. Meta expands beyond them when it predicts better performance. You cannot lock it to a list.
2. **Advantage+ Placements** — automatic placement optimization across Facebook, Instagram, Reels, Audience Network.
3. **Advantage+ Creative** — AI variations of your assets: backgrounds, text overlays, aspect ratios, music, per-placement adjustments.
4. **Advantage+ Shopping Campaigns (ASC)** — full automation for sales: targeting, budget, creative, placements, with catalog integration and an **existing-customer budget cap** (define your customer list, cap the share of spend that reaches them — typically 10–20%; 0% if acquisition-only).

## When to Use Advantage+ vs Manual

**Use Advantage+ (ASC) when:**
- 50+ purchases/week (the algorithm needs data)
- Budget $2,000+/month minimum; $5,000+ for reliable results
- Pixel + CAPI both firing on Purchase with values, deduplicated
- Goal is scaling proven products/offers, not testing new ones
- You have 5+ diverse creative assets and (ideally) a clean product catalog
- You're doing broad acquisition, not tight segment targeting

**Use manual campaigns when:**
- Early testing of new offers, audiences, or creative concepts (you need clean reads)
- Purchase volume < 50/week (high-AOV or niche products)
- You need strict audience control — VIP/high-LTV segment plays, retention offers, launch sequencing (ASC expands beyond any list; see meta-high-value-audiences)
- You need granular reporting by segment
- Fewer than 3 creative variations

**The hybrid (recommended):**

```
Manual campaigns — "where you learn"
 Audience validation (ABO), new concept testing,
 retargeting with specific windows, VIP-segment offers

Advantage+ Shopping — "where you earn"
 Scale proven offers with best-performing creative + catalog
 Existing-customer cap set; new-customer CAC as the KPI
```

Transition trigger: winning offer + validated creative + 50+ purchases/week → move scale to ASC.

### Budget Floor for Advantage+

Advantage+ needs conversion volume to work at all. From the ~50-events-per-week learning requirement:

| Target CPA | Minimum daily | Minimum weekly |
|---|---|---|
| $20 | ~$143 | ~$1,000 |
| $50 | ~$357 | ~$2,500 |
| $100 | ~$714 | ~$5,000 |

Below the floor, Advantage+ underperforms a manual campaign because it never leaves learning. **If you can't hit ~50 purchases a week**, the options are: optimize to a shallower event (AddToCart or InitiateCheckout) and accept a looser signal, retarget converters to build purchase volume first, or consolidate ad sets so the events concentrate. Do not simply run Advantage+ at half the floor and conclude automation doesn't work.

### The Red Flag: ASC Against Your Own Manual Campaign

**Running an Advantage+ Shopping campaign and a manual Shopping/catalog campaign against the same catalog is self-competition.** Both draw from the same audience for the same products, so you bid against yourself, raise your own CPMs, and split the conversion signal across two campaigns that each then struggle to leave learning. This is the single most common Advantage+ mistake in D2C accounts and it looks like "Advantage+ isn't working."

If you want both, separate them by product set — ASC on the core catalog, manual on a launch or a specific collection — with no overlap. Otherwise pick one.

### Advantage Custom vs Advantage Lookalike Audience

Two distinct behaviours that get conflated:

- **Advantage Custom Audience** — Meta expands *beyond* your uploaded or website custom audience when it finds better prospects outside it. In Advantage+ Shopping mode this **cannot be turned off**. Your audience is a suggestion, not a boundary.
- **Advantage Lookalike Audience** — you set 1%, and Meta may deliver into 3–5% if results hold there. It respects your seed but widens the ratio.

The practical consequence: an exclusion is far more reliable than an inclusion under Advantage+. If you need someone kept out, exclude them explicitly — don't rely on them being absent from your included audience.

## Setup (Step by Step)

1. Ads Manager → Create → **Sales** objective (defaults to Advantage+)
2. Conversion: website Purchase (Pixel + CAPI); connect the product catalog if you have one
3. Budget: CBO; minimum = (Target CPA × 50) ÷ 7 per day
4. Audience: provide customer lists and lookalikes as **suggestions** (create and sync them via the Meta Ads MCP: `ads_create_custom_audience`, `ads_update_custom_audience_users`); set the **existing-customer budget cap** using your synced customer list
5. Geo required; leave age/gender open unless you have data proving a segment never converts
6. Creative: 5–10 proven assets + catalog; enable Advantage+ Creative
7. Launch, wait 7 days, then judge on new-customer CAC — not in-platform ROAS alone (verify against MER and post-purchase survey first-purchase rate)

## Guardrails

- **All audiences are suggestions.** Uploaded lookalikes are starting signals; retargeting lists get served first, then Meta expands. If you need a locked audience, use a manual campaign with Advantage+ audience OFF.
- **"Further limit reach" filters:** use only with data proving a segment never buys, or for compliance. Guessing here slows learning and usually hurts performance.
- **Campaign Score:** 70+ generally means you're not fighting the algorithm — but don't optimize for the score. A 60 with profitable new-customer CAC beats a 90 full of existing-customer repeat orders.
- **Watch the new-customer mix.** ASC will happily harvest easy repeat purchases if the cap is loose. Audit the split monthly.

## Performance Expectations

Meta's own testing shows Advantage+ delivering meaningfully lower cost per result than manual targeting (roughly 20–30% in published tests), and CBO beating ABO on cost per conversion at scale. Independent results vary by category and price point — always A/B ASC against your best manual structure in your own account before shifting the majority of budget.

## Related Skills

- **meta-audience-strategy**: Seeds, exclusions and the audience quality validation that decides what Advantage+ gets to expand from.
- **meta-ads**: The e-commerce Meta hub — campaign strategy, structure, and optimization across the full account.
- **meta-high-value-audiences**: Locked VIP/high-LTV segment plays that must stay manual because ASC expands beyond any list.
- **meta-audience-strategy**: Building the customer-list seeds and lookalikes you feed ASC as suggestions.
- **meta-capi-and-events**: The Pixel + CAPI purchase signal ASC depends on to optimize toward real value.
- **full-audit**: The evidence-graded audit lane — 30 sections against live account data, where these benchmarks get tested rather than assumed.
