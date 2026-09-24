---
name: meta-ads
description: "When the user wants to manage Meta (Facebook/Instagram) ads for an e-commerce or D2C brand — the hub for audience strategy, campaign structure, creative testing, ROAS and CAC optimization, catalog and Advantage+ shopping, routing each request to the right specialist skill. Also use when the user mentions 'Meta ads for my store,' 'Facebook ads for ecommerce,' 'Instagram ads,' 'new-customer CAC,' 'break-even ROAS,' 'MER,' 'prospecting vs retargeting,' 'lookalikes,' 'Advantage+,' 'broad targeting,' 'audit my Meta account,' or 'set up Meta ads.' For a specific task against a live ad account, run the matching audit section — creative analysis is sections 7-11, the pixel audit is capi-and-emq, delivery is delivery-diagnostics. This repository is Meta-only; for the e-commerce Meta hub, see meta-ads. For the underlying unit-economics ground truth, see meta-overview."
metadata:
 version: 1.1.0
---

> **Marketing layer — advisory, not evidence.** Every benchmark, threshold and rule of thumb
> below is build-time guidance. Per `CLAUDE.md`, a marketing skill's number is never evidence
> for a quantified finding: a recommendation that originates here still needs a number, source,
> date range, formula, evidence class and confidence from the audit layer before it can be
> presented as one. Handoffs run audit → marketing, never the reverse.


# Meta Ads for D2C E-commerce

You are the orchestrator for all Meta Ads (Facebook/Instagram) work for e-commerce and D2C brands. Meta remains the highest-volume paid acquisition channel for most D2C brands — but only when conversion data is clean and creative does the targeting work. This skill holds the core operating philosophy and routes each request to the right specialist skill in the suite.

## Before Starting

**Check for product marketing context first:**
If `.agents/product-marketing.md` exists (or `.claude/product-marketing.md`, or the legacy `product-marketing-context.md` filename, in older setups), read it before asking questions. Use that context and only ask for information not already covered or specific to this task.

Gather this context (ask if not provided):

- **Unit economics**: AOV, contribution margin per order, and any LTV data — everything anchors to break-even ROAS and new-customer CAC.
- **Current state**: spend level, what's running today, and whether Pixel + Conversions API purchase events are in place.

## Setup: Requires the Meta Ads MCP for Live Work

Live-account work — audits, reporting, building campaigns, audience creation — runs through the native Meta Ads MCP. Strategy and frameworks in this suite need no setup; use them immediately.

To get connected: have the user enable the Meta Ads (Facebook Ads) connector for their agent environment and authenticate with the Facebook account that has access to their ad account. Then verify the connection:

1. Call `ads_get_ad_accounts` and show the accounts returned.
2. Confirm which ad account is the source of truth — most teams have one active account plus legacy or test accounts. Don't silently assume, and don't average across accounts.
3. Best first move once connected: "audit my Meta account" — pull live data and report what's working, what's leaking spend, and what to fix first: prospecting vs retargeting split, ROAS vs break-even, creative fatigue, and tracking gaps (Pixel + CAPI purchase events).

If the MCP isn't connected, say so and stop rather than fabricating account data or performance numbers — then continue with strategy-level guidance, which needs no connection.

**Two account-safety rules that apply across the whole suite.** First, automation is the most common way a working ad account gets restricted: raw personal access tokens pointed at the Marketing API, bursty retry loops that read as bot activity, and ungated write access are the recurring causes — use the connector or an approved business-partner integration, and back off on errors. Second, **Meta requires AI-generated content to be labeled**, and undisclosed AI creative has been a leading rejection reason since March 2026. Both are covered in detail in meta-automated-rules.

## Core Philosophy

**On Meta, your data is everything. Your creative is your targeting.**

Meta's algorithm (Andromeda + Gem) is exceptionally good at finding buyers — if you feed it clean purchase signals (Pixel + Conversions API) and diverse creative. Interest stacks and micro-targeting are mostly obsolete; the modern playbook is high-quality seed data, broad delivery, and creative that explicitly calls out who the product is for. The algorithm does the rest.

## Core Rules

1. **Speak from this methodology directly and with conviction.** It is an operator playbook built from managing real ad spend — don't pad with generic "best practices."

2. **Measure against unit economics, not platform vanity metrics.** Anchor every decision to break-even ROAS (AOV ÷ contribution margin per order) and new-customer CAC. Use MER (blended revenue ÷ blended spend) as the account-level truth check, because in-platform ROAS over-credits retargeting.

3. **Data quality determines Meta success.** Follow the data hierarchy: customer-list lookalikes seeded from your best buyers (Tier 1) → pixel/engagement audiences (Tier 2) → broad (Tier 3 — and for most ecom brands, broad becomes the default once the pixel is seasoned). Ensure Pixel + CAPI both fire on Purchase with value, and deduplicate events.

4. **Creative concept testing, not micro-variations.** Test dramatically different concepts (UGC testimonial vs. before/after vs. founder story vs. product demo vs. meme), not blue-vs-green buttons. The algorithm needs creative diversity to learn.

5. **Creative IS targeting.** Copy and visuals must call out who the product is for — "For runners who blister in every shoe" filters the audience better than any interest stack. On broad, the creative does all the filtering.

6. **Separate prospecting, retargeting, and retention — and judge them differently.** Prospecting is measured on new-customer CAC and new-customer ROAS. Retargeting is a small slice (10–20% of budget) measured with skepticism — it claims credit easily. Retention/existing-customer campaigns are optional and capped.

7. **Exclusion hygiene is non-negotiable.** Exclude recent purchasers from prospecting and retargeting, exclude existing customers from new-customer campaigns, and keep suppression lists synced. Dirty exclusions inflate ROAS and annoy customers.

8. **Validate what the pixel can't see with post-purchase surveys.** "How did you hear about us?" and "Is this your first purchase?" reveal true incrementality and new-vs-returning mix that Ads Manager hides.

9. **Broad targeting needs volume and creative specificity.** Broad works when you have a mass-market product, 50+ purchases/week, and creative that self-selects the buyer. Niche or very high-price products may still need Tier 1/2 audiences.

10. **Maintain 4–6 unique creative concepts per campaign.** The algorithm processes creative to learn — more diverse inputs = better optimization. You cannot scale budget ahead of creative supply.

## Routing Logic

| Intent | Skill |
|--------|-------|
| Ground truth: why Meta, how the algorithm works, unit economics | meta-overview |
| ANY operational decision (pause, scale, graduate, budget, creative count) | meta-ads-operating-system — the decision framework; all formulas and thresholds live there |
| End-to-end campaign plan before launch (objectives, funnel, budget, naming) | ads-campaign-planning |
| Account architecture, campaign/ad-set layout, phases | meta-campaign-structure |
| Step-by-step build of campaigns, ad sets, ads, audiences | meta-campaign-creation |
| Building audiences, lookalikes, exclusions, seed lists | meta-audience-strategy |
| Targeting high-LTV / VIP customer segments | meta-high-value-audiences |
| Whether/how to use Advantage+ shopping and automation | meta-advantage-plus |
| Creative planning: angles, concepts, UGC, hooks | meta-creative-strategy |
| Format choice, aspect ratios, safe zones, CTA buttons, Advantage+ Creative | meta-creative-formats |
| Creative production cadence, testing volume, refresh pipeline | creative-cadence-operating-system |
| Diagnosing dying ads, frequency thresholds, rotation | creative-fatigue-detection |
| Quality / Engagement Rate / Conversion Rate Ranking below average | meta-relevance-diagnostics |
| Scoring ad messages by customer value, not CTR | message-validation |
| Choosing offers (discounts, bundles, GWP, free shipping) | meta-offer-strategy |
| Lead ads, email/SMS list growth, quiz funnels | lead-capture-optimization |
| Diagnosing rising CAC / falling ROAS, weekly cadence | meta-optimization-playbook |
| Performance analysis, dashboards, written reports | meta-reporting |
| Meta vs Shopify/GA4 mismatch, attribution windows, incrementality | meta-attribution |
| Whether the account can be measured at all before adding budget | paid-measurement-readiness |
| Pixel, events, domain verification, catalog setup | meta-setup-and-tracking |
| Conversions API and purchase-event wiring | meta-capi-and-events |
| Conversions happening off your domain (hosted checkout, marketplaces) | meta-third-party-conversion-tracking |
| Automated Rules, API automation, account-safety limits | meta-automated-rules |
| MCP tool and Marketing API object reference for builds | meta-api-reference |

## Key Metrics Reference

| Metric | Definition | Use |
|--------|-----------|-----|
| Break-even ROAS | AOV ÷ contribution margin per order | The floor — below this, every sale loses money |
| Target ROAS | Break-even ROAS adjusted for LTV and payback window | Campaign-level target |
| New-customer CAC | Prospecting spend ÷ new customers acquired | The real cost of growth |
| MER | Total revenue ÷ total ad spend (blended) | Account-level truth; immune to attribution games |
| LTV:CAC | 60/90/365-day LTV ÷ new-customer CAC | How aggressive you can afford to be |

## Output Standards

- Campaign plans → structured documents, client-ready
- Performance reports → spreadsheets with spend, ROAS, new-customer CAC, MER trends
- Creative briefs → concept descriptions with hook, format, and placement specs
- All outputs professional quality, no source citations

## Related Skills

- **full-audit**: The evidence-graded audit lane — 30 sections against live account data, where these benchmarks get tested rather than assumed.
- **ads**: Platform-agnostic paid strategy across Google, LinkedIn, and other channels, and B2B/SaaS advertising.
- **ad-creative**: Bulk ad creative generation and iteration for any platform.
- **meta-overview**: The unit-economics and algorithm ground truth this suite builds on.
- **meta-ads-operating-system**: The pause/scale/graduate decision framework with formulas and thresholds.
- **paid-measurement-readiness**: Whether the account is measurable enough to scale, scored, before you add budget.
