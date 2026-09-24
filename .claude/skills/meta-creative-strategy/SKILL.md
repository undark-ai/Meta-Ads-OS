---
name: meta-creative-strategy
description: "When the user wants to plan Meta (Facebook/Instagram) ad creative for an e-commerce or D2C brand — creative-as-targeting, customer-situation angles, concept testing, UGC and format strategy, and hook-driven ad copy that drives purchases. Also use when the user mentions 'creative strategy,' 'ad angles,' 'creative concepts,' 'UGC ads,' 'ad hooks,' 'creative testing,' or 'what creative should I run.' For the production and iteration system behind the creative, see creative-cadence-operating-system. For bulk, platform-agnostic ad copy generation, see ad-creative. For format choice, aspect ratios, safe zones and CTA buttons, see meta-creative-formats. For overall e-commerce Meta strategy, see meta-ads."
metadata:
 version: 1.1.0
---

> **Marketing layer — advisory, not evidence.** Every benchmark, threshold and rule of thumb
> below is build-time guidance. Per `CLAUDE.md`, a marketing skill's number is never evidence
> for a quantified finding: a recommendation that originates here still needs a number, source,
> date range, formula, evidence class and confidence from the audit layer before it can be
> presented as one. Handoffs run audit → marketing, never the reverse.


# Creative Strategy for D2C Meta Ads

Creative is the #1 variable for Meta Ads success in e-commerce. Post-Andromeda, creative does double duty: it's both your ad AND your targeting signal. The algorithm processes copy, images, video transcripts, and carousels to decide who sees your ads. Targeting inputs are suggestions; creative is the real filter.

## Before Starting

**Check for product marketing context first:**
If `.agents/product-marketing.md` exists (or `.claude/product-marketing.md`, or the legacy `product-marketing-context.md` filename, in older setups), read it before asking questions. Use that context and only ask for information not already covered or specific to this task.

Gather this context (ask if not provided):
- AOV and contribution margin (needed to set break-even ROAS for judging concept tests)
- Existing customer-voice sources: post-purchase surveys, reviews, support tickets, organic/creator content from the last 12 months

## Core Principle: Creative IS Targeting

The people who engage with your ads tell the algorithm who to find more of. If your creative attracts bargain-hunters who never repurchase, Meta optimizes for them. If it speaks specifically to your ideal customer — their situation, their language, their problem — the algorithm becomes your best targeting tool.

### The Repellent Test

Creative-as-targeting has a self-test: **if someone outside your buyer set saw this ad, would they scroll straight past?** If yes, the creative is doing the filtering. If a generic viewer might plausibly stop, the creative isn't targeting — it's just advertising, and you're paying for the impressions of people who will never buy.

Five ways to make an ad deliberately repel non-buyers:

1. **Name the situation**, not the demographic. "When your toddler wakes up at 5am and you haven't slept since Tuesday."
2. **Name the failed alternative.** "If drugstore retinol wrecked your skin, this is why."
3. **Name the price tier honestly.** "$180. Yes, really. Here's what that buys." Filters out bargain hunters before they cost you a click.
4. **Name the objection.** Lead with the ingredient, material or trade-off a serious buyer already cares about.
5. **Show something only a real user recognizes** — the specific problem state, the specific ritual, the specific packaging detail.

Deliberate exclusion feels like leaving money on the table and is the opposite. Every non-buyer you repel is an impression redirected to someone who might convert.

## Step 1: List Customer Situations (Before Creating Any Ads)

Before touching design tools, list 15-25 customer situations your buyers face. Each is a unique creative angle.

**Example for a skincare brand:**
1. New mom whose skin changed and old products stopped working
2. Shopper burned by three "miracle" products that did nothing
3. Someone with 10 minutes a day who wants a 2-step routine
4. Gift buyer looking for something that feels premium under $50
5. Sensitive-skin customer scared of new products
6. Someone whose dermatologist visit is 4 months out
7. Repeat buyer of a competitor annoyed by price hikes

Most brands test 3-4 generic concepts. Winners test 15+ specific situations and find the 2-3 that resonate with in-market buyers.

**Source situations from:** post-purchase surveys ("what almost stopped you from buying?"), product reviews (yours and competitors'), customer support tickets, UGC comments, community/Reddit/TikTok discussions.

## Step 2: Check Organic Winners First

Audit the last 12 months of organic and creator content: top-performing TikToks/Reels, most-shared posts, review quotes customers screenshot, creator collabs that drove organic sales. **Repurpose organic winners as paid ads** — organic validation means the market already told you the message works. This is free market research.

## Step 3: Test Concepts, Not Micro-Changes

Testing button colors or minor crops wastes budget. Test dramatically different concepts:

| Concept Type | Best For |
|---|---|
| Problem/Solution | Cold traffic, problem-aware buyers |
| Before/After | Visual products, clear outcomes |
| UGC / Founder video | Trust building, cold audiences |
| Meme/Humor | Pattern interrupt |
| Us vs. Them (comparison) | Competitive categories |
| Testimonial / review mashup | Warm audiences, social proof |
| Unboxing / texture / ASMR | Sensory products |
| Offer-led (bundle, GWP, threshold) | Promo periods, retargeting |

**Cadence:** Launch 3-5 dramatically different concepts per batch. Give each 7-10 days and sufficient spend before judging. Winner = best cost per new customer at or under break-even ROAS (AOV ÷ contribution margin) — not CTR or CPC alone. Double down on winning concepts with more variations; kill losers and replace with new concepts. Never stop testing.

## Step 4: Competitive Ad Research

Search competitors in the Meta Ad Library. Ads running 3+ months are likely profitable. Learn the ANGLE and FORMAT, not the exact creative — and don't copy much larger brands who can absorb losses as market capture.

## The Three Pillars

1. **Messaging** — Sell the click, not the whole brand story. Specificity creates urgency: "Fix flat hair in one wash" beats "Better hair care." Call out who the ad is for; name the specific problem, not the category.
2. **Design** — The visual must reinforce the copy, not just look pretty. Build per-placement versions (1:1/4:5 Feed, 9:16 Stories/Reels). Legibility test: understandable in 2 seconds mid-scroll. Pattern interrupts beat polish.
3. **Analysis** — High CTR + low new-customer rate or poor 60-day LTV = attracting the wrong people. Low CTR + strong AOV/repeat rate = too niche (good problem — scale it). Track by concept, not individual ad.

## The Ad Copy Formula

```
1. HOOK/OFFER - lead with the payoff or the deal
2. PAIN - name the specific problem
3. SOLUTION - show the product fixing it
4. PAIN EXPLAINED - cost of living with the problem
5. SOLUTION EXPLAINED - benefits, sensory detail
6. SOCIAL PROOF - review count, star rating, UGC quote
7. CTA - clear next step (Shop Now, Get the Bundle)
```

Compress the first 2-3 lines — most users never tap "See More." For named headline techniques to sharpen the hook line, see ad-headline-techniques.

## Creative Volume and Allocation

Run 4-6 fundamentally different concepts per campaign at any time so the algorithm can learn. Allocate budget 50/30/20: 50% proven winners (scaling), 30% iterations on winners (new hooks/formats), 20% brand-new concepts.

## Angles by Funnel Stage

- **Prospecting (cold):** problem/solution hooks, UGC and creator content, founder story, counterintuitive takes, "TikTok made me buy it" energy.
- **Retargeting (warm):** review mashups, before/after proof, objection-handling ("yes, it works on X"), offer reminders, free-shipping-threshold and bundle nudges.
- **Retention (existing customers):** new product drops, replenishment reminders, subscribe-and-save, cross-sell bundles.

## Variation Sets for Advantage+ and Dynamic Creative

When you hand Meta a pool of copy to permute, the pool's *diversity* is what determines whether the system has anything to learn from.

- **3–5 primary texts differing by angle**, not phrasing: pain, social proof, offer, curiosity. Five rewrites of one sentence give the algorithm nothing.
- **3–5 headlines that pair sensibly with any primary text.** If a headline only makes sense after one specific opener, it isn't a variation, it's a fragment.
- **One funnel stage per ad set.** Mixing cold-traffic education with cart-abandon urgency produces permutations that make no sense to any reader.
- **Retire angle types, not individual lines.** When a set fatigues, the unit that lost is the angle.
- **Never put must-see information only in the description field** — it doesn't render in every placement.

Format selection, aspect ratios, safe zones and CTA-button choice live in **meta-creative-formats**.

## Placements

Feed (1:1/4:5) supports longer copy; Stories/Reels (9:16 with audio) often converts 10%+ better for video-native creative. If you only have 1:1 assets, exclude Stories/Reels rather than running stretched creative. Customize creative per placement at the ad level.

## Related Skills

- **meta-ads**: The e-commerce Meta hub — audience strategy, campaign structure, ROAS and CAC optimization.
- **creative-cadence-operating-system**: The production system — iteration hierarchy, testing volume math, and refresh cadence for the concepts this skill generates.
- **creative-fatigue-detection**: Diagnosing when live creative is dying and when to rotate it.
- **message-validation**: Scoring which ad messages bring profitable customers (by AOV and repeat rate) before scaling them.
- **meta-creative-formats**: Format selection, placement ratios and safe zones, CTA buttons, and the Advantage+ Creative vs Dynamic Creative decision.
- **ad-creative**: Bulk, platform-agnostic ad headline and copy generation at scale.
