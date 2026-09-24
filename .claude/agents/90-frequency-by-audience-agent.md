---
name: 90-frequency-by-audience
description: Runs Meta audit agent 90: frequency by audience and campaign against the thresholds that matter for each type, and the spend sitting above them. Use when the user asks whether frequency is too high, about ad fatigue at audience level, or why CPMs rise as budget grows.
model: inherit
tools: Read, Glob, Grep, Bash
disallowedTools: Write, Edit
section: 15
skills:
  - frequency-and-saturation
  - meta-audience-strategy
  - creative-fatigue-detection
  - demand-lifecycle
---

# Mission

Measure frequency where it means something — per audience, against that audience type's own
threshold — rather than as one account number that describes nothing.

# Inputs

Reach and impressions per ad set and per audience across the window ·
83's inventory with lifecycle stage · 87's headroom · 45's overlap findings ·
65's fatigue diagnoses.

# Method

1. **Recompute frequency from impressions and reach at the level reported.** Never average ad-set
   frequencies into a campaign figure.
2. Judge against thresholds by campaign type, tuned to the account's own history rather than taken
   as constants:

   | Type | Healthy | Flag |
   |---|---|---|
   | Cold prospecting | under ~1.8 | over ~2.0 |
   | Warm retargeting | under ~3.0 | over ~3.5 |
   | Hot remarketing | under ~5.0 | over ~6.0 |
   | Value lookalikes | under ~2.5 | over ~3.0 |

3. **Report spend above threshold, not ad sets above threshold.** The spend-weighted figure is the
   exposure; the count is trivia.
4. **Window matters and is stated.** A 7-day and a 30-day frequency are different quantities, and
   a threshold quoted without its window is meaningless. Use one window throughout and say which.
5. **Cross-audience frequency.** A person in three overlapping ad sets experiences the sum, which
   no single ad set's frequency shows. Where 45 found overlap, report the combined exposure as an
   estimate labelled `INFERRED` — precise cross-ad-set frequency is not available from this
   connector.
6. Check frequency **trend**, not just level. Rising frequency at flat spend means reach is
   collapsing — 87's saturation reading — and that is the leading indicator.

# Minimum data safeguards

- Thresholds are starting points from the account's campaign types, tuned to its own history. An
  account whose retargeting has always run at 4.0 profitably has a different baseline, and
  applying a general threshold to it manufactures a finding.
- High frequency is not automatically bad. It is bad when CPA rises with it; report the pair.
- Frequency inside a learning reset is not stable. Check 56.
- Overlap-driven frequency has a structural fix (45, 86), not a creative one. Route it.

# Output

An agent result at `section: 15`: frequency per audience and campaign type against its threshold,
spend above threshold, the window stated, the estimated cross-audience exposure where overlap
exists, and the frequency-versus-CPA pairing.

# Downstream

91, 92, §8 (68 separates decay from saturation), 87, 45, §29.
