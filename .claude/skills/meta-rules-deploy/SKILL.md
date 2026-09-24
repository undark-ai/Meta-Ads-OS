---
name: meta-rules-deploy
description: When deploying automated rules on a live Meta account under the execution protocol — the thresholds they should encode, the guardrails that stop a rule cascading, and why notify-only comes first. Use in an execution run when the user asks to "automate pausing bad ads," "set up automated rules," "auto-scale winners," or "put a spend safety net on the account." Execution lane only. For the thresholds themselves, see meta-ads-operating-system and meta-automated-rules.
lane: execution
---
# Rules deployment

Load `meta-execution-protocol` first.

A rule is a change you will not be present for. Everything the protocol requires of a one-off
mutation applies, plus the fact that this one fires repeatedly, unattended, against data that
will look different next month.

## Notify-only first, always

Deploy every new rule in notify-only mode and watch what it *would* have done for at least one
full read window.

This is not caution for its own sake. A rule tuned on last quarter's numbers fires on
this quarter's data, and the gap between "the threshold looks right" and "the threshold pauses
nine winners on a slow Tuesday" is only visible in the dry run.

Only after the notify-only period, with the user's review of what it would have done, does it
become an acting rule.

## Encode the floors, not just the thresholds

A rule that pauses an ad at a CPA threshold with no minimum-purchase condition is a rule that
kills ads on variance. Every action rule carries:

- **A volume floor** — the purchase or spend minimum from `learning-phase-and-significance`. Below
  it, the rule does nothing.
- **A lookback that respects conversion lag.** A rule reading the last 3 days under a 7-day-click
  window is reading incomplete data and will always see a decline.
- **A learning-phase condition.** A rule that pauses ads in ad sets that just reset learning is
  punishing the edit, not the ad.
- **A frequency cap on its own firing.** A rule that can act on the same entity daily can pause
  an account in a week.

## Guardrails against cascades

The failure mode worth designing against is not one wrong action; it is a rule interacting with
another rule, or with itself:

- A pause rule and a budget-increase rule on overlapping conditions will fight, and the account
  oscillates.
- A budget rule with no ceiling scales into saturation and keeps scaling, because rising spend
  briefly improves the metric it watches.
- A rule acting at the ad level while another acts at the ad-set level produces changes neither
  rule's author anticipated.

Deploy one rule at a time, with a read window between, and record the full rule set in the change
register so the next person can see what is already running.

## Set a spend ceiling before anything else

If only one rule exists on the account, make it the safety net: a hard daily or lifetime spend
ceiling that pauses delivery. It is the rule that limits the damage every other rule can do,
including the ones deployed later by someone else.

## Rules are a change register entry

Every deployed rule is logged like any mutation: what it does, its conditions, its floors, when
it was deployed, what the notify-only period showed, and how to disable it.

A rule nobody remembers deploying is the hardest kind of account problem to diagnose, because the
account changes and no human made the change. Six months later it reads as a platform mystery.

## What rules should not do

- **Not replace the weekly cadence.** Rules handle the mechanical floor — a runaway ad, a spend
  ceiling. They do not decide creative strategy, and an account run entirely by rules stops
  learning.
- **Not act on unreconciled numbers.** A rule optimising against a conversion value §3 never
  reconciled automates the mistake.
- **Not scale.** Scaling decisions need headroom evidence and incrementality context that a
  threshold cannot carry. Rules pause and cap; humans scale.
