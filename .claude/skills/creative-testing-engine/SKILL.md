---
name: creative-testing-engine
description: When auditing or designing a repeatable creative testing program for a Meta account — testing velocity, budget math, the iteration hierarchy, winner and kill criteria, and whether learnings are being written down. Use when the user asks "how many creatives should I test," "how much should I spend on testing," "when do I graduate an ad," "creative testing structure," "how often should we refresh," or "do we have a creative process." For deciding which dimension won, see creative-angle-analysis.
---
# Creative testing engine

Most accounts do not have a creative testing problem. They have a creative *system* problem:
tests run, results are read, and nothing is written down — so the same lesson is bought again
next quarter.

§10 audits whether the engine exists. This is what it is measured against.

## The two-campaign split

The structure that keeps testing from being starved and scaling from being disrupted:

| Campaign | Budget | Contains |
|---|---|---|
| **Scaling** | ~80% | Graduated ads only. Nothing enters without meeting the graduation bar |
| **Testing** | ~20% | New concepts and iterations, on protected budget |

The split matters because of what happens without it: testing budget is the first thing cut when
performance dips, which is precisely when the account most needs new creative in the pipe. A
protected allocation is a structural defence against a predictable managerial reflex.

The 80/20 is a starting point. Accounts with fast creative decay need more; accounts with
evergreen winners and thin production capacity need less. Derive it from the account's own
creative lifespan (`frequency-and-saturation`).

## How many tests the account can actually run

```
tests_per_week = (monthly_testing_budget ÷ (3 × target_CPA)) ÷ 4
```

The `3 × target CPA` is the spend needed to give one ad a fair read — enough to clear the
zero-conversion threshold in `learning-phase-and-significance` and produce a signal rather than
a coin flip.

Worked: €40k/month at 20% testing = €8k. Target CPA €50, so €150 per ad tested. €8k ÷ €150 = 53
ads/month ≈ 13/week.

Run this calculation before recommending a testing cadence. The common finding is that an
account is running **more** tests than its budget can read — twenty ads a week at €30 each, none
of which ever reaches a conclusion, producing a testing program that generates activity and no
learning. Fewer, better-funded tests beat more, starved ones every time.

Where the account's whole purchase volume sits below the floors, say so as a structural finding:
this account cannot run a creative testing program at this volume, and the fix is fewer, larger
tests.

## The iteration hierarchy

Not all "new creative" is equally new. Roughly:

| Layer | Share of production | What changes | Risk |
|---|---|---|---|
| **Iteration** | ~50% | Hook, opening, CTA, length on a proven concept | Low, reliable returns |
| **Variation** | ~30% | New angle or format on a proven concept | Medium |
| **New concept** | ~20% | Genuinely new angle, persona or mechanism | High, and where the step changes come from |

An account at 100% iteration compounds smoothly into a local maximum and then stalls. An account
at 100% new concepts never exploits what it learns. The **iteration ratio** — computable from
`iterated_from_ad_id` in the creative database — is one of the few numbers that says whether a
creative program is compounding.

## Winner and kill criteria, agreed in advance

Set before the test runs. Negotiating them afterwards is how losers get "one more week" and
winners get killed for being volatile.

| Decision | Bar |
|---|---|
| **Graduate to scaling** | ≥ 25 purchases, CPA at or below target, stable ≥ 7 days post-learning |
| **Iterate** | Above-median hook rate, below-target CPA — the attention works, the conversion does not |
| **Kill** | Spend ≥ 3× target CPA with zero purchases, lag elapsed; or ≥ 15 purchases at CPA well above target |
| **Keep testing** | Anything below the floor. `INSUFFICIENT_DATA` is a valid outcome |

All of these sit behind `learning-phase-and-significance`. A kill below the floor is variance,
not a decision.

## Where concepts come from

An engine needs an input, and "the creative team will think of something" is not one. The
sources that produce angles worth testing:

- **Reviews and support tickets** — the objection and the phrasing, in customers' own words
- **Post-purchase surveys** — what actually tipped them, which is rarely what the brand thinks
- **Sales and chat transcripts** — the questions people ask before buying
- **Competitor Ad Library** (§27) — angles the category runs that this account never has
- **The account's own winners** — the iteration layer

An account with no voice-of-customer input is guessing, and its angle library will be a list of
product features.

## Image-first validation

Static creative is cheap and fast. Validating an angle as a static before committing production
budget to video costs a fraction and reads faster — the hook and the claim are testable without
a shoot.

Not every angle survives the translation to video, so this is a filter rather than a proof. But
it is the cheapest filter available.

## What §10 audits

- New concepts, hooks, angles, creators, formats and offers per month
- Iteration ratio
- Testing velocity against the budget math above — is the account reading its tests?
- Testing budget as a share, and whether it survived the last downturn
- Winner and kill criteria: documented, or improvised each time?
- Whether fatigue is monitored at all, or noticed when performance drops
- **Whether learnings are written down.** An account that re-learns the same thing every quarter
 is paying for it every quarter

The last one is the finding that most often matters and is least often looked for. Ask to see
the document. If it does not exist, that is §10's headline.
