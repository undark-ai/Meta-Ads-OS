# Execution run

<!-- execution-boundary: documents-writes -->
<!-- the only workflow that mutates an account; it names the calls it governs. -->

**The only workflow in this repository that changes a live ad account.**

Governed by `EXECUTION-PROTOCOL.md`. Every agent in it loads `meta-execution-protocol`. It is
started deliberately by the user; it is never a step inside an audit.

## Sequence

| Step | Agent | What | Gate |
|---|---|---|---|
| 1 | **200** | Confirm the account, and that it is the one the plan refers to | Gateways hold several authenticated accounts |
| 2 | **200** | Load the findings this run will act on | Each must be reconciled, above the volume floor, and not on a `RED` measurement verdict |
| 3 | **201** | **Write `changes/<run-id>/change-plan.md`** | What, why, expected effect, risk, rollback with before values, review window |
| 4 | **203** | Preview: `ads_get_ad_preview` for anything that renders; a dry-run diff for everything else | Produced **before** approval, shown with it |
| 5 | **202** | **Request approval** | Per run. Approval for one change is never approval for the next |
| 6 | **202** | Record it verbatim in `approval.md`, including exclusions | And hold the boundary for the rest of the run |
| 7 | **204–211** | Apply, **creating paused**, logging each call as it returns | `applied.md` written as you go, never batched |
| 8 | **212** | Pre-activation check: budget against **account history**, previews looked at, destination URLs resolved, exclusions present | This is what create-paused exists for |
| 9 | **212** | **Separate approval for activation** | `ads_activate_entity` is never called in the same breath as the create chain |
| 10 | **213** | Write `rollback.md` from the captured before values | During the run, not after |
| 11 | **213** | Report: applied, skipped and why, failed, and when each becomes readable | A silent partial application is the worst outcome available |

**Which operator applies which change** (204–211): campaign · ad set · creative and ad · audience
and customer lists · budget and bid · status and pause · catalog · measurement config and
experiments. Only those eight touch write tools; 200–203 govern and 212–213 close.
`AGENT-INDEX.md` has the full band.

## Refusals

This workflow stops rather than proceeding when:

- The change is materially larger than what was approved — **re-ask**
- The finding behind it is unreconciled, below the floor, or rests on a `RED` verdict
- A retargeting or existing-customer scale has no incrementality evidence
- A customer-data upload lacks explicit per-upload authorisation, hashing, or a stated lawful
  basis
- The account id does not match the plan

## What it will not do

Approve its own plan. Delete what could be paused or archived. Scale on reported ROAS alone.
Mutate as a side effect of anything.

## Deliverables

`changes/<run-id>/change-plan.md` · `approval.md` · `applied.md` · `rollback.md`, and a report
of what changed and when it becomes readable.
