---
name: meta-capi-and-events
description: "When the user wants to wire the Conversions API and purchase funnel events for an e-commerce or D2C store — feeding real order, value, and customer signal back so Meta optimizes for profitable purchases, not clicks. Also use when the user mentions 'CAPI,' 'Conversions API,' 'server-side tracking,' 'Event Match Quality,' 'EMQ,' 'deduplication,' 'event_id,' 'hashed customer data,' 'purchase events don't match orders,' or 'send margin as value.' For initial pixel install, domain verification, and the launch checklist, see meta-setup-and-tracking. For purchases completing off your domain, see meta-third-party-conversion-tracking. For why Meta and the store never match even with clean wiring, see meta-attribution. For overall e-commerce Meta strategy, see meta-ads."
metadata:
 version: 1.1.0
---

<!-- execution-boundary: documents-writes -->
<!-- Names write tools without calling them: names pixel-event writes when describing what a fix would change.
     Calling them is the execution lane's, under EXECUTION-PROTOCOL.md. -->

> **Marketing layer — advisory, not evidence.** Every benchmark, threshold and rule of thumb
> below is build-time guidance. Per `CLAUDE.md`, a marketing skill's number is never evidence
> for a quantified finding: a recommendation that originates here still needs a number, source,
> date range, formula, evidence class and confidence from the audit layer before it can be
> presented as one. Handoffs run audit → marketing, never the reverse.


# Meta Conversions API (CAPI) & Events - D2C Ecommerce

Best practices for sending conversion data to Meta via the Conversions API: event hierarchy, platform-native vs middleware, deduplication, and Event Match Quality. Use this when setting up or auditing CAPI, choosing between your store platform's native integration and middleware (server-side GTM, Segment, n8n), or improving match quality.

## Before Starting

**Check for product marketing context first:**
If `.agents/product-marketing.md` exists (or `.claude/product-marketing.md`, or the legacy `product-marketing-context.md` filename, in older setups), read it before asking questions. Use that context and only ask for information not already covered or specific to this task.

Gather this context (ask if not provided):

- Store platform and current setup (pixel-only, native pixel + CAPI, middleware) and whether Meta-reported purchases roughly match store orders
- Whether they need custom signal logic (margin as value, new-customer-only Purchase, subscription events) or multiple destinations beyond Meta

## Requires the Meta Ads MCP

Live-account diagnostics in this skill call the Meta Ads MCP (tools like `ads_get_datasets`, `ads_get_dataset_quality`, `ads_get_dataset_stats`, `ads_pixel_event_read`, `ads_pixel_event_create`, `ads_pixel_parameter_read`, `ads_get_customconversions`). Use them to read the account's datasets/pixels, check event quality and EMQ, inspect configured events and parameters, and review custom conversions. If the MCP isn't connected, say so and stop rather than fabricating dataset stats, EMQ scores, or event counts — the setup guidance and frameworks below still work without it.

---

## Best Option for D2C: Server-Side Orders to CAPI (with Pixel)

- **Source of truth:** Your store's order system (Shopify, WooCommerce, custom backend) - not the browser.
- **Conversion events:** The full funnel (ViewContent, AddToCart, InitiateCheckout, Purchase), with **Purchase carrying real `value` and `currency`** so Meta can do value/ROAS optimization.
- **Sending:** Server-side via CAPI from the platform or backend.
- **Redundancy:** Send **both** pixel (browser) and CAPI (server) for the same events, with **deduplication** so Meta counts each once.

This gives optimization on real revenue, resilience to iOS/ad blockers, and a closed loop: ad click → order → server event back to Meta with value attached.

---

## Recommended Event Hierarchy (Ecom)

| Event | When to send | Why |
|-------|--------------|-----|
| ViewContent | Product page view | Top-of-funnel signal, powers dynamic retargeting |
| AddToCart | Add to cart | Intent; retargeting segment |
| InitiateCheckout | Checkout started | High intent; abandonment recovery |
| Purchase | Order completed | The optimization target; must carry value + currency + content_ids |
| Subscribe / custom LTV events | Subscription start, second order, high-LTV cohort | Optional: feed back quality signal so Meta finds repeat buyers, not just first orders |

Send one event per funnel stage. Set **conversion event priority** in Events Manager so Purchase ranks above everything else. On a connected account, read what's currently configured with `ads_pixel_event_read` and `ads_pixel_parameter_read` before changing anything, and review existing custom conversions with `ads_get_customconversions`.

### Aggregated Event Measurement: the 8-Event Limit

Setting event priority is not cosmetic. Under Aggregated Event Measurement, Meta allows **8 prioritized conversion events per verified domain**, and for a user who opted out of tracking, **only the single highest-priority event that fired in that session is reported.** Everything below it in the ranking is discarded for that session.

The consequence most accounts never notice: if `Purchase` is not ranked above `ViewContent`, a session where someone browsed a product *and then bought* reports only `ViewContent`. The purchase silently disappears from the signal your Purchase campaigns optimize on. Performance degrades with no error anywhere.

Priority ladder for a store, highest first:

1. `Purchase`
2. `AddPaymentInfo` / `InitiateCheckout`
3. `AddToCart`
4. `ViewContent`
5. `Search`
6. `AddToWishlist`
7. `CompleteRegistration` / `Subscribe` (list-growth events, if you run them)
8. `PageView`

Rules: only 8 slots exist, so anything past the eighth is unreported for opted-out users — spend them deliberately. Re-check the order after any Events Manager change, after adding a custom conversion, and after a checkout platform migration. AEM applies per **domain**, so a brand running two storefronts needs the ladder set on each.

---

## Where to Send From: Best vs Second Best

| Option | When it's best |
|--------|-----------------|
| **Platform native (e.g. Shopify → Meta, WooCommerce plugin)** | One place to manage sync. Customer data sharing (email, phone, click ID) is on at "Maximum", Event Match Quality is acceptable (6+/10), and you only need Meta. No custom logic required. |
| **Middleware (server-side GTM, Segment, n8n, custom backend)** | EMQ stays low despite native data sharing - you need to **normalize + hash per Meta's spec** (SHA-256, lowercase email, E.164 phone). You need **multiple destinations** (Meta + Google + TikTok + Pinterest). You need **custom logic** (send only new-customer purchases, send margin instead of revenue as value, exclude wholesale orders). You want **one event_id** shared by pixel + CAPI and full dedup control. **Compliance:** hash in middleware, filter by consent, never send plain PII. |

**Order of preference:** (1) Native platform integration with maximum data sharing. (2) If match quality stays low or you need custom logic / multi-destination / hashing control, add middleware between the store and Meta.

**High-leverage custom logic examples:** send contribution margin as the Purchase value so Meta's value optimization chases profit, not revenue; send a `Purchase` only for new customers to optimize new-customer CAC; send subscription renewals as a separate event.

---

## Deduplication: Where It Happens

- **Where:** In Meta's systems. You don't configure dedup in your platform or middleware; you send the right identifiers.
- **How:** Same `event_id` + same `event_name` from both the **pixel** (order confirmation page) and **CAPI** (order webhook). Meta merges them into one purchase.
- If the event only exists server-side (e.g. a subscription renewal or a refund adjustment days later), send CAPI only - there's nothing to dedupe.
- Without dedup you double-count purchases and your in-platform ROAS is fiction.

---

## Event Match Quality (EMQ)

- Send **user_data** with every CAPI event: at least **email** and **phone** (normalized, then SHA-256 hashed, lowercase hex). Optionally first/last name, city, zip, country, and **external_id** (your customer ID, hashed). Ecom has an advantage here: every checkout captures email and shipping details - use them.
- Always pass `fbp` and `fbc` cookies **unhashed**, plus `client_ip_address` and `client_user_agent` for web events.
- Check EMQ in Events Manager, or pull it from a connected account via `ads_get_dataset_quality`; aim for 6+/10 or "Good", and 8+ is realistic for Purchase since checkout data is rich. Scores of 3-4 mean Meta can't match orders to users - fix user_data or hashing.

### Reading the score

| EMQ | Read | Action |
|-----|------|--------|
| 8–10 | Excellent | Nothing. Monitor for drops. |
| 6–7 | Good | Acceptable. Add the next parameter up the lever list if you want headroom. |
| 4–5 | Fair | Meta is matching some orders and missing others. Fix before scaling. |
| 1–3 | Poor | Effectively unmatched. Treat as broken, not weak. |

### Levers, ranked by impact against effort

| Parameter | Impact | Difficulty | Notes |
|---|---|---|---|
| Hashed email (`em`) | High | Low | Every checkout has it. Non-negotiable. |
| Hashed phone (`ph`) | High | Low | Biggest incremental gain alongside email. |
| `fbc` (click cookie) | High | Medium | Only present on click-attributed events, where it matters most. Send raw. |
| `fbp` (browser cookie) | Medium | Medium | Send raw. Blocked pre-consent by most consent banners. |
| `external_id` (your customer ID) | Medium | Low | Stable when email or phone change. Underused. |
| First and last name (`fn`, `ln`) | Medium | Low | Cheap to add from the shipping address. |
| City / state / zip / country | Low–medium | Low | Additive rather than decisive. |
| IP + user agent | Baseline | None | Required for web events, not a lever. |

Target **5 or more well-formed matched parameters on Purchase.** More parameters only help if they are correctly normalized — a badly formatted phone number scores worse than a missing one.

### Normalization and hashing

| Field | Hash | Normalize first |
|---|---|---|
| `em` (email) | SHA-256 | lowercase, trim |
| `ph` (phone) | SHA-256 | E.164, digits only, no spaces or dashes |
| `fn` / `ln` | SHA-256 | lowercase, trim |
| `ct` (city) | SHA-256 | lowercase, strip spaces and punctuation |
| `st` (state) | SHA-256 | two-letter code, lowercase |
| `zp` (zip) | SHA-256 | lowercase, trim; first five digits for US |
| `country` | SHA-256 | two-letter ISO code, lowercase |
| `external_id` | SHA-256 | trim |
| `fbp`, `fbc` | **Never** | send raw |
| `client_ip_address`, `client_user_agent` | **Never** | send raw |

All hashes are **lowercase hex**:

```js
crypto.createHash('sha256').update(normalized).digest('hex')
```

**Hashing `fbp` or `fbc` breaks matching entirely.** They are cookies, not identifiers. This is the single most common middleware bug, and it presents as an unexplained EMQ collapse right after someone "fixed the PII handling."

---

## CAPI Best Practices (Summary)

- **Pixel + CAPI** for the same events (redundant setup).
- **Deduplication:** same `event_name` + `event_id` from both sides.
- **Parameters:** required (`action_source`, `event_source_url`, `client_user_agent`) plus hashed customer info (em, ph, fn, ln) and `custom_data` with `value`, `currency`, `content_ids`, `order_id`.
- **Real time:** send on the order webhook, not in a nightly batch - freshness feeds the learning phase.
- **Test:** Meta's Test Events tool and Payload Helper before going live; then place a real test order end to end.
- **Post-setup:** watch EMQ and the pixel/CAPI dedup rate (via Events Manager or `ads_get_dataset_quality` / `ads_get_dataset_stats`); avoid changing pixels or restructuring campaigns mid-learning.

---

## Failure Modes

Five signatures worth recognizing on sight. Each has one likely cause and a different fix.

| Symptom | Likely cause | Where to look |
|---|---|---|
| Conversions drop to near zero | Broken pixel snippet or a server call that stopped firing — a deploy, a theme change, a rotated token | Test Events; the order webhook's own error log |
| **Conversions roughly double overnight** | Deduplication broke. Pixel and CAPI are sending different `event_id` values for the same order | Compare `event_id` on a single real order across both sources |
| EMQ dropped after a site redesign | Checkout stopped passing hashed parameters, or a new consent banner now blocks `fbp`/`fbc` before consent | `ads_get_dataset_quality` trend; inspect a live checkout for the cookies |
| Meta reports fewer purchases than the store | An AEM gap for opted-out users, or `Purchase` not ranked top in event priority | The AEM priority ladder above |
| A test event never appears | Malformed CAPI payload — usually a bad `event_time`, a missing `action_source`, or unhashed PII being rejected | Test Events with a `test_event_code`, plus the Payload Helper |

Note the asymmetry: under-reporting is usually AEM or match quality, and over-reporting is almost always dedup. Diagnose in that direction rather than checking everything.

---

## Related Skills

- **meta-setup-and-tracking**: Pixel install, domain verification, catalog, and the pre-launch checklist that precedes CAPI work.
- **meta-third-party-conversion-tracking**: When checkout completes on a third-party platform and CAPI is the fallback path for the purchase signal.
- **meta-ads**: The e-commerce Meta hub — strategy, structure, and optimization once the signal foundation is solid.
- **full-audit**: The evidence-graded audit lane — 30 sections against live account data, where these benchmarks get tested rather than assumed.
- **analytics**: GA4 and cross-platform measurement to reconcile Meta-reported purchases against the store's numbers.
- **meta-attribution**: Why Meta and the store never match even with clean wiring, which attribution window to run, and how to prove incrementality.
- **meta-api-reference**: The raw Graph API layer, including the full `user_data` field list and CAPI event schema, in `references/graph-api-schema.md`.
