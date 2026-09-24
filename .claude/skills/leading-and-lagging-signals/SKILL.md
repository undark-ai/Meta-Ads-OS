---
name: leading-and-lagging-signals
description: When the purchase count on an entity is too thin to judge it, and you need a faster signal that has been validated to predict purchases on this account. Use when the user asks "how do I judge an ad with 3 purchases," "can I optimise on CTR," "what CPC should I target," "what should my CPM be," "when do I pause a test ad," or when a creative, angle or placement verdict is about to be issued below the purchase floor. Also supplies the break-even chain that sets a target at every funnel stage, not just at purchase.
---
# Leading and lagging signals

`learning-phase-and-significance` sets purchase floors and says: below the floor the answer is
`INSUFFICIENT_DATA`. That is correct and it is not sufficient — because on a real account most
individual ads sit below the floor for their whole life, and "insufficient data" on every ad is
not an audit, it is an abstention.

This skill is what you do instead. Not lowering the bar — **using a different signal, and being
explicit that it is a different signal.**

| | Leading | Lagging |
|---|---|---|
| Examples | Hook rate, hold rate, outbound CTR, cost per LPV, cost per ATC, cost per checkout | Purchases, CPA, ROAS, new-customer CAC, contribution, LTV |
| Available | Within days, at ad level | Weeks, and only where volume accumulates |
| Volume at ad level | Thousands of impressions, hundreds of clicks | Often single-digit purchases |
| Authority | Directional. Never a finding on its own | The verdict |
| Failure mode | Optimises the wrong thing, confidently | Arrives too late to act on |

The B2B version of this problem is a 2–24 month sales cycle. The D2C version is not time —
purchases land in days — it is **sparsity per entity**. A €4,000/month account with a €40 CPA
banks 100 purchases a month across perhaps 40 live ads. The account has plenty of data. Almost
none of its ads do.

## The rule

> A leading signal may be used to rank, prioritise or triage. It may not be used to issue a
> verdict unless it has been **validated on this account** to predict the lagging one.

Validated means measured, on these ads, in this window — not assumed because the metric is
famous. Hook rate predicting purchases is an empirical claim about an account, and on plenty of
accounts it is false.

## Validating a leading signal

Do this in §9 before any angle conclusion leans on a leading metric:

1. Take the entities that **do** clear the purchase floor — usually ad sets, angles or creative
 concepts rather than individual ads. Aggregate ads up to that level; never average their
 ratios (recompute from component sums).
2. Rank them by the candidate leading signal, and separately by CPA or purchase CVR.
3. Report the rank correlation, the n, and the window. `n` is the number of entities compared,
 not the number of ads.
4. Publish it as a stated correlation with its n — `INFERRED`, never `OBSERVED`, and never a
 causal claim. It is a within-account regularity, and it can change with the offer, the season
 or the audience.

With fewer than roughly 8–10 qualifying entities, say the correlation could not be established
and fall back to lagging signals with `INSUFFICIENT_DATA` on the rest. A rank correlation on
four points is decoration.

Where it holds, say so and use it, with the correlation quoted at the point of use. Where it
does not hold — a common and useful finding — say **that**: an account whose hook rate does not
predict purchases is an account whose creative team is optimising the first three seconds
against nothing, and that is a §9 finding in its own right.

## Leading signals are gameable, and Meta will game them for you

This is the failure mode that matters, because it is invisible in the reporting.

- A **bait opening** — a face, a jump cut, a loud claim unrelated to the product — lifts hook
 rate and 3-second plays and depresses purchase CVR. The dashboard shows the ad improving.
- **Clickbait copy** lifts outbound CTR and fills the landing page with people who did not want
 the product. Cost per LPV falls; cost per ATC rises.
- Optimising an ad set toward a **cheaper event** (LPV, ATC) buys the audience most likely to do
 the cheap thing, which is not the audience most likely to buy.

So: a leading signal that moves in the right direction while the lagging one moves in the wrong
direction is not a mixed result. It is evidence the leading signal has been gamed, and the ad is
worse. Check the pair before reporting either.

A usable leading signal is measurable, movable, not an average, correlated on this account, and
not trivially inflatable. Hold-rate-through-to-outbound-CTR passes more often than hook rate
alone, because it is harder to fake both ends.

## The break-even chain

Break-even ROAS and the CAC ceiling come from `cac-and-roas` and set a target at **purchase**.
That is one target, at the slowest, sparsest point in the funnel. Propagate it backwards through
the account's own observed step-through rates and you get a target at every stage — each of
which has 10× to 1000× the volume of the one below it.

```
target_cpa            = cac_ceiling                       (from cac-and-roas)
target_cost_per_ic    = target_cpa  × checkout→purchase rate
target_cost_per_atc   = target_cost_per_ic  × atc→checkout rate
target_cost_per_lpv   = target_cost_per_atc × lpv→atc rate
target_cpc            = target_cost_per_lpv × click→lpv rate
target_cpm            = target_cpc × ctr × 1000
```

Worked, at a €30 CAC ceiling with the account's own rates — 25% checkout→purchase, 30%
ATC→checkout, 8% LPV→ATC, 80% click→LPV, 1.4% CTR:

| Stage | Target |
|---|---|
| Purchase | €30.00 |
| Initiate checkout | €7.50 |
| Add to cart | €2.25 |
| Landing page view | €0.18 |
| Click | €0.14 |
| Mille (CPM) | €2.02 |

Two rules on using it:

- **The rates are the account's, measured, from §19.** Benchmark step-through rates make the
 whole chain fiction. If §19 could not measure a step, that link and everything below it is
 `null` — not filled with a plausible number.
- **A target beaten upstream and missed downstream localises the leak.** An ad hitting €0.13
 CPC and €4 cost per ATC is not an expensive ad; it is a page or offer problem, and it belongs
 in §20 rather than in a creative kill list. This is the chain's real value: it says *where*,
 which a CPA alone never does.

The chain is also how you set a floor for a brand-new ad that has no purchases at all. It is not
a verdict — it is a bound.

## Spend-loss caps, which are not significance tests

Two operating rules, carried in because they are what teams actually run. State plainly what
they are: **caps on how much you are willing to lose to find out**, not evidence that an ad is
bad.

| Rule | Trigger | Applies to |
|---|---|---|
| Non-performer | Spent 2–3× target CPA with zero purchases → pause | New ads in test |
| Maintenance | Trailing 7–14 day CPA 1.5–2× target → pause | Established ads |

An ad paused by the non-performer rule at 3× target CPA and zero purchases has **not** been
shown to be worse than its stablemates — at that spend the confidence interval is wide enough to
contain a perfectly good ad. What has been shown is that you have spent €90 to learn nothing,
and you would rather spend the next €90 on a different ad. That is a defensible budget decision
and an indefensible creative verdict, and this system will not let it be written up as the
second.

So a pause under either rule is logged as a **budget action with the spend and the zero stated**,
never as a creative learning. Nothing enters the creative learning system on this basis. The
maintenance rule is the stronger of the two — a trailing CPA over a 7–14 day window on an
established ad usually has real purchase volume behind it, and where it clears the floor in
`learning-phase-and-significance` it is a verdict, not a cap.

Check learning-phase state before either. An ad set that reset four days ago fails both rules on
schedule, and neither pause would mean anything.

## Signals by demand-lifecycle stage

Which leading signal is even plausible depends on the job the spend is doing (`demand-lifecycle`).

| Stage | Leading | Lagging |
|---|---|---|
| Create | Hook rate, hold rate, cost per LPV, new-visitor share | New-customer CAC, blended MER, incremental revenue |
| Capture | Outbound CTR, cost per ATC, cost per checkout | New-customer CAC, contribution per order |
| Accelerate | Cost per checkout, checkout→purchase rate | Incremental conversion rate |
| Revive | Cost per LPV among lapsed, reach against the lapsed list | Reactivation rate, contribution per reactivated customer |
| Expand | Reach and CTR among existing customers | Repeat rate, contribution per customer, LTV movement |

Judging a Create campaign on cost per ATC applies a Capture yardstick to spend whose job is to
make demand that did not exist. It will fail, correctly by that measure and wrongly for the
account — which is the mechanism by which accounts defund the only thing making them grow.

## Where this is cited

§9 (angle conclusions below the purchase floor) · §10 (test read-outs and kill criteria) ·
§18 (placement triage before an economics call) · §19 (localising the leak with the chain) ·
§29 (ranking candidates when purchase data is thin).

Every use carries the same tag: which signal, whether it was validated on this account, the
correlation and n if so, and the lagging number it stands in for.
