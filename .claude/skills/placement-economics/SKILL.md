---
name: placement-economics
description: When judging which Meta placements earn their share of budget — Feed, Stories, Reels, Explore, Audience Network, Messenger — after conversion rate and AOV rather than on last-click ROAS. Use when the user asks "should I exclude Audience Network," "which placements work," "placement breakdown," "are Reels worth it," or "should I run Advantage+ placements." Includes how to test an exclusion without resetting learning.
---
# Placement economics

Placement problems hide inside campaign averages. A campaign can show an acceptable blended ROAS
while one placement is actively unprofitable and another is starved of the budget it deserves.

## Pull it as its own query

`platform_position` is incompatible with `age` and `gender`. One breakdown dimension per call
(`meta-ads-data-validation`), and reconcile the placement rows against the campaign total — if
they do not sum, rows are missing.

Recompute every rate **from summed components**. Never average CPM, CTR or ROAS across placements;
a placement with 2% of impressions would weigh the same as one with 60%.

## Classify, don't rank

| | Criteria | Action |
|---|---|---|
| 🟢 **Star** | ROAS above account average **and** above ~15% of spend | Maintain or increase |
| 💎 **Hidden gem** | ROAS above ~2× account average **but** under ~10% of spend | Underinvested — scale it |
| 🔴 **Waste** | ROAS under ~50% of account average **and** above ~10% of spend | Reduce or exclude |
| ⚠️ **Low volume** | Under ~5% of spend | Insufficient data. Monitor; do not act |

The hidden-gem quadrant is the one most audits miss, because a ranked list puts it near the bottom
on volume. It is frequently the best available reallocation.

## Judge on economics, not last-click ROAS

A placement's reported ROAS is the least reliable input available here:

- **New-customer rate differs sharply by placement.** A placement with lower ROAS that skews new
  customers may be worth more than a higher-ROAS one recycling existing buyers (§24).
- **AOV differs by placement.** Two placements at the same ROAS with different AOVs contribute
  differently.
- **Upper-funnel placements get under-credited** by a click-based window. Reels and Stories drive
  discovery that converts elsewhere; killing them on last-click ROAS is a common, expensive
  mistake and only §26 can settle it.

So: CVR, AOV, new-customer rate and contribution — then the ROAS, with the caveat attached.

## Typical patterns — a starting reference, not a target

Verify against this account's own data before citing any of it:

| Placement | Character |
|---|---|
| Instagram Reels | High engagement, discovery-oriented — often over-indexes on clicks relative to purchases |
| Instagram Feed | Balanced reach and conversion |
| Facebook Feed | Usually the strongest direct-response placement |
| Instagram Stories | Suits urgency and CTA-led creative |
| Audience Network | Frequently the largest single source of wasted spend — check it first |

Audience Network deserves the specific attention because its waste is both common and easy to
quantify, and because accidental clicks inflate its click volume while contributing nothing.

## Advantage+ Placements

Meta distributes automatically and you cannot set allocation directly. Three things you *can* do:

1. **Exclude a specific placement** at ad-set level, where you have evidence.
2. **Supply placement-native creative** — 9:16 for Reels and Stories, 1:1 or 4:5 for Feed. Much
   apparent placement underperformance is a cropped asset, not a bad placement.
3. **Read where Meta is over-investing** and adjust the creative mix to match, rather than fighting
   the distribution.

Before recommending an exclusion, check the creative was actually native to that placement. A
letterboxed Feed video judged on its Reels performance is a production finding, not a placement
one.

## Testing an exclusion without wrecking the read

**Never edit placements on a live ad set to test an exclusion.** The edit resets learning, so the
post-change numbers describe the reset rather than the exclusion, and nothing can be attributed.

Duplicate the ad set, apply the exclusion to the duplicate, run both, compare. State the cost —
you are paying for two ad sets to learn one thing — and respect the read window
(`14-day-change-control`).

## Output

For §18: the placement matrix with each placement classified, the currency value of the waste
quadrant, the hidden gems with what scaling them would need, whether creative is placement-native,
and any exclusion recommendation written as a duplication test rather than an edit.
