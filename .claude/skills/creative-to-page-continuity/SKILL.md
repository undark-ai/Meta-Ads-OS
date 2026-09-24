---
name: creative-to-page-continuity
description: When scoring whether a landing page keeps the promise the Meta ad made — claim, visual and offer continuity from creative to page, and the promise-handoff score the dashboard renders. Use when the user asks "message match," "why do clicks not convert," "the ad and the page don't match," or when a large landing-page-view to add-to-cart gap needs a cause. The single largest post-click lever on paid social. For the page's own merits, see paid-social-landing-page.
---
# Creative-to-page continuity

The ad made a promise to a stranger who was not shopping. The page has about two seconds to
confirm they are in the right place.

On search, the visitor typed the query — they arrive already oriented. On paid social they
arrive mid-scroll, having been interrupted, holding one specific expectation the creative
created. Break that expectation and they leave, and the account pays for the click either way.

This is usually the largest single post-click lever, and it is fixable without redesigning
anything.

## The three continuities

| Continuity | The question | Breaks when |
|---|---|---|
| **Claim** | Is the ad's core claim repeated, in similar words, in the first screen? | The ad says "no more counting calories" and the page says "personalised nutrition platform" |
| **Visual** | Is the ad's hero image or scene recognisable on the page? | A UGC ad in a kitchen lands on a page of studio product shots |
| **Offer** | Is the offer the ad named present, at the price the ad named? | The ad says €20 off, the page shows full price and the code appears at checkout |

Offer breaks are the most damaging and the easiest to find. Someone who clicked an offer and
cannot see it assumes they were misled, and no amount of page quality recovers that.

## The promise-handoff score

Scored 0–1 per ad and stored on the creative record. It is what the dashboard's drill-down
renders, and what §19 and §20 cite.

| Component | Weight | Check |
|---|---|---|
| Claim repeated above the fold, on **mobile** | 0.30 | Not "present on the page" — present in the first screen at a phone viewport |
| Visual recognisable | 0.20 | Same product, same scene register, same person if the ad featured one |
| Offer present at the named price | 0.25 | Including the mechanism — code, automatic, threshold |
| Objection answered | 0.15 | If the ad raised one, the page addresses it without scrolling to an FAQ |
| Awareness level matched | 0.10 | An L1-unaware ad landing on a PDP asks the visitor to buy before they know what it is |

Record `promise_handoff_gaps` as named mismatches, not a number alone. "Claim not repeated;
hero image differs; offer absent above fold" is what a team can act on; 0.42 is not.

## Awareness-level mismatch

The mismatch that most often looks like a creative failure and is not.

An ad written for someone who does not yet know they have the problem cannot land on a product
page and expect a purchase. It needs an intermediate step — an advertorial, a quiz, an
explainer — and without one the ATC rate collapses while the ad's hook rate looks excellent.

Check `awareness_level` on the creative record against the destination:

| Awareness | Appropriate destination |
|---|---|
| L1 unaware | Advertorial, quiz, educational content |
| L2 problem-aware | Problem-framed landing page, quiz |
| L3 solution-aware | Category or comparison page |
| L4 product-aware | PDP |
| L5 most aware | PDP with the offer, or straight to cart |

An account routing every ad to the homepage regardless of awareness level has one finding that
explains several sections at once.

## Scoring it

1. Pull `link_url` per ad from the creative database; resolve the redirect chain.
2. Capture each distinct destination as a landing-page genome (`creative-dashboard`'s
   `LP_GENOMES`): hero claim, trust elements, section order, offer, CTAs — by **actually
   fetching the page**, at a mobile viewport, in an in-app browser context, cold.
3. Compare each ad's creative content against its destination's genome.
4. Score, record the named gaps, and store on the creative record.

Re-capture the genomes every run. A stale summary produces a confidently wrong score, which is
worse than no score.

## Reading the result

- **Low handoff, low ATC rate** → fix the handoff first. It is cheaper than new creative and it
  lifts every ad pointing at that page.
- **High handoff, low ATC rate** → the page's own merits are the problem
  (`pdp-for-paid-social`, `paid-social-landing-page`).
- **Low handoff, high ATC rate** → the page is carrying weak creative. Worth knowing, and
  usually means the offer is doing the work.
- **Handoff varies wildly across ads on one page** → the ads are promising different things and
  one page cannot serve them all. Either segment the destinations or narrow the creative.

## What this is not

It is not an argument for a dedicated landing page per ad. Most accounts cannot maintain them,
and a stale bespoke page is worse than a good shared one. The finding is usually **which promise
the page should keep** — the one the highest-spend ads are making — not that twelve pages are
needed.
