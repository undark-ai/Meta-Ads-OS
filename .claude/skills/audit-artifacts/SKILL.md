---
name: audit-artifacts
description: When creating and writing the persistent output of a Meta audit run — the run directory, which artifacts every full audit must produce, and why runs are never overwritten. Use at the start of every audit and whenever a section needs to write its output.
---
# Audit artifacts

Every run writes to its own directory. **Never overwrite a prior run** — the comparison between
audits is one of the more useful things the system produces, and it only exists if the old one
survives.

## The run directory

```
audits/<YYYY-MM-DD-HHMM>/
 preflight.md what was asked before the run, and what the user chose
 source-capabilities.md which connector-ladder rung supplied each source
 scope.md account, store, currency, timezone, window, attribution setting
 assumptions.md every labelled assumption, and what depends on it
 coverage.md all 30 sections, each with its state
 raw/ source responses as returned
 normalized/ canonical tables
 creative-database.csv one row per ad — the creative spine
 top-creatives.html the Top Creatives dashboard
 top-creatives-chrome.html the snapshot with real thumbnails
 reconciliations/ Meta claim vs store vs GA4, per metric
 findings/ per-section findings against finding-schema.yaml
 agent-results/ per-agent output against agent-contract.yaml
 scorecard.md published weights, per-category breakdown
 opportunity-matrix.md what is broken, ranked and de-duplicated
 scale-matrix.md where the next dollar goes
 action-plan.md 30/60/90, sequenced so each change stays readable
 quantified-upside.md what it is worth, and what could not be sized
 executive-summary.md the decision page
```

`audits/` is gitignored. It holds account ids, spend, creative and order data.

## Open the ledger first

`coverage.md` is created **when the run starts**, with all 30 sections `PENDING`, and updated as
each closes. An interrupted run then still shows which sections were reached. A ledger written at
the end is written from memory, and memory is generous about what it checked.

## `scope.md` is the contract

Written once, early, and every dataset header must agree with it:

- account id and name, and that it was confirmed live
- store domain and platform
- currency and **account timezone** (frequently not the store's)
- audit window and comparison window
- **the attribution setting**, one for the whole run
- the primary conversion event
- margin basis: `DERIVED` / `USER_SUPPLIED` / `ASSUMED`

A dataset whose window or attribution differs from `scope.md` is dropped, not silently included.

## `assumptions.md` earns its place

Every labelled assumption, what it was based on, and **what depends on it**. When a reader
disagrees with an assumption, they need to know immediately which conclusions change.

An assumption with no dependency list is a disclaimer. One with a dependency list is a tool.

## Prior runs

Read the previous run's `scorecard.md` and `coverage.md` for comparison — labelled as history,
with its date. Movement between audits is a genuine finding, and the account rarely has it any
other way.

Never carry forward a prior run's `UNAVAILABLE` verdict on a source. Connectors get authorised
between runs; re-checking is the cheapest test in the system.

## The execution lane writes elsewhere

`changes/<run-id>/`, never `audits/`. An audit run and an execution run never share a run id, and
the separation is what lets a reader trust that the account described is the account measured.
