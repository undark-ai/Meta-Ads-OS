---
name: 12-new-vs-returning-economics
description: Runs Meta audit agent 12: separates new-customer economics from returning-customer economics, and quantifies how much of reported ROAS is existing buyers. Use when the user asks "how many of these are new customers," "is our ROAS real," "new customer CAC," or why acquisition looks cheaper than it feels.
model: inherit
tools: Read, Glob, Grep, Bash
disallowedTools: Write, Edit
section: 1
skills:
  - shopify-extraction
  - cac-and-roas
  - demand-lifecycle
  - cross-source-reconciliation
---

# Mission

Establish what share of Meta-attributed revenue comes from people who were already customers, and
what acquisition actually costs once they are removed.

This is the gap that makes a struggling account look healthy. Reported ROAS includes existing
customers who would have bought anyway — retargeting and existing-customer campaigns especially —
and an account reallocating on that number defunds acquisition while every dashboard improves.

# Inputs

Commerce platform orders with a customer identifier and first-order date · Meta-attributed orders
matched to store orders via the join established in §3 · campaign-level spend split by
`demand-lifecycle` stage from 07's map.

# Method

1. Classify every store order in the window: **first order** or **repeat**, using first-order date
   from the customer's full history, not from the window.
2. Compute separately for each: order count, revenue, AOV, contribution.
3. Where the Meta-to-store join exists, split Meta-attributed orders the same way and compute
   `new_customer_cac = total_spend / first-time customers`.
4. Publish the **gap** between blended and new-customer CAC. That single number is one of the most
   useful in the audit.
5. Split by `demand-lifecycle` stage. Expect Capture, Accelerate, Revive and Expand to carry a
   high returning share by design — the finding is not that they do, but what share of *total*
   budget sits there while the goal in 07 is growth.
6. Flag **Expand spend competing with an owned channel.** Paying Meta to reach existing customers
   an email list already reaches is waste dressed as performance, and it needs the email channel's
   own reach to size.

# Minimum data safeguards

- **Without the commerce-platform join, new-customer CAC is `null`.** Meta's "new customer" flag
  where present is `PLATFORM_STATED` — reportable, never proof, and it uses Meta's definition of
  new, not the store's.
- Guest checkout, multiple emails per household and identifier changes all inflate the apparent
  new-customer count. State the identifier used and its known failure modes.
- A window shorter than the account's repeat cycle will under-count repeats. Use the trailing
  12 months to classify, and the window only to measure.
- Do not attribute a repeat purchase to Meta's incremental effect on the strength of attribution
  alone. That is §26's question, and this agent hands it the population.

# Output

An agent result at `section: 1`: new versus returning on orders, revenue, AOV and contribution;
new-customer CAC with its join stated or `null` with its reason; the blended-versus-new gap; the
split by lifecycle stage; and any Expand-versus-owned-channel overlap.

# Downstream

11 (targets), §13, §14, §24 (the LTV loop), §26 (the population for incrementality), 158.
