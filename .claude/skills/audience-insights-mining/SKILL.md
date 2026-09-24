---
name: audience-insights-mining
description: When building a quantitative profile of who actually converts on a Meta account — age, gender, device, country and daypart — from the account's own performance data rather than from assumption. Use when the user asks "who is buying," "which demographics convert," "should I narrow my targeting," "audience insights," or "are we reaching the right people." The quantitative counterpart to a persona library: this says which segments over-index, the persona work says why.
---
# Audience insights mining

Who converts, from this account's data. The counterpart to a persona library built from customer
voice: that one says *why*, this one says *which* — and the two disagreeing is itself a finding
worth reporting, because it usually means the creative is written for someone the account is not
reaching.

## Pull each breakdown separately

Several dimensions are mutually incompatible. One breakdown per call
(`meta-ads-data-validation`), reconciled against the parent total:

- Age
- Gender
- Age + gender — this pair *can* be queried together
- Country
- Device (`impression_device`)

Recompute every rate from summed components. Ranking segments on averaged ad-level ratios is the
fastest way to produce a confident, wrong demographic profile.

## The gap that matters: clickers versus converters

Volume rankings tell you where the traffic is. The **difference** between a segment's share of
clicks and its share of purchases tells you where the money is.

| Segment | % of clicks | % of purchases | Purchase CVR | Reading |
|---|---|---|---|---|
| | X% | Y% | Z% | 🟢 High-value converter · 🔴 Clicks but does not buy · 💎 Underserved |

- **Clicks a lot, rarely buys** — mistargeted, or the offer does not fit that segment. Attractive
  in every click-based report and worth less than it looks.
- **Small share of clicks, large share of purchases** — underserved. Usually the most actionable
  row in the section.

Rank on at least four axes and report more than one: **purchase CVR** (who converts), **ROAS or
contribution** (who is worth most), **volume** (who buys most), **CAC** (who is cheapest to
acquire). A segment can lead on one and be irrelevant on another, and a single-axis ranking hides
that.

## Before recommending a targeting change

The default answer to a demographic skew is usually **not** to narrow targeting. Three checks
first:

1. **Is the skew caused by the creative rather than the targeting?** On Meta, creative is closer
   to targeting than targeting is. A creative featuring one demographic will be delivered to that
   demographic; narrowing the audience to match confirms the creative's bias rather than testing
   it (§9).
2. **Does the skew survive the volume floor?** A segment with eleven purchases has not told you
   anything (`learning-phase-and-significance`).
3. **Would excluding the low-converting segment shrink the audience below what it needs to
   deliver?** Narrowing raises CPM and can trip learning-limited (`bid-strategy-and-learning`) —
   the efficiency gain gets eaten by the delivery cost.

Broad targeting with creative that speaks to a segment usually beats narrow targeting with generic
creative. The recommendation is more often a creative brief than a targeting change.

## Dayparting

Real, and usually smaller than it looks. Check whether an hour-of-day effect survives:

- Conversion lag — a purchase attributed to a click 6 days earlier says nothing about the hour
- Volume per bucket — 24 buckets divide thin purchase data 24 ways
- Whether the pattern is the audience's or the delivery system's

Recommend a schedule change only where the pattern is large, stable across weeks, and above the
floor.

## Output

For §12: the converter profile across each dimension, the clicks-versus-purchases gap table with
its verdicts, the segments that are underserved, and where the quantitative picture disagrees with
the account's stated persona. Recommendations routed correctly — creative where the cause is
creative, targeting only where the evidence supports it and the delivery cost has been checked.
