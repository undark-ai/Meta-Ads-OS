---
name: meta-api-reference
description: "When the user is building or modifying Meta ads objects for an e-commerce or D2C store and needs the reference layer — which Meta Ads MCP tool does what, plus the Marketing API objects, fields, enums, and gotchas behind them (objectives, optimization goals, bid strategies, CBO vs ABO, targeting specs, creative specs, insights fields, event payloads). Also use when the user mentions 'which MCP tool creates a campaign,' 'OUTCOME_SALES,' 'optimization goal,' 'bid strategy,' 'CBO or ABO,' 'promoted object,' 'object_story_spec,' 'action_types,' 'purchase_roas,' 'lookalike spec,' 'insights breakdowns,' or 'Marketing API fields.' For the step-by-step build workflow, see meta-campaign-creation. For analysis against a live account, see full-audit. For e-commerce Meta strategy, see meta-ads."
metadata:
 version: 1.1.0
---

<!-- execution-boundary: documents-writes -->
<!-- Names write tools without calling them: documents the Marketing API surface, including the write endpoints.
     Calling them is the execution lane's, under EXECUTION-PROTOCOL.md. -->

> **Marketing layer — advisory, not evidence.** Every benchmark, threshold and rule of thumb
> below is build-time guidance. Per `CLAUDE.md`, a marketing skill's number is never evidence
> for a quantified finding: a recommendation that originates here still needs a number, source,
> date range, formula, evidence class and confidence from the audit layer before it can be
> presented as one. Handoffs run audit → marketing, never the reverse.


# Meta MCP Tool & Marketing API Reference — E-commerce

The reference layer for doing live Meta ads work for an e-commerce store: which Meta Ads MCP tool to call for each task, and the Marketing API objects, fields, and enums those tools speak — the concepts are identical regardless of transport. This is a lookup document; for the guided build workflow, use meta-campaign-creation.

## Before Starting

**Check for product marketing context first:**
If `.agents/product-marketing.md` exists (or `.claude/product-marketing.md`, or the legacy `product-marketing-context.md` filename, in older setups), read it before asking questions. Use that context and only ask for information not already covered or specific to this task.

## Requires the Meta Ads MCP

All live operations in this reference run through the native Meta Ads MCP. If the MCP isn't connected, say so and stop rather than fabricating account data, IDs, or performance numbers — the field and enum reference below is still valid for planning. If a team is working against the raw Graph API instead, the same objects and fields apply — see [references/graph-api-schema.md](references/graph-api-schema.md) for the full enum, targeting-spec, insights-breakdown, attribution, CAPI-hashing and upload reference, and [meta-ads.md](../../tools/integrations/meta-ads.md) for HTTP transport details.

## Task → Tool Map

| Task | MCP tool |
|------|----------|
| List ad accounts / verify connection | `ads_get_ad_accounts` |
| List campaigns, ad sets, ads (with status/config) | `ads_get_ad_entities` |
| Create campaign | `ads_create_campaign` |
| Create ad set | `ads_create_ad_set` |
| Upload image / video | `ads_creative_upload_image`, `ads_creative_upload_video` |
| Create ad creative | `ads_create_creative` |
| Create ad | `ads_create_ad` |
| Preview an ad | `ads_get_ad_preview` |
| Update / rename / re-budget an entity | `ads_update_entity` |
| Pause or activate an entity | `ads_activate_entity` |
| Create custom audience | `ads_create_custom_audience` |
| Add hashed users to a customer-list audience | `ads_update_custom_audience_users` |
| Inspect an audience (size, rules) | `ads_get_custom_audience` |
| Pull performance metrics | `ads_get_ad_entities` (with insight fields), `ads_insights_performance_trend` |
| Spot anomalies | `ads_insights_anomaly_signal` |
| Pixel / dataset health and events | `ads_get_datasets`, `ads_get_dataset_quality`, `ads_get_dataset_stats`, `ads_pixel_event_read` |
| Custom conversions | `ads_get_customconversions` |
| Competitor ads | `ads_library_search` |

## Account Hierarchy

```
Ad Account (act_XXXX)
 -> Campaign (objective, budget if CBO, bid strategy)
 -> Ad Set (targeting, budget if ABO, optimization, schedule)
 -> Ad (creative reference, status)
 -> Ad Creative (media, copy, CTA, url_tags)
```

## Campaign (`ads_create_campaign`)

**Required:** `name`, `objective`, `status`, `special_ad_categories` (pass `[]` if none).
**Optional:** `daily_budget` / `lifetime_budget` (in cents — CBO), `bid_strategy`, `is_adset_budget_sharing_enabled` (string `"true"`/`"false"`).

**Objectives (ODAX):** `OUTCOME_SALES` (purchases, catalog sales — the ecom default), `OUTCOME_TRAFFIC`, `OUTCOME_ENGAGEMENT`, `OUTCOME_AWARENESS`, `OUTCOME_LEADS` (email/SMS list growth), `OUTCOME_APP_PROMOTION`.

**Bid strategy:** `LOWEST_COST_WITHOUT_CAP` (default), `COST_CAP` (max CPA), `LOWEST_COST_WITH_BID_CAP`, `LOWEST_COST_WITH_MIN_ROAS` (target ROAS floor).

**CBO vs ABO:** CBO = budget on the campaign + `is_adset_budget_sharing_enabled: "true"`, no ad set budgets. ABO = `"false"`, budget on each ad set, none on the campaign.

## Ad Set (`ads_create_ad_set`)

**Required:** `name`, `campaign_id`, `optimization_goal`, `billing_event`, `targeting`, `status`, budget (ABO only).
**Optional:** `bid_amount`, `start_time`/`end_time`, `promoted_object`, `destination_type` (`WEBSITE` most common), `is_dynamic_creative`, `targeting_automation`, `attribution_spec`.

**Key optimization goals:** `OFFSITE_CONVERSIONS` (pixel purchases — the ecom workhorse), `VALUE` (ROAS/value optimization, needs 50+ purchases/week with value), `LANDING_PAGE_VIEWS`, `LINK_CLICKS`, `REACH`, `THRUPLAY`, `LEAD_GENERATION` (list growth).
**Billing event:** `IMPRESSIONS` (95%+ of the time).

**Promoted object (pixel purchase optimization):**

```json
{"pixel_id": "YOUR_PIXEL_ID", "custom_event_type": "PURCHASE"}
```

(`ADD_TO_CART`, `INITIATE_CHECKOUT`, `VIEW_CONTENT`, `SUBSCRIBE` also valid.)

**Targeting spec essentials:**

```json
{
 "geo_locations": {"countries": ["US", "CA"]},
 "age_min": 18, "age_max": 65,
 "custom_audiences": [{"id": "RETARGETING_AUDIENCE_ID"}],
 "excluded_custom_audiences": [{"id": "PURCHASERS_180D_ID"}],
 "targeting_automation": {"advantage_audience": 1}
}
```

`geo_locations` is required; never overlap locations. Always exclude buyers from prospecting. `advantage_audience: 1` enables Advantage+ audience (default on in v23+). Exclude Singapore to avoid extra compliance fields.

## Ad Creative (`ads_create_creative`)

**Pattern A (simple link ad)** — `object_story_spec`:

```json
{
 "page_id": "PAGE_ID", "instagram_user_id": "IG_ID",
 "link_data": {
 "image_hash": "HASH", "link": "https://store.com/product",
 "message": "Body text", "name": "Headline",
 "call_to_action": {"type": "SHOP_NOW", "value": {"link": "https://store.com/product"}}
 }
}
```

**Pattern B (placement customization / dynamic creative):** put all content in `asset_feed_spec`; `object_story_spec` must be MINIMAL (page_id + instagram_user_id only — including link_data errors).

**Carousel:** `link_data.child_attachments` = 2–10 cards, each with `image_hash` + `link` (product URLs); `multi_share_optimized: true` lets Meta reorder cards.

**Common ecom CTAs:** `SHOP_NOW`, `BUY_NOW`, `ORDER_NOW`, `ADD_TO_CART`, `GET_OFFER`, `LEARN_MORE`, `SUBSCRIBE`, `SIGN_UP`.

**url_tags** (creation time ONLY — to change it, POST to the *ad* with a full inline `creative` spec): `utm_source={{site_source_name}}&utm_medium=paid_social&utm_campaign={{campaign.name}}&utm_content={{ad.name}}`. Dynamic params: `{{campaign.name}}`, `{{campaign.id}}`, `{{adset.name}}`, `{{adset.id}}`, `{{ad.name}}`, `{{ad.id}}`, `{{placement}}`, `{{site_source_name}}`. Use `paid_social`, not `cpc` — see **analytics** for the full template and why the wrong `utm_medium` makes Meta traffic show up as Organic Social in GA4.

## Ad (`ads_create_ad`)

`name`, `adset_id`, `creative` (`{"creative_id": "..."}`), `status` — create as `PAUSED`, never `ACTIVE`. Activate deliberately with `ads_activate_entity` after preview and QA.

## Custom Audiences (`ads_create_custom_audience`)

- **Customer list:** `subtype: "CUSTOM"`, `customer_file_source: "USER_PROVIDED_ONLY"`; then add users via `ads_update_custom_audience_users` with `schema: ["EMAIL","PHONE"]` and SHA-256 hashed, normalized data (lowercase emails, E.164 phones). Batches of up to 10,000.
- **Website audience:** `subtype: "WEBSITE"` with a rule on pixel events, e.g. AddToCart 14d: `retention_seconds: 1209600` on an `event_sources` rule filtered to the event.
- **Lookalike:** `subtype: "LOOKALIKE"`, `origin_audience_id` (purchaser list, 1,000–5,000 seeds ideal), `lookalike_spec: {"ratio": 0.01, "country": "US"}`. `lookalike_spec` mandatory since Jan 2026.

## Insights (`ads_get_ad_entities`, `ads_insights_performance_trend`)

Works at account/campaign/adset/ad level. Key params: `fields`, `date_preset` (`last_7d`, `last_30d`, `this_month`…) or `time_range`, `level`, `breakdowns`, `action_breakdowns`, `time_increment`, `filtering`.

**Ecom metrics:** `spend, impressions, clicks, ctr, cpc, cpm, reach, frequency, actions, action_values, purchase_roas, cost_per_action_type`.

**Key action_types:** `offsite_conversion.fb_pixel_purchase`, `omni_purchase`, `offsite_conversion.fb_pixel_add_to_cart`, `offsite_conversion.fb_pixel_initiate_checkout`, `offsite_conversion.fb_pixel_view_content`, `link_click`, `landing_page_view`.

To compute ROAS from a report row: purchases = the `omni_purchase` entry in `actions`; revenue = the `omni_purchase` entry in `action_values`; ROAS = revenue ÷ `spend`. Never average ratio metrics across rows — recompute from summed numerators and denominators.

**Breakdowns:** `age`, `gender`, `country`, `publisher_platform`, `platform_position`, `device_platform`, `product_id` (catalog ads). Cannot combine delivery breakdowns and `action_breakdowns` in one request — call separately.

**Attribution (2026):** default 7d click / 1d view; 7d and 28d view-through windows removed Jan 12, 2026. Set via `attribution_spec` on the ad set.

## Pixel & Server Events (`ads_get_datasets`, `ads_pixel_event_read`)

Inspect the pixel/dataset with `ads_get_datasets` and check Event Match Quality with `ads_get_dataset_quality`. Server-side Purchase events (Conversions API) must carry: `event_name`, `event_time`, `event_id` (dedup key matching the browser pixel event), `action_source: "website"`, hashed `user_data` (`em`, `ph`, `fn`, `ln`, `external_id` — SHA-256, lowercase hex), unhashed `fbp`/`fbc` (**never hash these** — it breaks matching entirely), and `custom_data` with `value`, `currency`, `content_ids`, `content_type`, `order_id`. For full CAPI wiring, see meta-capi-and-events.

## Media Upload (`ads_creative_upload_image`, `ads_creative_upload_video`)

- **Images:** JPG/PNG, ≤30MB, 1080x1080+ (1:1, 4:5, 9:16). Returns a `hash` used in creatives.
- **Videos:** MP4/MOV. A thumbnail is required before the video is usable in a creative.

## Key Gotchas

1. Budgets are in cents (5000 = $50.00); `is_adset_budget_sharing_enabled` is a string, not a boolean.
2. To update URLs/copy on a live ad: update the **ad** with an inline `creative` spec containing the full new content — creatives themselves are immutable for url_tags/content.
3. The Instagram account goes in TWO places (top-level `instagram_user_id` AND inside `object_story_spec`).
4. Empty `data: []` from insights = no activity in the window, not an error.
5. Custom Audience TOS error 1359208 = re-accept terms in Ads Manager UI (no API/tool can do it).
6. Ad copy formatting: `\n\n` between paragraphs, `\n` within lists.
7. Always create ads `PAUSED` and activate explicitly after QA.

## Related Skills

- **meta-campaign-creation**: The step-by-step build workflow that uses this reference — from customer-list audience to live purchase campaign.
- **meta-ads**: The e-commerce Meta hub — philosophy, routing, and setup.
- **full-audit**: The evidence-graded audit lane — 30 sections against live account data, where these benchmarks get tested rather than assumed.
- **meta-capi-and-events**: Full Conversions API and purchase-event wiring.
- **meta-setup-and-tracking**: Pixel, events, domain verification, and catalog implementation checklist.
