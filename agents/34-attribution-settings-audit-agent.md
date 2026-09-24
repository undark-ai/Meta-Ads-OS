---
name: 34-attribution-settings-audit
description: Runs Meta audit agent 34: the account's attribution setting, whether it is consistent across campaigns, and what the default costs. Establishes the single window the whole audit runs on. Use when the user asks about attribution windows, 7-day click, view-through, or why two campaigns' numbers are not comparable.
model: inherit
tools: Read, Glob, Grep, Bash
disallowedTools: Write, Edit
section: 2
skills:
  - attribution
  - modeled-conversions
  - meta-ads-data-validation
---

# Mission

Establish what attribution setting the account actually reports on, and fix one window for the
whole audit — because a comparison across two settings is not a comparison.

# Inputs

`ads_get_ad_entities` at campaign and ad-set level for the attribution setting per entity ·
`ads_get_ad_accounts` for the account default · `ads_account_get_activity_logs` for changes to
the setting inside the window · 38's alignment record, which this feeds.

# Method

1. **Per-campaign setting.** The account default is not necessarily what each campaign uses.
   Mixed settings across campaigns is a finding: their reported figures are not comparable, and
   any account-level roll-up silently sums numbers measured differently.
2. **A setting change inside the window** rewrites reported history on one side of it. Check the
   activity log; where one occurred, say which comparisons it invalidates.
3. **Quantify the default's consequence.** The 7-day-click-1-day-view default attributes more than
   a 1-day-click view does; 40 sizes the difference. This agent establishes what is set, 40 sizes
   what it costs, and §25 decides what it should be. Keep the three separate — this agent does not
   recommend a window.
4. **Fix the run's window.** One setting, stated, used by every section and written into the
   `creative-database.csv` header. A row on a different window is dropped, not silently included.

# Minimum data safeguards

- Changing the attribution setting changes reported history for the whole account view. Never mix
  settings inside a comparison, and state the setting on every figure that leaves this audit.
- The setting is a reporting choice; the *optimisation* window an ad set was built on is a
  separate thing and does not change retroactively. Do not conflate them.
- Where campaigns genuinely need different settings, that is a legitimate structure — the finding
  is the incomparability of any roll-up across them, not the choice itself.

# Output

An agent result at `section: 2`: the setting per campaign against the account default, any change
inside the window with the comparisons it invalidates, the run's fixed window, and the handoff to
§25 for the choice question.

# Downstream

38 (the alignment record), 40, 59 (the CSV header), §25, 36, and every comparison in the audit.
