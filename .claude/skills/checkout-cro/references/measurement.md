# Checkout Measurement

Most checkout audits stall because nobody can say where the drop-off is. This is the instrumentation that makes the next audit a data exercise instead of a guessing exercise.

---

## Event spec

Fire these as distinct events, each with the properties listed. Naming follows the GA4 / common e-commerce convention; adapt to the destination but keep the granularity.

| Event | Fires when | Key properties |
|---|---|---|
| `view_cart` | Cart page or drawer opens | `value`, `currency`, `items[]`, `item_count` |
| `begin_checkout` | Checkout first renders | `value`, `currency`, `items[]`, `coupon` |
| `checkout_contact_completed` | Contact step validated | `has_marketing_consent` |
| `add_shipping_info` | Shipping address validated | `shipping_country`, `used_address_autocomplete` |
| `shipping_method_selected` | Delivery option chosen | `shipping_tier`, `shipping_cost`, `was_default` |
| `add_payment_info` | Payment step reached | `payment_type` (card / wallet / bnpl / other) |
| `payment_error` | Payment attempt fails | `error_code`, `error_type`, `payment_type`, `attempt_number` |
| `purchase` | Order confirmed | `transaction_id`, `value`, `tax`, `shipping`, `coupon`, `items[]`, `payment_type`, `is_new_customer` |
| `coupon_opened` | Coupon field expanded | — |
| `coupon_applied` | Code accepted | `coupon`, `discount_value` |
| `coupon_failed` | Code rejected | `coupon`, `failure_reason` |
| `upsell_viewed` | Offer rendered | `offer_id`, `placement` |
| `upsell_accepted` | Offer added | `offer_id`, `placement`, `incremental_value` |
| `upsell_dismissed` | Offer declined or ignored on step exit | `offer_id`, `placement` |
| `checkout_field_error` | Any field validation fails | `field_name`, `error_type` |
| `checkout_abandoned` | Session ends after `begin_checkout` without `purchase` | `last_completed_step` |

Two events teams routinely skip and shouldn't:

- **`payment_error`** with a real error code. Decline distribution often reveals a configuration problem that no amount of UX work will fix.
- **`checkout_field_error`** with the field name. This is how you find the one field that's quietly costing you orders.

---

## Segmentation

A blended checkout completion rate hides almost everything worth knowing. Segment every funnel by, at minimum:

- **Device** — desktop vs. mobile vs. tablet. Non-negotiable; they behave as different products
- **New vs. returning customer**
- **Traffic source and campaign** — paid social converts differently from email
- **Payment type** — wallet vs. card vs. BNPL completion rates diverge sharply
- **Geography** — surfaces payment-coverage and duties problems
- **Order value band** — friction tolerance rises with value
- **Product or category**
- **Browser and OS** — where genuinely broken checkouts hide (in-app browsers especially: Instagram, Facebook, TikTok webviews break wallets and autofill routinely)

**Check in-app browser traffic specifically.** On paid-social-heavy stores this can be a large share of sessions with a materially worse completion rate, and it is a common invisible P0.

---

## The five metrics to watch

Everything else is diagnostic. These five are the scoreboard.

| Metric | Definition | Why it's on the list |
|---|---|---|
| **Revenue per visitor** | Total revenue ÷ sessions | The only metric that can't be gamed by trading one part of the funnel for another |
| **Checkout completion rate** | `purchase` ÷ `begin_checkout` | The direct measure of what this skill optimizes |
| **Cart → checkout start rate** | `begin_checkout` ÷ `view_cart` | Isolates cart-page problems from checkout problems |
| **Step-to-step drop-off** | Each step ÷ the previous, by device | Tells you *where*, which is the entire point |
| **Payment error rate** | `payment_error` ÷ `add_payment_info` | The leak most stores don't know they have |

Guardrails to track alongside, so a completion win isn't a revenue loss: return rate, refund rate, shipping margin, payment fees, and support ticket volume.

---

## Qualitative instrumentation

Numbers tell you where; these tell you why.

- **Session recordings filtered to abandoned checkouts.** Watch fifteen. You will usually find the problem in the first five. Filter to mobile, and to sessions containing a `checkout_field_error`
- **Rage-click and scroll heatmaps on the checkout.** Rage clicks concentrate on non-interactive elements customers expect to be interactive, and on failing validation
- **Exit survey on the cart page** — one question: "What's stopping you from completing your order?" Free-text. Run it for a week
- **Post-purchase survey** — "Was there anything that almost stopped you from buying?" The answers from people who *did* buy describe the friction that stopped the ones who didn't
- **Support ticket review.** Search tickets for "couldn't check out," "payment," "code." Support already knows what's broken

---

## Diagnosing before recommending

When analytics exist, run this sequence before writing any recommendation:

1. **Completion rate by device.** If mobile is more than ~30% below desktop relative, the audit is a mobile audit
2. **Step-to-step drop-off, mobile and desktop separately.** Find the single worst transition
3. **Completion by payment type.** A wallet completion rate far above card suggests the card form or the form length is the problem
4. **Payment error rate and decline codes.** Rule out a processor or 3DS configuration issue before touching design
5. **Completion by browser.** Isolate in-app webviews
6. **Field-level error rates.** Find the one field generating disproportionate errors
7. **Coupon-open rate vs. application rate.** A high open rate with a low application rate means the field is prompting code-hunting

Then write the audit against what you found, and say which findings came from data and which from the structural walk.

---

## Setup notes

- **GA4** gives you the enhanced e-commerce funnel out of the box on Shopify, but the intermediate steps (`checkout_contact_completed`, `shipping_method_selected`, field errors) need adding. Without them the funnel jumps from `begin_checkout` to `add_payment_info` and tells you nothing useful
- **Stripe** is the source of truth for decline reasons and payment method mix — richer than any front-end event
- **PostHog / Mixpanel / Amplitude** are better than GA4 for step-level funnels and for segmenting by arbitrary properties
- **Hotjar** for recordings and heatmaps filtered to abandonment
- On stock Shopify checkout, custom event injection is limited outside Plus / Checkout Extensibility. Say what's achievable on the user's plan rather than specifying events they can't fire

See `tools/integrations/` for setup details on each, and `../../analytics/SKILL.md` for the broader tracking plan.
