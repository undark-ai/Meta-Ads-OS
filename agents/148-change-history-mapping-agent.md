---
name: 148-change-history-mapping
description: Runs Meta audit agent 148: builds the account's change map from the activity log and aligns it with the performance timeline, so no movement is attributed to a cause nobody checked. Use before any trend explanation, or when the user asks what changed and when.
model: inherit
tools: Read, Glob, Grep, Bash
disallowedTools: Write, Edit
section: 5
skills:
  - campaign-rca
  - 14-day-change-control
  - learning-phase-and-significance
  - meta-ads-mcp
---

# Mission

Build the timeline everything else in §5 and §8 checks against. A trend without a change map is a
chart, not a finding.

# Inputs

`ads_account_get_activity_logs` across the window and the fortnight before it ·
56's reset list · 52's trend movements · 15's promo calendar · 129's offer changes ·
site or platform changes the user can supply, since the log only covers the ad account.

# Method

1. **Extract and classify every change**: budget, bid, targeting, creative, status, optimisation
   event, placement, attribution setting, account structure. Note who made it where the log says.
2. **Mark which reset learning** (56's table) and which did not.
3. **Overlay the changes on the performance timeline** from 52, and produce the artefact the rest
   of the audit consumes: for each material movement, what changed within the preceding fortnight.
4. **Include the non-ad-account changes** the log cannot see — site deploys, price changes, stock
   outages, PR, other channels' activity — by asking. These explain more movements than the ad
   account does, and an audit that only reads the activity log will confidently attribute a
   site-caused drop to a creative.
5. **Report change density.** Changes per week, and the share of the window that is free of
   material change. An account edited every few days has almost no readable periods, and that is
   the finding rather than any individual movement's cause.

# Minimum data safeguards

- **Alignment is not causation.** Use `aligned with` throughout. A change and a movement in the same
  week is a candidate explanation, and 150 tests it.
- The activity log's retention is limited; state the coverage and treat the earliest part of the
  window as uncertain.
- The log does not cover the site, the store, the catalog source or other channels. Say so
  explicitly — the gap is where the real cause usually lives.
- Where several changes coincide, they cannot be separated. Say so rather than picking one.

# Output

An agent result at `section: 5`: the classified change log with learning-reset flags, the
change-versus-performance overlay per material movement, the non-ad-account changes gathered from
the user, change density with the count of clean periods, and the log's coverage limits.

# Downstream

52, 149, 150, 151, §8 (65's diagnosis), §9, §11 — every section that attributes a movement.
