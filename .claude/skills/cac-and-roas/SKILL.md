---
name: cac-and-roas
description: When turning contribution margin into the targets that decide every scale and kill call on a Meta account — break-even ROAS, CAC ceiling, new-customer CAC, target ROAS and payback period. Use when the user asks "what ROAS do I need," "what can I pay for a customer," "break-even ROAS," "new customer CAC," "is 2.4 ROAS good," or "should I scale this." Computed once in section 1 from contribution-margin and consumed by every downstream section.
---
# CAC and ROAS targets

"Is a 2.4 ROAS good?" has no answer without the margin. These formulas turn §1's contribution
margin into the thresholds every other section compares against.

## The formulas

```
break_even_roas = 1 / contribution_margin_%
target_roas = break_even_roas / (1 - target_contribution_after_marketing_%)
cac_ceiling = contribution_margin_per_order
new_customer_cac = total_spend / NEW customers acquired
blended_cac = total_spend / all customers
payback_period = new_customer_cac / contribution_per_order_per_period
```

Worked: at 60% contribution margin, break-even ROAS is 1.67. To keep 20% of revenue as
contribution after marketing, target ROAS is 2.08. A €50 AOV at 60% margin gives a €30 CAC
ceiling on the first order alone.

## New-customer CAC is the number that matters

Blended CAC on an account with a healthy repeat base flatters acquisition, sometimes badly.
Reported ROAS includes existing customers who would have bought anyway — retargeting and
existing-customer campaigns especially.

```
new_customer_cac = total_spend / first-time customers
```

Requires the commerce-platform join: Meta cannot tell you who was already a customer. Where the
join is unavailable, `new_customer_cac` is **null**, not estimated — and every scale
recommendation that depends on it says so.

The gap between blended and new-customer CAC is one of the most useful single numbers in the
audit. A large gap means the account is buying its own customers back and calling it
acquisition.

## Break-even on revenue vs break-even on margin

Two figures, routinely conflated:

- **Break-even revenue ROAS** — the ROAS at which contribution covers ad spend. `1 / margin %`.
- **Break-even margin ROAS** — 1.0 by definition, when conversion value is sent as *profit*
 rather than revenue.

An account that sends profit as conversion value optimises directly toward contribution, which
is better — but its ROAS figures are then not comparable to any benchmark, and everyone reading
the account has to know that. State which the account does.

## LTV: what it changes and what it does not

LTV raises what you *can* pay, not what you *should* pay today.

- **First-order CAC ceiling** — contribution per first order. Acquisition is self-funding below
 it. Requires no assumptions.
- **LTV CAC ceiling** — contribution across the expected customer lifetime, discounted. Requires
 a cohort model, and it is only as good as that model.

Rules that keep this honest:

1. Use **realised** repeat behaviour from cohorts old enough to have repeated. A 90-day-old
 cohort tells you very little about 12-month LTV.
2. Discount future contribution. Cash in 9 months is not cash today, and the difference matters
 at the scale where this argument gets made.
3. **Say which ceiling a recommendation uses.** Scaling to LTV CAC with no cash to bridge the
 payback period is the most common way a well-performing account runs out of money.
4. LTV varies by acquisition source. Customers acquired on a 40% discount frequently repeat less
 than full-price customers; applying a blended LTV to a discount-led campaign overstates its
 ceiling in exactly the case where you would notice least.

## Payback period

```
payback_months = new_customer_cac / contribution_per_customer_per_month
```

This is the constraint that binds in practice. An account can be profitable on an 8-month
payback and still be unable to grow, because growth consumes cash faster than it returns it.
When the user asks how fast they can scale, payback is usually the honest answer rather than
break-even ROAS.

## Applying the targets

| Comparison | Verdict |
|---|---|
| ROAS below break-even | Losing money per order. Kill or fix — subject to the volume floor |
| Between break-even and target | Profitable, below goal. Optimise |
| At or above target | Scale, subject to the incrementality and measurement gates |
| Above target with high modelled share | Not yet a verdict. Reconcile first |

Every one of these is gated: no scale or kill call below the purchase floor in
`learning-phase-and-significance`, none on a `RED` measurement verdict, none on an unreconciled
ROAS, and none on retargeting without incrementality evidence.

## Where targets differ by campaign type

One account-wide target ROAS is a blunt instrument. Prospecting that acquires new customers at
1.8 may be worth more than retargeting at 6.0 that harvests demand — the second number is
larger and the first buys growth.

Set targets by role:

- **Prospecting** — judged on new-customer CAC against the CAC ceiling, not on ROAS
- **Retargeting** — judged on incremental ROAS, and until §26 measures it, judged sceptically
- **Existing customer / winback** — judged on incremental repeat revenue, and separated from
 acquisition entirely so it stops flattering the account average
