---
name: meta-execution-protocol
description: The contract every mutation of a live Meta ad account obeys — written change plan, explicit per-run approval, preview before publish, create-paused, logged change register, rollback, and the customer-data rules. Load before any execution agent calls a write tool. Use when the user asks to "build this campaign," "change the budget," "pause these ads," "launch this," or "apply the recommendations." Execution lane only; audit agents may never load this.
lane: execution
---
# Execution protocol

This repository can change a live ad account. `EXECUTION-PROTOCOL.md` in the repository root is
the authoritative contract; this skill is the working form of it that execution agents load.

If you are in an audit, you are in the wrong lane. Stop and write a recommendation.

## Before anything

1. **Is this an execution run?** `workflows/08-execution-run`, started deliberately by the user.
   Not a step inside an audit. An audit that mutates the account it is measuring destroys its own
   report.
2. **Is the tool classified `write`?** `schemas/meta-mcp-tool-classification.yaml`. Anything
   unclassified is treated as a write and does not get called until a human has looked at it.
3. **Is the finding behind this change sound?** No change acts on an unreconciled number, below
   the purchase floor, on a `RED` measurement verdict, or on a retargeting ROAS with no
   incrementality evidence.

## The seven rules

### 1. Written change plan first

`changes/<run-id>/change-plan.md`, per change: **what** (exact entity and field, with ids and
before values), **why** (the finding, its evidence, its section), **expected effect**, **risk**
(including whether it resets learning), **rollback** (the executable inverse), **review window**.

"Increase the budget" is not a plan. "Campaign `1203…` daily budget €400 → €520" is.

A change that cannot be written this way is not ready to be made.

### 2. Explicit approval, per run

The user approves before anything is called. Approval for one change is never approval for the
next; approval from a previous session has expired. Record it verbatim in
`changes/<run-id>/approval.md`, including what they excluded.

If the change turns out larger than what was approved — a bigger step, more entities, a
different campaign — **stop and re-ask**. Scope creep inside an approved run is the most likely
way this protocol gets broken while appearing to be followed.

### 3. Preview before publish

`ads_get_ad_preview` for anything that renders; a dry-run diff of the intended object against
its current state for everything else. Show it with the approval request, not after.

**Capture the current values before writing.** A rollback note written from memory afterwards is
a wish.

### 4. Create paused

New campaigns, ad sets and ads are created `PAUSED`. Always. Activation is a separate step with
its own approval — `ads_activate_entity` is never called in the same breath as the create chain.

This is the rule that makes every other rule recoverable. A paused mistake costs nothing.

Before activating, sanity-check the budget against account history, not against the plan. An
entity created correctly and activated at 10× the intended budget is the common failure, and one
look catches it.

### 5. Log as you go

`changes/<run-id>/applied.md`, per call: timestamp, tool, entity id and name, before, after, and
the plan line it implements. Written **as each call returns**, not batched — a run that dies
halfway must still leave a complete record.

Log failures too, with the error. A half-applied change set nobody wrote down is
indistinguishable from sabotage when someone opens the account tomorrow.

### 6. One material change at a time

Where a causal read is intended. Two simultaneous changes produce a result nobody can attribute,
and the account has paid for a test it cannot learn from.

Respect the 14-day window and the learning-phase cost (`14-day-change-control`,
`learning-phase-and-significance`). State the reset cost in the plan rather than discovering it
in the review.

Genuinely independent changes may be batched — twelve unrelated fatigued ads paused is one
decision. Say which it is.

### 7. Customer data has its own rules

Before `ads_update_custom_audience_users`:

- The user has authorised **this specific upload**, this run
- The data is hashed as Meta requires — never raw email or phone
- The lawful basis is the user's to assert. Ask, record the answer, do not assume consent
- Log the audience id and record count. **Never log the records**

`ads_pixel_event_create|update|delete` deserves the same care for a different reason: it rewrites
how the account measures itself from that moment on. Historical data keeps the old definition, so
the discontinuity is permanent and belongs in the change register — otherwise the next audit
reads the step in the trend as a performance event.

## What this lane will not do

- Approve its own plan. Not from enthusiasm, not from a prior yes, not because the change is
  obviously correct
- Act on an unreconciled number, below the volume floor, or on a `RED` measurement verdict
- Delete what could be paused or archived. `ads_catalog_delete_product`, `ads_creative_delete`
  and `ads_delete_custom_audience` are last resorts with named justification, not tidying
- Touch an account it was not pointed at. Confirm the account id before every write — gateways
  hold several authenticated accounts

## Reporting back

What was applied, what was skipped and why, what failed, and when each change becomes readable.
If anything in the plan was not applied, **say which and why**. A silent partial application is
the worst available outcome: the user believes the account is in a state it is not.
