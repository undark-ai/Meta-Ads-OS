---
name: advantage-plus-audit
description: When auditing Advantage+ Shopping and Advantage+ Creative on a live account — ASC structure and budget, the existing-customer budget cap, new-customer acquisition, catalog integration, and whether ASC is cannibalising the manual campaigns bidding against it. Use when the user asks "audit my Advantage+," "is ASC working," "ASC vs manual," "existing customer budget cap," or "is Advantage+ stealing from my other campaigns." For whether to adopt ASC at all, see meta-advantage-plus — that is the build-time question.
---
# Advantage+ audit

Two surfaces that get conflated and need auditing separately: **Advantage+ Shopping** (a campaign
type that buys the whole funnel) and **Advantage+ Creative** (enhancements Meta applies to assets
you uploaded). The second one changes the creative you thought you tested.

## The self-competition check — run it first

**ASC running alongside manual campaigns targeting the same catalog is the single most common and
most expensive Advantage+ finding.** ASC is designed to buy across the whole funnel, so a manual
prospecting or retargeting campaign on the same products is bidding against it in the same
auction. The account pays twice to reach the same person, and both campaigns report the purchase
as a success.

Check:

- Overlapping product sets between ASC and manual campaigns
- Auction overlap in `ads_insights_auction_ranking_benchmarks`
- Whether manual retargeting still runs while ASC is instructed to cover retargeting
- Whether the combined claimed purchases exceed store orders for those products (§3)

Quantify as **spend at risk**, not as a count of overlapping campaigns: "€22k/month across an ASC
and two manual campaigns on the same 40 products" is a finding.

## The existing-customer budget cap

ASC lets you cap the share of budget spent on existing customers. Left unset, ASC will happily
spend a large share of it reaching people who already buy — which produces excellent reported ROAS
and very little acquisition.

Three things to establish:

1. **Is the cap set at all?** Unset is the default, and it is the finding.
2. **Is it set where the §1 goal implies?** An account whose primary goal is new customers and
   whose ASC has no cap is optimising against its own objective.
3. **What is the actual new-customer share?** Requires the commerce join (§24). Where the join is
   unavailable this is `BLOCKED`, not estimated — and every ASC ROAS carries the qualifier.

The gap between ASC's reported ROAS and its new-customer CAC is usually the most informative
number in this section.

## Structure and budget

| Check | Why |
|---|---|
| ASC budget as a share of total | A large ASC share with no cap and no incrementality read is unmeasured spend |
| Number of ASC campaigns | More than one competes with itself; ASC is designed to be consolidated |
| Asset/creative mix inside ASC | Genuinely distinct concepts, or resizes of one asset? |
| Catalog connection and product sets | Which products ASC is actually allowed to sell |
| Country and placement scope | |
| Editing cadence | **Editing an existing asset group resets learning for the whole campaign**, not just that group — check the activity log against performance dips |

## Advantage+ Creative — a separate audit

Where enhancements are on, Meta may have cropped, added music, generated variants or restated
text. **You are then judging an ad you did not fully author.**

- Record which enhancements are active **per ad** on the creative record.
- A creative-mix conclusion drawn across ads where half were auto-enhanced is comparing two
  different things, and the enhancement is a plausible cause of any difference found.
- Enhancements that rewrite text can break the promise the landing page was built to keep
  (`creative-to-page-continuity`) — check the handoff score on enhanced ads specifically.

Non-adoption of Advantage+ is a **discovery item, not an automatic fail.** An account with a good
reason to run manual is not underperforming. What is a finding is an account that has never
evaluated it, or that leans on it entirely with no control group.

## Incrementality

ASC's reported ROAS is among the least incremental figures in the account, because it buys
retargeting and existing customers by design. A `SCALE` verdict on ASC needs evidence from §26,
not reported ROAS — `scale-matrix` enforces this.

Where no incrementality test has run, say so plainly and recommend the specific test: usually an
existing-customer holdout, which is cheap and directly answers the cap question.

## Output

For §17: the self-competition verdict with spend at risk, the existing-customer cap state and the
actual new-customer share, ASC structure findings, which enhancements are active and what they do
to the creative read, and the incrementality evidence class. Where ASC and manual overlap, name
which should own which part of the funnel rather than recommending both continue.
