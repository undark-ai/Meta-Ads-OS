---
name: scale-matrix
description: When deciding where the next dollar goes on a Meta account — ranking creative x product x offer x audience combinations by incremental profit rather than reported ROAS, with headroom, saturation signals and a decision per row. Use when the user asks "where should I put more budget," "what should I scale," "how much more can this take," "which winners should I double down on," or "build me a scaling plan." The artifact that answers the system's core question. For what is broken instead, see recommendation-prioritization.
---
# Scale matrix

The opportunity matrix answers *what is broken*. This answers *where the next dollar goes*. They
are separate documents because merging them buries the growth case under the defect list, and
the two get read by different people at different moments.

> **Which creative + product + offer combinations are generating incremental profitable
> customers, and how much more can we scale them?**

## Combination, not ad

The grain is `creative_angle × product_group × offer × audience_type`.

One winning ad is a data point. The same angle winning across three products and two offers is a
strategy, and only the combination grain shows the difference. It is also the only grain with
enough purchases to say anything — ad-level purchase counts on Meta are small, and aggregating
to the combination is why classification is worth the effort.

## Rank on contribution, gated on incrementality

Reported ROAS is not the scale signal.

A retargeting combination at 8× that would have converted anyway is worth less than a
prospecting combination at 2.1× that creates demand. Ranking by reported ROAS moves budget
toward the least incremental spend, systematically, with the dashboard agreeing at every step.

Rank by **expected incremental contribution**:

```
contribution_per_dollar = contribution_margin_total / spend
```

then adjust by the incrementality evidence class. Where incrementality has not been measured,
say `NOT_MEASURED` — do not apply an assumed haircut. An invented adjustment is worse than an
admitted gap because it looks like a measurement.

## Headroom, honestly

The honest answer is frequently "we cannot tell yet".

| Basis | Meaning |
|---|---|
| `OBSERVED_AT_HIGHER_SPEND` | This combination has run at higher daily spend and still cleared break-even. The strongest evidence available |
| `MODELLED_FROM_TREND` | Extrapolated from the spend/efficiency relationship in the window. Directional |
| `UNTESTED` | Never run above current spend. **`expected_incremental_contribution` is null** — do not invent a number to fill the column |

Saturation signals that cap headroom: frequency ceiling, audience size versus reach, CPM trend
at higher spend, diminishing purchases per additional dollar, placement mix drifting toward
cheaper inventory.

A combination that has only ever run at €200/day tells you nothing about €800/day. The correct
recommendation there is `TEST_HEADROOM` — a controlled step up with a defined read window — not
a scale plan built on a straight line.

## The gates

A row cannot carry a `SCALE` verdict through any of these:

| Gate | Rule |
|---|---|
| **Measurement** | No `SCALE` on a `RED` §2 verdict, or where modelled share exceeds the threshold. Scaling against conversion values the audit just showed unreliable is the specific mistake this system exists to prevent |
| **Volume** | No `SCALE` or `KILL` below the purchase floor. Under it the verdict is `INSUFFICIENT_DATA`, and the next step is to buy more data |
| **Margin** | Contribution, never revenue ROAS. Where margin is assumed, publish across the band and say whether the verdict changes |
| **Incrementality** | Retargeting and existing-customer combinations need evidence, not reported ROAS. Prospecting may scale on reported figures with confidence lowered and the gap named |
| **No double counting** | Where two rows share supporting ads, reconcile into one before totalling. The account-level upside is not the sum of the column |

## Verdicts

`SCALE` · `HOLD` · `ITERATE` · `TEST_HEADROOM` · `REDUCE` · `KILL` · `INSUFFICIENT_DATA`

Each row carries a rationale, **one** specific next step, what it is blocked by if anything, and
the review window. `INSUFFICIENT_DATA` is a legitimate and common verdict; forcing every row to a
decision is how a matrix becomes fiction.

## Output

`audits/<run-id>/scale-matrix.md`, ranked by expected incremental contribution:

| Combination | Ads | Spend | Purchases | New-cust CAC | Contribution | Contribution/$ | Incrementality | Headroom basis | Next spend | Expected incr. contribution | Action | Next step |

Close with a paragraph naming **what could not be sized and why**, and the one measurement or
test that would most improve the next run's version of this table. That paragraph is usually the
most valuable part: it tells the account what to fix so the next scaling decision is better than
this one.

## Handing it to the execution lane

Each row names the execution workflow that would apply it, if the user chooses to. It does not
apply anything. An audit that scales campaigns it recommended scaling is an audit nobody can
trust again — the account it describes is no longer the account it measured.
