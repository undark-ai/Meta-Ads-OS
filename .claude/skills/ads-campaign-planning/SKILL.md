---
name: ads-campaign-planning
description: "When the user wants to plan a paid ads campaign for an e-commerce or D2C brand end to end — objectives, funnel stages, audiences, offers, creative, budget, naming, and measurement locked before launch. Also use when the user mentions 'plan my Meta campaign,' 'ad campaign plan,' 'campaign brief,' 'launch structure for our new product,' 'BFCM campaign plan,' 'product launch ads,' or 'how should I structure my ad account.' This repository is Meta-only; for the e-commerce Meta hub, see meta-ads. For Meta-specific account architecture, see meta-campaign-structure. For the e-commerce Meta hub, see meta-ads."
metadata:
 version: 1.0.1
---

> **Marketing layer — advisory, not evidence.** Every benchmark, threshold and rule of thumb
> below is build-time guidance. Per `CLAUDE.md`, a marketing skill's number is never evidence
> for a quantified finding: a recommendation that originates here still needs a number, source,
> date range, formula, evidence class and confidence from the audit layer before it can be
> presented as one. Handoffs run audit → marketing, never the reverse.


# D2C Ads Campaign Planning & Execution

"Prepare to plan or plan to fail." Mapping a campaign before launch makes execution 10x easier — and in e-commerce, where budgets shift daily and creative burns out in weeks, a repeatable plan is the difference between scaling and thrashing.

## Before Starting

**Check for product marketing context first:**
If `.agents/product-marketing.md` exists (or `.claude/product-marketing.md`, or the legacy `product-marketing-context.md` filename, in older setups), read it before asking questions. Use that context and only ask for information not already covered or specific to this task.

Gather this context (ask only for what's missing):

- Product & price point (AOV), and contribution margin if available
- Primary goal: new-customer acquisition, launch, promo/sale event, or retention
- Monthly/total budget, target CAC or ROAS (or margin so you can derive it)
- Channels already running and available creative assets

## How to use this skill

When the user asks to plan a paid campaign, gather what you can from context, then ask only for what's missing among: product & price point (AOV), primary goal (new-customer acquisition, launch, promo/sale event, retention), monthly/total budget, target CAC or ROAS (or margin so you can derive it), channels already running, and available creative assets. Then produce a campaign plan covering the 6 elements below. Deliver it as a structured document the user can execute from or hand to an agency.

## 6 Essential Elements of a D2C Campaign Plan

1. **Objective & unit economics.** Every campaign gets one job: acquisition, launch, promo, retargeting, or retention. Anchor targets in unit economics, not platform metrics — define target CAC (or break-even ROAS = AOV ÷ contribution margin per order) before touching budget. If the brand has strong repeat purchase, note whether the target is first-order profitable or LTV-payback based.

2. **Funnel stage & audience.** D2C accounts are structured by funnel stage, not persona lists:
 - **Prospecting** (cold, ~70–80% of budget): broad or interest-based; on Meta favor broad + creative-as-targeting, on Google use Shopping/PMax + category search terms, on TikTok broad with strong hooks.
 - **Retargeting** (~10–20%): site visitors, viewed-product, add-to-cart, and engaged social audiences, with frequency caps and exclusion of recent purchasers.
 - **Retention/CRM-adjacent** (~5–10%): past purchasers for replenishment, cross-sell, or LTV offers — coordinate with email/SMS so paid isn't duplicating owned channels.

3. **Offer.** In ecom the offer often matters more than the audience. Decide it per stage: full price / bundle / gift-with-purchase / free shipping threshold for prospecting; urgency or incentive (first-order discount, low-stock, social proof) for retargeting; subscription or loyalty offers for retention. Protect margin — model the offer's effect on AOV and contribution before launch.

4. **Creative & copy.** Creative is the main performance lever. Plan a testing slate, not a single "hero" ad: 3–5 distinct angles (problem/solution, social proof/UGC, us-vs-them, unboxing/demo, founder story), each in the formats the channel rewards (9:16 video for Meta/TikTok, statics + catalog for retargeting, product feed quality for Shopping/PMax). Write hooks for the first 2 seconds. Define the refresh cadence (typically new creative every 2–4 weeks at scale).

5. **Channels & budget.** Allocate by where the category's buyers discover products: Meta as the default D2C workhorse, Google (Brand search, Shopping/PMax) to capture demand, TikTok for impulse/visual categories and lower CPMs, plus optional YouTube, Pinterest, or influencer whitelisting. Start concentrated (1–2 channels) rather than thin across five. Set daily budgets, a scaling rule (e.g., +20% every 3 days while CAC holds), and a kill rule (e.g., pause ad sets at 2× target CAC after ~50 clicks or 3 days).

6. **Measurement & naming.** Decide before launch how success is judged: blended MER / new-customer CAC as the source of truth, platform ROAS as directional, plus post-purchase survey ("How did you hear about us?") to correct attribution. Define the test window (typically 7–14 days) and what decision each result triggers.

## Naming Convention Best Practice

A consistent naming convention determines whether you can report cleanly later. Structure:

`[Channel]_[FunnelStage]_[Audience]_[Offer]_[Date]`

Examples:
- `META_PROSP_Broad_LaunchBundle_2026-08`
- `META_RTG_ATC-14d_10off_2026-08`
- `GOOG_PMAX_AllProducts_Evergreen_2026-08`
- `TT_PROSP_Spark-UGC_FreeShip_2026-08`

Carry the convention down to ad set (audience) and ad (creative angle + format, e.g., `UGC-Unboxing_9x16_v3`) so creative reporting works without spreadsheet archaeology.

## Execution Options

**Option 1 — DIY.** Use bulk tools for volume launches: Google Ads Editor, Meta bulk import/duplication, and catalog/feed rules for product-level ads. Format the campaign plan so rows map 1:1 to campaigns/ad sets for bulk upload. Keep one "evergreen" structure and duplicate it for promos rather than rebuilding. For Meta, the build itself can run through the Meta Ads MCP (see meta-campaign-creation).

**Option 2 — Outsource.** If you have budget but not time, hire a freelancer or ecom-focused agency. Ask your network for referrals first; otherwise use vetted marketplaces. Either way, hand them this campaign plan — the brand should always own strategy, naming, offer, and creative direction; the partner owns execution.

## Output format

Deliver the plan as a document with: (1) a one-page summary table (campaign, stage, channel, audience, offer, budget/day, target CAC/ROAS, launch date), (2) the creative testing slate with angles and hooks, (3) naming convention applied to every planned campaign, and (4) measurement rules — scaling, kill criteria, and test windows. If the user wants a spreadsheet for bulk import, structure it with one row per ad set.

## Key Takeaway

Keep plans simple and repeatable: one objective per campaign, budget weighted to prospecting, creative planned as a testing slate, and success defined by unit economics before launch. A plan means nothing until it's live — launch, then iterate on the schedule you set.

## Related Skills

- **google-ads-builder**: Once the plan says "run Google Search," this builds the actual campaign — ad groups, keywords, negatives, RSAs, extensions — and exports a Google Ads Editor CSV.
- **ads**: Platform-agnostic paid-ads strategy across Google, LinkedIn, Meta, and other channels.
- **meta-ads**: The e-commerce Meta hub — hands-on Meta strategy, audiences, creative, and optimization.
- **meta-campaign-structure**: Meta-specific account architecture, phases, and the scaling roadmap once the plan is set.
- **meta-campaign-creation**: Executing the plan on a live Meta account — the build chain via the Meta Ads MCP.
- **ad-creative**: Bulk generation and iteration of the ad copy and creative slate the plan calls for.
