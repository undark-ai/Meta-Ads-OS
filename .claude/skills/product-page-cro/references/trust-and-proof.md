# Trust and Proof on the PDP

PDP trust is a different problem from checkout trust. At checkout the anxiety is "will my card be safe, when will it arrive, can I return it." On the PDP it's earlier and more specific: **is this product right for me, and is this claim true?**

For payment-moment trust, see `../../checkout-cro/references/trust-payment-shipping.md`. This file covers the product-decision moment.

---

## Reviews

Usually the single most influential element on a PDP after the gallery. Audit the whole system, not just the rating.

| Item | The failure to look for |
|---|---|
| **Count and rating placement** | Not visible near the title. The rating should be in the first viewport on both devices, linked to the reviews |
| **Volume** | Too few to be persuasive. Under ~10 reviews, the count works against you — consider showing the rating without emphasis, or leading with other proof |
| **Recency** | Newest review is two years old. Recency signals the product is still sold and still good |
| **Verified purchase badges** | Absent, so the reviews read as potentially planted |
| **Photos in reviews** | Missing. Customer photos are the highest-trust asset on an apparel or homeware PDP, and they answer colour and scale questions the brand gallery can't |
| **Filtering and sorting** | No way to find reviews from someone with the same use case, size, or concern |
| **Negative reviews** | All-5-star with no criticism reads as filtered and lowers trust. A visible 3-star review with a helpful brand reply raises it |
| **Review content surfaced up-page** | The most useful sentence in the reviews ("runs small," "battery lasts about a day") buried 4000px down instead of quoted near the variant selector |
| **Structured summary** | No attribute breakdown (fit, quality, value) where volume supports one |
| **Widget performance** | A third-party review widget adding seconds to load or shifting layout — a real cost, measure it |
| **Brand replies** | Absent on critical reviews, where a reply does the most work |

### A note on authenticity

Never recommend generating, buying, incentivising-for-positive-sentiment, or selectively suppressing reviews. Beyond the trust damage, fake and gated reviews are directly actionable — the FTC's rule on consumer reviews carries civil penalties, and UK/EU consumer law treats them as banned practices.

Legitimate ways to increase review volume: post-purchase email and SMS requests timed to product delivery plus usage time, incentives offered for *any* review rather than a positive one, photo-upload prompts, and importing reviews across variants of the same product where the platform permits and the relationship is disclosed.

---

## Other proof, ranked by what it actually does

| Proof type | Best used for |
|---|---|
| **Customer photos / UGC** | Colour accuracy, scale, real-world appearance — answers what the studio gallery can't |
| **Video reviews** | High-consideration products where usage is hard to convey |
| **Review-sourced fit signal** | Apparel and footwear. Reduces both hesitation and returns |
| **Aggregate attribute ratings** | Products with multiple decision dimensions (comfort, durability, value) |
| **Expert or press citation** | Technical and premium products, where a named publication carries weight |
| **Certifications** | Only where the shopper knows and values the certification. An unrecognized logo is noise |
| **Sales or ownership counts** | Only if real, current, and dated. "12,000 sold" ages badly without a date |
| **Named testimonials** | B2B and high-ticket. Anonymous testimonials carry almost nothing |
| **Warranty length** | Durability claims — a long warranty is a costly signal, which is why it's believed |

### What to remove

- Badge clusters of five or more logos; they read as compensating
- Unrecognizable or expired certification marks
- Stock "trust seal" graphics not tied to anything real
- Testimonials with no name, role, or photo
- Any counter, timer, or stock figure that isn't live and true

---

## The zero-review problem

New products and new stores have no reviews, and the standard advice is useless to them. Recommend in this order:

1. **Borrow adjacent proof** — reviews of related products, brand-level rating, aggregate store reviews
2. **Substitute a costly signal** — extended returns window, a longer warranty, a satisfaction guarantee. These work precisely because they're expensive to offer falsely
3. **Be specific instead of proven** — falsifiable specifics ("17.5 micron merino, 340gsm") outperform unprovable superlatives when you have no social proof
4. **Show the making** — founder story, materials sourcing, manufacturing detail. Transparency substitutes for volume
5. **Seed legitimately** — send to early customers with a review request for honest feedback, disclose any sampling relationship
6. **Do not** fabricate reviews or display a rating based on a handful of internal ratings

---

## Shipping, returns, and risk reduction

The shopper must resolve all of these **without leaving the page**:

| Question | Where the answer belongs |
|---|---|
| What does shipping cost? | Adjacent to the CTA, or a free-shipping threshold with the gap stated |
| When will it arrive? | A date, next to the CTA. Computed from cutoff and transit, not a vague range |
| Do you ship to me? | Detectable by location, or clearly stated restrictions |
| Can I return it? | Window and whether it's free, one line near the CTA |
| How do exchanges work? | Linked, especially where sizing is a risk |
| What's the warranty? | Stated for durables, near the price or in a compact risk block |
| Are there duties or taxes? | Stated for cross-border, before add-to-cart |
| Who do I ask? | Support route and hours, findable without the footer |

**Name the risks this shopper perceives, then judge whether the page answers each.** Risk perception is category-specific: apparel is fit, electronics is compatibility and authenticity, furniture is scale and delivery, consumables is efficacy and reaction, gifts is arrival date.

Two patterns worth recommending in most audits:

- **Move risk answers adjacent to the CTA.** Shipping, delivery date, and returns in a compact block beside the button, not in the footer or a policy page. This is where the doubt actually occurs
- **Match the reassurance to the price.** A £15 impulse buy doesn't need a warranty block; a £450 considered purchase needs delivery certainty, returns clarity, and warranty stated before the shopper will commit

---

## Pricing presentation and compliance

Price framing is a trust surface, and increasingly a regulated one.

| Pattern | Assessment |
|---|---|
| Clear single price | Safe |
| Strikethrough "was / now" | Requires the higher price to have genuinely been charged for a defined prior period. The EU Omnibus Directive, UK pricing practices guidance, and several US state laws all constrain this. Recommend it only with **Legal review required** attached |
| "RRP" or "compare at" against a price you never charged | High risk. Flag it |
| Permanent "sale" | Erodes trust and is a common enforcement target |
| Per-unit or per-use maths | Genuinely useful on consumables and bulk — recommend freely |
| Subscription pricing | Show both the per-delivery and the effective saving, plus cancellation terms |
| BNPL instalment display | Useful above roughly £75/$75. Must show the total, not only the instalment |

Separate the UX recommendation from the legal question every time. Give the recommendation, then write **Legal review required** where jurisdiction or substantiation is in play — do not silently recommend a pattern that could be non-compliant.
