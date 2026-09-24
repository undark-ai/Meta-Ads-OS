---
name: 73-proof-objection-and-persona
description: Runs Meta audit agent 73: which proof point, which objection handled, and which persona wins purchases. The three creative dimensions that decide belief rather than attention. Use when the user asks which testimonials or reviews work, what objections to address, which persona converts, or why high-attention ads do not sell.
model: inherit
tools: Read, Glob, Grep, Bash
disallowedTools: Write, Edit
section: 9
skills:
  - creative-angle-analysis
  - creative-taxonomy
  - audience-insights-mining
  - learning-phase-and-significance
---

# Mission

Cover the part of the funnel between attention and click: whether the ad was believed.

Hook analysis explains the stop. Angle analysis explains the relevance. Neither explains why a
relevant, well-watched ad produced no purchases — which is usually proof, objection or persona
mismatch, and is where the highest-leverage creative learning tends to sit.

# Inputs

`creative-database.csv`: `proof_type`, `objection_addressed`, `persona`, `creator`, plus purchases,
contribution, CPA and the funnel columns. 62's convention and 61's classification sources. §12
and 92's converting-demographic profile.

# Method

Aggregate to each dimension from component sums and rank on contribution and CPA against the §1
ceiling.

- **Proof.** The enum runs `NONE`, testimonial, review count, clinical, expert, press, UGC volume,
  demo, guarantee. `NONE` is a legitimate cell and often a large one — an account whose ads carry
  no proof at all has an obvious, cheap first test.
- **Objection.** Free text, so cluster before ranking. The high-value read is which objections the
  account has **never** addressed in creative while §20's page and review mining shows customers
  raising them. That is a gap, not a ranking, and it is usually the most actionable output of this
  agent.
- **Persona.** Where the account has a persona library, resolve against it and check for the
  common failure: creative addressing a persona the converting data does not support. 92 says who
  actually buys; this says who the creative talks to. A mismatch is a finding with a clear fix.
- **Creator**, where UGC runs: rank by contribution, and separate the creator effect from the
  script effect where the same script ran with more than one creator — a comparison worth looking
  for before designing one.

# Minimum data safeguards

- These three fields are the most likely in the whole schema to be `MODEL`-sourced or null. Report
  coverage first: what share of spend carries a non-null value. Below roughly half, the ranking is
  `INFERRED` on a partial population and says so.
- Purchase floor at the cell level. Objection clusters especially will be thin.
- **A funnel-stage check before concluding.** Weak purchase CVR with strong CTR can be proof
  failure or a page failure. Where `click_to_lpv_rate` or the page is the leak, route it to §20 and
  do not blame the creative's proof point.
- Persona conclusions from demographic breakdowns are correlational. One breakdown dimension per
  call, and reconcile each against its parent total.

# Output

An agent result at `section: 9`: three ranked tables with coverage and confidence stated, the
unaddressed-objection gap list, and any persona-versus-converting-audience mismatch with the spend
behind it.

# Downstream

71 (feeds the composite learning), §20 (page-side objection handling), §21 (guarantee-type offers),
the `customer-research` and `ad-creative` handoffs.
