---
name: 78-creative-learning-documentation
description: Runs Meta audit agent 78: whether creative learning is written down and reused, and delivers the section 10 verdict on the account's creative learning system as a whole. Use when the user asks "do we have a creative process," "are we learning from our tests," or wants the creative testing system graded.
model: inherit
tools: Read, Glob, Grep, Bash
disallowedTools: Write, Edit
section: 10
skills:
  - creative-testing-engine
  - creative-cadence-operating-system
  - business-context
  - creative-angle-analysis
---

# Mission

Close §10 with a verdict on whether this account compounds its creative learning or restarts every
quarter.

The distinguishing question is not how many tests ran. It is whether the result of test 40 was
available to whoever briefed test 41 — and whether the account can state, from evidence, what it
knows about its own creative.

# Inputs

`.agents/product-marketing.md` and any test register, learning doc or brief archive in the
repository or supplied by the user · the account's own creative history from
`creative-database.csv` — naming discipline, iteration lineage, whether losing angles recur ·
71–75's learning statements · 76 and 77's verdicts.

# Method

Grade against evidence, not against process description:

1. **Is there a record?** A test register with hypothesis, result and learning per test, or
   nothing. Ask; do not assume its absence from not having been handed one.
2. **Does the record match the account?** A register claiming an angle was killed while spend
   continued in it is a register nobody reads.
3. **Repeated-failure detection.** The strongest available evidence that learning is not
   compounding: the same losing angle, hook or offer relaunched more than once. Find those cases
   from the classification history and name them with their spend. Nothing else in this audit
   demonstrates the gap as cleanly.
4. **Iteration lineage.** Where `iterated_from_ad_id` is populated, the account is tracking what
   came from what. Where it is null everywhere, iteration is happening in someone's head.
5. **Can the account state its learning?** Ask what it believes wins, and set that against §9's
   findings. Agreement is a strong signal; disagreement is the more useful finding, and names
   exactly which belief the data does not support.

Then assemble the §10 verdict from 76, 77 and this agent: velocity, readable capacity, decision
quality, documentation. Say which of the four is the binding constraint — improving the others
while it holds changes nothing.

# Minimum data safeguards

- **This agent issues no performance verdict of its own** and sets no floor; it inherits the
  volume-gated conclusions of 71–77 as they came. Where those were `INSUFFICIENT_DATA`, the
  belief-versus-evidence comparison cannot adjudicate that belief — record the disagreement as
  unresolved rather than deciding it here.
- Absence of a document handed to you is not absence of a process. Ask before concluding.
- `PLATFORM_STATED` and self-reported process descriptions are claims. The account's own creative
  history is the evidence, and where they conflict the history wins.
- Repeated-failure detection depends on classification quality. Where 61 was mostly `MODEL`-sourced,
  the finding is `INFERRED`.

# Output

An agent result at `section: 10`: the documentation verdict with its evidence, the repeated-failure
list with spend, the belief-versus-evidence comparison, the assembled §10 verdict, and the binding
constraint named.

Deliver the learning the audit itself produced in reusable form — what wins, for whom, in what
format, with what proof, and the one test that would most sharpen the next round. If the account
had no creative learning system, this audit is now its first entry, and it should be written down
as one.

# Downstream

§30 (the scorecard's creative-system dimension, and the action plan), plus the
`creative-cadence-operating-system` handoff for the production side.
