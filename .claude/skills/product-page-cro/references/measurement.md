# PDP Measurement

Most PDP audits are opinion because nobody instrumented the page. This is what turns the next audit into a data exercise.

---

## Event spec

| Event | Fires when | Key properties |
|---|---|---|
| `view_item` | PDP renders | `item_id`, `item_name`, `item_category`, `price`, `currency`, `in_stock`, `review_count`, `rating` |
| `gallery_interaction` | Thumbnail click, swipe, or zoom | `interaction_type` (click/swipe/zoom), `image_index`, `image_count` |
| `variant_selected` | Any variant option chosen | `option_name`, `option_value`, `price_delta`, `variant_in_stock` |
| `size_guide_opened` | Size or fit guidance opened | `guide_type` |
| `quantity_changed` | Quantity control used | `from`, `to` |
| `add_to_cart` | Add succeeds | `item_id`, `variant_id`, `quantity`, `value`, `currency` |
| `add_to_cart_error` | Add fails | `error_type` (out_of_stock / no_variant_selected / server), `variant_id` |
| `variant_out_of_stock_viewed` | Shopper selects an unavailable variant | `variant_id` |
| `back_in_stock_submitted` | Restock notification captured | `variant_id` |
| `review_section_viewed` | Reviews scroll into view | `review_count`, `rating` |
| `review_interaction` | Filter, sort, paginate, or expand a review | `interaction_type`, `filter_value` |
| `video_engagement` | Product video played | `video_id`, `percent_watched` |
| `accordion_opened` | Any detail section expanded | `section_name` |
| `faq_interaction` | FAQ item expanded | `question` |
| `shipping_info_viewed` | Shipping/returns block viewed or expanded | `placement` |
| `cross_sell_click` | Related product clicked | `source_item_id`, `target_item_id`, `placement` |
| `begin_checkout` | Checkout entered | (hands off to `checkout-cro`'s spec) |

Four that teams routinely skip and shouldn't:

- **`add_to_cart_error`** — a silent add-to-cart failure is invisible without it, and it's a total loss every time it fires
- **`variant_out_of_stock_viewed`** — quantifies exactly how much paid traffic is hitting a dead end
- **`accordion_opened`** with the section name — tells you what shoppers actually need, which settles most information-architecture arguments
- **`gallery_interaction`** with `image_index` — shows where in the sequence attention dies, so you know which images earn their weight

---

## Segmentation

A blended ATC rate hides nearly everything. Segment by:

- **Device** — desktop vs. mobile vs. tablet. Non-negotiable
- **New vs. returning**
- **Traffic source and campaign** — cold paid social needs the value prop restated; branded search does not
- **Product and category** — a template-level average conceals the outliers where the money is
- **Variant** — one size or colour with a collapsed ATC rate usually means a stock or imagery problem, not a page problem
- **Geography** — surfaces shipping-restriction and duties problems
- **Browser and OS** — including in-app webviews (Instagram, TikTok, Facebook), where galleries and sticky CTAs commonly break
- **Review volume band** — proves or disproves the review-volume argument with your own data

---

## The five metrics to watch

| Metric | Definition | Why it's here |
|---|---|---|
| **PDP conversion rate** | Purchases ÷ PDP sessions | The honest measure of whether the page works |
| **Revenue per PDP visitor** | Revenue ÷ PDP sessions | Can't be gamed by trading one funnel stage for another |
| **Add-to-cart rate** | `add_to_cart` ÷ `view_item` | Diagnostic, **not** a scoreboard metric — see the warning below |
| **PDP → checkout initiation** | `begin_checkout` ÷ `add_to_cart` | Catches an ATC gain that's really a qualification loss |
| **Return rate by reason** | Returns ÷ orders, by reason code | The PDP's delayed report card. Sizing, colour, and expectation-mismatch returns are all page failures |

**The add-to-cart trap, stated plainly:** ATC rate rises when you hide the price, bury shipping cost, add an aggressive sticky bar, or default a subscription. Every one of those pushes unqualified shoppers into a cart they abandon, and the loss lands on someone else's checkout metric. Never report an ATC win without its checkout-initiation and revenue numbers beside it.

---

## Qualitative instrumentation

- **Scroll-depth heatmaps** — where the page dies, and whether anyone ever reaches the reviews
- **Rage clicks** — concentrate on non-interactive images shoppers expect to zoom, and on variant swatches that don't respond
- **Session recordings filtered to non-converting PDP sessions.** Watch fifteen, mobile-first. Filter to sessions containing `add_to_cart_error` or `variant_out_of_stock_viewed`
- **On-page question widget** — "What else do you need to know about this product?" Answers become the FAQ and the missing gallery images
- **Post-purchase survey** — "Was there anything that almost stopped you buying?" Buyers describe the friction that stopped the non-buyers
- **Return reason codes** — the highest-signal PDP data most stores already have and never read. "Not as pictured" means a gallery problem; "wrong size" means a sizing problem; "not as described" means a copy problem
- **Pre-purchase support tickets** — every repeated question is a hole in the page

---

## Diagnosing before recommending

Run this before writing any recommendation:

1. **PDP conversion and ATC rate by device.** If mobile is far below desktop relative, this is a mobile audit
2. **ATC rate vs. checkout initiation.** A healthy ATC with poor initiation means the cart or the shipping surprise is the problem, not the PDP
3. **Scroll depth.** If 70% never reach the reviews, moving proof up-page outranks improving the reviews
4. **ATC rate by variant.** Isolate stock and imagery problems from page problems
5. **Return reasons.** Rank them. The top reason is usually the top PDP fix, and it's the one no cosmetic audit finds
6. **`add_to_cart_error` volume.** Rule out a straightforward bug before theorizing about persuasion
7. **`variant_out_of_stock_viewed` volume.** Quantify the dead-end traffic
8. **Accordion open rates.** What shoppers open is what belongs higher
9. **LCP on the PDP template**, throttled, cache-disabled — the gallery is usually the culprit

Then write the audit against what you found, and say which findings came from data and which from the structural walk.

---

## Setup notes

- **GA4** gives `view_item` and `add_to_cart` on Shopify by default; everything diagnostic above (gallery, variant, accordion, errors, out-of-stock) needs adding. Without them the funnel says "people don't add to cart" and nothing about why
- **Shopify** is the source of truth for variant-level stock and sell-through — often explains a variant's poor ATC rate outright
- **PostHog / Mixpanel / Amplitude** are better than GA4 for step-level funnels and arbitrary property segmentation
- **Hotjar** for scroll maps, rage clicks, and filtered recordings
- **Return reason data** usually lives in the returns platform (Loop, Returnly, or the platform's own), not in analytics — pull it deliberately

See `tools/integrations/` for per-tool setup, `../../analytics/SKILL.md` for the broader tracking plan, and `../../checkout-cro/references/measurement.md` for the events downstream of add-to-cart.
