---
name: meta-budget-ops
description: When changing budgets, bids or entity status on a live Meta account under the execution protocol — scaling steps, pausing, bid strategy changes, and the learning-phase cost of each. Use in an execution run when the user asks to "increase the budget," "scale this campaign," "pause these ads," or "change the bid strategy." Execution lane only. For what the budget should be, see scale-matrix and meta-ads-operating-system.
lane: execution
---
# Budget and status operations

Load `meta-execution-protocol` first.

These are the smallest-looking changes in the lane and the ones most likely to cost real money
quickly. A budget field is one number, and a misplaced digit spends ten times the intended
amount before anyone opens Ads Manager.

## The tool

`ads_update_entity` covers budget, bid, status and targeting. It is the broadest write in the
connector, which is exactly why every call names the field it is changing and its before value
in the plan.

## Scaling steps

| Step | Learning impact | When |
|---|---|---|
| Under ~20% | Usually no reset | The default. Repeatable every few days |
| 20–50% | Likely reset | Where the scale matrix shows real headroom and the account can absorb a re-learn |
| Over 50%, or doubling | Reset, and delivery may destabilise | Rarely justified on an existing ad set. Duplicating into a new one is often cleaner |

The percentages are Meta's stated behaviour, not a measured constant. Treat them as a prompt to
check the activity log after the change rather than a guarantee.

**Scale on headroom evidence, not on ROAS.** `scale-matrix.yaml` distinguishes
`OBSERVED_AT_HIGHER_SPEND` from `UNTESTED`. A combination that has only ever run at €200/day
tells you nothing about €800/day, and the correct move there is a controlled step with a defined
read window, not a scale plan built on a straight line.

## Before any budget increase

1. The finding behind it is reconciled (§3) and above the volume floor.
2. The §2 verdict is not `RED`.
3. Where the spend is retargeting or existing-customer, there is incrementality evidence.
4. **The new value is sanity-checked against account history**, not against the plan. This catches
   the typo the plan cannot.
5. The review window is stated. A budget change with no review date is a change nobody evaluates.

## Pausing

Pausing is the safest write available and still deserves a plan:

- Pausing **all** ads in an ad set is functionally pausing the ad set, and it resets learning when
  they come back.
- Pausing the last active ad in a campaign leaves an `ACTIVE` campaign spending nothing — an
  audit finding created by an execution run.
- Batch pausing unrelated fatigued ads is one decision, not twelve. Say so.
- Prefer pausing over deleting. Delivery history is worth keeping, and a pause is reversible.

## Bid strategy changes

Always reset learning, and change what Meta is buying. Two rules:

- One at a time, with a full read window. A bid strategy change inside another change's window is
  unreadable.
- A cost cap set below what the account has historically achieved will simply not deliver. Check
  the achieved CPA distribution before setting the cap, and say what happens if it under-delivers.

## Rollback

Budget and status rollbacks are genuinely executable — restore the before value — which is why
capturing before values is a rule rather than a nicety.

What rollback cannot restore: learning phase (reversing an edit does not un-reset it), delivery
history, and spend already incurred. The plan says so before the change, not after.
