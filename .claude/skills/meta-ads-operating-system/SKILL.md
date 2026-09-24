---
name: meta-ads-operating-system
description: "When the user wants to make an operational decision on a Meta Ads account for an e-commerce or D2C brand — when to pause, swap, graduate, or scale an ad, how to split budget between testing and scaling, and how many creatives to produce, all driven by formulas and thresholds tied to ROAS and new-customer CAC. Also use when the user mentions 'should I kill this ad,' 'when should I scale,' 'graduate a winning ad,' 'Target CPA,' 'break-even ROAS,' 'new-customer CAC,' 'testing budget,' 'ad count ceiling,' or 'how many ads should I run.' For diagnosing rising CAC or falling ROAS and ecom benchmarks, see meta-optimization-playbook. For evidence-graded analysis against a live connected account, see full-audit. For automating these thresholds as Automated Rules or API automation, see meta-automated-rules. This repository is Meta-only; for the e-commerce Meta hub, see meta-ads."
metadata:
 version: 1.1.0
---

> **Marketing layer — advisory, not evidence.** Every benchmark, threshold and rule of thumb
> below is build-time guidance. Per `CLAUDE.md`, a marketing skill's number is never evidence
> for a quantified finding: a recommendation that originates here still needs a number, source,
> date range, formula, evidence class and confidence from the audit layer before it can be
> presented as one. Handoffs run audit → marketing, never the reverse.


# Meta Ads Operating System — D2C E-commerce

The single decision framework for running Meta ad accounts for e-commerce. Every decision — when to swap an ad, when to graduate it, when to scale budget, how many creatives to produce — flows from this system.

## Before Starting

**Check for product marketing context first:**
If `.agents/product-marketing.md` exists (or `.claude/product-marketing.md`, or the legacy `product-marketing-context.md` filename, in older setups), read it before asking questions. Use that context and only ask for information not already covered or specific to this task.

Gather this context (ask if not provided):

- AOV, contribution margin per order, and 90-day LTV multiple — every threshold below derives from these.
- Monthly ad budget and current trailing 30-day new-customer CAC.

## Core Principle

Meta's algorithm is excellent at driving purchases, but it cannot see your economics. It counts a $20 order from a repeat customer the same as a $200 first order. Our job is to add the layer Meta cannot see — new-customer CAC and contribution margin — and make every decision on those numbers, not raw in-platform ROAS.

## 1. Set the Target

Every formula depends on one number: **Target CPA = target cost per new-customer purchase.**

- **Break-even ROAS = AOV ÷ contribution margin per order.** Example: AOV $80, contribution margin $32 → break-even ROAS 2.5.
- **Target CPA = contribution margin per first order + acceptable first-order loss funded by LTV.** If 90-day LTV is 1.6x first order, you can pay above first-order margin.
- **No historicals?** Use 30-day trailing new-customer CAC × 0.80 as the first target — achievable through cutting losers and graduating winners, no structural changes. Refine with real data within 30 days.

All thresholds below derive from Target CPA.

## 2. Campaign Structure

**2 campaigns. Both CBO.**

| Campaign | Budget | Purpose |
|----------|--------|---------|
| Scaling (CBO) | ~80% | Proven/graduated ads only. CBO distributes freely among winners. |
| Testing (CBO) | ~20% | New concepts + iterations. Protected budget so tests always get spend. |

Why two: in a single CBO, proven ads starve test ads. A hard testing budget lets tests compete only against each other. CBO's uneven distribution inside the Testing campaign is itself a signal — if Meta won't spend on a test ad, the creative isn't resonating.

**Ad count ceiling** (where ads start getting starved):

```
Ceiling = (Daily budget × 14) / (2 × Target CPA)
```

Sweet spot: 6–10 active ads = winners + 2–3 test slots. At the ceiling, queue tests; every new ad in means an old ad out.

1 ad set per campaign (broad or your validated audience — identical across both). The separation is budget control, not audience segmentation.

**Minimum viable daily budget per ad set.** The learning phase needs ~50 optimization events in 7 days, so:

```
Minimum daily budget per ad set ≈ 7 × Target CPA
```

| Target CPA | Minimum daily budget | Weekly |
|---|---|---|
| $10 | ~$70 | ~$490 |
| $25 | ~$175 | ~$1,225 |
| $50 | ~$350 | ~$2,450 |
| $100 | ~$700 | ~$4,900 |

The two formulas answer different questions and should agree: the ad-count ceiling tells you how many ads a budget can support, this one tells you whether a budget can support an ad set at all. Below the floor, consolidate ad sets rather than running several that all sit in permanent learning.

**Never run retargeting and prospecting in the same CBO campaign.** CBO optimizes for cheapest conversions and retargeting always looks cheapest, so it absorbs the budget and reports the credit while prospecting starves. This is a structural error no threshold can correct for.

## 3. The Decision Tree

**Stage 1 — Delivery check** (valid only at/below the ceiling):

- Ad active 7+ days with spend < (daily campaign budget ÷ active ads) × 7 × 0.5 → **KILL**. CBO deprioritized it.
- $0 spend after 7 days → **KILL** immediately.
- Ongoing: spent ≥ 1× Target CPA lifetime AND last-7-day spend under ~$10/day → **KILL**. CBO gave it a shot and pulled away.
- Delivery kills mean the hook/visual doesn't stop the scroll. Replace with a different hook or format — don't iterate the copy; nobody read it.

**Stage 2 — Quality evaluation** (every Monday, rolling 14-day data: spend, purchases, new-customer purchases, new-customer rate, AOV, CAC, frequency):

1. **Enough data?** Spend < 3× Target CPA → WAIT. (At target performance you'd expect ~3 purchases by then; zero has ~5% probability. 3× balances confidence with budget.)
2. **Any purchases?** Zero → SWAP. Abandon the concept entirely.
3. **Quality check (the layer Meta can't see).** Purchases but new-customer rate < 40%, or AOV far below account average (discount hunters) → SWAP with a version aimed at new buyers, and tighten exclusions. 40–60% new-customer rate → MONITOR. ≥ 60% → proceed.
4. **Cost check.** New-customer CAC ≤ Target CPA → potential winner. 1–1.5× → MONITOR (normal variance is 10–20%). > 1.5× over 14 days → SWAP; that's structural, not bad luck.
5. **Graduation (Testing → Scaling).** ALL true: 5+ new-customer purchases, CAC ≤ Target CPA, running ≥ 14 days, at least 1 purchase in last 7 days.
6. **Fatigue (Scaling ads).** Frequency < 3.0 and cost stable → healthy. 3.0–3.5 or cost +20% → produce 2 iterations now. > 3.5 or cost +40% or > 1.5× target for 2 weeks → swap immediately.

**Never pause without replacing.** Every swap needs a live replacement within 7 days; if the pipeline is empty, redirect budget to proven ads.

### Swap Rules: What to Change

Knowing to swap is half the decision. What you change depends on *why* it failed — iterating the wrong layer wastes the next cycle too.

| Swap reason | Iterate the creative? | What to change | Timeline |
|---|---|---|---|
| Delivery failure (CBO wouldn't spend) | **No — abandon it** | A different hook or format entirely. Nobody read the copy, so rewriting the copy changes nothing. | Immediate |
| Zero purchases at 3× Target CPA | **No — abandon the concept** | A different concept. The message didn't land, not the execution. | 48h |
| Purchases but low new-customer rate or low AOV | Yes | Keep the format and visual. Rewrite the copy to name the new buyer explicitly, and tighten exclusions. | 48h |
| CAC > 1.5× Target CPA over 14 days | Yes | Same angle, new execution — new hook, new opening frame, new visual treatment. | 48h |
| Fatigue (frequency > 3.5 or cost +40%) | Yes | Change the surface: new visual, new format, same proven message. | Immediate |
| Policy rejection or a flagged relevance ranking | **No — relaunch** | Rebuild as a *new ad*. Negative feedback attaches to the ad ID, so an edit carries the history forward. | Immediate |

Replacement live within **7 days maximum**. A swap with no replacement is a budget cut you didn't decide to make.

### Why These Thresholds

Defend the call, don't recite the number.

| Threshold | Why |
|---|---|
| 3× Target CPA before judging | At target performance you'd expect ~3 purchases by that spend. Getting zero has roughly a 5% probability, so it's a real signal rather than bad luck. 3× balances confidence against burn. |
| 1.5× Target CPA over 14 days | Normal week-to-week CAC variance is 10–20%. A 50% overshoot sustained across two weeks is structural, not noise. |
| Day 7 for delivery checks | CBO explores new ads over roughly 48–72 hours, so its preference is stable by day 7. Judging earlier reads exploration, not preference. |
| Half fair share = kill | If an ad has received under half of `(daily budget ÷ active ads) × days`, CBO has actively deprioritized it against its siblings. That's a verdict from the algorithm, not a slow start. |
| Frequency 3.0 / 3.5 bands | Below 3.0 the audience is still fresh. Between 3.0 and 3.5 costs begin drifting. Above 3.5 the cost curve steepens faster than any copy fix can offset. |
| 20% budget increases, 5-day gaps | Increases above ~30% reset the learning phase. 20% every 5 days compounds to roughly 3× a month without ever tripping it. |
| 5+ new-customer purchases to graduate | Below five, the CAC estimate is dominated by variance, and graduating a lucky ad into the Scaling campaign spends real money proving it wasn't. |

## 4. Creative Production Formula

```
Tests/month = (Monthly budget × 0.20) / (3 × Target CPA)
```

Win rates: iterations on winners ~25%, new concepts ~10%, blended ~17% (1 in 6). Inverted, **tests needed for X winners = X ÷ 0.17** — three new proven ads takes roughly 18 tests, which is the number to plan production against. Production split — **50%** iterations on top performers / **30%** iterations on other performers / **20%** new concepts. This is a production ratio, not a budget split; CBO handles budget.

**Image-first testing:** launch new concepts as static images. If delivery and CAC pass, then invest in video/carousel versions. Failed concepts die cheap.

**Minimum proven ads = monthly budget ÷ $5,000.** Each proven ad absorbs roughly $5K/month before fatigue. You cannot scale budget ahead of creative.

## 5. Scaling Protocol

Scale only when ALL true: enough proven ads for the next level, account frequency < 3.0, CAC at/below target 2+ consecutive weeks, 3+ replacements ready in Testing.

- Increase 20% every 5 days (never > 30% at once — learning-phase reset).
- Rollback trigger: CAC > 1.5× target post-scale → cut 20–30% immediately; resume at 10%/week after 2 stable weeks.
- Wall (frequency > 3.5): expand lookalikes 1% → 3%, refresh seed lists, go broader, lean into new creative concepts.

## 6. Diagnosing Underspend and Stuck Ad Sets

A budget that doesn't spend is not a delivery mystery; it has four common causes with different fixes.

| Symptom | Likely cause | Fix |
|---|---|---|
| Ad set spends a fraction of its budget from launch | Budget below the ~7× Target CPA floor, so the ad set can't reach 50 events and never exits learning | Consolidate ad sets or raise the budget to the floor. Don't lower the bid |
| One ad set in a CBO takes almost everything | CBO concentration — usually the broadest or largest ad set absorbing budget while a small retargeting ad set starves | Move the starved ad set into its own campaign with its own budget. Nothing inside a CBO will protect it |
| Spend fell off a cliff right after an edit | Learning reset from a >20% budget change, an audience edit, or an optimization-event change | Wait it out; don't stack another edit on top. Note what you changed |
| Whole account underspending | Auction competition rose (seasonal), the audience is exhausted (check frequency), or payment/account restriction | Check frequency trend first, then Business Manager for a restriction, then accept a higher CPM if it's competition |

**Underspend is never fixed by lowering the bid.** A cost cap set below what the auction charges produces exactly this symptom, and lowering it further makes it worse.

## 7. Weekly Cadence

| Day | Actions |
|-----|---------|
| Monday | Pull 14-day data (via the Meta connector — see meta-ads-mcp). Run the Decision Tree. Execute swaps/graduations. Check new-customer rate via post-purchase survey data. |
| Wednesday | Launch new tests. Run Stage 1 delivery checks on 7-day-old ads. |
| Friday | Check scaling criteria and rollback triggers. Verify MER (blended) agrees with in-platform trend. |
| Monthly | Creative library audit, Target CPA review vs. margin and LTV, frequency trend. |

## Related Skills

- **meta-optimization-playbook**: Diagnosis order for rising CAC or falling ROAS, ecom benchmarks, and the kill/optimize/scale rules for a live account.
- **meta-ads**: The e-commerce Meta hub — audience strategy, campaign structure, and creative testing across the full suite.
- **full-audit**: The evidence-graded audit lane — 30 sections against live account data, where these benchmarks get tested rather than assumed.
- **creative-cadence-operating-system**: Planning the creative production volume this system's testing math demands.
- **ads**: Platform-agnostic paid-ads strategy across Google, LinkedIn, and other channels, plus the D2C paid playbook reference (demand lifecycle, budget by stage, scaling quadrant).
- **meta-automated-rules**: Automating these thresholds safely, and why frequency and pacing must stay notify-only.
- **meta-relevance-diagnostics**: Which layer of an ad failed, when the swap reason isn't obvious from cost alone.
