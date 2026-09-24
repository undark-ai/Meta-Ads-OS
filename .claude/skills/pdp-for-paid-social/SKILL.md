---
name: pdp-for-paid-social
description: When auditing a product page that receives cold Meta traffic — hero continuity, above-fold offer, review placement, variant selection and the add-to-cart moment on mobile. Use when the funnel leaks between product view and add-to-cart, or when the user asks "why isn't my product page converting" for paid social specifically. For the general e-commerce product page, see product-page-cro; this covers what differs when the visitor arrived from an ad.
---
# PDP for paid social

`product-page-cro` covers the product page. This covers what changes when the visitor arrived
from an interruption rather than a search — and it changes more than most teams assume.

A PDP optimised for someone who searched the product name is being asked to do a different job:
that visitor already knows what the product is, has compared alternatives, and is deciding. The
paid-social visitor learned of the product forty seconds ago from a video.

## What differs

| | Search visitor | Paid-social visitor |
|---|---|---|
| Knows the product | Yes | No — only what the ad said |
| Knows the category | Usually | Often not |
| Compared alternatives | Frequently | No |
| Arrived expecting | This product | Whatever the ad promised |
| Needs the page to do | Confirm and close | **Explain, then convince, then close** |

The practical consequence: a paid-social PDP has to carry an explanation the search PDP can
skip, and it has to carry it above the fold without turning into a landing page.

## The first screen

1. **The hero image continues the ad.** If the ad was UGC in a kitchen and the PDP opens on a
   white-background studio shot, the visitor has to re-recognise the product. Some do not.
2. **What it is, in a sentence.** Not the brand tagline. What the object does.
3. **Price, and the ad's offer**, at the price the ad named. If the ad said €20 off and the page
   shows full price with a code applied later, the visitor believes they were misled.
4. **One proof element** — review count and rating is usually enough. Preferably the same proof
   type the ad used.
5. **Add to cart, visible without scrolling** at a phone viewport inside the in-app browser
   chrome, which is shorter than a designer's mobile mock.

## Reviews

The paid-social visitor has no prior trust, so reviews do more work here than on a search PDP.

- **Rating and count above the fold**; the reviews themselves can be deep in the page.
- Reviews that address the objection the ad raised are worth more than the highest-rated ones.
- Photo reviews outperform text for products where fit or appearance matters.
- A low count is better shown honestly than hidden. Hiding it reads as absence.

## Variants

Variant selection is where mobile PDPs lose people quietly.

- Pre-select the most common variant rather than requiring a choice before the price resolves.
- If the ad featured a specific variant, land on **that** variant. An ad for the blue one landing
  on a default grey is a continuity break.
- Out-of-stock variants shown as selectable, then failing at add-to-cart, is a real and
  frequently-missed leak — cross-check against §16's out-of-stock exposure.

## Cost transparency

Shipping cost discovered at checkout is the most common cart-abandonment cause. On paid social
it is worse, because the visitor has less invested and abandons more readily.

State shipping cost, or the free-shipping threshold, **on the PDP**. If there is a threshold, say
how far the current cart is from it — that is a merchandising lever as well as a trust one
(`offers`).

## The add-to-cart moment

- Sticky ATC on mobile once the primary button scrolls out of view.
- The button says what happens next. "Add to cart" and "Buy now" set different expectations, and
  a "Buy now" that opens a cart drawer breaks one.
- No interstitial between intent and cart. A popup firing on ATC is the worst possible timing
  (`popups`).

## Auditing it

Through the ad's real link, at a phone viewport, in the in-app browser, cold, on the
highest-spend destinations. Record the specific element at fault, not an impression: "the ad's
€20-off claim does not appear above the fold on mobile; first mention is at 1,400px scroll
depth" is a finding.
