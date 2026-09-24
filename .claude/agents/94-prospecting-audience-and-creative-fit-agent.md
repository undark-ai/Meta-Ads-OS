---
name: 94-prospecting-audience-and-creative-fit
description: Runs Meta audit agent 94: which audience and creative combinations actually acquire customers, and whether cold traffic is being shown creative built for someone further along. Use when the user asks what to run to cold audiences, why prospecting creative underperforms, or how to pair audiences with angles.
model: inherit
tools: Read, Glob, Grep, Bash
disallowedTools: Write, Edit
section: 13
skills:
  - creative-angle-analysis
  - demand-lifecycle
  - meta-audience-strategy
  - learning-phase-and-significance
---

# Mission

Find the pairings that acquire, and the mismatch that wastes most prospecting budget: L5 offer
creative shown to people who have never heard of the product.

# Inputs

75's creative × audience interaction grid · `creative-database.csv` with `awareness_level` and
classification · 84's targeting-type performance · 93's Create/Capture split ·
92's converting profile · 12's new-customer data.

# Method

1. **Awareness-level match.** Where `awareness_level` parses from the naming convention (62), map
   creative awareness against audience temperature. Report the **spend** running L4/L5 creative to
   cold audiences: an offer ad asking for a decision from someone who does not know the problem
   exists is asking for a step they have not taken, and it usually reads as a creative failure
   when it is a pairing failure.
2. **Winning pairings on new-customer CAC**, from 75's grid restricted to prospecting. Report at
   the depth the purchase floor supports — usually audience type × angle, not the full grid.
3. **Cross against the account-level angle ranking** (71). The finding is disagreement: an angle
   that wins overall and loses on cold traffic is being run in the wrong place, and that is more
   actionable than either ranking alone.
4. **Untested pairings.** Which audience × angle combinations the account has never run, weighted
   by the strength of each component. Route the gaps to §27's competitive angle inventory and to
   the creative brief.
5. Check whether prospecting creative volume is sufficient: an account testing one new concept a
   month into cold audiences cannot learn what acquires (§10).

# Minimum data safeguards

- Purchase floor per cell, applied to **new-customer** purchases where the join exists — a pairing
  that converts existing customers is not an acquisition finding.
- Where `awareness_level` is mostly model-inferred (61), the awareness-mismatch figure is
  `INFERRED`. Say so with the classification-source split.
- Check 56 before reading any cell.
- Absence of a pairing is not evidence it fails. Route untested combinations to the gap list, never
  to a ranking.

# Output

An agent result at `section: 13`: the awareness-mismatch spend with its classification source, the
winning prospecting pairings on new-customer CAC at the depth the data supports, the disagreements
against the account-level angle ranking, and the untested pairing gaps.

# Downstream

§9 (the creative brief), §27, 158, 75, §10.
