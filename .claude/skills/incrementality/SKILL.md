---
name: incrementality
description: When determining how much of Meta's reported revenue would have happened anyway — geo holdouts, conversion lift studies, retargeting incrementality, and the organic and direct interaction. Use when the user asks "is Meta actually driving sales," "incrementality," "holdout test," "geo lift," "conversion lift," "would they have bought anyway," or "what's my incremental ROAS." This is the question attribution cannot answer.
---
# Incrementality

> How much of Meta's reported revenue would have happened without Meta?

Attribution divides credit among channels for sales that happened. Incrementality asks whether
the sales would have happened at all. An account can have perfect attribution and be paying to
harvest demand it already had.

## Brand search is the cheapest incrementality signal you already have

A brand-search line converting far above the site average at a very low CAC is not a performing
channel — it is a **meter for demand other channels created**. Read it that way and it becomes
useful: when paid social scales, brand impressions and brand-search volume should follow, and a
paid-social campaign that lifts brand search is doing something its own reported ROAS cannot see.

This is also why `funnel-analysis` forbids comparing blended search to paid social. Folding brand
into a search figure and setting it against Meta credits Meta's own downstream effect to Google,
then uses it as the argument for moving budget away from Meta. Split it, report brand separately,
and treat its trend as evidence about *the other* channels.

Google Search Console makes this readable without a test — brand impressions and clicks over the
same window as the paid-social spend curve. It is not a holdout and does not replace one, but it is
free and already connected on most accounts.

## Why it matters most on Meta

Meta's strongest-reported campaigns are usually its least incremental:

- **Retargeting** reaches people who already visited. Reported ROAS is high; incremental ROAS is
 frequently a fraction of it.
- **Existing-customer campaigns** reach people who buy anyway. Advantage+ Shopping without an
 existing-customer budget cap does this by default.
- **Branded and high-intent audiences** capture demand created elsewhere.

Ranking budget by reported ROAS therefore moves money *toward* the least incremental spend —
systematically, and with the dashboard agreeing at every step.

## The methods, in order of strength

| Method | Strength | Cost | When |
|---|---|---|---|
| **Geo holdout** | Strongest available | Real revenue foregone in holdout regions | Multi-region accounts with enough volume per region |
| **Meta Conversion Lift** | Strong, and Meta runs it | Requires minimum spend and volume | Where eligible — check `ads_experiment_check_eligibility` |
| **Audience holdout** | Moderate — Meta's own split | Cheap | Retargeting incrementality specifically |
| **Full-channel pause** | Blunt but decisive | Expensive and disruptive | Where the question is "should this channel exist" |
| **Time-based on/off** | Weak — confounded by seasonality and everything else | Cheap | Last resort, and label the confounds |
| **Correlation with organic/direct** | Directional only | Free | A prompt to test, never a result |

## Designing a geo holdout

1. **Match regions on the outcome, not on population.** Pair regions with similar historical
 revenue trend, AOV and seasonality — not similar size.
2. **Hold out enough to detect the effect.** Under-powering is the standard failure: the test
 runs, returns "no significant difference", and everyone concludes Meta does nothing. Compute
 the detectable effect before starting, and if it is larger than the effect you care about, do
 not run the test.
3. **Run long enough for the purchase cycle plus the attribution window.** Two weeks minimum;
 four is better.
4. **Measure total regional revenue**, not Meta-attributed revenue. The whole point is to
 observe what happens to the business, not to what Meta claims.
5. **Change nothing else.** One material change at a time — this is where that rule earns its
 keep.

## Reading a lift study

`ads_experiment_lift_get_test` returns Meta's own conversion lift result. Two cautions:

- It is Meta measuring Meta. Classify `PLATFORM_STATED`. It is still far better than nothing, and
 far better than reported ROAS.
- Check the confidence interval, not the point estimate. A "34% lift" with an interval spanning
 zero is not a result, and it will be quoted as one.

## What to do without a test

Most accounts have never run one. Do not invent an incrementality adjustment — an assumed
haircut is worse than an admitted gap because it looks like a measurement.

Instead:

1. State plainly that incrementality has not been measured, and that reported ROAS on
 retargeting and existing-customer campaigns is therefore an upper bound.
2. Use structural proxies as **hypotheses**, labelled: retargeting share of spend, existing
 customers not excluded, high claim share concentrated in low-spend high-intent audiences,
 organic and direct trends that move independently of Meta spend.
3. Recommend the specific test worth running first, with its design and cost.

`scale-matrix.yaml` enforces this: a `SCALE` verdict on retargeting or existing-customer
combinations **requires** incrementality evidence. Prospecting may scale on reported figures with
confidence lowered and the gap named.

## Output

For §26: which tests have run, what they showed, the incrementality evidence class per major
spend bucket, and the one test that would most change the account's decisions. Where nothing has
been measured, that is the finding, and the recommendation is a test design rather than a
number.
