---
name: meta-offer-strategy
description: "When the user wants to choose or design offers for Meta campaigns for an e-commerce or D2C brand — first-order discounts, bundles, GWP, free-shipping thresholds, starter kits, quiz funnels, subscriptions, and which offer to run at each funnel stage without destroying margin. Also use when the user mentions 'offer strategy,' 'first-order discount,' 'gift with purchase,' 'free shipping threshold,' 'bundle offer,' 'cold traffic won't convert,' or 'what offer should I run.' For platform-agnostic offer design, see offers. For the ad creative that carries the offer, see meta-creative-strategy. For scoring which offers attract profitable customers, see message-validation."
metadata:
 version: 1.1.1
---

> **Marketing layer — advisory, not evidence.** Every benchmark, threshold and rule of thumb
> below is build-time guidance. Per `CLAUDE.md`, a marketing skill's number is never evidence
> for a quantified finding: a recommendation that originates here still needs a number, source,
> date range, formula, evidence class and confidence from the audit layer before it can be
> presented as one. Handoffs run audit → marketing, never the reverse.


# Offer Strategy for D2C Meta Ads

Your ads will never outperform a bad offer — the offer is the #1 lever for campaign success. Meta is a discovery platform, not a search engine: people are scrolling, not shopping. Your offer must match the shopper's awareness stage, justify the action you're asking for, and create urgency (specificity creates urgency by proxy).

**The core rule:** You sell the click. The product page sells the add-to-cart. The cart sells the checkout. Each step only needs to earn the NEXT step.

## Before Starting

**Check for product marketing context first:**
If `.agents/product-marketing.md` exists (or `.claude/product-marketing.md`, or the legacy `product-marketing-context.md` filename, in older setups), read it before asking questions. Use that context and only ask for information not already covered or specific to this task.

Gather this context (ask if not provided):

- AOV, contribution margin per order, and shipping cost — every offer must be checked against break-even ROAS after discount and shipping.
- Repeat-purchase behavior / LTV, so first-order losses can be sized honestly.

## Why "Just Buy It" Fails on Cold Traffic (for considered products)

For higher-AOV or considered purchases, pushing a full-price purchase at first touch underperforms because:

| Problem | Why |
|---|---|
| Intent mismatch | Meta = discovery mode, not "ready to buy" mode |
| Commitment too high | A $150+ first order from an unknown brand isn't an impulse buy |
| Trust gap | No reviews seen, no social proof absorbed, no risk reversal |
| Low volume for optimization | Few conversions → the algorithm can't learn → CAC spirals |

**Exception:** Impulse-priced products (under ~$40), strong offers, or heavily retargeted warm audiences can convert cold in one session.

## Offer Types by Funnel Stage

### Stage 1: COLD — Prospecting

**Goal:** New-customer acquisition at or under break-even ROAS (AOV ÷ contribution margin), plus building pixel/retargeting audiences and the email/SMS list.

| Offer Type | Example | Why It Works |
|---|---|---|
| First-order discount | "15% off your first order" | Classic risk-reducer; gate behind email capture to fund the discount with LTV |
| Starter kit / trial size | "Try the routine — $29 starter set" | Lowers entry price, seeds the replenishment cycle |
| Free shipping threshold | "Free shipping over $50" | Raises AOV while removing the #1 cart objection |
| Bundle | "The complete set — save 25% vs buying separately" | Higher AOV covers CAC; better first experience |
| Quiz funnel | "Find your formula in 60 seconds" | Personalization + email capture + zero-party data |
| Risk reversal | "90-day money-back guarantee" | Removes the trust barrier without discounting |

**What doesn't work cold:** generic "Shop Now" with no angle or proof; deep discounts on unproven creative (attracts deal-seekers with terrible repeat rates); subscriptions as the first ask for most categories.

### Stage 2: WARM — Retargeting

**Audience:** site visitors, video viewers, engagers, cart/checkout abandoners.

| Offer | Example |
|---|---|
| Objection-handling + proof | Review mashups, before/after, "10,000+ five-star reviews" |
| Cart recovery nudge | "Your cart's waiting — free shipping still applies" |
| GWP (gift with purchase) | "Free travel size with any order this week" — urgency without margin-killing discounts |
| Bundle upsell | "Complete the set" to product-page viewers |
| Time-boxed offer | "Ends Sunday" — real deadlines only |

Retargeting is cheap (small audience, high ROAS). Even modest daily budgets create useful "everywhere" presence — but cap frequency and exclude recent purchasers.

### Stage 3: RETENTION — Existing Customers

| Offer | Example |
|---|---|
| Subscribe & save | "Never run out — 15% off on subscription" |
| Replenishment reminder | Timed to product usage cycle |
| Cross-sell / new drop | "You loved X — meet Y" |
| VIP / loyalty early access | Launches and restocks for past buyers first |

## The "No-Brainer" Offer Framework

An offer converts cold traffic when it passes these tests:

1. **Value asymmetry** — does the deal feel clearly better than full price elsewhere?
2. **Differentiated** — can they get the same thing cheaper on a marketplace? (If yes → weak)
3. **Margin-aware** — does the offer still clear break-even ROAS after discount and shipping?
4. **Specific** — "Free 5-piece gift set with orders $60+" beats "great deals inside"
5. **Immediate** — value at checkout, not "points toward a future reward"
6. **Low friction** — offer auto-applies; no hunting for codes

## Offer Strategy by AOV Tier

| Tier | AOV | Cold Offer | Warm Offer | Meta's Role |
|---|---|---|---|---|
| Impulse | <$40 | Direct purchase, strong hook | Cart recovery | Full-funnel conversion |
| Mid | $40-150 | First-order discount, starter kit, quiz | GWP, bundles, proof | Acquisition + retargeting |
| Considered | $150+ | Quiz/lead capture, financing, risk reversal | Proof-heavy retargeting, consultations | Awareness + assisted conversion (watch MER, not just in-platform ROAS) |

### The Staged Offer Path for High-AOV D2C

Above roughly $300 AOV — furniture, mattresses, jewelry, high-end electronics — a single "buy now" offer asks for a decision the buyer isn't ready to make, and the AOV tier table above tells you *what* to offer without telling you in what order. Sequence it:

1. **Free tool or quiz** — a mattress firmness finder, a ring-size guide, a room planner. Zero commitment, captures an email, and segments the buyer for everything downstream.
2. **Guide or comparison content** — how to choose, what the trade-offs actually are, why the cheap option fails. Earns credibility on a decision the buyer knows they can get wrong.
3. **Consult, fitting or design call** — a human touchpoint. Converts at a high rate and is the step most brands skip because it doesn't scale in a spreadsheet.
4. **Sample, swatch or trial** — physical proof. For anything tactile this is the highest-converting step in the whole path.
5. **Full purchase**, with the risk reversal that makes the price survivable: a real trial period, free returns, financing.

Each step is a separate campaign with its own audience and its own conversion event. Judge each on cost per step-completion, and the whole path on new-customer CAC and payback — not on the first step's ROAS, which will look terrible in isolation because it isn't selling anything.

**Where the offer actually gets communicated.** A free-shipping threshold, a bundle or a first-order discount only works if the store surfaces it at the right moment — the threshold on the cart, the bundle on the product page, the discount before the shipping line lands. Designing the offer here and never checking how it renders is the most common way a good offer underperforms. See **product-page-cro** for bundle and cross-sell presentation, and **checkout-cro** for threshold and discount mechanics in the cart.

## Common Mistakes

1. **One offer for every stage** — cold and warm shoppers need different asks
2. **Discount as the only lever** — trains customers to wait for sales; use GWP, bundles, thresholds first
3. **Ignoring contribution margin** — a 25% discount plus free shipping can turn "profitable ROAS" negative
4. **Testing 10 creatives on 1 bad offer** — 10x wasted budget; fix the offer first
5. **No offer ladder** — going straight from unaware to "buy the $200 bundle"
6. **Fake urgency** — evergreen "ends tonight" countdowns erode trust and repeat rates

## Related Skills

- **offers**: Platform-agnostic offer design — value framing, pricing psychology, and offer construction beyond Meta.
- **meta-creative-strategy**: The creative angles and hooks that carry the offer into the feed.
- **message-validation**: Scoring which offers and messages actually attract profitable, repeat customers — not just cheap conversions.
- **meta-ads**: The e-commerce Meta hub — audience strategy, campaign structure, and creative testing across the full suite.
- **lead-capture-optimization**: When the cold offer is email/SMS capture (quiz funnels, giveaways) rather than a purchase.
