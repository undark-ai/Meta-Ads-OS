---
name: creative-taxonomy
description: When classifying what a Meta ad actually IS — concept type, angle, hook, proof, objection, offer, persona, creator and format — so creative performance can be aggregated by pattern instead of read ad by ad. Use when the user asks "what kind of ads are we running," "tag my creatives," "which concepts are we over-indexed on," or when the creative database needs its classification columns filled. For building the underlying dataset, see creative-data-model. For deciding which classification wins, see creative-angle-analysis.
---
# Creative taxonomy

A list of winning ads is not a learning. "Ad 41293 got a 3.2 ROAS" tells you to keep running ad
41293. "Founder-led problem/solution ads with a clinical proof point win at 2× the account
median across three products" tells you what to make next.

Classification is what turns the first into the second. It is the difference between a creative
report and a creative learning system.

## Three sources, and the source is recorded

| Source | When | Confidence effect |
|---|---|---|
| `NAMING_CONVENTION` | The ad name parses against the account's convention | Highest — a human encoded it at production time |
| `MODEL` | Name does not parse; inferred from copy, creative and landing page | Lower — carries into the finding's confidence |
| `HUMAN` | Someone corrected it | Highest, and it should be pushed back into the naming convention |

**Record which.** A §9 conclusion built on model-inferred angles is not as strong as one built
on a parsed convention, and the reader must be able to tell which they are reading. This is why
`concept_type_source` and `angle_source` are required columns rather than metadata.

## Naming conventions are load-bearing

Rule-based tagging runs off the account's ad-naming convention. That makes naming compliance a
**prerequisite for creative learning**, not a cosmetic hygiene finding — which is why §28 reports
it spend-weighted and says exactly what breaks without it.

A convention like:

```
110126_MENO_W_45-55_UGC_L1_HP_STATIC_OFFER_V01
│ │ │ │ │ │ │ │ └─ variant
│ │ │ │ │ │ │ └─ angle token
│ │ │ │ │ │ └─ format
│ │ │ │ │ └─ destination
│ │ │ │ └─ awareness level
│ │ │ └─ concept / format token
│ │ └─ audience
│ └─ angle
└─ date / concept id
```

...gives most of the classification for free. If no convention is documented, **infer the most
common pattern from the highest-spend ads and propose it as the standard** rather than declaring
the account non-compliant against a convention it never had.

Report compliance as a share of **spend**, not a count of ads. Ninety percent of ads parsing
while the three biggest spenders do not is a failing account, and a count-based metric hides it.

## Concept types

Sixteen, chosen because they are what production actually briefs against:

| Type | What it is |
|---|---|
| `PROBLEM_SOLUTION` | Names a problem, presents the product as the resolution |
| `PRODUCT_DEMO` | Shows the thing working |
| `UGC` | Customer-shot or creator-shot, unpolished register |
| `FOUNDER` | Founder to camera |
| `TESTIMONIAL` | A named customer telling their story |
| `REVIEW` | Review text or star ratings as the creative |
| `BEFORE_AFTER` | Transformation as the argument |
| `COMPARISON` | Against a competitor, a category, or the old way |
| `EDUCATIONAL` | Teaches something true whether or not you buy |
| `ENTERTAINMENT` | Earns attention on its own merits, sells second |
| `OFFER_PROMOTION` | The offer is the message |
| `SOCIAL_PROOF` | Volume of others as the argument — "50,000 customers" |
| `PRODUCT_BENEFITS` | What it does for you |
| `PRODUCT_FEATURES` | What it is |
| `OBJECTION_HANDLING` | Leads with the reason people don't buy |
| `LIFESTYLE` | Aspiration and context, product incidental |

`UNCLASSIFIED` is a valid value and is better than a wrong one. A concept mix that is 40%
unclassified is itself the finding.

## The other axes

Concept type alone is too coarse. Two `UGC` ads can differ on every axis that matters:

- **Angle** — the customer situation the ad speaks to. This is the axis that usually wins, and
 it is account-specific: "post-pregnancy", "gifting", "switching from a subscription", "the
 thing you already tried didn't work".
- **Hook** — the opening line, or the first-three-seconds description for video. Store the text,
 not a category; §9 clusters it afterwards.
- **Proof type** — `TESTIMONIAL`, `REVIEW_COUNT`, `CLINICAL`, `EXPERT`, `PRESS`, `UGC_VOLUME`,
 `DEMO`, `GUARANTEE`, `NONE`. `NONE` on a high-spend ad is a finding.
- **Objection addressed** — price, fit, effort, scepticism, timing, trust. Frequently the
 highest-leverage axis and almost never tracked.
- **Offer in creative** — joins to §21. **Null is a real value**: "no offer" competes against the
 discounts, and on many accounts it wins on margin.
- **Persona** — resolves against the account's persona library where one exists. Do not invent a
 fictional persona book to fill the column; build the library first.
- **Creator** — which UGC creator or talent. A real axis: creator effects are often larger than
 format effects, and they are actionable in a way format effects are not.
- **Format** — `SINGLE_IMAGE`, `SINGLE_VIDEO`, `CAROUSEL`, `COLLECTION`, `DYNAMIC`.
- **Duration** — video only.
- **Awareness level** — L1 unaware through L5 most aware. Determines what the ad can assume, and
 mismatches between awareness level and audience are a common structural finding.
- **Product IDs** — the join to §22 SKU economics, and the "product" axis of the scale matrix.

## Advantage+ Creative changes the thing you classified

Where Advantage+ Creative enhancements are on, Meta may have altered the asset after upload —
cropping, adding music, generating variants, restating text. **You are then classifying an ad
you did not fully author.**

Record which enhancements are active per ad. A creative-mix conclusion drawn across ads where
half were auto-enhanced is comparing two different things, and the enhancement is a plausible
cause of any difference found.

## Classification hygiene

**Do not classify from the ad name alone when the name does not parse.** A model reading copy,
creative and landing page produces a better answer than pattern-matching a filename someone
typed in a hurry, and it says so in `*_source`.

**Do not let classification drift between runs.** Two audits of the same account should produce
comparable pattern tables; a taxonomy that changes between them destroys the comparison. Where a
new value is genuinely needed, add it and note it in the run's `assumptions.md`.

**Do not classify what you cannot see.** If `ads_get_creatives` returned no copy for an ad —
which happens for some dynamic and catalog formats — the classification is `UNCLASSIFIED` with a
stated reason, not a guess from the campaign name.

## What the classification is for

Aggregation. Once every ad carries these columns, the patterns table becomes computable: tag →
ads, spend, purchases, CPA, ROAS, new-customer share. That table is the input to §9's "which
angle wins" analysis, and the angle axis of the scale matrix.

Aggregate on **spend and purchases**, never on ad count. Twelve ads on a losing angle and two on
a winning one is a production-allocation finding, and counting ads inverts it.
