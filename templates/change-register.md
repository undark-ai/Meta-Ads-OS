# Change register — <run-id>

Execution lane. Governed by `EXECUTION-PROTOCOL.md`.

**Account:** <id and name, confirmed against the plan> · **Lane:** execution ·
**Started:** <timestamp>

---

## Plan

| # | Entity | Field | Before | After | Finding | Resets learning? | Review date |
|---|---|---|---|---|---|---|---|

Per change: what, why, expected effect, risk, rollback, review window.

**Before values captured:** yes/no. *A rollback written from memory afterwards is a wish.*

## Approval

> Verbatim, including anything the user excluded.

**Approved:** <timestamp> · **Excluded:** <what, and why>

*Approval for one change is never approval for the next. Approval from a previous session has
expired.*

## Applied

| Timestamp | Tool | Entity id | Entity name | Before | After | Plan line | Result |
|---|---|---|---|---|---|---|---|

*Written as each call returns, not batched. Failures logged with their error.*

## Activation

Created paused at <timestamp>. Pre-activation check:

- [ ] Budget sanity-checked against **account history**, not against the plan
- [ ] Every ad previewed and looked at
- [ ] Destination URLs resolved through their redirect chains
- [ ] Exclusions present, especially existing customers on prospecting
- [ ] Optimisation event matches the objective and the §1 goal

**Separate approval for activation:** <timestamp>

## Rollback

| # | Entity | Restore to | Executable? |
|---|---|---|---|

**Cannot be restored:** learning phase, delivery history, spend incurred, event-configuration
history, audience membership history.

## Report

Applied: · Skipped and why: · Failed: · Readable from:

*A silent partial application is the worst available outcome — the user believes the account is
in a state it is not.*
