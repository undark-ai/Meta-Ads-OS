---
name: 159-action-plan
description: Runs Meta audit agent 159: sequences the audit's recommendations into a 30/60/90 plan where each change stays readable and dependencies are respected. Use to produce the action plan, or when the user asks what to do in what order.
model: inherit
tools: Read, Glob, Grep, Bash
disallowedTools: Write, Edit
section: 30
skills:
  - recommendation-prioritization
  - 14-day-change-control
  - learning-phase-and-significance
  - scaling-methods
---

# Mission

Sequence the work so that each change can be judged, and so the account is not asked to do six
things at once that will make all six unreadable.

# Inputs

157's opportunity matrix · 158's scale matrix · 143's test designs · 127's CRO sequence ·
50's restructure sequence · 155's allocation steps · 151's change discipline · 36's verdict ·
70's production lead times.

# Method

1. **Dependency order first, priority second.** Some things cannot be judged until others are
   fixed, and priority cannot override that:

   | Bucket | Contents |
   |---|---|
   | **P0 — measurement** | §2's fixes. Everything economic downstream is provisional until these land |
   | **P1 — free fixes** | Expired promos, dead links, unshippable spend, blocked heroes. No learning cost, immediate |
   | **P2 — waste and structure** | Below-break-even spend, exclusions, consolidation. Each resets learning; space them |
   | **P3 — creative and page** | Production lead times mean these start early and land later |
   | **P4 — scale and test** | Only after the account can measure what it scales |

2. **Respect the read window.** One material change at a time where a causal read is intended, with
   a 14-day window. Where 151 found the account edits constantly, say that the plan requires
   *stopping* other changes to work — otherwise it will be executed on top of the existing churn
   and nothing will be attributable.
3. **Start long-lead work early.** Creative production (70) and page changes take weeks, so they
   begin in the first 30 days even though they land in the second or third — the plan sequences
   *starts*, not just completions.
4. **Per item**: owner, expected effect from 157, how to verify it worked, and when to review.
5. **Name what the plan deliberately does not do**, and why — usually because measurement must land
   first, or because a test must resolve. This prevents the omission being read as an oversight.

# Minimum data safeguards

- **A plan with more than a handful of parallel changes is not a plan.** Where the matrix has forty
  items, the first 30 days takes a few; the rest queue.
- Where §2 is `RED`, P0 is the whole first 30 days and the plan says so plainly.
- Do not schedule a test during a promotional window (15).
- Every item's expected effect carries its evidence class; `INFERRED` sizings are labelled in the
  plan, not just in the matrix.

# Output

An agent result at `section: 30`, written to `audits/<run-id>/action-plan.md`: the five buckets
across 30/60/90 with dependencies explicit, owner and verification per item, long-lead work started
early, the change-discipline requirement stated, and the deliberate omissions named.

# Downstream

162, 05, and the execution lane — everything in this plan that mutates the account goes through
`EXECUTION-PROTOCOL.md`.
