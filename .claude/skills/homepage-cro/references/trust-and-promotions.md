# Trust, Promotions, and the Brand/Conversion Balance

The D2C-specific tensions. Getting these wrong doesn't just cost conversion — it costs pricing power.

---

## The brand vs. conversion balance

The defining homepage tension for a D2C brand, and it is a **margin** question, not a taste question.

| Failure mode | Symptoms | What it costs |
|---|---|---|
| **Too conversion-heavy** | Promo bar stack, discount in the hero, urgency badges everywhere, sale-first navigation, aggressive popup | Trains every visitor to wait for a discount. Erodes full-price sell-through and pricing power. The damage is slow and shows up in margin, not in the A/B test |
| **Too brand-heavy** | Beautiful hero with no product, editorial above discovery, no proof above the fold, no clear CTA, product not visible until the third scroll | Visitors admire and leave. Shows up immediately as a low product-view rate from the homepage |
| **Balanced** | Brand voice carries the page while product discovery and proof do the work | |

### How to judge it for a specific brand

| Brand context | Where the balance should sit |
|---|---|
| Premium / identity-led, pricing power to protect | Brand-forward, but product visible above the fold and proof by the first scroll. Promotions restrained and rare |
| Scaling, thin margin, paid-social dependent | Conversion-forward. Discovery and proof early, promotion visible but not the whole message |
| Commodity or price-competitive category | Conversion-led is correct. Price and offer prominence is the positioning |
| New brand, unfamiliar category | Education-forward, but must reach product by the second scroll. A brochure homepage is a failure mode, not a brand choice |
| High repeat / subscription | Returning-customer utility first. Brand-building already happened |

State the recommendation as a balance with a reason, not as "add more brand" or "add more selling." And name what to preserve — a brand-heavy homepage usually has genuinely good assets that a conversion-led rebuild would throw away.

---

## Social proof

### The anxiety framework

Build this table. It's the most useful artifact in the trust section because it forces proof to attach to a real objection.

| Customer anxiety | Current proof | Missing proof | Recommendation |
|---|---|---|---|

Anxieties are **category-specific**. Do not use a generic list:

| Category | The dominant first-purchase anxiety |
|---|---|
| Apparel / footwear | Will it fit? Does the colour match the photo? |
| Beauty / supplements | Will it work? Will it irritate? Is it safe? |
| Electronics / tech | Is it genuine? Is it compatible? What's the warranty? |
| Furniture / homeware | Will it fit the space? What's the delivery like? |
| Food / perishable | Will it arrive fresh? Is it worth the price? |
| Premium / high AOV | Is this worth it? Can I return it if not? |
| Any new brand | Is this a real company that will ship my order? |

### Proof types, ranked by what they do

| Proof | Best for | Placement |
|---|---|---|
| **Aggregate rating + review count** | Universal. The highest-value single trust element | Above or near the fold, and on product cards |
| **UGC / customer photos** | Apparel, homeware, anything where appearance matters | Mid-page, linked to the products shown |
| **Written reviews with specifics** | Answering a named objection | Immediately after the claim they support |
| **Press logos** | Category credibility for newer brands | One compact row. Dated if older than ~2 years |
| **Creator / influencer content** | Younger audiences, social-led brands | Where it routes to product, not as decoration |
| **Guarantee / returns promise** | High-AOV and first-purchase anxiety | Near CTAs and in the value bar |
| **Customer count** | Scale reassurance | Only if current, verified, and dated |
| **Certifications** | Only where the audience knows the certification | Compact, near the relevant claim |
| **Founder / making story** | New brands with no review volume | Mid-page, brief, routing to product |

### Rules

- **Proof goes immediately after the claim it supports**, not collected in a single block at the bottom. Placement beats volume
- Specific beats impressive. "4.7 from 3,412 reviews" beats "loved by thousands"
- Never recommend fabricated, purchased, or sentiment-gated reviews. Beyond the trust damage, the FTC rule on consumer reviews carries civil penalties, and UK/EU consumer law treats fake reviews as a banned practice
- Never recommend invented customer counts, fake live-visitor tickers, or "X people are viewing this" widgets that aren't real
- Remove badge clusters of five or more; they read as compensating
- **Zero-review brands** need a different strategy — costly signals (extended returns, longer warranty), falsifiable specifics, and transparency about the making. See `../../product-page-cro/references/trust-and-proof.md`

---

## Promotional strategy

The question isn't whether promotion works. It's whether it works **net of what it does to full-price sell-through**.

| What to audit | The failure |
|---|---|
| **Promo bar count** | Two or three stacked bars, each with a different message, consuming the mobile fold |
| **Rotating promo bar** | Messages rotating faster than they can be read |
| **Message clarity** | "Up to 40% off selected lines" — the visitor can't tell if it applies to them |
| **Prominence vs. positioning** | Discount as the loudest element on a premium brand's homepage |
| **Repetition** | The same offer in the bar, the hero, a mid-page banner, and the popup |
| **Currency** | Expired offers still displayed — a live trust and support cost |
| **Attention cannibalization** | The promo competing with the primary conversion path rather than feeding it |
| **Urgency honesty** | Countdown timers on evergreen offers; "ends soon" that never ends |
| **Free-shipping threshold** | Not stated, or stated without the amount, so it can't motivate anything |

### Recommendations that usually hold

- **One promo message maximum above the fold.** If there are three offers, the homepage has no offer
- **Free-shipping threshold beats a percentage discount** for most D2C brands — it raises AOV instead of cutting margin, and it doesn't train discount-waiting
- **Value-driven over discount-driven** where the brand has pricing power: lead with the guarantee, the returns promise, or the product benefit, and let the offer be secondary
- **A permanent sale isn't a promotion**, it's a price. Recommend repricing instead, and note that permanent "sale" framing is a common enforcement target
- **Welcome offers** are fine, but consider what they cost: every visitor who would have paid full price and takes a 10% code is margin given away to acquire someone already acquired. Test the offer's presence, not just its size

### Compliance

| Pattern | Flag |
|---|---|
| Strikethrough / "was → now" pricing | The higher price must genuinely have been charged for a defined prior period. Constrained by the EU Omnibus Directive, UK pricing practices guidance, and several US state laws. **Legal review required** |
| "RRP" or "compare at" against a price never charged | High risk. Flag it |
| Countdown timers on offers that don't actually expire | Misleading urgency; actionable in the UK/EU. **Legal review required** |
| Invented stock or viewer counts | Same |
| Undated customer or subscriber counts | Ages into a misleading claim |

Give the UX recommendation, then attach the flag. Never silently recommend a pattern that could be non-compliant.

---

## Email and SMS capture

The most contested element on a D2C homepage. Audit it as a conversion element with a real cost, not as a free win.

| Check | The failure |
|---|---|
| **Trigger timing** | Fires at 2 seconds, before the visitor has seen anything. Maximum interruption, minimum intent |
| **Trigger type** | Time-based on every session, rather than scroll depth, exit intent, or second-page |
| **Returning subscriber suppression** | Re-firing at people already on the list. Pure annoyance with zero upside — check whether suppression exists at all |
| **Dismissibility** | A 12px × in the corner, or no visible close, or a close that reopens |
| **Mobile behaviour** | Full-screen takeover on a first visit — the highest-cost version of this pattern |
| **Value exchange** | "Sign up for our newsletter" with no reason. Either offer something or don't ask |
| **Offer cost** | A 10%-off welcome code given to visitors who would have paid full price. Measure the margin, not just the capture rate |
| **Field count** | Asking for name, birthday, and phone at first contact |
| **SMS consent** | Bundled with email rather than separately and explicitly opted into — a compliance problem as well as a UX one |
| **Interrupting a task** | Firing while a returning customer is mid-navigation |

### Default recommendation

Delay the trigger to scroll depth or exit intent, suppress for known subscribers, keep it to one field, make the close target real, and never full-screen on mobile first visit.

Then **test its presence, not just its design.** Suppressing the homepage popup entirely is a legitimate variant with revenue per session as the primary KPI and email capture rate as the guardrail. Many brands find the trade favourable and have never checked, because capture rate is owned by one team and revenue per session by another.

If the popup is removed or delayed, add an inline capture section lower on the page — it captures the visitors who were going to subscribe anyway, at no interruption cost.

See the `popups` skill for the modal itself: copy, design, and trigger mechanics.
