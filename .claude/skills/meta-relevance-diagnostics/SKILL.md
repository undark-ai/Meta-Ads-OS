---
name: meta-relevance-diagnostics
description: "When the user wants to diagnose Meta's ad relevance diagnostics on an e-commerce or D2C account — Quality Ranking, Engagement Rate Ranking, and Conversion Rate Ranking — and fix the layer that is actually failing instead of guessing. Also use when the user mentions 'quality ranking,' 'below average ranking,' 'engagement rate ranking,' 'conversion rate ranking,' 'relevance score,' 'my CPMs are too high,' 'why is Meta charging me more,' or 'Meta says my ad is below average.' For an ad that started strong and is now decaying, see creative-fatigue-detection. For account-wide rising CAC or falling ROAS, see meta-optimization-playbook. For the pause/scale/graduate decision itself, see meta-ads-operating-system. For fixing the post-click experience a low Conversion Rate Ranking points at, see product-page-cro, checkout-cro and ux-audit."
metadata:
 version: 1.0.1
---

> **Marketing layer — advisory, not evidence.** Every benchmark, threshold and rule of thumb
> below is build-time guidance. Per `CLAUDE.md`, a marketing skill's number is never evidence
> for a quantified finding: a recommendation that originates here still needs a number, source,
> date range, formula, evidence class and confidence from the audit layer before it can be
> presented as one. Handoffs run audit → marketing, never the reverse.


# Meta Relevance Diagnostics — D2C E-commerce

Meta publishes three per-ad diagnostics that tell you *which layer* of an ad is losing the auction: the creative, the hook, or the post-click experience. Most operators either ignore them or read them as a grade. They are neither a grade nor a score — they are a pointer, and each one points at a different fix.

## Before Starting

**Check for product marketing context first:**
If `.agents/product-marketing.md` exists (or `.claude/product-marketing.md`, or the legacy `product-marketing-context.md` filename, in older setups), read it before asking questions. Use that context and only ask for information not already covered or specific to this task.

Gather this context (ask if not provided):

- **The specific ad or ad set** in question, and how long it has been running.
- **AOV and contribution margin per order**, so a CPM or CPA change can be judged against break-even rather than in isolation.

## Requires the Meta Ads MCP

Relevance diagnostics are per-ad fields you have to pull. Use `ads_get_ad_entities` for the ad and its delivery metrics — request the relevance and delivery fields explicitly, since the call returns nothing you did not ask for, `ads_insights_auction_ranking_benchmarks` for the ranking fields themselves, and `ads_get_creatives` to read the actual creative behind a finding. If the MCP isn't connected, say so and stop rather than fabricating rankings or performance numbers — then continue with the framework below, which needs no connection.

## The Three Diagnostics and What Each One Points At

| Diagnostic | What Meta is measuring | The lever it points at |
|---|---|---|
| **Quality Ranking** | Perceived quality against ads competing for the same audience — including negative feedback (hides, reports), engagement bait, sensationalized claims, withheld information, and excessive text | The creative and the claim. Not the targeting. |
| **Engagement Rate Ranking** | Expected rate of clicks, reactions, comments, shares, expands against competing ads | The hook and format fit. The first second, the thumbnail, the aspect ratio. |
| **Conversion Rate Ranking** | Expected conversion rate against ads with the same optimization goal competing for the same audience | Everything after the click: page speed, offer strength, checkout friction, audience-offer match. |

Two properties change how you read all three:

**They are relative, not absolute.** A "Below Average" ad is not a bad ad — it is an ad losing to the specific set of advertisers bidding on the same people right now. The same creative can be Average in January and Below Average in November because Q4 competition arrived. Never report a ranking as a verdict on the creative without saying what it is relative to.

**They need volume before they mean anything.** Rankings do not populate until roughly 500 impressions, and they stay noisy well past that. On a new ad, "-" means "not enough data," not "fine." Do not act on a ranking until the ad has real delivery behind it.

## Diagnostic Framework: Isolate the Failing Layer

Read all three together. The *pattern* is the diagnosis, not any single field.

| Pattern | Likely root cause | Fix direction |
|---|---|---|
| Quality low, others OK | Negative feedback or a claim problem — hides, reports, engagement bait, over-promising, text-heavy image | Rebuild the creative around a credible claim. Cut clickbait framing. Reduce on-image text. Check the comment section for what people are actually reacting to. |
| Engagement low, others OK | The hook fails or the format doesn't fit the placement | New hook, new first frame, new thumbnail. Check aspect ratio against placement — see meta-creative-formats. |
| Conversion low, others OK | The problem is after the click, not in the ad | PDP load speed on mobile, shipping-cost shock at checkout, a weak or mismatched offer, or an audience that was never going to buy this product. |
| All three low | The concept is wrong for this audience | Kill it. Don't iterate — iterating a triple-Below-Average ad spends money proving what you already know. Start a different concept. |
| Rankings declining while frequency rises | Not a relevance problem — fatigue | Route to creative-fatigue-detection. The audience has seen it too many times; the ad hasn't changed. |
| Rankings fine but CPA above target | Not a relevance problem either | The ad is competitive in the auction and still unprofitable. That's an economics or offer question — meta-ads-operating-system and meta-offer-strategy. |

## Conversion Rate Ranking Is Usually a Store Problem

For D2C, a lone Below Average Conversion Rate Ranking is the most common and most misdiagnosed pattern. Operators change targeting; the fix is almost always on the store. Check in this order:

1. **Mobile PDP speed and mechanical defects.** Most Meta traffic is mobile. A PDP that takes 5+ seconds on a mid-range phone loses the sale before the page paints. Hand this to **ux-audit**, which diagnoses speed, responsiveness and interaction defects rather than messaging.
2. **The product page itself.** Gallery, variant and size selection, review placement, product copy — a page that ranks fine and converts badly is a PDP problem. Hand it to **product-page-cro**.
3. **Shipping-cost shock.** A shipping charge that first appears at checkout is the single largest silent conversion killer for D2C. Compare add-to-cart rate against checkout-completion rate — a healthy ATC with a collapsing checkout rate is a cost-surprise signature. Hand it to **checkout-cro**.
4. **Offer strength for a cold buyer.** "Just buy it" underperforms on cold traffic. See **meta-offer-strategy**.
5. **Ad-to-page match.** If the ad sells one situation and the page sells the catalog, the click was earned under different terms than the page honors.
6. **Audience-offer mismatch.** A lookalike seeded on discount buyers will click a full-price ad and not convert.

Only after those are ruled out is it worth touching the audience. Note the division of labour: this skill tells you *that* the post-click experience is losing the auction and roughly where; the CRO skills tell you *what to change*.

## Cross-Check Against CPM Before Acting

A poor ranking that isn't costing you anything isn't worth a rebuild. Pull the ad's CPM trend alongside the rankings. If the ranking dropped and CPM is flat, Meta is not penalizing you meaningfully in this auction — log it and move on. If the ranking dropped and CPM rose in step, the ranking is now the mechanism of a real cost increase, and it earns a fix. Report both numbers together; a ranking without its CPM is half a finding.

## Never Edit a Flagged Ad — Relaunch It

Negative feedback and quality signal attach to the **ad ID**, not the creative file. Editing the image or copy in place carries the accumulated history forward, and a rebuilt ad can stay suppressed for reasons that no longer exist in its current form. Create a new ad with the new creative and let the old one go. This also keeps your reporting honest: the new ad's numbers are its own.

## Common Mistakes

- **Treating the rankings as a report card.** They are a pointer to a layer, not a score to improve.
- **Acting before 500 impressions.** A blank or freshly-populated ranking is noise.
- **Fixing targeting when Conversion Rate Ranking is the one that's low.** That is a store and offer signal.
- **Iterating an ad that is Below Average on all three.** The concept lost. Change concepts.
- **Reporting a ranking without its CPM trend.** Then nobody can tell whether it cost anything.
- **Comparing rankings across accounts or seasons.** They are relative to whoever is bidding on the same people at that moment.

## Related Skills

- **creative-fatigue-detection**: When rankings decay while frequency climbs, that's fatigue, not relevance — diagnose it there.
- **meta-creative-formats**: Format and placement fit, aspect ratios and safe zones, when Engagement Rate Ranking is the failing layer.
- **meta-creative-strategy**: Rebuilding the concept and the hook when Quality or Engagement is the failing layer.
- **meta-offer-strategy**: Offer strength for cold traffic when Conversion Rate Ranking is the failing layer.
- **meta-ads-operating-system**: The kill, swap and scale decision once you know which layer failed.
- **product-page-cro**: Fixing the PDP a low Conversion Rate Ranking points at — gallery, variants, reviews, product copy.
- **checkout-cro**: Cart and checkout, including the shipping-cost shock that produces a healthy add-to-cart rate and a collapsing checkout rate.
- **ux-audit**: Mobile speed, responsiveness and interaction defects — the mechanical reasons a page loses conversions.
- **full-audit**: The evidence-graded audit lane — 30 sections against live account data, where these benchmarks get tested rather than assumed.
