---
name: bid-strategy-and-learning
description: When auditing how a Meta account buys — bid strategy per campaign, learning-phase state, learning-limited detection, and whether a cost cap is set somewhere the account can actually deliver. Use when the user asks "which bid strategy should I use," "should I use cost cap," "my ad sets are stuck in learning," "learning limited," "why is my campaign not spending," or "should I switch to lowest cost." Bid changes reset learning, so this skill is deliberately conservative about recommending one.
---
# Bid strategy and learning phase

Bid mistakes are expensive to reverse: switching resets learning, which costs roughly a week of
stable delivery. So the bar for recommending a change is higher here than anywhere else in the
audit.

## The strategies

| Strategy | How it works | Suits | Risk |
|---|---|---|---|
| **Lowest cost** | Maximises results at any CPA, no cap | New campaigns, testing, broad audiences | CPA can spike unpredictably |
| **Cost cap** | Targets a CPA ceiling; spends less if CPA exceeds it | Established campaigns with 50+ conversions/week | Underspends badly if the cap is too tight |
| **Bid cap** | Max bid per auction — the strictest control | Hard cost requirements | High risk of not spending at all |
| **Minimum ROAS** | Maintains a ROAS floor | Variable-price catalogues, value optimisation | Limits volume |
| **Highest value** | Maximises total conversion value | Variable-price products | Does not control CPA |

Match the strategy to conversion volume and to the §1 goal, not to preference. A cost cap on an
ad set doing 12 conversions a week is a cap on an ad set that cannot exit learning.

## Learning phase

Roughly **50 optimisation events per ad set per week** to exit.

| State | Meaning | What to do |
|---|---|---|
| **Learning** | Still gathering; delivery volatile | **Make no changes.** CPA during learning typically runs 2–3× the stable rate — that is expected, not failure |
| **Exited** | Stable | Safe to scale or adjust |
| **Learning limited** | Cannot accumulate 50 events/week at this budget and audience | **Structural, not creative** |

Detect learning-limited from: fewer than ~50 optimisation events in 7 days, an ad set older than
7 days still flagged learning, and CPA running well above the account average.

**The fix for learning-limited is structural** — consolidate ad sets, widen the audience, raise
budget, or move the optimisation event up-funnel. It is not new creative, and routing it to the
creative team wastes a production cycle and returns with the same problem.

## What resets learning

Check `ads_account_get_activity_logs` before attributing any movement to creative:

| Resets | Usually does not |
|---|---|
| Targeting change | Budget change under ~20% |
| Optimisation event change | Status toggles within an existing set |
| Bid strategy or bid amount change | Name changes |
| Adding or removing ads | |
| Placement change | |
| Budget change of ~20%+ | |
| Creative change on an existing ad | |

These are Meta's stated behaviours, not measured constants; they move. Treat them as a prompt to
read the activity log rather than a rule to compute against.

**The consequence that matters:** a performance drop the day after an edit *is* the edit. An ad
"failing" inside an ad set that reset four days ago has not failed, and the common trap is
reverting a good change during its re-learn — two resets, no learning, worse than before.

## Setting a cost cap

Where a cost cap is warranted, derive it from what the account has actually achieved:

```
cost cap ≈ trailing 14-day average CPA × 1.25
```

The margin matters. A cap set at or below the achieved average will simply not deliver, and the
account reads "cost cap doesn't work" when what happened is that the cap was set below the price.

Check the achieved CPA **distribution**, not just the average — a cap near the median leaves half
the auction unreachable.

## Budget-constrained versus bid-constrained

Two different problems that both look like underspending:

- **Budget-constrained** — spending the full budget every day, delivery capped by money. Headroom
  exists; this is a §29 allocation question.
- **Bid-constrained** — not spending the budget. The bid or cap is too low, or the audience too
  small to spend it at any bid. Raising budget does nothing.

Distinguish by budget utilisation before recommending either.

## Output

For §6: bid strategy per campaign with its cap value, learning state per ad set, learning-limited
ad sets with the structural cause named, budget utilisation, and whether each campaign is budget-
or bid-constrained.

Recommend a strategy change only where the evidence is strong, and **state the learning-reset cost
up front** — roughly a week of stable delivery — so the decision is made with its price visible.
