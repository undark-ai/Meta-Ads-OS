---
name: 14-day-change-control
description: When sequencing changes to a Meta account so each one can actually be judged — the read window, learning-phase cost, one-material-change-at-a-time, and which changes can safely be batched. Use when building an action plan, designing a test, or deciding whether two changes can be made in the same week.
---
# Change control

A change you cannot read is a change you cannot learn from. The account paid for it either way.

## The read window

Default **14 days**, and it is composed of:

```
conversion lag (up to the attribution window)
+ learning phase (if the change reset it)
+ enough stable days to read
= the earliest honest review date
```

On a 7-day-click window with a learning reset, 14 days is the *minimum*, not a comfortable
margin. Judging at day 4 reads the learning phase.

Shorten it only with evidence — a high-volume account with a 1-day cycle can read faster, and
should say why.

## One material change at a time

Where a causal read is intended, change one thing. Two simultaneous changes produce a result
nobody can attribute.

This is not a counsel of perfection; it is a budgeting rule. The account spent money to learn
something, and stacking changes means it spent the money and learned nothing.

## What can be batched

Genuinely independent changes are one decision:

| Batchable | Not batchable |
|---|---|
| Pausing twelve unrelated fatigued ads | A budget increase plus a creative swap on the same ad set |
| Fixing UTMs across the account | A bid strategy change plus an audience change |
| Adding exclusions to several prospecting sets | Anything where you want to know which one worked |

Say in the plan which it is. "These are independent" is a claim the reader can check.

## Learning-phase cost

Check which changes reset learning (`learning-phase-and-significance`) and state the cost **up
front** rather than discovering it in the review.

The common trap: an account makes a good change, performance dips for five days while the ad set
re-learns, the operator panics and reverts — resetting learning a second time. Two resets, no
learning, worse performance than before the good change.

Where a reset is unavoidable, the plan says so and the review date accounts for it.

## Sequencing an action plan

- **P0 measurement fixes first.** They change what every subsequent number means, so making them
 first is what makes later changes readable.
- Do not stack changes inside one read window on the same entity.
- Order by time-to-read as well as by value — a fast-reading change unblocks the next decision.
- Where two P1 items touch the same campaign, sequence them rather than running both.

## In the execution lane

`EXECUTION-PROTOCOL.md` binds this: every change plan states its review window and its rollback,
and the register records when each change becomes readable. A change with no review date is a
change nobody will ever evaluate.
