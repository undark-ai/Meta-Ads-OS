---
name: data-cache
description: When caching source results within an audit run so downstream agents reuse them instead of re-querying Meta. Use whenever an agent needs data another agent already pulled. Prevents rate-limit exhaustion and, more importantly, prevents two agents analysing subtly different versions of the same data.
---
# Data cache

Two reasons, and the second is the important one.

**Rate limits.** Meta limits by account and by app, and the budget is shared. Twenty agents each
pulling their own ad-level data will exhaust it and push late sections to `DEGRADED` for no
reason.

**Consistency.** Two agents querying the same thing at different moments, with different field
sets or row limits, will produce slightly different numbers — and then two sections of the same
report disagree with no way to tell which is right. This is the failure that costs an audit its
credibility, and it is invisible until someone adds up two tables.

## The rule

Within a run, a source result is pulled **once** and written to `audits/<run-id>/raw/`.
Downstream agents read from there.

The creative database is the strongest case: §7 writes `creative-database.csv`, and §§8–11, 19,
22 and 30 read it. Nothing re-queries Meta for creative performance, including the dashboard.

## What to cache

| Dataset | Written by | Read by |
|---|---|---|
| Ad / ad set / campaign entities and insights | §5, §7 | Nearly everything |
| `creative-database.csv` | §7 | §8–11, 19, 22, 30, dashboard |
| Creative content | §7 | §9, §20 |
| Activity log | §5 | §6, §8, §9, §25 |
| Dataset quality and pixel state | §2 | §3, §25 |
| Commerce orders and line items | §1 | §3, §22, §24 |
| Catalog diagnostics | §16 | §17 |

## Cache keys

A cached result is only reusable if it was pulled on the same terms. Key on:

```
source · entity level · date range · attribution window · breakdown dimension · field set
```

A cache hit on a different attribution window is not a hit. Returning it is worse than
re-querying, because the mismatch is invisible downstream.

## Never cache across runs

Each run pulls fresh. Accounts change, connectors get authorised, and a stale creative database
would silently describe last month's account while the report claims to describe this one.

The one thing that legitimately crosses runs is **prior-run output** for comparison — the
previous scorecard, the previous coverage ledger — and it is read as history, explicitly labelled
with its date, never as current state.

## Preserve raw alongside normalised

Write the source response as returned, next to the normalised table. §3's first question when a
gap appears is what each source actually reported, and a run that only kept the normalised value
cannot answer it.
