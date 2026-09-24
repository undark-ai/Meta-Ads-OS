# PDP Audit Protocol

The full walk, plus the blueprint you produce from it.

---

## Phase 0 — Setup

Establish before touching the page:

- Product URL, brand, category
- Platform, and which PDP sections are theme-editable, app-injected, or hard-coded
- Product type: considered vs. impulse; needs sizing, compatibility, or configuration?
- Price point and margin
- Traffic mix landing on this page
- Supplied artifacts: analytics, heatmaps, recordings, review exports, return reasons, support tickets, prior tests

Use everything supplied. Name every gap rather than filling it with an assumption dressed as fact.

---

## Phase 1 — The live walk

Run twice: desktop 1440px, mobile 375px. Log an observation at each step with the viewport attached.

| # | Step | What to record |
|---|---|---|
| 1 | Above the fold | Screenshot before any scroll. What's visible: image, title, price, summary, CTA, trust, reviews? |
| 2 | Gallery | Image count, click every thumbnail, test zoom, swipe on mobile, note load behaviour and any blur/pop-in |
| 3 | Title | Read it cold — is the product comprehensible without category context? |
| 4 | Price | Visibility, hierarchy, sale vs. original, discount framing, per-unit or subscription pricing |
| 5 | Summary | Does the copy above the variant selector carry the value proposition, or is it filler? |
| 6 | Variants | Select each option. Does price change? Availability? Gallery? URL? Is the default sensible? |
| 7 | Quantity | Control type, min/max, keyboard entry, whether bulk discounts surface |
| 8 | Stock status | In stock, low stock, out of stock, per-variant. Is a back-in-stock capture offered? |
| 9 | Shipping message | Cost, threshold, delivery estimate — present or absent at the decision point? |
| 10 | Add to cart | Click it. What confirms? Drawer, toast, redirect, page jump, nothing? |
| 11 | Full scroll | Description, specs, reviews, video, FAQ, cross-sell, footer — in what order, at what depth? |
| 12 | Reviews | Count, rating, recency, verified badges, photos, filter/sort, and read the actual text |
| 13 | Edge states | Out-of-stock variant, quantity above stock, unavailable region |
| 14 | Interruptions | Popups, promo bars, chat, newsletter prompts, cookie notices, floating widgets — note trigger and timing |

Stop and note anything you couldn't test, and why.

---

## Phase 2 — Product and customer context

| Question | Why it changes the audit |
|---|---|
| Considered or impulse? | Considered needs proof and specs; impulse needs speed and clarity |
| Does it need sizing or fit? | Sizing guidance moves both conversion and return rate |
| Does it need compatibility checking? | A compatibility tool can be the single biggest lever |
| Price point | High price justifies more reassurance and more images |
| First-time or repeat buyers? | First-time is a trust problem; repeat is a speed problem |
| Cold or warm traffic? | Paid social lands cold and needs the value prop restated on the PDP |
| Review volume | Zero-review products need a different proof strategy entirely |
| Return rate and reasons | Return reasons name the exact page gaps — the highest-signal data available |

State the implications, don't just list the facts. "A £180 considered purchase landing cold from Meta with 4 reviews means the page's job is proof and risk reversal, not gallery polish" is analysis.

---

## Phase 3 — The 10-second test

For each viewport, look only at the above-fold frame and answer:

1. **What is this?**
2. **Why might I want it?**
3. **What does it cost?**
4. **What do I do next?**

Report which fail and on which viewport. Mobile commonly fails #2 and #3 because a full-bleed gallery consumes the fold and pushes the title, price, and summary below it.

This is the highest-leverage single check in the audit. Treat any failure as P0.

---

## Phase 4 — Information architecture

Record the **current** section order top to bottom, then design the **ideal** order for this product.

There is no canonical sequence. Choose by what the decision needs:

| Product type | Order the decision needs |
|---|---|
| **Apparel** | Gallery → title/price → size + fit guidance → fabric/care → reviews with photos → returns → styling cross-sell |
| **Technical / component** | Gallery → title/price → compatibility check → key specs → what's included → reviews → detailed specs → support |
| **Consumable / beauty** | Gallery → title/price → benefit + ingredients → how to use → results proof → subscription option → reviews |
| **Furniture / large item** | Gallery in context → title/price → dimensions + scale → materials → delivery + assembly → reviews → returns |
| **Gift / impulse** | Gallery → title/price → single strong benefit → CTA → reviews → shipping cutoff for gifting |

Whatever you recommend, the rules that hold:

- Everything needed for the buy/don't-buy decision goes above or immediately around the CTA
- Detail the shopper *may* want goes below, in progressive disclosure
- Proof appears immediately after the claim it supports, not only in a review block at the bottom
- The CTA repeats at each natural decision point on long pages
- Never make the shopper leave the page for shipping cost, returns, or sizing

---

## Phase 5 — Ideal PDP blueprint

Write it section by section. For each: what should appear, what should disappear, what should move, what should be simplified, what should be emphasized.

A defensible default for a considered purchase:

| # | Section | What belongs here |
|---|---|---|
| 1 | Header | Minimal. Search and cart, no promo stack pushing content down |
| 2 | Gallery | 6–8 purposeful images, hero first, zoom available, thumbnails visible without scroll on desktop |
| 3 | Title + rating | Product name a stranger understands, star rating and review count linking to reviews |
| 4 | Price | Unambiguous. Sale framing honest and compliant. Subscription/per-unit maths shown |
| 5 | Value summary | 3 benefit lines — the strongest first and last (serial position), not a feature dump |
| 6 | Variants | Clear labels, sensible default, swatches over dropdowns, availability per option, sizing/compatibility help inline |
| 7 | Quantity + CTA | One primary action. Buy Now only if it genuinely shortens the path |
| 8 | Fulfilment + risk | Delivery estimate as a date, shipping cost or threshold, returns window, warranty — one compact block adjacent to the CTA |
| 9 | Payment reassurance | Wallets and BNPL indication if offered, so affordability is visible before checkout |
| 10 | Detail | Description, what's included, how to use, specs — progressive disclosure, scannable |
| 11 | Demonstration | Video or interactive demo where it answers a real objection, placed at that objection |
| 12 | Proof | Reviews with photos, filterable, recent, verified; UGC; press or certifications if genuine |
| 13 | FAQ | The actual top pre-purchase support questions, answered |
| 14 | Cross-sell | Accessories and completions, below the decision, never competing with the CTA |
| 15 | Repeat CTA | Final add-to-cart with price and delivery restated |

---

## Phase 6 — Mobile blueprint

Write separately. Not the desktop list reflowed.

| # | Section | Mobile-specific requirement |
|---|---|---|
| 1 | Header | Minimal, no stacked promo bars stealing the fold |
| 2 | Gallery | Capped height so title, price, and a benefit line share the fold. Swipe with visible position indicator, tappable zoom |
| 3 | Title + price + rating | Must be in the first viewport. This is the most common mobile PDP failure |
| 4 | Value summary | One or two lines, not a collapsed accordion |
| 5 | Variants | Swatches and chips, not dropdowns. Tap targets ≥44×44px, availability visible per option |
| 6 | CTA | Sticky bottom bar with price and selected variant, above the safe-area inset |
| 7 | Fulfilment + risk | One compact line near the CTA |
| 8 | Detail | Accordions — but never bury shipping, returns, or sizing behind one |
| 9 | Reviews | Lazy-loaded, but the rating and count visible near the top |
| 10 | Interruptions | Audit every popup and floating widget for what it covers on a 375×667 viewport |

Mobile failures to look for specifically: gallery consuming the entire fold; price below the fold; variant dropdowns; sticky CTA hiding content or the last review; a review widget adding seconds to load; chat and accessibility widgets overlapping the CTA; accordion depth burying decision-critical information.

---

## Phase 7 — Desktop vs. mobile comparison

| Element | Current desktop | Current mobile | Recommended desktop | Recommended mobile |
|---|---|---|---|---|

Fill only meaningful differences. Do not assume the two should be identical — and do not assume they should differ where there's no reason.

---

## Phase 8 — Competitive benchmark

Review 3–5 comparable PDPs plus 2–3 best-in-class ones in the category.

Compare: gallery depth and sequence, copy structure, trust treatment, review presentation, variant UX, CTA, shipping and returns visibility, mobile layout, cross-sell.

Answer: **what do excellent PDPs in this category consistently do that this page does not?** Patterns across several are signal; one competitor's choice is noise. Never copy because they're bigger.

---

## Phase 9 — Synthesis

1. Cognitive load scorecard with justifications
2. Prioritized roadmap by Impact × Confidence ÷ Effort
3. Top 15 changes, ranked
4. Ideal desktop and mobile blueprints
5. Desktop vs. mobile table
6. A/B roadmap — see `experiments.md`
7. Measurement plan — see `measurement.md`
8. 30-day action plan: concrete steps, each with an owner type and a success signal

Executive summary is written last and goes first.
