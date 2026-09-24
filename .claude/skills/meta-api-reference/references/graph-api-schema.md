# Meta Marketing Graph API Schema Reference

The raw API layer beneath the MCP tools. Load this only when you are hitting the Graph API directly — server-side Conversions API, catalog feed automation, a custom reporting job, or middleware. For normal campaign work use the task-to-tool map in `../SKILL.md`; the MCP tools already encode most of what follows.

Enums and field lists are scoped to **e-commerce** use. Lead-gen, app-promotion and messaging values are noted where they exist but not expanded — a D2C sales account rarely needs them.

Budgets are always in **minor currency units**: `5000` = $50.00.

## Contents

- Campaign fields and objectives
- Ad set: optimization goal, billing event, destination, promoted object
- Targeting spec
- Ad creative: object_story_spec, link_data, video_data, carousel
- CTA types
- Custom audiences
- Insights: date presets, metrics, breakdowns, action types, async reports
- Attribution and data retention (2026)
- Conversions API: event structure, dedup, hashing
- Media upload
- Pagination and CRUD
- Gotchas

## Campaign

**Objectives (ODAX).** For e-commerce, `OUTCOME_SALES` is the objective for nearly everything. `OUTCOME_TRAFFIC` and `OUTCOME_AWARENESS` have narrow upper-funnel uses; `OUTCOME_ENGAGEMENT`, `OUTCOME_LEADS` and `OUTCOME_APP_PROMOTION` are outside D2C sales work except for list-growth campaigns (see `lead-capture-optimization`).

**Bid strategy** is set at the campaign level when the campaign holds the budget (CBO), at the ad set level otherwise: `LOWEST_COST_WITHOUT_CAP`, `LOWEST_COST_WITH_BID_CAP`, `COST_CAP`, `LOWEST_COST_WITH_MIN_ROAS`.

**CBO vs ABO** is determined by *where the budget field lives*, not by a flag: `daily_budget` or `lifetime_budget` on the campaign = CBO; on the ad set = ABO. You cannot set both.

**Special ad categories** (`special_ad_categories`) must be declared for credit, employment, housing, social issues, elections and politics. Declaring one restricts targeting — most D2C accounts pass `[]`, but supplements and financial products should be checked against current policy.

**Status**: create as `PAUSED`, then activate deliberately. `ACTIVE`, `PAUSED`, `DELETED`, `ARCHIVED`.

## Ad Set

### Optimization goal

For a sales account the relevant values are:

| Value | Use with | Description |
|---|---|---|
| `OFFSITE_CONVERSIONS` | `OUTCOME_SALES` | Pixel/CAPI conversions. The default for purchase campaigns. |
| `VALUE` | `OUTCOME_SALES` | Optimize for conversion value (ROAS bidding). Needs reliable value on every Purchase event. |
| `LANDING_PAGE_VIEWS` | `OUTCOME_TRAFFIC` | Requires the pixel. A fallback when purchase volume is too low to optimize on. |
| `LINK_CLICKS` | `OUTCOME_TRAFFIC` | Rarely correct for D2C; buys clicks, not buyers. |
| `REACH`, `IMPRESSIONS`, `AD_RECALL_LIFT` | `OUTCOME_AWARENESS` | Upper funnel only. |
| `THRUPLAY` | `OUTCOME_ENGAGEMENT` | Video views of 15s+. |

The API accepts 34 values in total. Others include `ADVERTISER_SILOED_VALUE`, `APP_INSTALLS`, `APP_INSTALLS_AND_OFFSITE_CONVERSIONS`, `AUTOMATIC_OBJECTIVE`, `CONVERSATIONS`, `DERIVED_EVENTS`, `ENGAGED_USERS`, `EVENT_RESPONSES`, `IN_APP_VALUE`, `LEAD_GENERATION`, `MEANINGFUL_CALL_ATTEMPT`, `MESSAGING_APPOINTMENT_CONVERSION`, `MESSAGING_PURCHASE_CONVERSION`, `NONE`, `PAGE_LIKES`, `POST_ENGAGEMENT`, `PROFILE_AND_PAGE_ENGAGEMENT`, `PROFILE_VISIT`, `QUALITY_CALL`, `QUALITY_LEAD`, `REMINDERS_SET`, `SUBSCRIBERS`, `VISIT_INSTAGRAM_PROFILE`.

### Billing event

`IMPRESSIONS` in almost every case. Also `LINK_CLICKS`, `CLICKS`, `THRUPLAY`, `POST_ENGAGEMENT`, `PAGE_LIKES`, `APP_INSTALLS`, `LISTING_INTERACTION`, `NONE`, `OFFER_CLAIMS`, `PURCHASE`.

### Destination type

`WEBSITE` for a store. `SHOP_AUTOMATIC` for on-platform Shops. `ON_AD` for instant experiences and on-platform forms. Messaging destinations (`MESSENGER`, `WHATSAPP`, `INSTAGRAM_DIRECT`) apply to conversational commerce. Others exist (`APP`, `FACEBOOK`, `ON_POST`, `ON_VIDEO`, `INSTAGRAM_PROFILE`, `FACEBOOK_PAGE`, and the messaging combinations) but are outside standard D2C.

### Promoted object

Required whenever the ad set optimizes for a conversion. For a store:

```json
{"pixel_id": "YOUR_PIXEL_ID", "custom_event_type": "PURCHASE"}
```

`custom_event_type` values relevant to e-commerce: `PURCHASE`, `ADD_TO_CART`, `INITIATE_CHECKOUT`, `ADD_PAYMENT_INFO`, `ADD_TO_WISHLIST`, `VIEW_CONTENT`, `SEARCH`, `COMPLETE_REGISTRATION`, `SUBSCRIBE`, `START_TRIAL`, `LEAD`, `CUSTOMIZE_PRODUCT`, `DONATE`, `FIND_LOCATION`, `SCHEDULE`, `CONTACT`, `SUBMIT_APPLICATION`, `OTHER`.

For catalog campaigns the promoted object carries `product_set_id` (and `product_catalog_id`) instead of, or alongside, the pixel.

## Targeting Spec

```json
{
  "geo_locations": {
    "countries": ["US", "CA"],
    "country_groups": ["north_america"],
    "regions": [{"key": "3847"}],
    "cities": [{"key": "2430536", "radius": 10, "distance_unit": "mile"}],
    "zips": [{"key": "US:10001"}],
    "location_types": ["home", "recent"]
  },
  "age_min": 25,
  "age_max": 55,
  "genders": [1],
  "locales": [6],
  "flexible_spec": [
    {"interests": [{"id": "6003107902433"}], "behaviors": [{"id": "6002714895372"}]}
  ],
  "exclusions": {"interests": [{"id": "123"}]},
  "custom_audiences": [{"id": "AUDIENCE_ID"}],
  "excluded_custom_audiences": [{"id": "EXCLUDED_AUDIENCE_ID"}],
  "targeting_automation": {"advantage_audience": 1},
  "publisher_platforms": ["facebook", "instagram", "audience_network", "messenger"],
  "device_platforms": ["mobile", "desktop"],
  "facebook_positions": ["feed", "story", "facebook_reels", "marketplace", "video_feeds", "profile_feed", "right_hand_column", "search"],
  "instagram_positions": ["stream", "story", "reels", "explore", "profile_feed", "ig_search"],
  "messenger_positions": ["story", "inbox"],
  "audience_network_positions": ["classic", "rewarded_video"]
}
```

**flexible_spec logic**: within one object, fields are OR'd; multiple objects in the array are also OR'd. Use `exclusions` for AND-NOT. This is why "stacking interests" does not narrow an audience the way people expect — see `meta-audience-strategy`.

**Advantage+ audience**: `targeting_automation.advantage_audience` = 1 enables expansion beyond your defined targeting. Defaults to enabled from API v23.0. You still supply base geo and age.

**Geo rules**: use `country_groups` rather than listing thirty countries. **Never overlap locations** — passing both `US` and a US city errors. Excluding Singapore avoids triggering regulatory compliance fields.

**Interest search**: `GET /search?type=adinterest&q=KEYWORD&limit=10000&locale=en_US` returns interests with `id`, `name`, `audience_size` and `path`. The API exposes thousands that Ads Manager's autocomplete does not. `type=adinterestsuggestion` with `interest_list` returns adjacent suggestions. Note that many detailed-targeting interests were consolidated from June 2025, and ad sets built on interests created before 8 October 2025 may stop delivering.

**Placements**: omit the placement fields entirely to run Advantage+ Placements, which is the default recommendation. Specify them only to exclude a placement you have evidence against — see delivery-diagnostics.

## Ad Creative

`object_story_spec` has two shapes:

1. **Inline creative** — `page_id`, `instagram_user_id`, plus `link_data` or `video_data` describing the ad.
2. **Existing post** — `page_id` plus `{"instagram_actor_id": ..., "effective_object_story_id": ...}` to promote a post that already exists, preserving its social proof.

**link_data** fields: `link` (destination URL), `message` (primary text), `name` (headline), `description`, `image_hash`, `call_to_action` (`{"type": ..., "value": {"link": ...}}`), `child_attachments` for carousels.

**video_data** fields: `video_id`, `message`, `title`, `link_description`, `image_url` or `image_hash` for the thumbnail, `call_to_action`.

**Carousel**: `link_data.child_attachments`, 2–10 cards, each with `image_hash` (or `video_id`), `link`, `name` and `description`. `multi_share_optimized: true` lets Meta reorder cards by performance. 3–5 cards is the practical optimum.

**Dynamic creative / asset feed**: `asset_feed_spec` with a minimal `object_story_spec` (page_id and instagram_user_id only, no link_data). `optimization_type: "PLACEMENT"` delivers different images per placement; `REGULAR` runs dynamic creative but **limits the ad set to one ad**.

**url_tags** is settable at creative **creation time only** — it cannot be updated on the creative. To change it, POST to the *ad* with a full inline `creative` spec. Dynamic parameters: `{{campaign.name}}`, `{{campaign.id}}`, `{{adset.name}}`, `{{adset.id}}`, `{{ad.name}}`, `{{ad.id}}`, `{{placement}}`, `{{site_source_name}}`. For the UTM template itself and the GA4 channel-grouping consequences, see `analytics`.

### CTA types

E-commerce: `SHOP_NOW`, `BUY_NOW`, `ORDER_NOW`, `ADD_TO_CART`, `GET_OFFER`, `SUBSCRIBE`, `PURCHASE_GIFT_CARDS`, `BUY_TICKETS`, `SELL_NOW`, `PAY_TO_ACCESS`, `LEARN_MORE`, `SIGN_UP`, `BOOK_NOW`, `GET_QUOTE`, `SEE_MENU`, `GET_DIRECTIONS`, `WATCH_MORE`, `MESSAGE_PAGE`, `INSTAGRAM_MESSAGE`, `SAVE`, `NO_BUTTON`.

The full enum also covers app promotion (`INSTALL_APP`, `USE_APP`, `PLAY_GAME`, …), media (`WATCH_VIDEO`, `LISTEN_NOW`, …), social (`LIKE_PAGE`, `EVENT_RSVP`, `DONATE`, …) and travel (`BOOK_TRAVEL`, `REQUEST_TIME`). For which button to choose, see `meta-creative-formats`.

## Custom Audiences

**Customer list**: create with `subtype: "CUSTOM"` and `customer_file_source: "USER_PROVIDED_ONLY"`, then POST to `/{audience_id}/users` with a `schema` array and `data` rows. Batches up to 10,000. Data must be normalized and SHA-256 hashed per the rules below. 1,000+ matched records is the practical floor for a usable lookalike seed.

**Website custom audience**: `subtype: "WEBSITE"` with a rule over pixel events. `retention_seconds` sets the window (14 days = `1209600`).

**Lookalike**: `subtype: "LOOKALIKE"`, `origin_audience_id`, and `lookalike_spec: {"ratio": 0.01, "country": "US"}`. `lookalike_spec` has been mandatory since January 2026.

**Value-based**: the seed customer list must carry a `LOOKALIKE_VALUE` column alongside the identifiers for Meta to weight by customer value.

Error **1359208** on audience creation means the Custom Audience terms need re-accepting in the Ads Manager UI. The API cannot detect or resolve this.

## Insights

**Core parameters**: `level` (`account` / `campaign` / `adset` / `ad`), `fields`, `time_range` or `date_preset`, `breakdowns`, `action_breakdowns`, `filtering`, `time_increment`.

**Date presets**: `today`, `yesterday`, `last_3d`, `last_7d`, `last_14d`, `last_28d`, `last_30d`, `last_90d`, `this_week_mon_today`, `this_week_sun_today`, `last_week_mon_sun`, `last_week_sun_sat`, `this_month`, `last_month`, `this_quarter`, `last_quarter`, `this_year`, `last_year`, `maximum`, `lifetime`.

**Common fields**: `spend`, `impressions`, `clicks`, `reach`, `frequency`, `ctr`, `cpc`, `cpm`, `actions`, `action_values`, `cost_per_action_type`, `conversions`, `conversion_values`, `cost_per_conversion`, `purchase_roas`.

**Delivery breakdowns**: `age`, `gender`, `country`, `region`, `dma`, `publisher_platform`, `platform_position`, `device_platform`, `impression_device`, `frequency_value`, `product_id`, `hourly_stats_aggregated_by_advertiser_time_zone`, `hourly_stats_aggregated_by_audience_time_zone`. Dynamic-creative breakdowns: `ad_format_asset`, `body_asset`, `call_to_action_asset`, `description_asset`, `image_asset`, `link_url_asset`, `title_asset`, `video_asset`.

**Action breakdowns**: `action_type`, `action_device`, `action_destination`.

**You cannot combine delivery breakdowns and action breakdowns in one request.** Issue them separately. Some delivery breakdowns are also mutually incompatible — `platform_position` with `age` or `gender`, for instance.

**action_type values for e-commerce**: `offsite_conversion.fb_pixel_purchase`, `offsite_conversion.fb_pixel_add_to_cart`, `offsite_conversion.fb_pixel_initiate_checkout`, `offsite_conversion.fb_pixel_add_payment_info`, `offsite_conversion.fb_pixel_view_content`, `offsite_conversion.fb_pixel_search`, `offsite_conversion.fb_pixel_custom`, `omni_purchase`, `omni_add_to_cart`, `omni_initiated_checkout`, `link_click`, `landing_page_view`, `video_view`, `post_engagement`, `page_engagement`.

**Extracting a conversion count** — `actions` comes back as an array of `{action_type, value}` objects, so you have to sum the type you want rather than reading a scalar:

```
purchases = sum(int(a["value"]) for a in row.get("actions", [])
                if a["action_type"] == "offsite_conversion.fb_pixel_purchase")
```

Prefer `omni_purchase` when the brand sells across web and on-platform Shops; prefer the pixel type when you want web only. Never mix them in one figure.

**Never average a ratio across rows.** Recompute CTR, CPA, CPM and ROAS from summed numerators and denominators. See meta-ads-data-validation.

**Async reports** for wide date ranges or heavy breakdowns: pass `async=true` to the insights edge, take `report_run_id` from the response, poll `GET /{report_run_id}` until `async_status` is `Job Completed`, then read `GET /{report_run_id}/insights`.

**Reach estimation**: `GET /{account_id}/delivery_estimate` with a targeting spec and optimization goal returns an estimated audience size. Treat it as an order of magnitude, not a number.

### Data retention (2026)

- Unique-count fields: 13 months
- Frequency breakdowns: 6 months
- Hourly breakdowns: 13 months
- Over 100 metrics have been deprecated, including `unique_actions`

Anything older than these windows is unavailable, which matters for year-over-year seasonal analysis — archive your own history.

## Attribution

```json
"attribution_spec": [
  {"event_type": "CLICK_THROUGH", "window_days": 7},
  {"event_type": "VIEW_THROUGH", "window_days": 1}
]
```

**Windows available after 12 January 2026**: click-through 1 day or 7 days; view-through 1 day only. The 7-day and 28-day view-through windows were **removed**, and historical reports built on them no longer return data. Default is 7-day click plus 1-day view.

Changing the window changes the numbers, not the delivery. For which window to run and how to reconcile against store-side revenue, see `meta-attribution`.

## Conversions API

**Endpoint**: `POST /{pixel_id}/events` with `data` as an array of event objects.

Each event carries `event_name`, `event_time` (Unix seconds), `event_id`, `event_source_url`, `action_source` (`website`, `app`, `phone_call`, `chat`, `email`, `other`, `system_generated`, `business_messaging`), `user_data`, and `custom_data` (`value`, `currency`, `contents`, `content_ids`, `content_type`, `order_id`, `num_items`).

**Standard event names** for a store: `Purchase`, `AddToCart`, `InitiateCheckout`, `AddPaymentInfo`, `ViewContent`, `Search`, `AddToWishlist`, `CompleteRegistration`, `Subscribe`, `StartTrial`, `Lead`, `PageView`.

**Deduplication**: the browser Pixel event and the server CAPI event for the same action must share the **same `event_id`** and the same `event_name`. Use the store's order ID as `event_id` for Purchase. Mismatched IDs mean Meta counts the order twice — the signature is conversions doubling overnight.

### user_data hashing

| Field | Hash | Normalize first |
|---|---|---|
| `em` (email) | SHA-256 | lowercase, trim |
| `ph` (phone) | SHA-256 | E.164, digits only, no spaces or dashes |
| `fn` / `ln` | SHA-256 | lowercase, trim |
| `ct` (city) | SHA-256 | lowercase, no spaces or punctuation |
| `st` (state) | SHA-256 | two-letter code, lowercase |
| `zp` (zip) | SHA-256 | lowercase, trim; first five digits for US |
| `country` | SHA-256 | two-letter ISO code, lowercase |
| `external_id` | SHA-256 | trim |
| `fbp`, `fbc` | **NO** | send raw |
| `client_ip_address`, `client_user_agent` | **NO** | send raw |

All hashes are **lowercase hex**. Hashing `fbp` or `fbc` breaks matching entirely — these are cookies, not identifiers, and they carry the highest match value on click-attributed events.

Use the Test Events tool with a `test_event_code` while wiring, and remove it before going live. For event hierarchy, event match quality bands and the failure modes, see `meta-capi-and-events`.

## Media Upload

**Images** — `POST /{account_id}/adimages`. JPG or PNG, 30MB max, 1080×1080 minimum recommended. The response returns a `hash` per filename, which is what `link_data.image_hash` expects. Ratios: 1:1 and 4:5 for feed, 9:16 for Stories and Reels.

**Videos** — `POST /{account_id}/advideos`. Files over 100MB must use chunked upload (`start` / `transfer` / `finish` phases). After upload, fetch a thumbnail from `GET /{video_id}/thumbnails` — a video creative without a thumbnail will fail.

## Pagination and CRUD

List edges return `data` plus `paging.cursors.after`; pass `after` to continue. An empty `data: []` means no activity in the period, **not** an error.

- **Create**: `POST /{account_id}/{edge}` where edge is `campaigns`, `adsets`, `ads`, `adcreatives`, `adimages`, `advideos`, `customaudiences`.
- **Read**: `GET /{object_id}?fields=...`
- **Update**: `POST /{object_id}` with the changed fields. To change creative content — URL, copy, `url_tags` — POST to the **ad** with a full inline `creative` spec, not to the creative.
- **Delete**: `DELETE /{object_id}`, or set `status: "ARCHIVED"`, which is usually what you want.

## Gotchas

1. **Budgets are in minor units.** `5000` = $50.00.
2. **`is_adset_budget_sharing_enabled` is a string**, `"true"` / `"false"`, not a boolean.
3. **Creative content is updated through the ad**, never through the creative. `url_tags` included.
4. **The Instagram account appears in two places** — top-level `instagram_user_id` and inside `object_story_spec`. Set both.
5. **`optimization_type: "REGULAR"` limits the ad set to one ad.** Use `"PLACEMENT"` when you need multiple.
6. **Video thumbnails are required**, fetched separately after upload.
7. **Files over 100MB fail single upload.**
8. **Never overlap geo locations** — a country plus one of its cities errors.
9. **Custom Audience TOS error 1359208** must be resolved in the UI.
10. **Empty `data: []` is not an error.**
11. **Cannot combine delivery and action breakdowns** in one insights request.
12. **Paragraph breaks in ad copy** are `\n\n`; single `\n` within a list.
13. **Create everything `PAUSED`**, verify with a preview, then activate.
14. **Never hardcode a token.** Load it from the environment, and never build a Graph API call by interpolating a token into a shell string — use an HTTP client.
