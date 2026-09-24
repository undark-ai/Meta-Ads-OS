# Executive review

For the conversation where someone who does not run the account decides what to do about it.
Assembles from an existing audit run; it does not re-analyse.

## Inputs

A completed `audits/<run-id>/`. If none exists, run `02-full-account-audit` first — an executive
review built on a partial read is a confident summary of an incomplete picture.

## Sequence

| Step | What | Agent |
|---|---|---|
| 1 | Verify the run's coverage ledger: how much of the account was actually inspected | 06 |
| 2 | Pull the reconciliation headline — the number every other number depends on | 37–42 |
| 3 | Pull the scorecard and its movement against the prior run | 156 |
| 4 | Pull the opportunity and scale matrices | 157, 158 |
| 5 | Assemble the decision page | 06 |

## The eight questions

1. What is the account's true economic performance? *Reconciled, in contribution.*
2. What is measurement or attribution overstating?
3. Where is money being wasted?
4. Which creative + product + offer combinations deserve more budget, and how much more?
5. What should stop?
6. What should change first?
7. What is the single number to watch next month?
8. What important conclusion remains unproven?

## Rules

- **Lead with the largest supported business implication.** Not with the first section, and not
  with the biggest number if it is the least certain.
- **Coverage on the page**, not in an appendix. An executive who does not know what was not
  inspected cannot calibrate anything else on the page.
- **Flag the recommendations that lower reported ROAS while improving the business** — excluding
  existing customers, fixing a double-counting purchase event. Unflagged, they get applied, the
  dashboard drops, and they get reverted.
- **No number without a source.** Every figure traces to a section.
- **Say what remains unproven.** An executive page with no uncertainty on it is a sales document.

## Deliverable

One page, plus the appendix. If it does not fit on one page, the ranking is not finished.
