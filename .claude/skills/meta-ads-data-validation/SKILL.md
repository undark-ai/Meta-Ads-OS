---
name: meta-ads-data-validation
description: When checking that data pulled from the Meta connector is complete and comparable before analysing it — row completeness against parent totals, window and currency consistency, breakdown validity, and the parsing traps. Use before any analysis of Meta data, and whenever two numbers from Meta disagree. Catches the failures that make an analysis confidently wrong rather than obviously broken.
---
# Meta data validation

The failures worth catching are not the ones that error. They are the ones that return a
plausible number computed on the wrong rows.

Run these checks before analysing, not after a result looks odd.

## Completeness

**Reconcile every breakdown against its parent total.** If ad rows do not sum to the campaign
total, rows are missing — from a row limit, a date filter, a status filter, or a breakdown that
silently dropped entities.

Check row limits explicitly rather than assuming, in either direction. An analysis of "all ads"
that silently got the top 100 is wrong in the direction that matters: the long tail is where
waste lives.

Where a platform withholds data by design, state the coverage share instead of implying the
analysis is exhaustive.

## Comparability

| Check | Failure it prevents |
|---|---|
| One attribution window across all rows | Comparing a 7d-click ad against a 7d-click-1d-view ad |
| One currency | Silent mixing on multi-currency accounts |
| Account timezone recorded, and not assumed to be the store's | A day-level gap that looks like a measurement defect |
| Same date range on both sides of every comparison | Period comparisons where one side is 30 days and the other 28 |
| Attribution setting unchanged across the compared periods | A ROAS "improvement" that was a settings change |

## The parsing traps

- Values come back as formatted strings: `"$58,758.12 USD"`, `"1,694,974"`, `"1.55%"`.
- **`"Not available"` is null, never zero.** A zero is a claim that you looked and found none.
- Keep the raw string next to the parsed value. §3's first question is what each source actually
 reported.
- Percentages come back as percentages, not fractions. Dividing by 100 twice is a real and
 invisible error.

## The aggregation traps

- **Never average a ratio across entities.** Recompute from component sums. This is the single
 most common way a Meta report becomes fiction, and the output looks entirely reasonable.
- **One breakdown dimension per call.** Meta rejects some combinations and changes totals across
 others.
- Frequency is impressions ÷ reach. Reach does not sum across entities — the same person is
 reached by several ads — so an ad-set reach is not the sum of its ads' reach.

## The status traps

- `effective_status` is not `status`. Rejections and limited delivery live in `effective_status`.
- An `ACTIVE` campaign whose children are all paused spends nothing and looks live.
- Archived and deleted entities may or may not appear depending on the filter. Decide
 deliberately whether the analysis includes them, and say which.

## The time traps

- **The last 7 days are incomplete** under a 7-day-click window; the last 1–2 days severely so.
 A week-over-week comparison including them always shows a decline, which manufactures fatigue
 findings that do not exist.
- `first_seen_date` must come from account history, not the audit window. An eleven-month-old ad
 looks new in a 30-day pull, and every fatigue conclusion about it is then wrong.
- Learning-phase resets from `ads_account_get_activity_logs` invalidate performance reads across
 them.

## What to do on a failed check

State it and degrade. A section that says "campaign rows sum to 94% of the account total; the
missing 6% is in campaigns deleted mid-window" is more useful than one that silently analyses
94% and reports it as 100%.
