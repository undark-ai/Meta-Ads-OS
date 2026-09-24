---
name: meta-setup-and-tracking
description: "When the user wants to set up Meta ads tracking for an e-commerce or D2C store — pixel install, purchase funnel events, domain verification, catalog connection, pre-launch audiences, and the implementation checklist for a clean measurement base. Also use when the user mentions 'Meta pixel,' 'Facebook pixel,' 'pixel setup,' 'Events Manager,' 'domain verification,' 'Purchase event not firing,' 'tracking setup,' 'Commerce Manager catalog,' or 'launch my first Meta campaign.' For Conversions API depth — deduplication, middleware, Event Match Quality — see meta-capi-and-events. For purchases that complete off your domain (hosted checkouts, marketplaces), see meta-third-party-conversion-tracking. For overall e-commerce Meta strategy, see meta-ads."
metadata:
 version: 1.1.0
---

> **Marketing layer — advisory, not evidence.** Every benchmark, threshold and rule of thumb
> below is build-time guidance. Per `CLAUDE.md`, a marketing skill's number is never evidence
> for a quantified finding: a recommendation that originates here still needs a number, source,
> date range, formula, evidence class and confidence from the audit layer before it can be
> presented as one. Handoffs run audit → marketing, never the reverse.


# D2C Meta Ads Setup & Tracking - Implementation Guide

Step-by-step setup to run your first e-commerce campaign on Meta. Use this when you already have account access and need to configure tracking, then launch.

## Before Starting

**Check for product marketing context first:**
If `.agents/product-marketing.md` exists (or `.claude/product-marketing.md`, or the legacy `product-marketing-context.md` filename, in older setups), read it before asking questions. Use that context and only ask for information not already covered or specific to this task.

Gather this context (ask if not provided):

- Store platform (Shopify, WooCommerce, BigCommerce, custom) — it determines the recommended pixel install path
- Whether any pixel or events are already firing, and which domain(s) receive ad traffic

## Where Things Live in Meta

| What you need | Where to go |
|---------------|-------------|
| Pixel, events, data sources | **Events Manager** (Ads Manager → All Tools → Events Manager) |
| Create and run campaigns | **Ads Manager** (campaigns, ad sets, ads) |
| Domain verification, business assets | **Business Settings** (business.facebook.com → Settings) |
| Product catalog, feeds, product sets | **Commerce Manager** (catalog for dynamic/Advantage+ catalog ads) |

---

## 1. Create and Install the Meta Pixel

1. **Events Manager** → Data Sources → **Add new data source** → **Website** → **Meta Pixel** → name it (e.g. "[Store] - Main Website") → note the **Pixel ID**.
2. Install the base code on **every page** (not just the order confirmation page):
 - **Platform integration (recommended):** Shopify, WooCommerce, BigCommerce, Webflow etc. all have native Meta integrations via **Set up → Use a partner**. These usually install standard ecom events automatically.
 - **Google Tag Manager:** Custom HTML tag with the base pixel code, fire on All Pages.
 - **Manual:** paste the `fbq('init')` + `fbq('track', 'PageView')` block into the global `<head>`.
3. **Verify it fires:** Events Manager → **Test events**, or the Meta Pixel Helper extension. To check the dataset/pixel from a connected account, use the Meta Ads MCP (`ads_get_datasets`, `ads_get_dataset_stats` — see meta-ads-mcp and capi-and-emq). Until the pixel fires, don't rely on Meta for optimization or retargeting.

**Pro tip:** Pay two freelancers $20 each to independently verify your pixel and events. $40 is cheap insurance against burning thousands optimizing on broken tracking. Even experienced media buyers miss technical setup issues.

---

## 2. Set Up Conversion Events

The base code sends PageView only. For ecommerce you need the standard purchase funnel:

- **ViewContent** - product page view (with `content_ids`)
- **AddToCart** - add to cart
- **InitiateCheckout** - checkout started
- **Purchase** - order completed, with **`value` and `currency`** (required) and `content_ids`. This is your optimization event.

Fire Purchase when the order **actually completes** (confirmation page or server callback), not on button click. Platform integrations handle this; in GTM, one tag per event triggered on the relevant page/dataLayer event.

**Event prioritization:** if events share a page, set priority in Events Manager so Purchase ranks above upper-funnel events. Meta uses this for optimization and attribution.

---

## 3. Domain Verification

Required for reliable conversion matching. **Business Settings** → **Brand Safety** → **Domains** → **Add** → verify via DNS TXT record, meta tag in `<head>`, or HTML file upload. Can take minutes to 72 hours. Verify every root domain you send ad traffic to, before scaling spend.

---

## 4. Conversions API (CAPI) - Strongly Recommended for Ecom

Ad blockers and iOS privacy features drop browser events; CAPI sends the same events server-side so Meta sees more of your real purchases.

- **When:** after the pixel and Purchase event are firing. Especially valuable if your store's order count is meaningfully higher than Meta-reported purchases.
- **How:** most platforms (e.g. Shopify's native integration) ship pixel + CAPI together. Otherwise: Events Manager → Pixel → Settings → Conversions API.
- **Deduplication:** same `event_id` on the pixel and CAPI versions of the same event so Meta counts each purchase once.

You can launch pixel-only and add CAPI later, but do it before scaling. For the full CAPI playbook — event hierarchy, platform-native vs middleware, Event Match Quality — see meta-capi-and-events.

---

## 5. Catalog (for Dynamic and Advantage+ Catalog Ads)

- Commerce Manager → create a catalog → connect a product feed (platform sync or feed file).
- Connect the pixel as the catalog's event source so ViewContent/AddToCart/Purchase pass `content_ids` that match the feed.
- Check catalog diagnostics: missing images, prices, or mismatched IDs kill dynamic retargeting.

---

## 6. Audiences You Need Before the First Campaign

- **Retargeting:** Custom Audiences from website traffic (30/90/180-day visitors), plus event-based segments: viewed product, added to cart, initiated checkout - each excluding purchasers.
- **Exclusions:** recent purchasers (e.g. 30-180 days depending on repurchase cycle) excluded from prospecting so you don't pay to acquire existing customers.
- **Prospecting seeds:** customer list upload (hashed emails/phones) for lookalikes and as the seed signal for Advantage+ shopping's "existing customer" definition.

---

## 7. Running Your First Campaign - Checklist

| Step | What to do |
|------|------------|
| 1 | Start with **retargeting** (cart abandoners + product viewers). Objective **Sales**, optimize for **Purchase**. Small daily budget. |
| 2 | Then add **prospecting** - broad or Advantage+ shopping, still optimizing for Purchase, purchasers excluded. |
| 3 | Use **4-6 distinct creative concepts** (UGC, problem/solution, offer, social proof) - not micro-variations. Copy must make clear who the product is for. |
| 4 | **Placements:** Advantage+ default is fine if you have 1:1, 4:5, and 9:16 assets. |
| 5 | **Naming:** clear convention, e.g. `[Product] - Retargeting - ATC 14d` / `[Product] - Prospecting - Broad`. |
| 6 | **Launch, then test:** place a test order and confirm the Purchase event (with correct value) shows in Events Manager and matches your store's order. |

---

## 8. Pre-Launch Quick Reference

- [ ] Pixel installed on all pages and firing
- [ ] ViewContent / AddToCart / InitiateCheckout / Purchase firing on completion, with value + currency + content_ids
- [ ] Event prioritization set
- [ ] Domain(s) verified
- [ ] CAPI live (or planned before scaling) with deduplication
- [ ] Catalog synced and connected to the pixel
- [ ] Retargeting audiences built; purchasers excluded from prospecting
- [ ] Test order visible in Events Manager and matching the store's order value

---

## 9. Troubleshooting

Four tables covering the failures that actually happen. Work from the symptom, not from the checklist.

### Pixel not firing

| Symptom | Likely cause | Fix |
|---|---|---|
| No events at all in Events Manager | Snippet missing from the theme, or removed by a theme update or app uninstall | Re-install, then verify with the Meta Pixel Helper on a live page — not on a preview URL |
| Events fire on some pages, not others | Snippet lives in a template that not every page uses | Move it to the base layout; check the checkout and thank-you templates separately, since many platforms render those outside the main theme |
| Purchase fires but with no `value` | The template passes the order total as a formatted string, or the variable is empty on first render | Log the payload; send a raw number, no currency symbol or thousands separator |
| Events duplicate from the browser alone | Pixel installed twice — once by an app, once manually | Check for two base codes; remove one |
| Events fire in your browser, not in aggregate | An ad blocker or consent banner suppresses them for most real visitors | Expect this; it is the reason CAPI exists, not a bug to chase |

### CAPI issues

| Symptom | Likely cause | Fix |
|---|---|---|
| Duplicate conversions | Mismatched `event_id` between pixel and server for the same order | Use the store's order ID as `event_id` on both sides |
| Events delayed by hours | The platform or CRM is batching, or sending on a nightly job | Send on the order webhook, on stage change, not on a schedule. Freshness feeds the learning phase |
| Events rejected silently | Unhashed PII in a field that requires a hash, or a malformed `event_time` | Test Events with a `test_event_code`, plus the Payload Helper |
| EMQ good in test, poor in production | The test payload was hand-built with full user data; production sends less | Compare a real production payload against the test one field by field |
| Server events arrive, pixel events do not | Consent gating blocks the browser event but not the server call | Correct behaviour, but dedup can no longer pair them — expect a reporting shift, not an error |

### Domain verification

| Symptom | Likely cause | Fix |
|---|---|---|
| Verification stuck on Pending | TXT record on a subdomain instead of the root, or DNS not propagated | Publish the TXT at the root domain and allow up to 72 hours |
| Verified but events attributed to another domain | Events fire on a subdomain or a checkout host you did not verify | Verify every domain that fires events, including the checkout host |
| Can't verify — someone else owns the domain | The domain is claimed in another Business Manager | Resolve ownership in Business Manager; DNS alone will not override a claim |
| Verified, but event priority unavailable | Priority is set per verified domain; you are looking at the wrong one | Set the ladder on each verified domain separately |

### Third-party and hosted checkouts

| Symptom | Likely cause | Fix |
|---|---|---|
| No Purchase event at all | Checkout completes on a domain you don't control and can't script | Use the CAPI-from-backend path — see meta-third-party-conversion-tracking |
| Purchase fires with no value | The hosted platform's redirect drops order parameters | Send the value server-side from the order record instead of the redirect |
| Attribution lost between your site and checkout | The checkout host strips URL parameters, including `fbclid` | Capture `fbclid` on your domain, persist it with the order, and send it as `fbc` on the server event |
| Marketplace sales invisible | Marketplaces don't expose per-order attribution | Accept it, and measure with MER plus a post-purchase survey — see meta-attribution |

---

## Related Skills

- **meta-capi-and-events**: Conversions API depth — event hierarchy, deduplication, middleware choice, and Event Match Quality.
- **meta-third-party-conversion-tracking**: When the purchase completes off your domain (hosted checkouts, marketplaces, ticketing) and Meta still needs the signal.
- **meta-ads**: The e-commerce Meta hub — audience strategy, campaign structure, and ROAS/CAC optimization once tracking is live.
- **meta-campaign-creation**: The step-by-step build chain for the first live purchase campaign after this setup.
- **analytics**: Cross-platform measurement (GA4 etc.) to reconcile against Meta-reported conversions.
- **meta-attribution**: Why Meta and the store never match, which attribution window to run, and how to measure incrementality.
- **paid-measurement-readiness**: Whether the account is measurable enough to scale, scored, before you add budget.
