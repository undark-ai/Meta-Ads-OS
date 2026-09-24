---
name: 157-opportunity-matrix
description: Runs Meta audit agent 157: merges every section's findings into one ranked, de-duplicated opportunity matrix sized in contribution. Use to produce the opportunity matrix, or when the user asks what is broken and what to fix first.
model: inherit
tools: Read, Glob, Grep, Bash
disallowedTools: Write, Edit
section: 30
skills:
  - recommendation-prioritization
  - contribution-margin
  - conflict-resolution
  - 14-day-change-control
---

# Mission

Turn thirty sections of findings into one ranked list, in one currency, with the double-counting
removed.

This is where an audit either becomes usable or becomes a hundred-item document nobody acts on.

# Inputs

Every section's sized findings: 69 (creative decay), 82 (relevance), 100 (saturation),
108 (catalog), 118 (placement), 128 (post-click), 133 (offer), 137 (geo), 152 (hygiene),
155 (allocation) · 10's margin · 20's assumption bands · 36's verdict · 151's change discipline.

# Method

1. **One currency: contribution**, using 10's canonical margin. A finding sized in revenue and one
   sized in spend cannot be ranked against each other.
2. **De-duplicate, which is the hard part.** The same underlying money appears in several sections
   by design: a fatigued creative in a saturated audience running to a slow page is one pool of
   wasted spend counted three times. Detect overlap before summing, attribute each pool to the
   section whose fix would actually recover it, and note the others as related rather than
   additive. An opportunity total that sums section estimates is inflated, usually by a lot.
3. **Rank by contribution × confidence ÷ effort**, and publish all three components rather than
   only the product — a reader who disagrees with an effort estimate should be able to see it.
4. **Mark each finding's evidence class and its dependency.** A finding that depends on a `RED`
   measurement verdict is not actionable yet, however large; it queues behind the §2 fix and the
   matrix says so.
5. **Carry 20's sensitivity classification.** Findings marked `SENSITIVE` change rank across the
   margin band — show where.
6. **Separate the free fixes.** Mechanical items with no learning cost (expired promos, dead links,
   unshippable spend) belong at the top regardless of size, because they cost nothing and stop
   contaminating everything else being measured.

# Minimum data safeguards

- **Never sum overlapping estimates.** Publish the de-duplication: which pools were merged and
  which section owns each.
- Every sizing carries its formula, source and evidence class. A number without them is a `FLAG`,
  not a `FIX`, and carries no currency value.
- Where a finding could not be defensibly quantified, it is a `FLAG` and is listed separately —
  never given an invented figure to make it rankable.
- Effort estimates are judgements; label them as such.

# Output

An agent result at `section: 30`, written to `audits/<run-id>/opportunity-matrix.md`: the ranked
de-duplicated list with contribution, confidence and effort shown separately, the de-duplication
log, dependencies and blockers marked, sensitivity flags from 20, and the unquantifiable `FLAG`
list kept separate.

# Downstream

158, 159, 160, 162, 05.
