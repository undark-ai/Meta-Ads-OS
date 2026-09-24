---
name: meta-campaign-creation
description: "When the user wants to create campaigns, ad sets, ads, or audiences on Meta for an e-commerce or D2C brand — the full build chain and the settings that matter, step by step, from customer-list audience to live purchase campaign. Also use when the user mentions 'create a Meta campaign,' 'build the campaign,' 'set up an ad set,' 'upload a custom audience,' 'create a lookalike,' 'launch this ad,' or 'push the campaign live.' Live builds run through the Meta Ads MCP. For deciding the architecture before building, see meta-campaign-structure. For live-account analysis and audits, see full-audit. For the e-commerce Meta hub, see meta-ads."
metadata:
 version: 1.0.0
---

<!-- execution-boundary: documents-writes -->
<!-- Names write tools without calling them: describes the build chain an execution run applies.
     Calling them is the execution lane's, under EXECUTION-PROTOCOL.md. -->

> **Marketing layer — advisory, not evidence.** Every benchmark, threshold and rule of thumb
> below is build-time guidance. Per `CLAUDE.md`, a marketing skill's number is never evidence
> for a quantified finding: a recommendation that originates here still needs a number, source,
> date range, formula, evidence class and confidence from the audit layer before it can be
> presented as one. Handoffs run audit → marketing, never the reverse.


# Creating Campaigns, Ads, and Audiences on Meta — D2C

The full build chain, end to end. Meta's structure is strict and nested:

```
Campaign (objective, budget if CBO)
 → Ad Set (audience, placement, budget if ABO, optimization goal, schedule)
 → Ad (references a creative + an ad set)
 → Ad Creative (media, copy, CTA, link, url_tags)
Custom / Lookalike Audiences (account level, referenced by ad sets)
Catalog + Product Sets (account level, for dynamic/catalog ads)
```

**Golden rules (always):**
- **Everything is created PAUSED.** Never activate a campaign, ad set, or ad without explicit user confirmation. Spend only starts when the user says go.
- **Budgets are in cents.** `5000` = $50.00.
- **Build order:** audiences (and catalog/product sets if used) first → campaign → ad set → creative → ad.

## Before Starting

**Check for product marketing context first:**
If `.agents/product-marketing.md` exists (or `.claude/product-marketing.md`, or the legacy `product-marketing-context.md` filename, in older setups), read it before asking questions. Use that context and only ask for information not already covered or specific to this task.

Gather this context (ask if not provided):

- The ad copy, media assets, landing page URL, and offer — never invent these
- Daily budget, target audience/geo, and whether the campaign is CBO or ABO

## Requires the Meta Ads MCP

Live-account work in this skill calls the Meta Ads MCP — the build chain maps directly to its tools: `ads_create_custom_audience` (and `ads_update_custom_audience_users` for list uploads), `ads_create_campaign`, `ads_create_ad_set`, `ads_creative_upload_image` / `ads_creative_upload_video`, `ads_create_creative`, `ads_create_ad`, `ads_get_ad_preview` to review before launch, and `ads_activate_entity` to go live. Use `ads_get_ad_accounts` first to confirm the target account. If the MCP isn't connected, say so and stop rather than fabricating account data, IDs, or performance numbers — the build plan and settings below still work as a spec the user can execute manually.

## 1. Audiences

Build these first with `ads_create_custom_audience` — ad sets reference them.

**Custom audiences** — build at the account level from:
- **Customer list:** create the audience, then upload best buyers via `ads_update_custom_audience_users` with email, phone, name, zip, and a customer-value (LTV) column for value-based lookalikes. Follow the data hierarchy in meta-audience-strategy: value-based customer-list lookalikes (Tier 1) → pixel/engagement audiences (Tier 2) → broad (Tier 3).
- **Website/pixel:** purchasers (for seeds and exclusions), add-to-cart 7–14d, viewed-product 14–30d (for retargeting).
- **Engagement:** IG/FB engagers, 50%+ video viewers.

**Lookalikes** — create the source custom audience first, then a lookalike from it (origin audience + country + ratio; start at 1%, value-based where possible).

**Exclusions are part of the build:** recent purchasers (30–60d) excluded from prospecting and retargeting; existing customers excluded from new-customer offers. Create these audiences now — ad sets reference them.

## 2. Campaign

Create with `ads_create_campaign`:
- Objective: **Sales** (`OUTCOME_SALES`) for purchase campaigns. Traffic/clicks objectives are vanity for ecom.
- CBO (budget on the campaign) for scaling; ABO (budget per ad set) for audience validation — one ad set per audience source, same ads across all.
- For catalog/dynamic ads, attach the product catalog at the campaign level.
- Starts PAUSED. Keep the returned campaign ID for the next step.

## 3. Ad Set

Create with `ads_create_ad_set`. Key fields:
- `campaign_id` (from step 2), name, `status: PAUSED`
- Optimization goal: **offsite conversions → Purchase** (with the pixel + Purchase event as the promoted object). Only step down to Add to Cart / Landing Page Views if purchase volume can't feed learning (< 50/week), and consolidate ad sets before downgrading the event.
- Targeting: custom/lookalike audiences plus geo and age; for broad, geo + age only and let creative do the filtering. Apply exclusion audiences here.
- Daily budget (in cents) only if ABO.
- For retargeting DPA: product set + retention window (e.g. viewed or added to cart, 14 days, purchasers excluded).

Validate audiences before scaling creative: one ad set per source, same ads across all, judge on new-customer rate, AOV, and margin in your order data — not just in-platform CPA.

## 4. Ad Creative

Upload media first (`ads_creative_upload_image` or `ads_creative_upload_video`), then create the creative with `ads_create_creative`. The creative holds the actual content (page/IG identity + media, primary text, headline, description, CTA, link):
- **`url_tags` (UTMs) are set at creation and cannot be edited later — get them right up front.** Consistent UTMs power MER reporting and post-purchase survey cross-checks.
- **Creative IS targeting.** The copy must call out who the product is for; on broad audiences the creative does all the filtering.
- Never invent ad copy. Use exactly the headline/body/description/CTA the user provides.
- For catalog ads, the creative references the product set with a dynamic template instead of fixed media.

## 5. Ad

Wire it together with `ads_create_ad`: name, `adset_id` (step 3), `creative_id` (step 4), `status: PAUSED`. One ad per creative variation; 4–6 unique concepts per campaign so the algorithm has diversity to learn from.

## 6. Go Live

When the user confirms: activate campaign, ad set, and ad with `ads_activate_entity` (all three must be active to spend). Before enabling:
- Confirm budget (remember: cents), audience, and exclusions one more time
- Verify the Purchase event fires with value and currency (Pixel + CAPI, deduplicated)
- Show the user the rendered ad with `ads_get_ad_preview` and confirm the landing page matches the ad's promise

After launch, hand operational decisions (pause/scale/graduate) to the meta-ads-operating-system framework: no judgments before adequate spend, weekly decision cadence, never pause without a replacement.

## Related Skills

- **meta-campaign-structure**: Decide the account architecture, phases, and settings before building anything.
- **meta-audience-strategy**: The audience data hierarchy (value-based lookalikes → pixel/engagement → broad) that step 1 follows.
- **meta-ads-operating-system**: The pause/scale/graduate decision framework that takes over after launch.
- **meta-ads**: The e-commerce Meta hub for strategy, creative, and optimization around the build.
- **full-audit**: The evidence-graded audit lane — 30 sections against live account data, where these benchmarks get tested rather than assumed.
