# Execution protocol

<!-- execution-boundary: documents-writes -->
<!-- this document IS the contract governing every write tool. -->

This repository can change a live Meta ad account. Google-Ads-OS cannot — the official Google
Ads MCP is read-only, so that system's safety story is "we have no hands". This one has hands,
which means the safety story has to be a protocol instead of an absence.

Every mutation obeys all seven rules below. Not most of them, and not the ones that seem
proportionate to the change at hand: the small changes are where the discipline slips, and a
budget typo at 3am costs more than a bad campaign build.

---

## The boundary

| | Audit lane | Execution lane |
|---|---|---|
| Agents | 00–199 | 200+ |
| Skills | audit + marketing layers | execution layer |
| Meta tools | `read` only | `read` + `write`, under this protocol |
| Output | findings, recommendations | applied changes + a change register |
| Invocation | `/full-audit`, `workflows/01–07`, `09–10` | `workflows/08-execution-run` only |

`schemas/meta-mcp-tool-classification.yaml` is the machine-readable list of which Meta tool is
which. **An unclassified tool is treated as a write.** Fail closed — if Meta ships something
this repository has not seen, the audit lane refuses it until a human has looked at what it
does.

`scripts/validate-execution-boundary.py` fails the build if any audit agent or audit skill so
much as references a write tool by name.

**An audit never mutates as a side effect.** Not "usually", not "unless the user seems to want
it". An audit that discovers a broken pixel event writes the fix as a recommendation; applying
it is a separate invocation the user starts deliberately. The moment an audit is allowed to fix
things it finds, nobody can trust a report from it again — because the account it describes is
no longer the account it measured.

---

## The seven rules

### 1. A written change plan comes first

Before any write tool is called, `changes/<run-id>/change-plan.md` exists and contains, per
change:

- **What** — the exact entity and field, with ids. "Increase the budget" is not a plan;
  "campaign `1203…` daily budget €400 → €520" is.
- **Why** — the finding it comes from, with its evidence and section number.
- **Expected effect** — the number expected to move, and by roughly how much.
- **Risk** — what happens if it is wrong, including whether it resets learning.
- **Rollback** — the exact inverse change, with the prior values recorded so the inverse is
  executable rather than approximate.
- **Review window** — when this becomes readable, normally 14 days.

A change that cannot be written this way is not ready to be made.

### 2. Explicit approval, per run

The user approves the plan before anything is called. **Approval for one change is never
approval for the next**, and approval given in a previous session has expired. Record the
approval verbatim in `changes/<run-id>/approval.md`, including anything the user excluded.

Where a change is materially larger than what was approved — a bigger budget step, more
entities, a different campaign — stop and re-ask. Scope creep inside an approved run is the
most likely way this protocol gets broken while appearing to be followed.

### 3. Preview before publish

Call `ads_get_ad_preview` for anything that renders, and produce a dry-run diff of the intended
object against its current state, for everything else. Show the diff to the user with the
approval request, not after.

For a rollback to be real, capture the **current** values before writing. A rollback note
written from memory after the fact is a wish.

### 4. Create paused

New campaigns, ad sets and ads are created with status `PAUSED`. Always.

Activation is a **separate step with its own approval** — `ads_activate_entity` is never called
in the same breath as the create chain that built the thing. This is the rule that makes every
other rule recoverable: a paused mistake costs nothing, and a live one starts spending
immediately at whatever budget the mistake specified.

Budget sanity-check before activation: daily budget against account history, not against what
the plan says. An entity created correctly and activated at 10× the intended budget is the
common failure, and it is caught by looking once.

### 5. Everything is logged

`changes/<run-id>/applied.md` records, per call: timestamp, tool, entity id, entity name,
before value, after value, and the plan line it implements. Written **as each call returns**,
not batched at the end — a run that dies halfway must still leave a complete record of what it
already did.

A failed write is logged too, with its error. A half-applied change set that nobody wrote down
is indistinguishable from sabotage when someone opens the account tomorrow.

### 6. One material change at a time, with a readable window

Where a causal read is intended, change one thing. Two simultaneous changes produce a result
nobody can attribute, and the account has then paid for a test it cannot learn from.

Respect the 14-day change-control window and conversion lag before judging. Respect Meta's
learning phase specifically: an edit that resets learning costs roughly a week of stable
delivery, and the plan must say so up front rather than discovering it in the review.

Batching is allowed where the changes are genuinely independent — pausing twelve unrelated
fatigued ads is one decision, not twelve. Say which it is in the plan.

### 7. Customer data has its own rules

`ads_update_custom_audience_users` uploads customer PII to Meta. Before it is called:

- The user has explicitly authorised **this specific upload**, this run.
- The data is hashed as Meta requires — never send raw email or phone.
- The lawful basis is the user's to assert; ask, record the answer, and do not proceed on an
  assumption about consent.
- Log the audience id and the record count. Never log the records themselves.

The same care applies to `ads_pixel_event_create|update|delete`: changing event configuration
rewrites how the account measures itself from that moment on, and it is not reversible in the
history. Historical data keeps the old definition; the discontinuity is permanent and belongs
in the change register so the next audit knows why the trend line steps.

---

## What the execution lane will not do

- **Approve its own plan.** No agent infers approval from enthusiasm, from a prior "yes", or
  from the fact that a change is obviously correct.
- **Act on an unreconciled number.** A scale or kill change whose justification traces back to
  a ROAS that section 3 never reconciled does not get made. Fix the measurement first — that is
  what the ordering exists for.
- **Act below the volume floor.** `learning-phase-and-significance` sets the purchase floor. A
  kill under it is variance, not a decision.
- **Scale on a `RED` measurement verdict.** The audit has just demonstrated the conversion
  values are unreliable; spending more against them is the specific mistake this system exists
  to prevent.
- **Delete anything recoverable another way.** Pause instead of delete; archive instead of
  destroy. `ads_catalog_delete_product`, `ads_creative_delete` and `ads_delete_custom_audience`
  are last resorts with named justification, not tidying.
- **Touch an account it was not pointed at.** Confirm the account id against the plan before
  every write. Gateways hold several authenticated accounts, and the live one is not always the
  one you were pointed at.

---

## Change register

`changes/<run-id>/` after a completed execution run:

```
change-plan.md   what was proposed, with before values, rollback and review window
approval.md      what the user actually approved, verbatim, and what they excluded
applied.md       what was called, when, with before/after per entity
rollback.md      the executable inverse of everything in applied.md
```

The register is gitignored — it holds live entity ids and account data — but it is a
deliverable, not a scratch file. It is what the next audit reads to explain a step change in
the trend, and it is what a human reads at 9am when something looks wrong.

## Rollback

Rollback is a normal outcome, not an emergency one. `rollback.md` is written **during** the run
from the captured before-values, so reversing does not depend on anyone reconstructing what the
account looked like.

What rollback cannot restore, and the plan must say so before the change is made: learning
phase (reversing an edit does not un-reset it), delivery history, spend already incurred, and
event-configuration history.

## Reporting back

After an execution run, report what was applied, what was skipped and why, what failed, and
when each change becomes readable. If anything in the plan was not applied, say which and why —
a silent partial application is the worst outcome available, because the user believes the
account is in a state it is not.
