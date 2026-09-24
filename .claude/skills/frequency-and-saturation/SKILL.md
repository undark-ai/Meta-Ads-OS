---
name: frequency-and-saturation
description: When diagnosing whether a Meta ad is dying because the creative wore out or because the audience ran out — frequency thresholds by campaign type, audience size and saturation, reach curves, and the different fixes each requires. Use when the user asks "my frequency is too high," "is this audience saturated," "why is CPM rising on the same creative," "how often should I refresh," or "is this creative fatigue or audience fatigue." For the creative-side decay signals specifically, see the fatigue analysis in the creative sections.
---
# Frequency and saturation

Two failures that look identical in the metrics and have opposite fixes:

- **Creative fatigue** — the audience is large enough, but this specific ad has been seen too
 often by the people it reaches. Fix: new creative.
- **Audience saturation** — the ad may be fine; the addressable pool is exhausted at this spend.
 Fix: widen the audience, or accept the ceiling.

New creative into a saturated audience buys a brief lift and then the same decline, and it is
the more expensive mistake because it also consumes production capacity.

## Telling them apart

| Signal | Creative fatigue | Audience saturation |
|---|---|---|
| Frequency | High on **this ad** | High across **every ad** in the ad set |
| A new ad in the same ad set | Recovers to near-original performance | Also underperforms, from launch |
| Reach | Still growing | Flat despite rising spend |
| CPM | Rising modestly | Rising sharply |
| CTR | Declining on the fatigued ad | Declining across the set |
| Audience size vs reach | Reach well below audience size | Reach approaching audience size |
| Placement mix | Unchanged | Drifting toward cheaper inventory as good inventory exhausts |

**The diagnostic that settles it:** launch a genuinely new concept into the same ad set. If it
performs, the problem was the creative. If it does not, the problem is the audience — and no
amount of creative will fix it.

## The seven diagnoses

Pattern-match the decay to one signature, prescribe one move, stop. Do not try to be
comprehensive — run again on a different cut if needed. **If the signature does not match
cleanly, say so** rather than forcing a diagnosis onto data that does not support one.

| # | Diagnosis | Primary signature | Secondary | First move |
|---|---|---|---|---|
| 1 | **Concept fatigue** | Frequency above threshold on cold + CTR falling week on week | CPM stable, hold rate falling | Hook batch refresh on the same body |
| 2 | **Audience saturation** | Frequency above threshold + CPM rising + reach plateaued | CTR stable, CPA rising | Widen the audience, or add a lookalike tier |
| 3 | **Broken bridge** | Hook rate steady, **hold rate dropped sharply** | Video drop-off concentrated in the 8–15s window | Re-edit that window; keep the hook |
| 4 | **Wrong offer** | CTR strong, **CVR dropped sharply** | Funnel starts steady, completions falling | Test an alternate offer — or fix the page (§20) |
| 5 | **Auction pressure** | CPM up sharply week on week + auction overlap flagged | CTR stable, CPA rising in proportion to CPM | Consolidate ad sets; check self-competition (§11) |
| 6 | **Audience too narrow** | Spend stuck below the budget cap + frequency rising fast | Reach plateaued under budget | Broaden, or merge with an adjacent ad set |
| 7 | **Concept never landed** | Low lifetime spend + weak CTR **from day one** | No retention past the 25% video mark | Kill. The concept is the problem; this is not fatigue |

Diagnosis 7 is the one most often mislabelled as fatigue. An ad that never worked is not decaying,
and refreshing its hook buys another weak ad. Check `first_seen_date` and the ad's *opening* week
before calling anything fatigue.

Diagnosis 3 is the one most often missed, because the ad still stops the scroll: the hook works and
the middle loses them. It is a cheap fix and only visible if hook and hold rate are read
separately.

Two matching at once is normal — an account can fatigue for more than one reason. Report both,
ranked by spend at risk.

## Frequency thresholds

Frequency has no universal ceiling. It depends on campaign type, window and creative variety,
and quoting "3.0" without those is meaningless.

| Campaign type | Window | Watch | Act |
|---|---|---|---|
| Broad prospecting | 7 days | > 1.8 | > 2.5 |
| Interest / lookalike prospecting | 7 days | > 2.0 | > 3.0 |
| Retargeting — mid funnel | 7 days | > 3.0 | > 4.5 |
| Retargeting — cart abandoners | 7 days | > 4.0 | > 6.0 |
| Existing customers / winback | 30 days | > 4.0 | > 6.0 |

These are prompts to investigate, not kill triggers. Frequency alone is never the finding —
frequency **plus** a rising CPM or declining CTR against the ad's own baseline is.

Measure at the level you intend to act on. Ad-set frequency hides a single ad carrying most of
the impressions, and ad-level frequency ignores that a person sees the whole set.

**Never average frequency across entities.** Recompute from impressions and reach.

## Audience size and reach

Saturation is reach approaching addressable size, not a frequency number:

```
saturation_ratio = reach (window) / estimated addressable audience size
```

Above roughly 0.5 on a prospecting audience, expect rising costs. Above 0.7, the audience is
effectively exhausted at this spend and the only levers are widening it or accepting the ceiling.

Meta's audience size estimates are wide ranges and are `PLATFORM_STATED`. Use the ratio as a
trend across the audit window rather than a precise number: the direction is reliable, the level
is not.

Small audiences saturate fast, which is the argument against tight interest stacks that has
nothing to do with targeting theory: a 200k audience at €500/day is exhausted in days, and every
subsequent day is more expensive than the last.

## Retargeting saturation specifically

Over-retargeting is the most common saturation failure and the hardest to see, because the
reported ROAS stays high the whole way down. The pool refills only as fast as prospecting fills
it, so retargeting spend that outpaces prospecting is spending more to reach the same people
more often.

Check:

- Retargeting spend as a share of total, against the rate at which prospecting adds new site
 visitors
- Frequency on the shortest window (1-day, 7-day) — these saturate first
- Whether existing customers are excluded. If not, retargeting ROAS is partly repeat purchases
 that were going to happen
- Whether the retargeting ROAS survives an incrementality test (§26). It usually does not
 survive intact

## Refresh cadence

Derive it from the account's own data, not a rule of thumb. Take the median time from launch to
the point where an ad's CTR falls a defined amount below its own first-week baseline — that is
this account's creative lifespan, and the refresh cadence is somewhat shorter than it.

Then check whether production capacity can sustain that cadence (§10). An account whose creative
dies in 18 days and which ships two new concepts a month is structurally fatigued, and no
optimisation fixes it. That is the finding — not "refresh more often".

## Output

Per ad set with material spend: frequency at the relevant window, saturation ratio, the
fatigue-vs-saturation verdict with the evidence that separated them, and one named fix.

Where the verdict is saturation, the recommendation is an audience action (widen, add a
lookalike tier, move to broad, accept the ceiling) — **not** a creative brief. Sending a
saturation finding to the creative team wastes a production cycle and returns with the same
problem.
