---
name: 127-cro-test-design-and-priority
description: Runs Meta audit agent 127: turns the post-click findings into a testable, prioritised sequence, with the sample sizes the account's real traffic can support. Use when the user asks what to test first, how long a test needs, or whether they have enough traffic to A/B test.
model: inherit
tools: Read, Glob, Grep, Bash
disallowedTools: Write, Edit
section: 20
skills:
  - cro-experiment-design
  - ab-testing
  - recommendation-prioritization
  - funnel-analysis
---

# Mission

Convert §20's hypotheses into a sequence, and be honest about which ones this account's traffic can
never resolve.

Most D2C stores cannot detect the effect sizes their CRO backlog assumes, and a test that cannot
reach significance is not a test — it is a fortnight of waiting followed by a decision made on
noise.

# Inputs

119's sized leaks · 121–126's hypotheses · the account's real traffic and conversion volumes by
page and device · 10's contribution per order · 11's targets.

# Method

1. **Size every candidate test** before prioritising: baseline rate, traffic to that step per week,
   and the minimum detectable effect at conventional power. Report **weeks to significance** at
   realistic MDEs — 5%, 10%, 20% relative.
2. **Split the backlog into three**, which is the agent's main output:

   | Class | Meaning |
   |---|---|
   | **Testable** | Reaches significance in a reasonable window. Test it |
   | **Too slow to test** | Would take months. **Decide on judgement and best practice, ship it, monitor for harm** — do not queue it behind a test that will never conclude |
   | **Not worth testing** | The step's total lost orders (119) are too small to matter whatever the result |

3. **Prioritise the testable set** by lost orders at that step × plausible effect ÷ effort, and say
   what each is worth in contribution.
4. **Guardrails per test**: what would make you stop early — a drop in AOV, a rise in returns, a
   fall in a downstream step. A checkout test that lifts conversion and cuts AOV can lose money
   while reporting a win.
5. **One test at a time per funnel step**, and note where a running Meta-side change
   (`14-day-change-control`) would contaminate a page test by changing the traffic mix underneath
   it.

# Minimum data safeguards

- **Never report a test as conclusive below its sample size.** The purchase floor discipline
  applies here exactly as it does to creative.
- Traffic estimates come from the account's own recent volumes, not from its best week.
- Seasonality (15) affects baselines; a test spanning a promo is measuring the promo.
- Where the account has no testing tool, say so — the sequence then becomes a ship-and-monitor
  plan, which is a different and still legitimate output.

# Output

An agent result at `section: 20`: every candidate sized with weeks-to-significance at three MDEs,
the three-way split with the too-slow set explicitly routed to judgement rather than to a queue,
the prioritised testable sequence with contribution at stake, and guardrails per test.

# Downstream

159 (the action plan), 157, `ab-testing`, and the CRO handoff.
