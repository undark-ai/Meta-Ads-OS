---
name: creative-angle-analysis
description: When determining which creative dimension actually drives purchases on a Meta account — hook, problem, benefit, product, proof point, objection, format, creator, opening three seconds, CTA, offer or persona — rather than which individual ad won. Use when the user asks "which angle wins," "what should we make next," "why did that ad work," "which hooks perform," or "build me a creative learning system." Requires a classified creative database. For classification, see creative-taxonomy. For deciding how much more to spend on a winner, see scale-matrix.
---
# Creative angle analysis

Don't ask "which ad won". Ask which **dimension** won, and whether it won on purchases or only
on clicks.

The output is a creative learning system: a set of statements about what this account's
customers respond to, each attached to evidence, that survives the ads it was learned from.

## The twelve questions

For each, the same method: aggregate the classified creative database by that dimension, on
spend and purchases, and compare against the account median.

1. Which **hook** wins?
2. Which **problem** wins?
3. Which **benefit** wins?
4. Which **product** wins?
5. Which **proof point** wins?
6. Which **objection**, addressed head-on, wins?
7. Which **format** wins?
8. Which **creator** wins?
9. Which **opening three seconds** win?
10. Which **CTA** wins?
11. Which **offer** wins?
12. Which **persona** responds?

And the one that gates all of them: **which of these generate purchases rather than just
clicks?**

## Purchases, not clicks

The most common failure of creative analysis is ranking on CTR or hook rate because those have
volume and purchases do not. It produces a confident, well-evidenced ranking of the ads best at
generating cheap attention, which is not the thing being bought.

Rank on:

1. **Contribution per dollar** — first choice, where margin is available
2. **New-customer CAC** — where the §1 goal is acquisition
3. **Purchase CVR and CPA** — where margin is not available
4. Hook rate, hold rate and CTR — **diagnostic only**, never the ranking

An angle with excellent hook rate and below-median purchase CVR is not a winning angle. It is an
angle that attracts the wrong people, and scaling it buys more of them.

## The volume problem, honestly

Ad-level purchase counts on Meta are small. Most accounts have a handful of ads with enough
purchases to say anything about, and dozens with three or four.

This is the constraint that makes the analysis hard, and pretending otherwise is how creative
analysis produces confident nonsense.

**Aggregate to the dimension, not the ad.** Twelve ads sharing an angle, each with 4 purchases,
is 48 purchases on that angle — enough to say something, where no individual ad was. This is the
main reason classification is worth the effort.

Even aggregated, apply the floor from `learning-phase-and-significance`. Below it the answer is
`INSUFFICIENT_DATA`, and the recommendation is to concentrate the next round of testing on that
dimension rather than to act on the reading.

## Confounds to rule out before claiming a dimension won

Creative dimensions are not randomly assigned. They correlate with everything, and most
"winning angle" findings are one of these instead:

| Confound | Check |
|---|---|
| **Spend concentration** | Is the "winning" angle one ad with most of the budget? Then you learned about an ad, not an angle |
| **Audience** | Did the angle run only to retargeting? Retargeting flatters everything it touches |
| **Time** | Did it run during a promo, a peak, or a period when the whole account performed? Compare against the account's own trend, not a flat baseline |
| **Learning phase** | Were the ad sets stable? An ad set that re-entered learning is reporting the edit, not the ad |
| **Product** | Is the angle bound to the hero product? Then the product may be winning and the angle riding along |
| **Landing page** | Did it point somewhere different? A quiz funnel versus a PDP is not a creative difference |
| **Placement** | Reels-heavy delivery has different economics. Check the placement mix per angle |
| **Advantage+ Creative** | Were the enhancements on for one group and not the other? |

State which confounds were checked. A finding that names its confounds is worth several that
do not.

## Interaction, not just main effects

The single-dimension answer is the start. The useful answer is usually an interaction:

- angle × audience — the angle that wins on broad often loses on retargeting, and vice versa
- angle × product — an angle that carries the hero product may not carry the range
- angle × offer — an angle that needs a discount to work is a different proposition from one
 that does not
- hook × format — the same hook lands differently as static and as video
- creator × persona — matching is frequently the whole effect

Interactions run out of volume faster than main effects. Test the two or three the main effects
suggest, not the full grid.

## What a learning looks like

A finding here is written to survive the ads it came from:

> **Objection-handling openers on the price objection outperform benefit-led openers for
> first-time buyers.** 9 ads, €31k spend, 214 purchases; purchase CVR 3.1% vs account median
> 1.9%; new-customer CAC €41 vs €58. Holds across two products and both offer states. Checked:
> spend concentration (top ad is 22% of the angle's spend), learning phase (all ad sets stable),
> placement mix (within 5pp of account). Confidence: MEDIUM — angles are model-classified for 4
> of the 9 ads.
>
> **Next:** brief three new objection-handling openers against the fit objection and the
> effort objection, to test whether the effect is about objections or about price specifically.

Note what it does: names the dimension, quantifies against a median, states the population,
names the confounds checked, states the classification source, and proposes the test that would
falsify or extend it.

## Write it down

The learning goes somewhere durable — a creative learning document the account keeps between
audits — not just into this run's report. §10 audits whether that document exists, because an
account that re-learns the same thing every quarter is paying for the same lesson repeatedly.

Each entry: the statement, the evidence, the date, the confidence, and what was tested next.
