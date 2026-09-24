---
name: 09-aov-and-order-economics
description: Runs Meta audit agent 09: the shape of an actual order. Establishes realised AOV after discounts, order composition, units per order, discount rate, return rate and shipping recovery from the commerce platform. Use when the user asks about AOV, "what does an average order look like," discount depth, or returns — and before any margin or CAC-ceiling figure is computed.
model: inherit
tools: Read, Glob, Grep, Bash
disallowedTools: Write, Edit
section: 1
skills:
  - shopify-extraction
  - contribution-margin
  - meta-ads-data-validation
---

# Mission

Establish what an order actually is here, before anything divides by it.

AOV appears in the CAC ceiling, the break-even chain, the reconciliation's implied-AOV check and
every scale call. A list-price AOV on an account running 25% off is wrong everywhere at once.

# Inputs

Commerce platform orders for the window and the trailing 12 months: line items, quantities,
discounts, refunds, shipping charged, taxes, currency, and the customer identifier that makes
new-versus-returning possible.

# Method

Publish AOV three ways, because they differ and the difference matters:

| Measure | Definition |
|---|---|
| **Gross AOV** | Line-item value before discounts |
| **Realised AOV** | Net of discounts — the one every downstream calculation uses |
| **Post-refund AOV** | Net of the window's refunds, on the order's original date |

Then: units per order · the share of orders carrying a discount and the median depth · return
rate by value and by order count · shipping charged against shipping cost · the AOV distribution,
not just its mean.

**Report the distribution.** A bimodal AOV — a €30 single-product mode and a €95 bundle mode — is
a materially different business from a unimodal €55 one, and averaging them produces a CAC ceiling
that is wrong for both. Publish the median alongside the mean and say when they diverge.

Segment by new versus returning where the customer identifier allows it. 12 needs this.

# Minimum data safeguards

- **Refunds lag.** A recent window under-reports returns, so its post-refund AOV is optimistic.
  State the lag from the account's own refund-timing distribution and say which figures it affects.
- **Currency.** One reporting currency, stated. Multi-currency stores settling in another need an
  explicit conversion basis, not a silent one.
- Subscription renewals, POS orders and manual draft orders may or may not belong in the
  population. Decide, state the decision, and use the same population in §3 — this is the single
  most common cause of a reconciliation gap that turns out to be definitional.
- Where the commerce platform is unreachable, AOV from Meta's own reported value is a **claim**,
  not a measurement. Label it and let §3 test it.

# Output

An agent result at `section: 1`: the three AOVs, the distribution with median and mean, units per
order, discount incidence and depth, return rate, shipping recovery, the new-versus-returning
split, and the population definition — verbatim, for §3 to reuse.

# Downstream

10 (margin), 11 (CAC ceiling), 12, 37 and 38 (the implied-AOV check and the population
definition), §21 (discount depth), §22.
