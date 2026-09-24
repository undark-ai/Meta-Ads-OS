---
name: meta-third-party-conversion-tracking
description: "When e-commerce or D2C conversions happen off the brand's own domain — hosted checkouts, marketplaces, booking/ticketing platforms, crowdfunding pages, pop-up shop platforms — and Meta still needs the purchase signal. Also use when the user mentions 'hosted checkout,' 'off-domain conversion,' 'checkout on another site,' 'Kickstarter ads,' 'ticketing platform tracking,' 'pixel on a third-party platform,' 'thank-you page redirect,' or 'Meta can't see our purchases.' For tracking on your own domain — pixel, events, domain verification — see meta-setup-and-tracking. For the server-side Conversions API fallback in depth, see meta-capi-and-events. For overall e-commerce Meta strategy, see meta-ads."
metadata:
 version: 1.0.0
---

> **Marketing layer — advisory, not evidence.** Every benchmark, threshold and rule of thumb
> below is build-time guidance. Per `CLAUDE.md`, a marketing skill's number is never evidence
> for a quantified finding: a recommendation that originates here still needs a number, source,
> date range, formula, evidence class and confidence from the audit layer before it can be
> presented as one. Handoffs run audit → marketing, never the reverse.


# Meta Ads - Third-Party / Off-Domain Conversion Tracking (Ecommerce)

When the purchase completes on a **third-party platform** (hosted checkout, subscription billing page, ticketing/booking platform, crowdfunding page, pop-up shop platform) instead of on your own domain, use this for best-practice setup. Applies to anyone running Meta ads where checkout finishes off-domain.

## Before Starting

**Check for product marketing context first:**
If `.agents/product-marketing.md` exists (or `.claude/product-marketing.md`, or the legacy `product-marketing-context.md` filename, in older setups), read it before asking questions. Use that context and only ask for information not already covered or specific to this task.

Gather this context (ask if not provided):

- Which third-party platform completes the purchase, and whether it supports adding your Meta pixel, a post-purchase redirect, or an orders API/webhooks
- Whether the platform passes order value back, and where attribution reporting needs to reconcile (Meta, analytics, post-purchase survey)

---

## The Problem

- User lands on **your site** (product or landing page, with UTMs).
- User clicks "Buy" / "Book" / "Back this project" → goes to a **third-party platform** to complete the purchase.
- The conversion happens **off your domain**. If your pixel is only on your site, Meta never sees the purchase - so it optimizes for clicks, not buyers, and your ROAS reporting is blind.

---

## Best Practice: Two Decisions

### 1. Where to track the conversion (pixel in platform vs thank-you page)

| Option | When to use | What to do |
|--------|-------------|------------|
| **Pixel in the platform** | The platform supports adding your Meta pixel (most hosted checkouts, ticketing, and crowdfunding tools do, sometimes on a paid plan). | Add your Meta pixel in the platform's settings. The platform fires `Purchase` (with value) or `CompleteRegistration` on completion. Add the platform's domain(s) to your Meta pixel **Traffic permissions** (allow list). |
| **Thank-you page on your site** | The platform can't fire your pixel but **can redirect after purchase** to a URL you control. | Set the post-purchase redirect to a thank-you page on your domain. Fire `Purchase` there (pass the order value through the redirect URL if possible). Optimize for that event. |

**Recommendation:** Pixel in the platform is best when available - one setup, real conversion with real value. The thank-you page redirect is the fallback; its weakness is that users who close the tab before redirecting are lost, and value data may be approximate.

If the platform supports neither, the last resort is server-side: pull orders from the platform's API or webhooks and send `Purchase` via **CAPI** with hashed customer email/phone (see meta-capi-and-events for the full setup). Slower to build, but gives Meta the truest signal.

### 2. Passing UTMs (and click IDs) to the checkout link

- The platform will **not** automatically see the UTMs from the page the user was on when they clicked "Buy."
- **Best practice:** the outbound link to the third-party checkout should **carry the same UTM parameters** (and ideally `fbclid`) from the current page.
- **How:** build the link dynamically - read the current query string (`window.location.search`) and append it to the platform URL. Example: `https://platform.com/checkout/xyz` → `https://platform.com/checkout/xyz?utm_source=meta&utm_medium=paid-social&utm_campaign=...&fbclid=...`
- This keeps attribution intact in the platform's reporting, in your analytics, and in any post-purchase survey / order export you use to reconcile Meta's numbers.

---

## Example Setup Pattern

- **Pixel:** In the platform's settings, add your Meta Pixel ID. Confirm which events it sends (typically PageView, InitiateCheckout, Purchase with value for paid transactions). Add the platform's domain(s) - including any short-link domains - to your pixel's Traffic permissions.
- **UTM:** On your product/landing page, a small script appends the current URL's parameters to every checkout link.
- **Verify:** run a test purchase from an ad preview link and confirm the Purchase event appears in Events Manager with the right value and attributes to the campaign. On a connected account you can also confirm event receipt via the Meta Ads MCP (`ads_get_dataset_stats`, `ads_pixel_event_read` — see meta-ads-mcp and capi-and-emq).

---

## Quick Message Template

Use when asking a platform partner (or their team) to enable pixel + UTM pass-through:

Hi [Name],

Quick ask for [product/drop/event name] so we can track purchases properly in Meta:

1. **Meta pixel in [platform]** - If your plan supports it, can you add our Meta pixel in [platform]? ([Where to find it, e.g. Settings → Integrations → Tracking].) That way we get real purchase events with order value and can optimize for buyers, not clicks. We'll allow [platform domain] in our Meta pixel settings on our side.

2. **UTMs on the checkout link** - When someone clicks "Buy" on the page, we need the UTM parameters (from the page they're on) passed through to the [platform] checkout URL. If your team can update the button/link to append the current URL's parameters, attribution stays correct end to end.

Thanks,
[Your name]

---

## Sanity Checks

- Test purchase shows in Events Manager with correct value and currency.
- Platform-side revenue reconciles with Meta-reported purchases (expect some gap; a big gap means the pixel or redirect is broken).
- Purchasers from the platform are excluded from prospecting audiences (upload the customer list if the pixel can't build the audience).

---

## Related Skills

- **meta-setup-and-tracking**: On-domain pixel, events, domain verification, and the launch checklist — the base this skill extends.
- **meta-capi-and-events**: The server-side CAPI path in depth — the last-resort option when the platform supports neither pixel nor redirect.
- **meta-ads**: The e-commerce Meta hub — strategy and optimization once the purchase signal is flowing.
- **meta-audience-strategy**: Building exclusion and retargeting audiences when purchasers come from an off-domain platform.
- **analytics**: Reconciling platform-side revenue, Meta-reported purchases, and your analytics stack.
