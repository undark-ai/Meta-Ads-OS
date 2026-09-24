# Scale decision

Where does the next dollar go? Section 29 plus the scale matrix, with the gates that stop a
scale verdict being issued on a number that cannot carry it.

## Sequence

| Step | § | What | Agents |
|---:|---:|---|---|
| 0 | — | Preflight, discovery, scope | 02 |
| 1 | 2 | Measurement verdict — a `RED` blocks every scale verdict in this workflow | 21–36 |
| 2 | 3 | Reconciliation — an unreconciled ROAS cannot justify a budget increase | 37–42 |
| 3 | 1 | Canonical economics: contribution, break-even ROAS, CAC ceiling | 7–20 |
| 4 | 7 | Creative database — the combination grain depends on classification | 59, 61–64 |
| 5 | 22 | SKU economics — the product axis | 134–135 |
| 6 | 26 | Incrementality evidence, or the honest absence of it | 142–144 |
| 7 | 15 | Saturation signals and headroom | 100, 90–92 |
| 8 | 29 | Budget allocation | 153–155 |
| 9 | 30 | **Scale matrix** | 158 |

## The gates

A row cannot carry `SCALE` through any of these (`schemas/scale-matrix.yaml`):

- **Measurement** — not on a `RED` verdict, or an unknown modelled share
- **Volume** — not below the purchase floor; the answer there is `INSUFFICIENT_DATA`
- **Margin** — contribution, never revenue ROAS
- **Incrementality** — retargeting and existing-customer combinations need evidence, not
  reported ROAS
- **No double counting** — overlapping rows reconciled before totalling

## Headroom honesty

`OBSERVED_AT_HIGHER_SPEND` · `MODELLED_FROM_TREND` · `UNTESTED`.

A combination that has only ever run at €200/day says nothing about €800/day. The correct verdict
there is `TEST_HEADROOM` with a defined step and read window — not a scale plan drawn as a
straight line.

## Deliverables

`scale-matrix.md`, ranked by expected incremental contribution, each row with a verdict, one
next step, and its review window. Close by naming what could not be sized and the one
measurement or test that would most improve the next version of the table.

Where the user wants the plan applied, that is `08-execution-run` — a separate invocation.
