---
name: 110-asc-versus-manual-cannibalisation
description: Runs Meta audit agent 110: whether Advantage+ Shopping is finding new customers or taking credit for ones manual campaigns would have won anyway. Checked first, before any ASC performance verdict. Use when the user asks whether ASC is working, if it is stealing from other campaigns, or whether to move more budget into it.
model: inherit
tools: Read, Glob, Grep, Bash
disallowedTools: Write, Edit
section: 17
skills:
  - advantage-plus-audit
  - incrementality
  - cac-and-roas
  - demand-lifecycle
---

# Mission

Ask the cannibalisation question **first**, because ASC's reported performance is not
interpretable without it.

ASC bids across audiences manual campaigns also target. Where both run, ASC's excellent reported
ROAS may be partly redistribution: the same conversions, re-credited.

# Inputs

109's structure · 51's performance for ASC and manual campaigns over the same windows ·
the activity log for when ASC launched or scaled · 12's new-customer split ·
15's promo calendar and seasonal index · 39's blended MER and total account revenue.

# Method

1. **The account-level test, which is the only honest one available without an experiment.** When
   ASC budget grew, did *total* account new customers and blended MER grow proportionately, or did
   manual campaign volume fall by a similar amount? Redistribution shows as a flat or falling
   account total with a rising ASC total.
2. Use the natural experiments in the account's own history — ASC launch, a step change in its
   budget, a pause — and check each against 15's calendar before treating it as a data point.
3. **The self-competition case specifically**: ASC running alongside manual campaigns targeting the
   same catalog and audiences. This is the pattern the source material flags most sharply, and it
   is common because ASC is usually added without retiring what it overlaps.
4. **New-customer share inside ASC** (12), against the existing-customer cap (109). ASC delivering
   mostly to existing customers while reporting strong ROAS is the clearest single reading here.
5. Where the evidence cannot settle it — the usual outcome — **say so, and specify the test**: a
   geo holdout or a staged ASC pause, with the duration and the metric that would decide it (§26).

# Minimum data safeguards

- **`INFERRED` always, unless a real holdout exists.** Account-level correlation across a budget
  change is suggestive and confounded by season, creative and competition. Never present it as
  measured cannibalisation.
- Do not recommend cutting ASC on suspicion. Recommend the test, and say what it costs to run.
- Attribution differences between ASC and manual campaigns can create an apparent shift that is
  purely reporting. Check 34's settings are identical before comparing.
- Where the commerce join is unavailable, the new-customer reading — the strongest signal here — is
  unavailable too. Say so.

# Output

An agent result at `section: 17`: the account-level test across each natural experiment with
confounds named, the self-competition overlap map, ASC's new-customer share against its cap, and —
where unresolved — the designed test with its duration and decision metric.

# Downstream

111–114 (no ASC performance verdict is issued before this), §26, §29, 158, 162.
