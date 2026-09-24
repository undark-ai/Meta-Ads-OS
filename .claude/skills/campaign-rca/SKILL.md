---
name: campaign-rca
description: When a Meta campaign has underperformed and the cause could be anywhere — objective, targeting, creative, bidding, or the tracking layer — and a systematic sweep is needed rather than a fast pattern-match. Use when the user asks "why did performance drop," "what happened to this campaign," "our ROAS fell off a cliff," or "root cause this." Starts by confirming the move is real, because most reported drops are reporting artefacts. For decay that clearly matches a fatigue signature, see frequency-and-saturation first — it is faster.
---
# Campaign RCA

A broader diagnostic than the fatigue check. Fatigue pattern-matches creative and audience decay
against named signatures and deliberately stops at the ad. This is for when the cause could be
anywhere, when several things changed at once, or when the fatigue check came back "no clean
match".

## Step 0 — Confirm the move is real

**Before diagnosing anything.** Three ways a change is an artefact of reporting rather than a
change in performance. Skipping this is how a team spends a week root-causing a number that was
never wrong.

| Artefact | How it fools you | Check |
|---|---|---|
| **Attribution restatement** | Meta keeps attributing for up to 7 days as delayed data lands, so the last 1–2 days of any pull are systematically understated | Is the entire magnitude of the "drop" in the last 48 hours? Re-pull the identical range 3–5 days later. If it shrinks, that was the cause |
| **Timezone mismatch** | The ad account's timezone and the reporting timezone shift daily boundaries, manufacturing a cliff at a period edge | Compare both before trusting any day-over-day read |
| **The attribution window changed** | Moving 7-day-click → 1-day-click can roughly halve reported conversions with zero change in delivery, creative or audience | Check the setting and `ads_account_get_activity_logs`. Nobody thinks of this as an account change, and it is the largest one available |

Only once the move survives all three is there something to root-cause. Say so explicitly in the
output — "confirmed real" is a finding, and so is "this was the lag".

## Step 1 — Locate the inflection

Pull daily campaign-level data for 30 days and find where it turned. The shape names the family
of causes before you look at anything else:

| Shape | Reading |
|---|---|
| **Sudden drop on a specific date** | Almost always a change was made. Go to the activity log first, not to the creative |
| **Gradual decline over 7–14 days** | Fatigue, saturation, or rising auction pressure — hand to `frequency-and-saturation` if a signature matches |
| **Volatile, no clear trend** | Still in learning, or the volume is too thin to read. Check `bid-strategy-and-learning` before diagnosing anything else |

## Step 2 — Walk the five layers

In order. A fault in an earlier layer makes the later ones unreadable.

**1. Objective and optimisation event.** Does the objective match the §1 goal? Is the optimisation
event right for current volume — still on ViewContent when the account does 50+ purchases a week?
Does the bid strategy suit the volume? A sales campaign optimising for link clicks is an objective
mismatch, not a performance problem, and no amount of creative fixes it.

**2. Targeting and audience.** Audience too narrow to spend the budget, or so broad the signal is
diluted? Overlap with other campaigns (§11 auction diagnostics)? Frequency above its campaign-type
threshold? Is the retargeting pool shrinking because prospecting stopped feeding it?

**3. Creative.** CTR trend, days since a real refresh, whether one ad is dragging an otherwise-fine
ad set, whether the format suits the placement mix it is actually being delivered into.

**4. Bidding and budget.** Budget utilisation under 50% means the bid is too low or the audience
too narrow to spend it. CPM and CPC trend. Learning-phase state. **Any budget change above ~20%
resets learning** — check the log before blaming the ads.

**5. Landing page and tracking.** Has page conversion rate changed independently? Mobile load time?
Are pixel and CAPI events still firing — did something break (`capi-and-emq`)? Has the offer,
price or availability changed without the ad being updated to match? This last one is common and
invisible from inside Ads Manager.

## Step 3 — Compare against what still works

Pull the same metrics, same period, for campaigns on the same account that are performing. The
specific difference — audience, creative, bid, objective — isolates the cause faster than
theorising from first principles, and it controls for everything account-wide that changed at the
same time.

## Platform-side versus account-side

Two families, and the distinction changes who fixes it:

- **Account-side** — something in this account changed: an edit, a creative rotation, a budget
  move, a broken event. The activity log and the change map find it.
- **Platform-side** — auction pressure, seasonality, a delivery-system change affecting everyone.
  The signature is that it appears across unrelated campaigns simultaneously, and often across the
  industry benchmark too.

An account-side diagnosis you can act on; a platform-side one you plan around. Calling one the
other wastes a cycle either way.

## Output

The confirmed-real verdict and what ruled out the artefacts, the inflection date and shape, the
layer at fault with its evidence, what the healthy campaigns do differently, and **one** first
move. Where two layers are both implicated, say so — an account can break in more than one place
at once — but rank them by spend at risk.

Where the honest answer is that the data does not identify a cause, say that and name what would:
usually a specific pull, a specific test, or waiting for the attribution lag to complete.
