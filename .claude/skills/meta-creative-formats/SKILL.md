---
name: meta-creative-formats
description: "When the user wants to choose the right Meta ad format and asset specs for an e-commerce or D2C brand — single image vs video vs carousel vs Collection, aspect ratios and safe zones per placement, CTA button choice, and whether to let Advantage+ Creative or Dynamic Creative build the variations. Also use when the user mentions 'what format should I use,' 'carousel or video,' 'Collection ads,' 'Instant Experience,' 'aspect ratio,' '4:5 or 1:1,' 'safe zone,' 'Reels specs,' 'which CTA button,' 'Advantage+ Creative,' or 'Dynamic Creative.' For the angle, concept and hook behind the creative, see meta-creative-strategy. For production volume and refresh cadence, see creative-cadence-operating-system. For copy character limits across platforms, see ad-creative."
metadata:
 version: 1.0.0
---

> **Marketing layer — advisory, not evidence.** Every benchmark, threshold and rule of thumb
> below is build-time guidance. Per `CLAUDE.md`, a marketing skill's number is never evidence
> for a quantified finding: a recommendation that originates here still needs a number, source,
> date range, formula, evidence class and confidence from the audit layer before it can be
> presented as one. Handoffs run audit → marketing, never the reverse.


# Meta Creative Formats & Specs — D2C E-commerce

Concept decides whether an ad works. Format decides whether the concept survives contact with the placement. A great hook cropped out of the frame on Reels is a wasted production cycle, and most format mistakes in D2C accounts are exactly that mundane.

This skill covers the format decision and the asset specs. It does not cover angles, hooks or concepts — that is meta-creative-strategy.

## Before Starting

**Check for product marketing context first:**
If `.agents/product-marketing.md` exists (or `.claude/product-marketing.md`, or the legacy `product-marketing-context.md` filename, in older setups), read it before asking questions. Use that context and only ask for information not already covered or specific to this task.

Gather this context (ask if not provided):

- **Catalog shape**: one hero SKU, a small range, or a real multi-SKU catalog with a product feed. This determines whether half the formats below are even available.
- **What assets exist**: product photography, UGC video, lifestyle imagery, or nothing yet. The format decision is constrained by what you can actually produce this week.
- **Funnel stage** the creative is for, and **AOV**, since format economics differ between a $30 impulse buy and a $400 considered one.

## Format Selection

| Format | Best for | Notes |
|---|---|---|
| **Single image** | Concept testing, one clear claim, fast iteration | The default for validating a new concept. Cheapest to produce, fastest to kill. Launch concepts here before investing in video — see creative-cadence-operating-system. |
| **Single video** | Demonstration, transformation, UGC testimonial, anything that needs motion to make sense | Highest ceiling and highest production cost. Earn it with a static that already works. |
| **Carousel** | Multi-benefit stories, before/after sequences, range display, objection-handling card by card | 3–5 cards is the practical optimum; more and completion collapses. Card 1 has to work alone. |
| **Collection** | Real catalog with a working product feed, browse-then-buy behavior | Strong for e-commerce with genuine catalog breadth. Weak for a single SKU or a brand with three products — there's nothing to browse. |
| **Instant Experience** | High-AOV or high-consideration purchases needing more explanation before the click | A full-screen post-click canvas. Worth it when the PDP is the friction point, not the ad. Adds a build step most brands skip and shouldn't attempt at low AOV. |

Two rules that override the table:

- **Validate with statics first.** Concept risk and production risk are separate risks. Test the message on an image, then build the video for the messages that survived.
- **Format follows the message.** If the claim needs motion to be credible (a texture, a mechanism, a transformation), a static will underperform for reasons that have nothing to do with the message.

## Format-to-Placement Fit

Build assets per placement group. Do not hand Meta one asset and let it crop.

| Placement | Ratio | Notes |
|---|---|---|
| **Feed** (Facebook, Instagram) | 4:5 or 1:1 | 4:5 claims more vertical scroll real estate than 1:1 and generally wins on mobile. 1:1 is the safer multi-placement compromise. |
| **Reels / Stories** | 9:16 | Full screen. Keep all text and product inside the safe zone — the platform overlays UI at both ends. |
| **Marketplace** | 1:1 | Renders Feed-like; a Feed asset generally carries over. |
| **Audience Network** | Varies by publisher | Least controllable. Judge it on performance, not on how the asset looks. |

**Safe zones on 9:16 are the highest-frequency avoidable error.** The top and bottom of a vertical placement carry platform UI — profile row, caption, CTA, and on Reels a comment and share stack on one side. Keep headline text, price callouts, logos and the product itself out of those bands. A hook rendered behind the caption block is invisible to every viewer.

**The flagship failure: one square asset, all placements.** Supplying a single 1:1 or horizontal asset and letting Meta auto-crop into 9:16 produces bad vertical creative every time — heads cut off, text cropped, product half out of frame. Meta will happily run it. Produce the vertical cut deliberately, or exclude the vertical placements.

For **copy character limits** across primary text, headline and description, see `ad-creative/references/platform-specs.md` — that file is the authority and this skill does not restate it. The one placement rule worth repeating here because it is a format decision: the description field does not render in every placement, so **never put must-see information only in the description.**

## CTA Button Selection

| Goal | Button |
|---|---|
| Direct purchase, product-led ad | `SHOP_NOW`, `BUY_NOW` |
| Cart-building, multi-item catalog ad | `ADD_TO_CART`, `ORDER_NOW` |
| Offer-led ad (discount, bundle, GWP) | `GET_OFFER` |
| Subscription or replenishment | `SUBSCRIBE` |
| Cold-traffic education, high-consideration first touch | `LEARN_MORE` |

`LEARN_MORE` on cold traffic is not weakness. On a first touch for a considered purchase it consistently beats `BUY_NOW`, which asks for a commitment the viewer hasn't been given a reason to make yet. Match the button to the ask the creative actually made.

## Advantage+ Creative vs Dynamic Creative vs Manual Variations

Three overlapping systems. Pick deliberately.

| Approach | What it does | When to use it |
|---|---|---|
| **Manually built variations** | You produce each complete ad | Concept testing, where you need to attribute a result to a specific creative. The only approach that gives clean read-outs. |
| **Dynamic Creative** | Meta combines your supplied images, primary texts and headlines into permutations | Scaling a validated concept across executions. You lose per-variant attribution. |
| **Advantage+ Creative** | Meta applies automatic enhancements — crops, brightness, music, text tweaks, catalog overlays | On proven ads at scale, once you are optimizing delivery rather than learning. Turn enhancements off individually where they break brand or claims. |

Rules:

- **Advantage+ Creative wants at least 5 genuinely distinct** primary texts and headlines. Five rephrasings of the same sentence give it nothing to work with; five different angles do.
- **Diversify by angle, not by phrasing.** Supply 3–5 primary texts that differ by *angle* — pain, social proof, offer, curiosity — and 3–5 headlines that pair sensibly with any of them.
- **One funnel stage per ad set.** Mixing cold-traffic education and cart-abandon urgency in one variation pool produces permutations that make no sense to anybody.
- **Retire angle types, not individual lines.** When a variation set fatigues, the losing unit is the angle, not the sentence.
- **Never let automation carry brand-critical claims.** Auto-generated text tweaks can rephrase a regulated or substantiated claim into one you can't support.

## Common Mistakes

- One asset for every placement, with Meta cropping into vertical.
- Text or product inside the 9:16 safe zone.
- Producing video for an unvalidated concept.
- Running Collection or Instant Experience without the catalog depth to justify them.
- Carousels with more than 5 cards, or a first card that doesn't stand alone.
- Must-see information only in the description field.
- `BUY_NOW` on a cold first touch for a considered purchase.
- Feeding Advantage+ Creative five rephrasings and concluding automation doesn't work.

## Related Skills

- **meta-creative-strategy**: The angle, concept, customer situation and hook. Decide the message there, then choose the format here.
- **creative-cadence-operating-system**: Production volume, the image-first testing sequence, and the refresh pipeline these formats feed.
- **creative-fatigue-detection**: Format-specific lifespans and when to rotate a format out.
- **meta-relevance-diagnostics**: When Engagement Rate Ranking is the failing layer, format-to-placement fit is the usual cause.
- **ad-creative**: Copy character limits per platform, bulk variation generation, and static ad templates.
- **image**: Producing and optimizing the visual assets themselves.
