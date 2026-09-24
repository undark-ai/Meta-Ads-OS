---
name: demand-lifecycle
description: When classifying a Meta account's spend by what job it does — creating demand, capturing existing demand, accelerating a decided buyer, reviving a lapsed one, or expanding an existing customer. Use when the user asks "how should my account be structured," "how much should go to prospecting," "what's the right budget split," "are we just retargeting," or when a scale or incrementality question needs to know which layer the spend sits in. Create versus Capture is the incrementality distinction, made structural.
---
# Demand lifecycle

Most accounts are described as prospecting and retargeting. That two-way split is too coarse to
allocate against: it collapses winback and repeat-purchase into "retargeting", and it hides the
one distinction that decides whether spend is worth anything.

Five stages, by the job the spend does:

| Stage | Job | Awareness | Offers that fit | The number that judges it |
|---|---|---|---|---|
| **Create** | Build demand that did not exist | L1 unaware · L2 problem-aware | Education, entertainment, problem-framing, founder story | New-customer CAC, and **incremental** revenue |
| **Capture** | Convert demand that already exists | L3 solution-aware · L4 product-aware | Product, comparison, proof, direct response | New-customer CAC — with the incrementality caveat |
| **Accelerate** | Close a buyer who already decided | L4 product-aware · L5 most aware | Urgency, guarantee, free shipping threshold, cart nudge | Incremental conversion rate, not ROAS |
| **Revive** | Restart a lapsed customer | L5, previously bought | Winback offer, new-arrival, replenishment reminder | Reactivation rate, contribution per reactivated customer |
| **Expand** | More revenue from an existing customer | L5, active | Cross-sell, bundle, subscription upgrade, replenishment | Repeat rate, contribution per customer, LTV movement |

## Create versus Capture is the incrementality question

This is why the framework is worth having rather than being a nicer way to draw a funnel.

**Create makes demand. Capture harvests it.** §26 asks how much of Meta's reported revenue would
have happened anyway — and the answer is structurally different by stage. Capture spend is
reaching people who were already going to look for this. Create spend is the only layer that can
plausibly claim to have caused the demand.

Which means the reported figures point the wrong way, systematically:

- Capture reports the best ROAS and is the least incremental
- Create reports the worst ROAS and carries most of the growth
- An account that reallocates on reported ROAS drains Create to fund Capture, watches blended ROAS
  improve, and stops growing

`scale-matrix`'s incrementality gate exists because of this. Tag every campaign with its stage
before reading §29, so the allocation question is asked in the right units.

## Accelerate, Revive and Expand are not "retargeting"

Collapsing them loses three different jobs:

- **Accelerate** targets someone mid-decision — a cart or checkout abandoner. Short window, offer
  or friction-removal, and its real measure is whether it *changed* an outcome. Much of it would
  have converted regardless, which is why it is the most over-credited spend in most accounts.
- **Revive** targets someone who bought once and stopped. Different creative, different offer,
  different economics — you are not acquiring, you are reactivating, and the CAC ceiling is the
  *repeat* contribution, not the first-order one.
- **Expand** targets an active customer. Cross-sell, bundle, replenishment. Judged on LTV
  movement, and frequently better served by email than by paid — which is a finding worth making
  when an account is paying Meta to reach people it can email for nothing.

That last point matters: **Expand spend competing with an owned channel is waste dressed as
performance.** Check the email and SMS programme (§24) before recommending paid Expand budget.

## Auditing the distribution

For §13, §14 and §24: classify every campaign by stage, then report **spend share, new-customer
share and contribution by stage.**

The distributions that are findings:

| Pattern | Reading |
|---|---|
| Create under ~40% of spend on a growing account | The account is harvesting a pool nothing is refilling. Retargeting performance will decay on its own schedule |
| Accelerate + Revive + Expand above ~40% | Reported ROAS is flattered. Check §3's claim ratio and §24's new-customer share |
| No Revive or Expand at all | `N/A` — and itself a finding where repeat purchase is meaningful |
| Expand spend alongside an active email programme | Paying for reach the account already owns |
| Every stage running the same creative | Awareness-level mismatch. An L1 ad shown to an L5 buyer wastes the impression, and vice versa (`creative-to-page-continuity`) |

There is no universal correct split. It depends on the §1 goal, category repeat rate and how fast
the Create pool refills. What is *not* defensible is a split nobody chose — which is what most
accounts have.

## Awareness level is the join

`creative-record.yaml` already carries `awareness_level` per ad. Cross-tabulate it against stage:
an ad written for the unaware running in a Capture campaign is a mismatch that explains
underperformance neither section would find alone.

## Output

Stage tagged per campaign, spend and contribution share per stage, the Create/Capture ratio with
its incrementality caveat stated, any stage running at `N/A`, and awareness-level mismatches
between creative and stage.

Route the recommendation to the right place: a thin Create layer is a §29 allocation finding, and
an awareness mismatch is a §9 creative one.
