---
name: delivery-diagnostics
description: When diagnosing why a Meta ad is expensive to deliver rather than why it converts badly — Quality, Engagement Rate and Conversion Rate Ranking, auction overlap, ad quality, and decomposing CPM into its causes. Use when the user asks "why are my CPMs so high," "Meta says my ad is below average," "quality ranking," "engagement rate ranking," "conversion rate ranking," "am I bidding against myself," or "auction overlap." For an ad that started strong and is decaying, see frequency-and-saturation.
---
# Delivery diagnostics

CPM is not a market price you accept. It is partly a verdict Meta has passed on the creative,
and the relevance rankings say which part.

This is Meta's own opinion about Meta, so every finding here is classified `PLATFORM_STATED`:
reportable, corroborated against outcomes, never proof on its own.

## The three rankings

Available per ad against ads competing for the same audience. Each is `Above Average`,
`Average`, `Below Average (bottom 35%)`, `Below Average (bottom 20%)` or `Below Average
(bottom 10%)`.

| Ranking | What it measures | What a low score costs |
|---|---|---|
| **Quality** | Perceived quality vs ads competing for the same audience — feedback, engagement-bait signals, low-quality attributes | Directly raises CPM. The auction discounts ads people dislike |
| **Engagement Rate** | Expected click, like, share, comment vs competitors | Raises effective cost per click |
| **Conversion Rate** | Expected conversion vs ads with the same optimisation goal | Raises effective CPA — Meta delivers less to people likely to convert |

**Fix the one that is actually failing.** They point at different layers and the fixes do not
transfer:

- Low **Quality** → the creative itself. Clickbait framing, sensational claims, poor production,
 negative feedback. Not a targeting problem.
- Low **Engagement** → the hook and the format. Nobody is interacting. This is the same diagnosis
 hook rate gives, arrived at from the other direction — check they agree.
- Low **Conversion Rate** → the **post-click experience**, most often. Meta is saying people who
 click do not convert relative to competitors. Route this to §20, not to creative. Replacing the
 ad will not fix a page that does not convert.

An ad below average on all three is not three problems; it is usually one upstream problem
(wrong audience, wrong offer) expressing itself three ways.

## Decomposing CPM

A rising CPM has a small number of possible causes, and they are separable:

| Cause | Evidence |
|---|---|
| Relevance penalty | Rankings dropped, same audience, same period |
| Audience narrowing | Audience size shrank, or exclusions grew; frequency rose |
| Auction pressure | `ads_insights_auction_ranking_benchmarks` shows competitor pressure up; industry benchmark moved too |
| Seasonality | Compare same weeks prior year, not last month. Q4 CPMs are not a finding |
| Self-competition | Auction overlap — multiple ad sets targeting overlapping audiences |
| Placement mix shift | Delivery moved toward more expensive placements; check the placement breakdown |
| Optimisation change | Different optimisation event or bid strategy; check the activity log |

Do not report "CPM is up 34%" as a finding. Report which of these it is, and say what evidence
separated it from the others. "CPM up 34%, of which the placement mix shift toward Reels
accounts for roughly half" is a finding; the raw number is a symptom.

## Auction overlap and self-competition

`ads_insights_auction_ranking_benchmarks` shows where your own ad sets compete against each
other. This is one of the few genuinely self-inflicted costs on Meta, and it is common:

- Overlapping lookalike percentiles (1% and 1–3% both running)
- Prospecting and retargeting without exclusions
- Advantage+ Shopping running alongside manual campaigns targeting the same catalog — **the
 single most common version**, because ASC is designed to buy the whole funnel and manual
 campaigns are then bidding against it
- Duplicated ad sets from a "test" that was never cleaned up

Quantify as spend at risk, not as a count of overlapping sets: "€18k/month across two ad sets
with 61% audience overlap" lands where "audience overlap detected" does not.

## Industry benchmarks

`ads_insights_industry_benchmark` gives CPA, CPM and CTR context. Two rules:

1. **Vertical, not global.** Apparel and high-ticket B2B do not share a CPM.
2. **Context, never a target.** An account at 1.4× benchmark CPM with an excellent margin
 structure is fine. An account at benchmark with a thin margin is not. §1's break-even ROAS
 decides; the benchmark only says whether the delivery cost is unusual.

## Meta's ranking architecture — context, not a rule

Meta's engineering material describes a multi-stage ranking stack: a retrieval stage narrowing a
large eligible pool, a ranking model using longer behaviour sequences, and a consolidation layer
across surfaces.

Use this only to sharpen audit questions: is the optimisation data valid, timely, deduplicated
and aligned to real business value; are the creative variants genuinely distinct rather than
resizes of one asset; is the account structure solving a real constraint.

**Never** use it to justify a specific campaign count, creative-angle count or budget split
someone read in a conference recap. Tag any claim leaning on it `PLATFORM_STATED`, and never
present a vendor-reported lift number as this account's expected result.

## Output

Per ad or ad set with material spend: the three rankings, the CPM decomposition, the auction
overlap exposure in currency, and **one** named layer to fix. Where the rankings and the
account's own funnel data disagree — Meta says Conversion Rate is above average, but the
post-click funnel is leaking — say so and trust the first-party data.
