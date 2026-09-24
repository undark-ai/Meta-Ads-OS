---
name: contribution-margin
description: When establishing the canonical unit economics for a D2C account — gross margin, contribution margin, and the variable costs that sit between revenue and profit. Use when the user asks "what's my real margin," "am I actually profitable on this," "contribution margin," "what should my ROAS be," or whenever a scale, kill or budget recommendation needs a profit basis. Computed once in section 1 and consumed everywhere; never recomputed per agent. For turning it into CAC and ROAS targets, see cac-and-roas.
---
# Contribution margin

Revenue, conversion value, ROAS, MER and GMV are **not profit**. Every decision this system
makes about scaling or killing runs on contribution, and contribution is computed once, in §1,
from the commerce platform.

An agent that recomputes margin from its own assumptions will disagree with the executive page,
and the reader has no way to tell which is right.

## The stack

```
Revenue (net of discounts and refunds)
 − COGS product cost
 = Gross profit
 − Shipping cost what you pay, not what the customer paid
 − Payment processing ~2–3% plus fixed
 − Fulfilment / pick and pack
 − Returns cost restocking, unsellable stock, return shipping
 − Other variable costs packaging inserts, gift wrap, duties
 = Contribution margin ← the number every decision uses
 − Ad spend
 = Contribution after marketing
```

Fixed costs — salaries, rent, software, agency retainers — sit **below** this line. They do not
belong in a per-order margin used to judge whether one more order is worth buying, because they
do not change when you buy it.

## Getting the inputs

In order of preference, and the escalation ladder matters more than the precision:

1. **Derive from the commerce platform.** Shopify carries unit cost per variant, order line
 items, discounts, refunds and shipping. Compute per order and aggregate. Report **coverage** —
 "cost is set on 71% of variants, representing 88% of revenue" — rather than silently averaging
 over the gaps.
2. **Ask the user, without stalling the sweep.** One batched question, while everything else
 continues.
3. **Proceed on a clearly labelled assumption**, published as a range across the plausible band.

**Missing margin never stops the run.** Waste, structure, creative, measurement, catalog,
audiences and CRO findings are all still delivered in full. Withhold only what genuinely
requires margin: break-even ROAS, CAC ceiling, scale and kill calls.

## Publishing a range honestly

When margin is assumed, do not publish a single break-even ROAS. Publish the band, and then
answer the question the reader actually has:

> At 55% contribution margin, break-even ROAS is 1.82. At 65%, it is 1.54. The prospecting
> campaigns in question run at 1.15–1.30, which is below break-even at **either** end — so the
> recommendation does not change across the plausible range, and the exact figure is not needed
> to act.

Stating that the decision is robust to the uncertainty is more useful than withholding the
number, and more honest than picking a midpoint and presenting it as fact.

## Returns

Returns are a variable cost that D2C accounts routinely leave out, and on apparel it is the
difference between profitable and not.

- Use the **return rate by product**, not the account average. One category frequently carries
 most of it.
- Cost per return is return shipping plus handling plus unsellable stock, not just refunded
 revenue.
- Returns lag. A 30-day window understates the return rate on a 60-day policy, which
 systematically overstates margin on recent cohorts — including exactly the cohorts a scale
 decision is being made on.

## Discount stacking

Site-wide sale plus a welcome code plus free shipping plus a bundle discount, all on one order,
is a common margin leak that no single discount setting reveals. Compute realised discount **per
order** from the order data rather than reading the discount configuration.

Where realised discount exceeds intent, that is a §21 finding with a currency value attached.

## Subscription and repeat products

First-order contribution and lifetime contribution are different numbers and answer different
questions.

- **First-order contribution** decides whether acquisition is self-funding — whether you can
 scale without financing it.
- **LTV contribution** decides what you *could* pay if you can fund the gap.

Report both, and be explicit about which one a recommendation uses. Scaling on LTV contribution
with no cash to bridge the payback period is how accounts run out of money while their
dashboards look excellent.

## Per-SKU margin

The account-level figure hides that the hero product may be the thinnest-margin item. §22 needs
margin **per SKU** to answer which products are worth buying customers for.

The common finding: spend concentrated on a bestseller with below-average contribution, while a
higher-margin product gets nothing — a reallocation with real upside that ROAS-based reporting
cannot surface, because the bestseller's ROAS looks fine.

## Output

Written to §1 and consumed everywhere:

| Value | Basis |
|---|---|
| Gross margin % | DERIVED / USER_SUPPLIED / ASSUMED |
| Contribution margin % | " |
| Contribution per order | " |
| Return-adjusted contribution | " |
| Contribution per SKU | " |
| Coverage | share of revenue the cost data actually covers |

The basis label is required. A downstream agent must be able to tell whether it is consuming a
measurement or an assumption.
