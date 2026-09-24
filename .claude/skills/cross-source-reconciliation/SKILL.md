---
name: cross-source-reconciliation
description: When setting Meta's claimed purchases and revenue against banked orders from Shopify and GA4 — the mandatory reconciliation that runs before any economic conclusion. Use when the user asks "why doesn't Meta match Shopify," "Meta says 400 sales but we only got 250," "which number do I trust," "blended MER," or whenever a ROAS is about to be used to justify a decision. Produces order claim ratio, value claim share, blended MER, implied AOV and modelled share. For the modelling mechanics behind the gap, see modeled-conversions.
---
# Cross-source reconciliation

An ad platform grading its own homework is the default failure mode of paid-media reporting.
Meta reports what Meta believes it caused. The store reports what was banked. **Never let an
unreconciled ROAS reach a recommendation.**

This runs in §3, before any economic conclusion, in every full audit. It is not optional and it
is not "if there's time".

## Every ad platform over-claims, so pick one numerator and use it for all of them

Reconciliation usually starts as "is Meta telling the truth", and stops there. It should not.

On one live account, measured against the same GA4 property over the same window, **Meta claimed
2.09× GA4's paid-social transactions and Google search claimed 2.21× GA4's paid-search
transactions.** Neither platform is unusually dishonest; both count their own conversions on their
own window with their own modelling, and both therefore over-claim against last-click.

Two consequences:

- **Never compare platform A's self-reported conversions to platform B's self-reported
  conversions.** That comparison measures which vendor attributes more aggressively, not which
  channel performs. Take both numerators from the same neutral source.
- **A cross-channel CAC table built from each platform's own numbers is not a reconciliation.** It
  is two press releases in one table.

Where the comparison is search against paid social, `funnel-analysis`'s brand/generic rule applies
on top of this one: split first, then take both sides' transactions from GA4.

## Align before comparing

Most gaps are definitional. Comparing before aligning manufactures findings that do not exist,
and then the real gap gets lost among them.

| Dimension | What to align |
|---|---|
| **Date basis** | Meta reports on the **conversion** date and credits back to the click; the store reports on the **order** date. With a 7-day window a purchase can be credited to a click a week earlier |
| **Timezone** | The ad account's timezone is frequently not the store's |
| **Currency** | One reporting currency; check for multi-currency stores settling in another |
| **Attribution window** | One window for the whole comparison, stated explicitly |
| **Attribution model** | Meta's is last-touch within its own window; GA4's default is data-driven across channels. These are not comparable without saying so |
| **Event set** | Which events count as a purchase. A subscription renewal, a POS sale or a manual draft order may be in one source and not the other |
| **Counting type** | Every conversion, or one per click |
| **Refunds and cancellations** | The store nets them; Meta does not |
| **Gross vs net** | Tax, shipping and discounts in or out |
| **Population** | Meta-attributed orders, or all store orders. Comparing Meta's implied AOV against *all* store orders is a common and wrong comparison |

Record which alignments were performed. An unaligned comparison is not a reconciliation, and
`reconciliation-schema.yaml` requires the list.

## The five headline measures

Published in every run, regardless of what else is found:

| Measure | Formula |
|---|---|
| **Order claim ratio** | Meta-claimed purchases ÷ store orders |
| **Value claim share** | Meta-claimed value ÷ store revenue |
| **Blended MER** | store revenue ÷ **total** ad spend, every channel |
| **Implied AOV** | Meta-claimed value ÷ Meta-claimed purchases, against store AOV |
| **Modelled share** | share of Meta-claimed purchases Meta modelled rather than observed |

**Blended MER uses total ad spend.** Enumerate every paid channel first — Google, TikTok,
Pinterest, affiliates, retail media. Computed on Meta's spend alone it is not a partial MER, it
is a different and wrong number, and it hides the case it exists to reveal: two platforms each
claiming the same order. That is only visible when the claims are summed and compared to one
store revenue figure.

## Diagnosing the gap

| Pattern | Likely cause | Confirm by |
|---|---|---|
| Meta purchases **>** store orders | Double counting — pixel and CAPI not deduplicated; or a second event firing | Check `event_id` presence and dedup rate in the dataset quality report |
| Meta purchases > store orders, dedup clean | View-through and modelled conversions inflating the claim | Compare 1-day-click only against the default window |
| Implied AOV **far below** store AOV | A micro-conversion is being counted as a purchase — a lead, a subscription signup, an add-to-cart mapped wrong | Inspect the purchase event configuration and its value parameter |
| Implied AOV **far above** store AOV | Subscription lifetime value or a bundle being sent as the value; or currency mismatch | Check the value parameter and currency on the purchase event |
| Meta purchases **<** store orders, tracking healthy | Under-attribution: ATT signal loss, short window, or genuinely non-incremental store orders | Check platform mix and EMQ; then §26 |
| High claim share on **low** spend, concentrated in retargeting | Harvesting demand, not creating it | §26 incrementality — this is the finding that matters most |
| Store revenue far exceeds all platform claims combined | Healthy organic and returning-customer base, or broken tracking | Check untagged traffic share in GA4 |

Confirm each hypothesis against the actual event configuration before stating it. A plausible
diagnosis presented as a finding is exactly the kind of confident wrongness this system exists
to avoid.

## Classification

Every compared metric gets one:

- **`MATCH`** — within tolerance after alignment
- **`EXPLAINED GAP`** — a gap with an identified, evidenced cause
- **`UNRESOLVED GAP`** — a gap that survived alignment and diagnosis. Say so plainly rather than
 picking a cause that fits
- **`INVALID COMPARISON`** — the two figures were never measuring the same thing. Not a failure
 state; the correct answer, and calling it a gap would manufacture a finding

## When paid traffic is untagged

If §2 finds paid clicks reaching the store without UTMs, first-party data cannot separate paid
from organic at all. The platform claim share then becomes an **upper bound, not a
measurement** — and that qualifier travels everywhere the number appears, including §25, §26 and
the executive page.

This is a common and under-reported situation. An account cannot be told its Meta ROAS is
overstated by 40% if nothing at the store end can attribute anything; the honest statement is
that the claim cannot be checked, and here is what it would take to check it.

## Output

`audits/<run-id>/reconciliation.md`, plus per-metric rows against
`schemas/reconciliation-schema.yaml`. Carry the headline to the executive page whenever the gap
is material — that is, whenever a reader acting on the reported figure would make a different
decision than one acting on the reconciled one.

Never present Meta-claimed value as banked revenue. Where both appear in one table, label them.
