# PDP Imagery and Copy

The two things carrying most of the persuasion on a product page. Shoppers cannot touch the product, so the gallery and the copy are the product.

---

## Gallery: the rule

**Every image must answer a customer question.** If you can't name the question, the image is weight, not value — and on a PDP, weight is measured in LCP seconds.

Never recommend "add more images." Recommend the specific images that answer the specific questions this product raises.

Find the questions in: pre-purchase support tickets, review text ("wish I'd known…"), return reasons, and the product's own ambiguities (scale, colour accuracy, what's in the box).

---

## The default sequence

Adapt to the product; don't apply blindly.

| # | Image | Question it answers |
|---|---|---|
| 1 | **Hero** — product clean, front, on neutral ground | What is it? |
| 2 | **In use / on model** | What does it look like in real life? |
| 3 | **Scale / context** | How big is it actually? |
| 4 | **Detail / macro** | What's the material and build quality? |
| 5 | **Alternate angle** — back, side, open | What does the rest of it look like? |
| 6 | **What's included** — everything laid out | What do I actually get? |
| 7 | **Dimension diagram or size chart** | Will it fit? |
| 8 | **Packaging / unboxing** | Is it giftable? Will it arrive protected? |

Category adjustments:

- **Apparel** — on-model on multiple body types, fabric macro, fit on a stated model height, movement video
- **Furniture** — in-room at scale, dimension diagram, material macro, assembly state
- **Technical** — port/connector detail, compatibility diagram, size against a known object
- **Beauty / consumable** — texture/swatch, before-and-after only if substantiable, ingredient list legible, size relative to a hand
- **Food** — prepared and plated, portion size, packaging, ingredient close-up

---

## Gallery specs

| Item | What to check |
|---|---|
| Count | 6–8 for most products. Fewer than 4 is usually a P0; more than 12 dilutes and slows |
| Consistency | Same lighting, background, and crop discipline across the set. A mismatched set reads as untrustworthy |
| Ordering | Hero first. Never lead with packaging, a lifestyle shot that hides the product, or a promo graphic |
| Zoom | Available, and actually higher-resolution — a zoom that upscales the same file is worse than none |
| Thumbnails | Visible without scrolling on desktop; position indicator on mobile |
| Colour accuracy | Does the variant swatch match the image? Colour mismatch is a top return reason |
| Video in gallery | Fine, but not first, and never autoplaying with sound |
| Promo overlays | Badges burned into images can't be updated or translated, and date-stamp the page. Flag them |

**Performance is part of this lens.** The PDP gallery is the most common LCP offender in e-commerce. Check: modern format (WebP/AVIF), `srcset` with sensible widths, correct intrinsic dimensions to prevent layout shift, `fetchpriority="high"` on the hero only, and lazy loading on everything below the fold. A 2MB hero PNG is a conversion defect, not an image-quality choice. See `../../ux-audit/references/ux-defects.md` for measurement.

---

## Copy: the four layers

Separate these explicitly in the audit, and name which layer the page is missing. Most PDPs are heavy on features and empty on outcomes and proof.

| Layer | Definition | Example |
|---|---|---|
| **Feature** | What it has | "Merino wool blend, 17.5 micron" |
| **Benefit** | Why that matters | "Regulates temperature, so it works in both seasons" |
| **Outcome** | What the customer gets | "One jumper you can wear from October to April" |
| **Proof** | Why they should believe it | "Rated 4.7 for warmth across 812 reviews" |

Write it as **Feature → Benefit → Outcome → Proof**. Any claim without a proof layer is a claim the shopper discounts.

---

## What to audit in the copy

| Check | The failure to look for |
|---|---|
| Clarity | Can a stranger tell what the product is from the title and first line alone? |
| Scannability | Wall-of-text paragraphs where three bullets would do |
| Jargon | Unexplained technical terms, internal product names, or spec units with no context |
| Feature-dumping | Specs presented as if they were benefits |
| Differentiation | Nothing that distinguishes this from the cheaper alternative one tab over |
| Repetition | The same benefit restated three times in different words |
| Objection handling | The top three buyer objections unaddressed anywhere on the page |
| Missing information | Things reviews and support tickets prove people need and can't find |
| Generic marketing language | "Premium quality," "innovative design," "perfect for any occasion" — delete and replace with something specific and checkable |
| Voice | Written for the brand's internal audience rather than the buyer |

---

## The value proposition test

The page must answer all six. Name which ones it fails.

1. **What is it?**
2. **Who is it for?**
3. **Why should I care?**
4. **Why this instead of the alternatives?**
5. **Why should I trust this brand?**
6. **Why should I buy now?**

Note on #6: "why now" should come from something real — a shipping cutoff, a genuine seasonal reason, a verified low-stock figure, a stated price change. Manufactured countdowns and invented stock counters answer it dishonestly, damage trust, and in several jurisdictions attract regulatory attention. If the honest answer is "there's no urgency," don't fabricate one.

---

## The benefit summary above the CTA

The three-to-five lines sitting between the price and the variant selector do more work than anything else in the copy. Audit them specifically:

- Strongest benefit **first**, second-strongest **last** — the middle is where attention dips (serial position effect)
- Each line is a benefit or outcome, never a feature
- Each line is specific enough to be falsifiable
- Under about 12 words per line so it survives a mobile viewport
- Total block short enough to sit above the fold on mobile alongside title and price

This block is also the highest-value A/B test on most PDPs, because it's cheap to change and sits directly in the decision path.

---

## Specs and detail

- **Progressive disclosure**, but never hide sizing, compatibility, shipping, or returns behind an accordion — those are decision inputs, not detail
- Spec tables need units and, where they aren't self-evident, context ("17.5 micron — finer than standard merino")
- "What's included" as an explicit list, not implied by photography
- Care, assembly, and usage instructions available pre-purchase, because they're purchase objections
- On mobile, accordion labels must say what's inside; "More information" has no information scent

---

## FAQ

Not a filler section. Populate it from the **actual** top pre-purchase support questions — ask the support team, or read the questions people leave in reviews.

A PDP FAQ answering questions nobody asked, while the real objection goes unaddressed, is a missed opportunity dressed as thoroughness. If FAQ content is genuinely useful, it also earns FAQ structured data — see the `schema` skill.
