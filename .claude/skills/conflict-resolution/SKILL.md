---
name: conflict-resolution
description: When two sources or two agents disagree about the same number — the order in which to check definitions before assuming a defect, which source wins for which metric, and how to report a disagreement that survives. Use whenever Meta, GA4 and the commerce platform report different figures, or when two audit sections reach different conclusions from the same data.
---
# Conflict resolution

Sources disagree constantly and most disagreements are definitional. The order below matters:
checking for a defect before checking for a definition manufactures findings, and the real
disagreement then gets lost among them.

## The order

1. **Definitions.** Is each side measuring the same event? A "purchase" may include subscription
 renewals in one source and not the other.
2. **Dates and timezone.** Conversion date vs order date. Ad account timezone vs store timezone.
3. **Attribution window and model.** 7d-click vs 7d-click-1d-view vs GA4's data-driven default.
4. **Filters and exclusions.** Status filters, deleted entities, order types, test orders.
5. **Currency, tax, shipping, refunds.** Gross vs net on both sides.
6. **Population.** Meta-attributed orders vs all store orders — a common and wrong comparison.
7. **Only then**, look for a defect.

Record which of these were checked. `reconciliation-schema.yaml` requires the list, because an
unaligned comparison is not a reconciliation.

## Which source wins

```
orders / revenue / customers : commerce platform > analytics > Meta
margin / COGS : commerce platform or finance > anything derived from ROAS
media delivery : Meta > third-party estimates
creative content : Meta > inference from the ad name
relevance / auction / EMQ : Meta, classified PLATFORM_STATED, never OBSERVED
catalog / feed state : Meta catalog diagnostics > inference from ad performance
web behaviour : GA4 > assumption
rendered post-click UX : browser > screenshots > assumption
competitor creative : Ad Library — what is running, never what is working
incrementality : a test > all of the above
```

Authority is per **metric**, not per source. Meta wins on impressions and loses on revenue, in
the same table.

## When two agents disagree

Reconcile the underlying data before publishing either finding. Two sections of one report
contradicting each other is the failure that costs an audit its credibility, and it is usually
caused by two agents querying separately — which is what `data-cache` exists to prevent.

If the disagreement survives reconciliation, it is a finding in its own right: something about
the account is genuinely ambiguous, and saying so is more useful than picking a side.

## Reporting a surviving disagreement

**Never silently pick the number that makes the recommendation look better.** Preserve the
discrepancy:

> Meta reports 412 purchases; Shopify banked 271 in the aligned window. Dedup rate is 71%, which
> accounts for roughly 60 of the 141 difference. The residual ~80 is unexplained after window,
> timezone and order-type alignment. Classified `UNRESOLVED GAP`. Every ROAS below carries this
> qualifier; the account's true ROAS is between the two readings and closer to the lower one.

That is more useful than a confident single number, and it is the only version a reader can
check.

## Escalation

Where the disagreement blocks a decision the user needs, say what would resolve it and what it
costs — usually a specific tracking fix or a specific test. An unresolved gap with a named
resolution path is a finding; one without is a shrug.
