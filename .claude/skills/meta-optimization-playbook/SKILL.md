---
name: meta-optimization-playbook
description: "When the user wants to optimize a live Meta Ads account for an e-commerce or D2C brand — the diagnosis order for rising CAC or falling ROAS, ecom benchmarks, kill/optimize/scale rules, learning-phase math, and the weekly optimization cadence. Also use when the user mentions 'CAC is rising,' 'ROAS is dropping,' 'CTR is falling,' 'my campaigns stopped working,' 'learning phase,' 'creative fatigue,' 'Meta benchmarks,' or 'when should I kill a campaign.' For the standing decision framework with graduation and budget formulas, see meta-ads-operating-system. For a live-data fatigue diagnosis on a connected account, run the creative deep-dive workflow; the fatigue verdict is section 8, and frequency-and-saturation separates creative decay from audience exhaustion. This repository is Meta-only; for the e-commerce Meta hub, see meta-ads."
metadata:
 version: 1.1.1
---

> **Marketing layer — advisory, not evidence.** Every benchmark, threshold and rule of thumb
> below is build-time guidance. Per `CLAUDE.md`, a marketing skill's number is never evidence
> for a quantified finding: a recommendation that originates here still needs a number, source,
> date range, formula, evidence class and confidence from the audit layer before it can be
> presented as one. Handoffs run audit → marketing, never the reverse.


# Meta Ads Optimization Playbook — D2C E-commerce

What to do when things go right, wrong, or sideways: decision trees, weekly cadence, thresholds, and benchmarks for managing D2C Meta accounts.

## Before Starting

**Check for product marketing context first:**
If `.agents/product-marketing.md` exists (or `.claude/product-marketing.md`, or the legacy `product-marketing-context.md` filename, in older setups), read it before asking questions. Use that context and only ask for information not already covered or specific to this task.

Gather this context (ask if not provided):

- AOV and contribution margin per order — break-even ROAS anchors every judgment below.
- What changed recently: budget moves, new creative, offer changes, site changes.

## Core Rule: Meta Thinks in Weeks, Not Days

Single-day or 3-day fluctuations are normal. Never make decisions on less than 7 days of data. The most common way to kill a winning campaign is changing it every 2-4 days because a metric dipped. Let it run.

## D2C Meta Benchmarks (directional)

| Metric | Typical | Strong | Red Flag |
|---|---|---|---|
| CTR (all) | 1.5-2.5% | 3%+ | < 1% |
| Hook rate (3s views/impr.) | 20-30% | 35%+ | < 15% |
| CPM (prospecting, US) | $15-35 | < $15 | > $50 |
| Purchase CVR (site) | 2-3% | 4%+ | < 1.5% |
| Frequency (prospecting) | 1.5-2.5 | < 2 | > 4 |
| Frequency (retargeting) | 3-6 | — | > 8 |
| ROAS target | Set by unit economics: break-even ROAS = AOV ÷ contribution margin. Judge blended MER + new-customer CAC, not in-platform ROAS alone. |

**Seasonality:** Q4 CPMs spike 40-80% (BFCM). Q1 is cheapest — scale prospecting aggressively in Jan-Feb.

### Vertical ROAS Bands (context only)

Useful for sanity-checking an account against its category, never as a target. **Break-even ROAS is the target; these are context.**

| Category | Typical blended ROAS | Caveat |
|---|---|---|
| Apparel and fashion | 2–4x | Returns can be 20–40%; ROAS before returns is a fiction |
| General merchandise | 3–6x | Wide margin spread within the band |
| Beauty and consumables | 3–5x | Repeat rate carries the economics; first-order ROAS understates it |
| High-ticket / furniture | 1.5–3x | Long consideration means a real share of purchases fall outside any attribution window |

Two break-even formulations circulate. `AOV ÷ contribution margin per order` is the canonical one used throughout this suite because it accounts for fulfilment, payment and variable costs. `1 ÷ gross margin %` is a faster sanity check that ignores them — a 40% gross margin implies roughly 2.5x. Use the first to set targets; use the second to spot an account whose target is wildly wrong.

## Decision Tree 1: CAC Rising / ROAS Falling

Work in this order:

1. **Tracking** — Pixel firing? CAPI sending purchase events (recovers 20-30% of lost conversions)? Attribution window changed?
2. **Frequency + creative fatigue** — Frequency > 4 on prospecting? CTR down 20%+ from baseline? → refresh creative. Frequency 3-4 → prepare replacements now.
3. **Learning phase** — Changes in the last 7 days? Budget moved > 30%? Under ~50 purchases/week per ad set? → you reset learning; wait, don't touch.
4. **Audience/placement** — Ad-set overlap? Audience Network draining spend with junk clicks? Check the placement breakdown (via the Meta connector — see meta-ads-mcp).
5. **Site funnel** — Page load > 3s, out-of-stock bestsellers, checkout errors, ad-to-PDP message mismatch, shipping-cost shock at checkout. Falling site CVR with stable CTR = a site problem, not an ad problem.
6. **External** — Q4 CPMs, new auction competitor, discount fatigue after a big sale, seasonality of your category.

## Decision Tree 2: CTR Dropping

- **Creative fatigue** (most common): same ads 14+ days, frequency creeping, only 1-2 concepts live → launch 3-4 new concepts.
- **Audience exhaustion**: small audience + high frequency → broaden.
- **Format staleness**: all statics → test video/UGC; all video → test statics and carousels.
- **Message drift**: offer expired or season shifted → update copy and offer.

Fix priority: creative refresh → new formats → audience expansion → copy rewrite.

## Decision Tree 3: ROAS Fine, But Business Isn't

In-platform ROAS can look great while the business stalls. Check:

- **New vs returning split** — retargeting/existing customers inflating ROAS? Track new-customer CAC separately (cost per NEW customer).
- **MER** (total revenue ÷ total ad spend) trending down while ROAS holds → attribution is flattering you.
- **AOV dropping** — discount-led creative attracting low-AOV, no-repeat buyers. Check 60-day repeat rate by campaign.
- **Post-purchase survey** ("how did you hear about us?") diverging from attribution → recalibrate channel judgment.
- **Post-click experience** — if the traffic is right and the economics still don't work, the leak is on the store, not the account. Route by where it drops: product page → **product-page-cro**, cart or checkout → **checkout-cro**, mechanically broken or slow → **ux-audit**. Don't keep optimizing an account whose problem is downstream of the click.

## Kill / Optimize / Scale

**KILL:** zero purchases after 3-5x target CPA in spend; ROAS < 50% of break-even after 7 full days; frequency > 6 with declining performance; never exited learning after 14 days.

**OPTIMIZE:** CAC within 20-30% of target but inconsistent; CTR mediocre; plateaued after learning; frequency 2.5-4 (refresh creative); good ROAS but weak new-customer share.

**SCALE (all must be true):** ~50 purchases/week for 2+ weeks; CAC at/below target 3+ consecutive days; frequency < 3; new-customer share healthy; inventory can absorb the volume.

## Scaling Protocol

Increase budget 15-20% every 3-5 days. Never > 30% at once (resets learning). If CAC rises > 15% after an increase, hold. If you break it: roll back 20-30%, stabilize 3-5 days, resume at 10% every 5 days.

**Learning phase math:** Daily budget ≈ (target CPA × 50) ÷ 7. Can't afford that? Consolidate ad sets (one at $500/day beats five at $100/day) or optimize for a higher-volume event (add-to-cart) temporarily.

**What resets learning:** targeting changes, creative swaps inside an ad set, optimization-event changes, big budget jumps. **What doesn't:** small budget nudges (<10%), copy tweaks, pausing < 24h, adding new ads alongside old ones.

## Weekly Cadence

- **Monday — review:** last 7 days of CAC, ROAS, MER, frequency, new-customer share; flag fatigue; identify top 3 ads and why.
- **Wednesday — creative:** launch new variants; hold the 50/30/20 split (50% proven winners, 30% iterations, 20% new concepts).
- **Friday — budget:** scale qualifying winners, kill per criteria, check pacing, queue next week's creative.
- **Monthly:** full account audit, cohort check (60/90-day LTV by campaign), refresh exclusion lists, review offers.
- **Quarterly:** structure consolidation, CAPI/pixel health (Event Match Quality), competitive sweep, cross-channel budget reallocation on MER.

## Seasonal Peaks: Freeze Structure Before BFCM

The learning phase does not care that it's your biggest week of the year.

- **No structural edits in the days before a peak.** No new campaigns, no ad set consolidation, no optimization-event changes, no budget jumps over 20%. Every one of those resets learning, and the reset lands exactly when volume and CPMs are at maximum.
- **Get changes in early.** Whatever you want live for the peak should be running and out of learning at least two weeks before it.
- **Pace against inventory, not against ROAS.** Scaling spend on a SKU you'll stock out of mid-week is worse than underspending — you pay for demand you then fail, and the reviews follow.
- **Expect CPMs 40–80% higher.** A ROAS decline during peak that tracks the CPM rise is not an account problem.
- **Run a post-peak review** while the data is fresh: which offers worked, which creative held up at high frequency, which audiences saturated, what to build earlier next year.

## The 80/20 Rule

20% of campaigns drive 80% of results. Identify the campaigns actually driving profitable new customers, pause (don't trim) the rest, reinvest in winners, and keep testing to a disciplined 20% budget slice.

## Related Skills

- **meta-ads-operating-system**: The standing decision framework — Target CPA formulas, graduation thresholds, ad count ceiling, creative production math.
- **meta-relevance-diagnostics**: Which layer of an ad is failing when the diagnosis trees don't resolve it.
- **meta-attribution**: When the numbers themselves are the problem rather than the performance.
- **meta-ads**: The e-commerce Meta hub — audience strategy, campaign structure, and creative testing across the full suite.
- **full-audit**: The evidence-graded audit lane — 30 sections against live account data, where these benchmarks get tested rather than assumed.
- **creative-fatigue-detection**: Deeper fatigue signals, frequency thresholds by campaign type, and rotation rules.
- **meta-reporting**: Turning account performance into a branded dashboard or written report.
