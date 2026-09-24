---
name: message-validation
description: "When the user wants to validate which ad messages actually drive profitable customers for an e-commerce or D2C brand — scoring ads by new-customer value, AOV, and repeat rate instead of CTR or CPA, then scaling only the validated messages. Also use when the user mentions 'message validation,' 'which ads actually make money,' 'customer quality by ad,' 'low CPA but bad customers,' 'ad-level LTV,' or 'scaling winning ads.' For general experiment design, see ab-testing. For generating the creative angles to test, see meta-creative-strategy. For overall e-commerce Meta strategy, see meta-ads."
metadata:
 version: 1.1.0
---

> **Marketing layer — advisory, not evidence.** Every benchmark, threshold and rule of thumb
> below is build-time guidance. Per `CLAUDE.md`, a marketing skill's number is never evidence
> for a quantified finding: a recommendation that originates here still needs a number, source,
> date range, formula, evidence class and confidence from the audit layer before it can be
> presented as one. Handoffs run audit → marketing, never the reverse.


# Message Validation & Ad Scaling — D2C E-commerce

How to identify your true top-performing ads — not by CTR or in-platform CPA, but by the value of the customers they bring in — and systematically scale what works.

## Before Starting

**Check for product marketing context first:**
If `.agents/product-marketing.md` exists (or `.claude/product-marketing.md`, or the legacy `product-marketing-context.md` filename, in older setups), read it before asking questions. Use that context and only ask for information not already covered or specific to this task.

Gather this context (ask if not provided):
- AOV, contribution margin, and typical 60-day repeat rate (needed to compute new-customer contribution)
- Whether order data can be joined back to the ad/ad set that acquired each customer (post-purchase survey, UTMs, platform attribution)

## Why Message Validation Matters

Standard Meta metrics don't tell you which ads drive profit. An ad with a $18 CPA and 2.4% CTR might acquire one-time deal-seekers who return half their orders. An ad with a $40 CPA and 1.2% CTR might bring full-price buyers who subscribe and reorder for a year. You must validate ads against **downstream customer quality**, not platform metrics.

## The Validation Process

### Phase 1: Launch Initial Ads (First 2-4 Weeks)

**Before creating ads, list 15-25 customer situations** your buyers face. Each becomes a creative angle.

Example for an apparel brand: the shopper whose current brand keeps shrinking in the wash; the gift buyer with a deadline; the person between sizes who's been burned by returns; the customer who found you on TikTok and wants proof it's legit; the loyalist of a competitor annoyed by a price hike — and 10-20 more.

The more situations you test, the better your odds of finding the 2-3 angles that resonate with genuinely in-market buyers. Create 3-5 ads per situation across formats (static, video, carousel, UGC) and launch with fair budget distribution for testing.

### Phase 2: First ~50 Customers — Score Them

Once campaigns generate roughly 50 purchases, score the customers each ad produced:

| Factor | 0 Points | 1 Point | 2 Points | 3 Points |
|---|---|---|---|---|
| **Order value** | Deep-discount minimum order | Below-average AOV | At/above average AOV | High AOV, bundle or multi-item |
| **Intent quality** | Discount-code hunter, immediate refund/return | Single item, coupon-driven | Full or near-full price | Full price + subscription or repeat within 60 days |
| **Fit** | Outside target customer, high return risk | Partial fit | Good fit | Ideal customer; engages with email, reviews, referrals |

Max score: 9. Pull signals from your order data, post-purchase survey ("how did you hear about us?", "what almost stopped you?"), and 60-day repeat behavior. Log scores against the ad/ad set that generated each customer, then compute the average per ad.

### Phase 3: Identify the True Top 3 Ads

Sort by average customer-quality score, NOT by CPA or CTR:

| Ad | CPA | CTR | Avg Quality | Verdict |
|---|---|---|---|---|
| A (Problem/Solution) | $28 | 1.8% | 7.2 | **WINNER** |
| B (Giveaway-style hook) | $22 | 2.1% | 4.1 | Platform vanity — low-value buyers |
| C (Quiz/education angle) | $35 | 1.1% | 8.0 | **WINNER** — best customers |
| D (Meme/deal hook) | $18 | 2.4% | 3.5 | Cheap volume, terrible LTV |
| E (UGC review story) | $32 | 1.3% | 6.8 | **WINNER** |

**Critical insight:** the ad that makes the most money is often NOT the one with the lowest CPA. Judge against new-customer contribution: (AOV × contribution margin + 60-day repeat value) − CAC.

### Phase 4: Scale Winners — Top 3 → 10 Variations Each

**Keep the winning angle. Change the format.** For each winner produce ~10 variations: 3 video versions (creator UGC, founder-to-camera, product demo), 2 carousels, 2 new hooks on the same concept, 1 testimonial using the same angle, 2 new static designs. Move variations into a consolidated scaling campaign and let Meta allocate budget across them.

### Phase 5: Continuous Iteration

- Every 2 weeks: review quality scores on new customer cohorts
- Kill variations whose average quality drops below 5
- Add new variations of winning concepts
- Test 1-2 completely new angles monthly (the 20% in the 50/30/20 rule)
- When a winning angle saturates its audience, expand with story-led creative for less-aware shoppers

## Ad Set Structure for a Validation Run

Two viable layouts. Pick one deliberately — mixing them makes the results unreadable.

| Structure | Layout | Use when |
|---|---|---|
| **By concept** | One ad set per concept, ~10 ads inside each | You have distinct concepts and enough budget for each ad set to clear its learning threshold. Gives a clean per-concept read, since the ad set is the unit Meta optimizes within |
| **By batch** | Mixed concepts in one ad set, launched as a batch. Batch 1 runs to a decision, then batch 2 iterates on what won | Budget can only support one ad set at the ~7× Target CPA floor. Concentrates signal, at the cost of a clean per-concept comparison |

Most accounts should use **by batch** and think they should use by concept. If splitting by concept puts any ad set below its budget floor, you have not built a cleaner test — you have built several tests that never leave learning.

## Organically Validated Ads

Before creating from scratch, audit your last 12 months of organic and creator content: high-engagement TikToks/Reels, most-saved posts, review quotes people screenshot, creator collabs that drove sales. Repurpose winners as paid ads — organic validation is free market research. A single creator video that quietly drove organic sales for a year often becomes a top paid performer, because the message is already proven.

## The Ad Copy Formula

```
1. HOOK/OFFER - lead with the payoff
2. PAIN - the specific problem
3. SOLUTION - product fixing it
4. PAIN EXPLAINED - cost of not solving
5. SOLUTION EXPLAINED - benefits, specifics
6. SOCIAL PROOF - reviews, ratings, UGC quote
7. CTA - clear next step
```

## Competitive Ad Research

In the Meta Ad Library, study competitor ads running 3+ months — long-running ads are likely profitable. Learn their persistent angles, offer types, and formats. Don't copy exact creative (their audience is warmed to their brand), don't imitate much larger brands (they can absorb losses as market capture), and don't assume ad volume equals profitability. Your ads need to pay back within your cash-conversion window.

## Related Skills

- **meta-creative-strategy**: Generating the customer-situation angles and concepts that enter this validation process.
- **creative-cadence-operating-system**: The production math and iteration cadence for turning validated winners into ~10 variations each.
- **creative-fatigue-detection**: Knowing when validated winners are dying and need rotation.
- **meta-ads**: The e-commerce Meta hub — audiences, campaign structure, and account-level ROAS/CAC strategy.
- **ab-testing**: General experiment design, statistics, and test hygiene beyond ad-message validation.
