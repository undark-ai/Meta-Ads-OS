---
name: creative-fatigue-detection
description: "When the user wants to diagnose creative fatigue on an e-commerce or D2C Meta account — the signals an ad is dying, frequency thresholds by campaign type, creative lifespans by format, rotation rules, and refresh timing to protect ROAS. Also use when the user mentions 'creative fatigue,' 'ad fatigue,' 'frequency too high,' 'CTR dropping,' 'CPMs rising,' 'ads stopped working,' or 'when should I refresh my ads.' For a live-data fatigue diagnosis on a connected account, run the creative deep-dive workflow; the fatigue verdict is section 8, and frequency-and-saturation separates creative decay from audience exhaustion. For the production system that keeps replacement creative ready, see creative-cadence-operating-system. For Quality, Engagement Rate or Conversion Rate Ranking flagged below average, see meta-relevance-diagnostics."
metadata:
 version: 1.1.0
---

> **Marketing layer — advisory, not evidence.** Every benchmark, threshold and rule of thumb
> below is build-time guidance. Per `CLAUDE.md`, a marketing skill's number is never evidence
> for a quantified finding: a recommendation that originates here still needs a number, source,
> date range, formula, evidence class and confidence from the audit layer before it can be
> presented as one. Handoffs run audit → marketing, never the reverse.


# Creative Fatigue Detection & Rotation — D2C Meta

How to detect when Meta ads are losing effectiveness, when to rotate creative, and how to maintain ROAS through systematic creative management. Fatigue happens when your audience has seen your ads too many times: the algorithm keeps serving, engagement drops, CPMs and CAC rise.

## Before Starting

**Check for product marketing context first:**
If `.agents/product-marketing.md` exists (or `.claude/product-marketing.md`, or the legacy `product-marketing-context.md` filename, in older setups), read it before asking questions. Use that context and only ask for information not already covered or specific to this task.

## The Signals (in order of urgency)

| Signal | Threshold | Urgency |
|---|---|---|
| Frequency > 4.0 (prospecting) | Immediate action | URGENT |
| Frequency > 8.0 (retargeting) | Immediate action | URGENT |
| CTR drops 20%+ from baseline over 7 days | Creative dying | WARNING |
| Hook rate falling week over week | Scroll-stop power fading | WARNING |
| CPM rising 30%+ over 2 weeks | Algorithm struggling to deliver | WARNING |
| Ad Relevance "Below Average" on any metric | Quality issue | WARNING |
| CAC rising / ROAS falling with stable targeting and site CVR | Likely fatigue (rule out other causes) | MONITOR |

## Frequency Thresholds by Campaign Type

| Campaign Type | Safe | Warning | Critical |
|---|---|---|---|
| Prospecting (cold) | 1.0-2.5 | 2.5-3.5 | > 4.0 |
| Retargeting | 3.0-6.0 | 6.0-8.0 | > 8.0 |
| Retention / existing customers | 2.0-5.0 | 5.0-7.0 | > 8.0 |

Retargeting tolerates higher frequency because reinforcement is intentional for warm shoppers — but even warm audiences hit diminishing returns, and over-serving existing customers burns goodwill. Always exclude recent purchasers (7-30 days) except for deliberate cross-sell.

## D2C Creative Lifespan

| Format | Typical Lifespan | Why |
|---|---|---|
| Static image | 14-28 days | Registered quickly, scrolled past |
| Video (<30s) | 21-35 days | People engage at different points each view |
| Carousel | 21-35 days | Multiple cards = built-in novelty |
| UGC / creator content | 28-42 days | Authenticity fatigues slowest |

D2C ads fatigue faster than most categories at scale — high spend against finite prospecting pools builds frequency quickly. Plan on a 2-3 week refresh cycle for active prospecting campaigns, faster during promo periods.

## Weekly Detection Workflow (run every Monday)

1. **Pull frequency** (from Ads Manager, or via the Meta connector — see meta-ads-mcp) — add the Frequency column, filter last 7 and 14 days, flag anything above its campaign-type threshold.
2. **Check CTR and hook-rate trend** — compare this week to the prior 2 weeks. Down 15-20%+ = fatigue likely. CTR stable but frequency rising = preemptive refresh within 7 days.
3. **Check CPM trend** — rising CPM with a stable audience is a leading indicator that often precedes the CTR drop. 30%+ over 2 weeks = fatigue or auction competition; check both.
4. **Check Ad Relevance diagnostics** — Quality, Engagement Rate, and Conversion Rate rankings. Any "Below Average" = investigate and likely replace.
5. **Classify each ad:**

| Classification | Criteria | Action |
|---|---|---|
| Healthy | CTR stable, frequency under threshold | Keep running |
| Warning | CTR declining or frequency approaching threshold | Prepare replacement, launch within 7 days |
| Urgent | Over threshold, CTR down 20%+ | Replace within 24-48 hours |
| Depleted | 4+ weeks running, frequency > 5, well below baseline | Pause. Don't iterate — the concept is exhausted. |

## Is It Fatigue, Saturation, or Seasonality?

Three different problems produce the same chart. Prescribing the wrong fix costs a full cycle.

**The test: swap the creative, hold the audience.** Put fresh creative into the same ad set and watch for two weeks.

| Result | Diagnosis | Fix |
|---|---|---|
| Performance recovers | **Creative fatigue.** The audience was fine; the ad was worn out | Rotate on cadence (below) |
| Performance stays flat with fresh creative | **Audience saturation.** You have exhausted the reachable pool at this frequency | Expand the audience: widen the lookalike percentage, refresh the seed, go broader. New creative into the same exhausted pool won't help |
| Everything is down, including untouched campaigns and other channels | **Seasonality or external** | Check the calendar, competitor activity in the Ad Library, and platform-wide CPM trends before changing anything |

Check the third case *first* — it is the cheapest to rule out and the most embarrassing to miss. A Q4 CPM rise or a competitor's launch week explains a lot of "fatigue."

**Refresh depth matters.** A refresh means **a new hook and a new visual concept**. A colour grade, a new font, or a reordered caption is not a refresh; the audience has already decided about that ad and will keep scrolling past its cousin.

**Active variations per ad set: 3–6.** Below 3, each ad carries too much frequency and fatigues faster. Above 6–8, budget spreads too thin for any single ad to gather learning signal. The band is a real constraint, not a preference.

**Sharper trigger.** Rotate when the frequency threshold is crossed **and** CTR is down 20%+ from the ad's own early-flight baseline. Either signal alone produces false positives. A **CPM rise of 30–40% from that ad's baseline** is the third confirming signal.

## The Rotation System

**The 50/30/20 rule for your live library:** 50% proven winners (scaling), 30% iterations on winners (new hook/format/creator on the same angle), 20% new concepts. This guarantees replacement creative exists before fatigue hits.

**Cadence:** check fatigue weekly; launch new variations every 2 weeks; test completely new concepts monthly; retire when CTR drops 30%+ from peak or frequency > 5; full library refresh quarterly (before BFCM, rebuild the entire slate).

**Rotate without resetting learning phase:**
- Don't swap creative inside a performing ad set (resets learning)
- Do launch new ads alongside existing ones in the same ad set
- Do spin up a fresh ad set with the same targeting when the old one is depleted
- Pausing an ad ≠ editing — it doesn't reset learning

## Creative Pipeline Management

| Campaign Type | Minimum Active | Ready in Pipeline | Refresh Rate |
|---|---|---|---|
| Prospecting | 4-6 concepts | 3-4 ready to launch | Every 2 weeks |
| Retargeting | 3-4 concepts | 2-3 ready | Every 3 weeks |
| Retention | 2-3 concepts | 2 ready | Every 3-4 weeks |

**Feed the pipeline from:** post-purchase surveys and reviews (customer language), organic/creator winners, competitor ads in the Meta Ad Library (angles, not creative), and iterations on your own winners.

## Rotation Schedule by Recency Tier

Retargeting audiences burn creative far faster than cold ones, because the pool is small and the same people see every impression. Set the cadence by how recently the audience interacted:

| Audience recency | Rotate every | Active variants |
|---|---|---|
| Hot (0–14 days) | 2 weeks | 3–4 |
| Warm (15–45 days) | 3–4 weeks | 2–3 |
| Cool (46–90 days) | Monthly | 2 |
| Cold prospecting | On the signals above, typically 4–8 weeks | 4–6 |

Evergreen retargeting on a two-week cadence is not over-production — it is the cost of running retargeting at all. Brands that set one refresh cadence account-wide always over-serve the hot tier and under-serve prospecting.

## Format-Specific Refresh Tactics

- **Statics:** fatigue fastest. New headline on the same visual buys 7-14 days; a distinct colorway/layout of the same concept counts as "new."
- **Video:** swap the opening hook, keep the body — extends lifespan significantly. 9:16 with audio typically converts better per dollar.
- **Carousel:** reorder cards or add 1-2 new cards while keeping the best ones.
- **UGC:** when it fatigues, switch to a different creator, not a different concept. Multiple creators on one concept = a rotation system built in.

## Controlling Frequency

Meta offers no precise caps on conversion campaigns, so control frequency via: larger audiences (go broad), more active ads (impressions distribute), budget pacing, and exclusions (recent purchasers, recent converters). Targets: prospecting 1-2 impressions/person/week; retargeting 3-6/week.

## Add Relevance Diagnostics to the Weekly Read

Alongside frequency, CTR and CPM, pull the three relevance rankings for each ad in the weekly workflow. **Below Average on all three is a kill**, regardless of what frequency says — the concept lost the auction on every dimension. Rankings declining *while frequency climbs* confirms fatigue rather than a relevance problem. See **meta-relevance-diagnostics** for reading them.

## Related Skills

- **full-audit**: The evidence-graded audit lane — 30 sections against live account data, where these benchmarks get tested rather than assumed.
- **creative-cadence-operating-system**: The production side — iteration hierarchy, testing volume math, and cadence that keeps replacements ready before fatigue hits.
- **meta-creative-strategy**: The angles and concepts to build when the pipeline needs new creative.
- **meta-relevance-diagnostics**: Reading Quality, Engagement Rate and Conversion Rate Ranking to tell a relevance problem from a fatigue one.
- **meta-creative-formats**: Format-specific specs and the placement fit behind format lifespan differences.
- **meta-ads**: The e-commerce Meta hub — campaign structure, audiences, and account-level ROAS/CAC strategy.
