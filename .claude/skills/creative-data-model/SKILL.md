---
name: creative-data-model
description: When building or reading the creative database for a Meta ad account — the one row-per-ad dataset that every creative analysis computes from. Use when the user asks to "build a creative database," "pull all my ad creatives," "analyze creative performance across the account," or when any section from creative inventory through the scale matrix needs ad-level data. Defines which connector calls produce which fields, how to compute hook and hold rate, and the nullability rules that stop a ranking becoming fiction. For classifying what each ad IS, see creative-taxonomy. For rendering it, see creative-dashboard.
---
# Creative data model

One dataset, written once, read by everything. `audits/<run-id>/creative-database.csv`, one row
per ad, against `schemas/creative-record.yaml`.

The rule this exists to enforce: **nothing downstream re-queries Meta for creative
performance.** Fatigue analysis, angle analysis, the funnel, the SKU join, the scale matrix and
the dashboard all read this file. Two components pulling their own data with slightly different
windows will disagree, and a dashboard that contradicts the findings list is worse than either
alone — the reader stops trusting both.

## Build order

The joins matter. Building in a different order means re-fetching, and re-fetching under rate
limits is how a run ends up `DEGRADED` for no good reason.

| Step | Call | Gives |
|---|---|---|
| 1 | `ads_get_ad_accounts` | Confirm the live account. Check `is_ads_mcp_enabled` — `false` beats `is_queryable: true` |
| 2 | `ads_get_ad_entities` at `ad_account` level, wide range, `time_increment: monthly` | Find the window that actually has spend. A dormant account is a preflight answer, not a mystery later |
| 3 | `ads_get_ad_entities` at `ad` level, sorted `amount_spent_descending` | The spine: ids, names, status, spend, delivery, funnel actions, video metrics |
| 4 | `ads_get_ad_entities` at `adset` and `campaign` level | Parents, objectives, bid strategies, budgets — and the totals every rollup reconciles against |
| 5 | `ads_get_creatives` | Copy, headline, CTA, `link_url`, `object_type`, thumbnail and image URLs |
| 6 | `ads_account_get_activity_logs` | Creative launch and removal dates, edit history — `first_seen_date` and learning resets depend on it |
| 7 | Commerce platform | The new-customer and margin join. Without it, `new_customer_share` is null, never assumed |

## Fields that must be pulled explicitly

The ad-level call returns nothing you did not ask for. This field list is the difference between
a creative analysis and a spend report:

```
id, name, status, effective_status, creative_id, adset_id, campaign_id,
amount_spent, impressions, reach, frequency,
outbound_clicks, outbound_clicks_ctr, omni_landing_page_view,
actions:omni_purchase, action_values:omni_purchase, purchase_roas, cost_per_omni_purchase,
actions:omni_add_to_cart, actions:omni_initiated_checkout, actions:omni_view_content,
3_second_video_plays, video_thruplay_watched_actions,
video_p25_watched_actions, video_p50_watched_actions,
video_p75_watched_actions, video_p100_watched_actions,
attribution_setting
```

`effective_status` is not `status`. Rejections and limited-delivery states live in
`effective_status`, and an ad that is `ACTIVE` but not delivering is a §6 finding hiding in a
column most pulls skip.

## Parsing what comes back

Meta returns numbers as formatted strings: `"$58,758.12 USD"`, `"1,694,974"`, `"1.55%"`,
`"Not available"`.

Parse them, and **keep the raw string alongside the parsed value**. When §3 finds a gap between
Meta and Shopify, the first question is what each side actually reported, and a run that
overwrote the source cannot answer it.

`"Not available"` parses to **null**. Never to zero. A zero is a claim — it says "we looked and
there were none" — which is the opposite of what the field meant.

## The attention metrics

The part of the funnel that only exists on Meta, and the reason a Meta creative analysis is not
a Google ad analysis with different words.

```
hook_rate = 3_second_video_plays / impressions # did the scroll stop
hold_rate = thruplay / impressions # did they stay
```

These are different diagnoses with unrelated fixes:

| Hook | Hold | Reading |
|---|---|---|
| High | High | The creative works. Question is headroom, not quality |
| High | Low | The opening earns attention the rest of the ad loses. Fix the middle, keep the hook |
| Low | — | Nobody stopped. The hook, the thumbnail or the first frame is the problem; nothing after it matters yet |
| High | High, but CVR low | The ad works and the page does not. This is §20, not a creative finding |

`hook_rate` on a static ad is **null**, not zero. A null hook rate and a 0.0 hook rate mean
opposite things, and a ranking that conflates them puts the wrong ads on top — which is exactly
the failure the dashboard's "rank by hook rate" would surface first.

**`3_second_video_plays` is not served at ad level on every account.** Some connector builds accept
it at account level and reject it at ad level, and `video_continuous_2_sec_watched_actions` can
come back null on the same ads. The creative database is one row per ad, so when that happens
`hook_rate` is null for **every** row. Walk the ladder in `creative-record.yaml` and record the
rung in `video_plays_3s_source`; a 2-second view is a different metric and is labelled as one,
never relabelled as a 3-second play. `hold_rate` is unaffected and still computes — report it and
say plainly that the hook half of the attention funnel was unavailable.

Quartiles (`p25`/`p50`/`p75`/`p100`) are the retention proxy. Per-second retention curves,
storyboards, transcripts and comment data are **not available** from the connector; do not
promise an analysis that depends on them.

## Derived ratios

Every ratio is stored **with its components**, so any rollup can be recomputed:

```
cpm = spend / impressions * 1000
click_to_lpv_rate = landing_page_views / outbound_clicks
lpv_to_atc_rate = add_to_cart / landing_page_views
atc_to_ic_rate = initiate_checkout / add_to_cart
ic_to_purchase_rate = purchases / initiate_checkout
purchase_cvr = purchases / landing_page_views
aov = revenue / purchases
```

**Never average a ratio across ads to get an ad-set or campaign figure.** Sum the components
first. Averaging weights a 12-impression ad the same as a 1.2-million-impression one, the result
is wrong in a direction nobody can predict from the output, and it looks entirely plausible.
This is the single most common way a Meta report becomes fiction.

A low `click_to_lpv_rate` is a page-speed or redirect problem, not a creative one. It belongs to
§20 even though it was found in the creative dataset.

## Measurement quality travels with the row

Carried per row so a creative ranking cannot quietly become a ranking of measurement artefacts:

- `modelled_purchase_share` — from §2/§3. If unknown, `UNKNOWN`, never `0`.
- `view_through_share`
- `attribution_window` — must equal the file-header window. A row that differs is **dropped**,
 not silently included.
- `evidence_class` — `KNOWN` / `OBSERVED` / `INFERRED`
- `volume_sufficient` — from `learning-phase-and-significance`. `false` blocks a kill
 recommendation for that ad, full stop.

An ad whose purchases are 60% modelled is not comparable to one whose purchases are observed,
and no amount of dashboard polish makes it so.

## Creative age and lifecycle

`first_seen_date` is the first day with impressions in the account's **history**, not in the
audit window. An ad that has been running eleven months looks new in a 30-day pull, and every
fatigue conclusion about it is then wrong.

`iterated_from_ad_id` links a variant to its parent. Without it, §10 cannot compute the
iteration ratio — the share of new production that iterates on winners versus starting fresh —
which is one of the few numbers that tells you whether a creative program is compounding.

## The window header

Written once at the top of the file, not per row:

```
date_start, date_end, attribution_setting, currency, account_timezone
```

Mixing windows across rows silently breaks every ranking the dashboard offers, and the breakage
is invisible: the cards still render, the numbers still look reasonable, and the order is wrong.

The account timezone is frequently not the store's. A day-level comparison across the two
without aligning it produces a gap that looks like a measurement defect and is not one.

## Nullability

A missing value is null and stays null. Where a whole column is unavailable for the account —
no video ads, no commerce join, no catalog — the dashboard hides that tab rather than rendering
it empty, and the section says `N/A` rather than `CLEAN`.

## What this file does not contain

Interpretation. `fatigue_state`, `is_evergreen` and `iteration_candidate` are written by §8;
`promise_handoff_score` by §20; `angle` and `concept_type` by `creative-taxonomy`. The builder
leaves those columns empty rather than guessing, so a downstream agent can tell "not yet
computed" from "computed and negative".
