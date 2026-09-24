---
name: ad-library-extraction
description: When pulling competitor creative from the Meta Ad Library for competitive context — which angles, offers and formats the category runs, how long they have run, and which angles this account has never tested. Use when the user asks "what are competitors running," "competitor ads," "Meta ad library," "what angles are we missing," or "how does our creative compare." Competitive context only; never evidence that a competitor's ad is profitable.
---
# Ad Library extraction

The Meta Ad Library is public and it is the only outside reference a Meta creative audit has.
Google has no equivalent — you cannot see a competitor's search ads at this fidelity — which
makes §27 a section with no counterpart in the Google system.

## The rule that governs every finding here

**Longevity is not proof of profitability.** An ad running for six months means it is running.
Plenty of accounts leave losers on, and plenty of good ads are killed for reasons unrelated to
performance.

Every observation is competitive **context**, classified `PLATFORM_STATED` at best. There is no
evidence class in `finding-schema.yaml` that would let it become proof, and that is deliberate.

## What to pull

`ads_library_search` by advertiser or keyword:

- Which advertisers in the category are active, and roughly at what breadth
- Creative content: copy, format, hook, offer
- How long each ad has been running
- Which platforms and placements

## What to do with it

**Classify against the same taxonomy** the account's own creative uses (`creative-taxonomy`).
That is the whole point: an angle inventory that cannot be compared to your own is a slideshow.

Then produce the two things §27 exists for:

1. **The category's angle distribution** — which concepts, proof types and offers the category
 leans on. Where the account's distribution differs sharply, that is either a differentiation
 or a blind spot, and the account should know which it intended.
2. **The gap list** — angles the category runs that this account has never tested. This is the
 most actionable output of the section, and it feeds §10's concept sourcing directly.

## Useful signals, honestly labelled

| Signal | What it suggests | What it does not prove |
|---|---|---|
| An ad running many months | Worth investigating | That it is profitable |
| Many variants of one concept | The advertiser is iterating on it | That the concept wins |
| A sudden category-wide offer shift | Seasonal or competitive pressure | What it did to anyone's margin |
| An advertiser's total ad count | Production capacity | Efficiency |

**Do not benchmark spend.** The Library does not report it outside political advertising, and
estimates from third parties are estimates.

## What it cannot see

Performance, spend, targeting, landing pages behind gated flows, and anything paused before the
search. An absence in the Library is not evidence the competitor never ran it.

## Output

For §27: the category angle distribution, this account's distribution beside it, the untested
angle gaps ranked by how much of the category runs them, and any offer or format shift worth
noticing. Each labelled as context, and each ending in a **test to run** rather than a
conclusion to act on.
