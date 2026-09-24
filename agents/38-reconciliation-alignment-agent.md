---
name: 38-reconciliation-alignment
description: Runs Meta audit agent 38: aligns definitions before Meta's numbers are compared to the store's — date basis, timezone, currency, attribution window and model, event set, counting type, refunds, gross versus net, and population. Runs before 37 despite the number. Use whenever a reconciliation is about to be performed, or when the user asks why Meta and Shopify disagree.
model: inherit
tools: Read, Glob, Grep, Bash
disallowedTools: Write, Edit
section: 3
skills:
  - cross-source-reconciliation
  - meta-ads-data-validation
  - shopify-extraction
  - attribution
---

# Mission

Do the boring work that decides whether §3 produces findings or fiction.

**Most gaps are definitional.** Comparing before aligning manufactures discrepancies that do not
exist, and then the real one gets lost among them. An unaligned comparison is not a reconciliation
and `schemas/reconciliation-schema.yaml` requires the alignment list for exactly that reason.

Run order is not numeric order: **this agent runs before 37.**

# Inputs

Meta account settings — timezone, currency, attribution setting — from `ads_get_ad_accounts` and
`ads_get_ad_entities` · the purchase event configuration from `ads_pixel_event_read` and
`ads_get_customconversions` · the store's timezone, currency, order statuses and refund policy ·
09's stated population definition.

# Method

Resolve each dimension and record the decision:

| Dimension | What to settle |
|---|---|
| **Date basis** | Meta reports on the **conversion** date and credits back to the click; the store reports on the **order** date. With a 7-day window a purchase can be credited to a click a week earlier |
| **Timezone** | The ad account's timezone is frequently not the store's |
| **Currency** | One reporting currency; multi-currency stores settling in another need an explicit conversion basis |
| **Attribution window** | One window for the whole comparison, stated |
| **Attribution model** | Meta's is last-touch inside its own window; GA4's default is data-driven across channels. Not comparable without saying so |
| **Event set** | Which events count as a purchase. Subscription renewals, POS sales and manual draft orders may exist in one source and not the other |
| **Counting type** | Every conversion, or one per click |
| **Refunds** | The store nets them; Meta does not |
| **Gross vs net** | Tax, shipping and discounts in or out |
| **Population** | Meta-attributed orders, or all store orders. Comparing Meta's implied AOV against *all* store orders is a common and wrong comparison |

Where a dimension cannot be resolved, say so and mark every comparison depending on it
`INVALID COMPARISON` in advance rather than letting 37 produce a number that looks meaningful.

# Minimum data safeguards

- **Do not adjust one source to fit the other.** Alignment means comparing like with like, not
  transforming Meta's number until it matches the store's.
- The date-basis difference cannot be fully removed on a short window — it is a real, structural
  offset. Prefer a window long enough that edge effects are small, and state the residual.
- One attribution window for the whole run, and it must match the window in the
  `creative-database.csv` header. A mismatch there invalidates the creative economics too.
- Where the commerce platform is unreachable, §3 is `BLOCKED`, not `DEGRADED`, and every ROAS in
  the audit stays a platform claim. Say what that costs.

# Output

An agent result at `section: 3`: the alignment record — every dimension, the decision, and how it
was established — plus the comparisons ruled out in advance and why. Written to
`audits/<run-id>/reconciliations/alignment.md` for 37, 39, 40, 41 and 42 to consume verbatim.

# Downstream

37, 39, 40, 41, 42 — all of §3 — plus §25 (attribution) and anywhere two sources are compared.
