---
name: coverage-ledger
description: When recording which of the 30 audit sections ran and what each concluded — the five coverage states, how to derive the tally, and why an unrun section is a defect rather than an omission. Use whenever a full or partial audit is being run, and whenever a report needs to say what was and was not inspected. For the section definitions themselves, see full-audit.
---
# Coverage ledger

The second failure mode of an audit, after optimising numbers that were not true, is **silence**.
A reader cannot tell "checked and fine" from "never looked" unless you say which it was — and
the reader will assume the more flattering one.

## The five states

| State | Meaning | Common mistake |
|---|---|---|
| `FINDINGS` | Ran; produced findings | — |
| `CLEAN` | Ran; nothing wrong found | Omitting it. A clean result **is** a result and must be stated |
| `DEGRADED` | Ran on partial data | Not saying what was missing or what the partial result still supports |
| `N/A` | The layer does not exist in this account | Confusing with `BLOCKED`. No retargeting configured is `N/A` — and is itself a finding |
| `BLOCKED` | An input is genuinely unavailable | Not naming the input, the reason, and what it would have answered |

"I didn't get to it" is not one of the five. An unrun section is a defect in the run, not an
omission in the report.

## `N/A` versus `BLOCKED`

The distinction carries real information and gets collapsed constantly:

- **`N/A`** — the account has no catalog, so §16 has nothing to audit. Nothing is wrong with the
 audit. Whether the *account* should have a catalog is a separate finding, and often a good one.
- **`BLOCKED`** — the account has a catalog and the connector could not reach it. Something is
 missing from the run, and the report must say what conclusion is unavailable as a result.

Writing `N/A` where the truth is `BLOCKED` silently converts a gap in the audit into a fact about
the account.

## Open it at the start

`coverage.md` is created when the run starts, with all 30 sections listed as `PENDING`, and
updated as each closes. An interrupted run then still shows exactly which sections were reached.

A ledger written at the end is written from memory, and memory is generous about what it checked.

## Derive the tally

**Count the states programmatically and check the total is 30.** Never write the summary line by
hand.

A hand-written summary drifts from the table beneath it, and because it is the first thing a
reader trusts, a wrong one discredits the ledger it summarises. Where the ledger appears in more
than one place — the report, the dashboard, a slide — check they agree.

## Format

```markdown
# Coverage — <run-id>

24 FINDINGS · 3 CLEAN · 2 DEGRADED · 1 N/A · 0 BLOCKED (30 of 30)

| § | Section | State | Sources | Note |
|---|---|---|---|---|
| 1 | Business & economics | FINDINGS | Shopify, user | Margin derived; 88% revenue coverage |
| 2 | Tracking & measurement | FINDINGS | Meta datasets | Verdict YELLOW — dedup rate 71% |
| 16 | Product catalog | N/A | — | No catalog connected to this account; account runs no DPA |
| 26 | Incrementality | DEGRADED | Meta | No holdout has ever run; reported ROAS carried with the gap named |
```

Every `DEGRADED` and `BLOCKED` row states the missing input **and its consequence**. "Partial
data" is not a note; "GA4 unavailable, so the mid-funnel between click and add-to-cart is
inferred from Meta's own events only" is.

## The relationship to confidence

Coverage state is about whether the section ran. Confidence is about how much the result can
bear. They are independent: a `FINDINGS` section can carry `LOW` confidence, and a `DEGRADED`
one can still produce a high-confidence finding about the part it could see.

Do not collapse them into a single quality score. The reader needs both.
