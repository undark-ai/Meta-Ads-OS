---
name: cro-experiment-design
description: When designing a post-click test that Meta traffic volumes can actually resolve — sample size and minimum detectable effect from real traffic, guardrail metrics, and deciding whether a test is worth running at all. Use when the user asks "should I A/B test this," "how long will this test take," "is this result significant," or before committing a page change to a test. For the general A/B testing method, see ab-testing; this covers the volume reality of paid-social traffic.
---
# CRO experiment design

Most proposed CRO tests on a D2C account cannot be resolved by that account's traffic. Running
them anyway costs weeks and produces a shrug that gets interpreted as "no difference".

The first job of this skill is to say, honestly, whether the test is worth running.

## Start from the minimum detectable effect

Work backwards from the traffic, not forwards from the hypothesis:

```
Given: baseline conversion rate, weekly sessions on the page, an acceptable test duration
Compute: the smallest effect the test could detect at that volume
```

Then ask the only question that matters: **is that effect smaller than the one you care about?**

If a page gets 3,000 sessions a week at a 2% conversion rate, a four-week test can reliably
detect roughly a relative 25–30% change — not a 5% one. If the change under test plausibly moves
conversion by 8%, the test cannot see it, and running it produces a false negative that gets
treated as evidence the change does not work.

## What to do when the test is under-powered

Three honest options, in order:

1. **Test something bigger.** A radical variant resolves where a button-colour change never
   will. Test the offer, the hero claim, the page structure — not the copy tweak.
2. **Ship it on judgement, and monitor.** Where a change is clearly correct — express payment,
   shipping stated earlier, an offer the ad promised now visible — the correct action is to ship
   it and watch the funnel, not to hold it hostage to a test that cannot resolve.
3. **Pool traffic.** Test at the template level across many products rather than on one PDP.

What not to do: run the under-powered test, get an inconclusive result, and record it as "no
effect". That is how good changes get rejected on evidence that never existed.

## Guardrails

Every test needs a metric it must not damage, agreed in advance:

| Primary | Guardrail |
|---|---|
| Add-to-cart rate | Purchase rate — a change that lifts ATC and drops purchase moved friction downstream |
| Conversion rate | AOV — a discount lifts conversion and can lose contribution |
| Checkout completion | Refund and chargeback rate |
| Email capture | Purchase rate — an aggressive popup buys addresses with orders |

Rank the result on **contribution**, not on the primary metric alone. A variant that lifts
conversion 12% and drops AOV 15% lost money.

## The traffic-mix trap

Meta traffic composition changes constantly — creative rotates, placements shift, audiences
saturate. A page test running across a creative refresh is comparing two different populations,
and the page change is confounded with the audience change.

- Keep the ad set and creative mix stable for the test's duration, or accept the confound and
  say so.
- Do not start a page test in the same week as a campaign restructure — `14-day-change-control`
  applies to post-click changes too.
- Check §5's change map before trusting any test that spans a structural change.

## Set the kill number in advance

The test's stopping rule is agreed before it runs: the sample it needs, the date it will be
read, and what result triggers which action. A test without one gets stopped when someone likes
the number, which is not a test.

`test-schema.yaml` records it. `learning_recorded` on that schema is the field that matters
most — a result nobody wrote down gets re-tested next quarter.

## When not to test

- The change is required for correctness (a broken variant selector, a missing express payment,
  a shipping cost that surprises). Ship it.
- The traffic cannot resolve the effect and the change is cheap. Ship it and monitor.
- The change is a continuity fix the ads already paid for
  (`creative-to-page-continuity`). Ship it.

Testing is for changes where the direction is genuinely uncertain and the volume can resolve it.
Everything else is a decision, and dressing a decision as a test delays it by a month.
