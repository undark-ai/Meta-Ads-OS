---
name: 100-frequency-and-saturation-verdict
description: Runs Meta audit agent 100: closes the frequency and saturation section with a verdict that separates audience exhaustion from creative decay and sizes what each is costing. Use to close the saturation section, or when the user asks whether they need new creative or new audiences.
model: inherit
tools: Read, Glob, Grep, Bash
disallowedTools: Write, Edit
section: 15
skills:
  - frequency-and-saturation
  - creative-fatigue-detection
  - scaling-methods
  - recommendation-prioritization
---

# Mission

Close §15 with the answer that decides where the next month of effort goes: more audience, or more
creative.

68 makes that call per audience-by-concept cell. This assembles those calls into an account-level
verdict, sizes it, and sequences the response.

# Inputs

90's frequency by audience · 91's reach curves and inflection points · 87's headroom ·
68's per-cell verdicts · 69's decay curve and fatigue exposure · 45's overlap ·
70's refresh requirement · 11's targets.

# Method

1. **Aggregate 68's cell verdicts spend-weighted.** How much of the account's spend sits in cells
   diagnosed `AUDIENCE_SATURATION` versus `CREATIVE_DECAY` versus `BOTH` versus
   `INSUFFICIENT_DATA`. The account-level answer is whichever carries the spend, and reporting the
   distribution matters more than declaring a single cause.
2. **Size each.** Saturation cost is the CPA gap between saturated and unsaturated cells applied to
   saturated spend; creative decay is 69's figure. Both `INFERRED`, both with the formula and the
   comparison cohort published, and both using the account's own median rather than its best.
3. **Check the manufactured-frequency share.** Where 45 found overlap, part of the measured
   frequency is self-inflicted and its fix is structural — exclusions, not new audiences and not
   new creative. Separate it before sizing the other two, or it gets counted twice.
4. **Sequence the response**, because the two fixes have different lead times: exclusions are
   immediate, audience expansion takes days, creative production takes weeks. An account that is
   creative-constrained should start production now and fix exclusions this week, not choose
   between them.
5. Name the **binding constraint** for the next quarter, and what it implies for budget: an account
   that is audience-saturated cannot scale on budget alone regardless of creative quality.

# Minimum data safeguards

- Cells below the purchase floor are `INSUFFICIENT_DATA` and are reported as a share of spend
  rather than assigned a cause.
- Sizing both saturation and decay risks double-counting where a cell is diagnosed `BOTH`.
  Attribute it once, say which, and note the ambiguity.
- Frequency thresholds are the account's own, tuned from its history (90) — not general constants.
- Where 36's verdict is `RED`, the CPA gaps underlying both sizings are unreliable. Report the
  diagnosis, withhold the currency figures, and say why.

# Output

An agent result at `section: 15`: the spend-weighted distribution of cell verdicts, each cause
sized with its formula and comparison cohort, the manufactured-frequency share separated out, the
sequenced response with lead times, and the binding constraint named.

# Downstream

§8 (70's refresh requirement), §12 (audience expansion), 86 and 45 (exclusions), §29, 157, 159.
