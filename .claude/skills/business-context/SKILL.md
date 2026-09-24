---
name: business-context
description: When establishing the commercial frame an audit judges everything against — the one primary goal, the product and customer context, hero products, promotional calendar, seasonality and geographic priorities. Use at the start of every audit, and whenever a recommendation needs to know what the account is actually optimising for. Reads .agents/product-marketing.md where it exists; never promotes it to evidence.
---
# Business context

Section 1 runs first because every later section needs an answer to one question: **what is this
account for?**

Without it, an audit reports that ROAS fell and cannot say whether that matters. An account
deliberately trading ROAS for new-customer volume is executing a strategy; the same numbers with
no strategy behind them are a problem.

## Name one primary goal

Not a list. One:

| Goal | What the audit then optimises toward | What it will tolerate |
|---|---|---|
| **Revenue** | Top-line growth | Lower margin, higher CAC |
| **Profit** | Contribution after marketing | Slower growth |
| **New customers** | New-customer volume at a CAC ceiling | Low blended ROAS, thin first-order margin |
| **CAC** | Cost per new customer | Volume ceiling |
| **LTV** | Cohort value, retention-weighted acquisition | Long payback |
| **Incremental revenue** | Measured lift over baseline | Lower reported ROAS |

These conflict. An account cannot maximise new customers and CAC simultaneously, and an audit
that tries to serve every goal produces recommendations that cancel each other.

Where the user names several, ask which one wins when they conflict. That answer is the primary
goal, and it goes at the top of the executive page.

## Reading the context document

`.agents/product-marketing.md` carries product, ICP, positioning and offer context. Read it
first; do not interrogate the user for basics it already answers.

**It is context, never evidence.** A claim in it about who the customer is does not support a
quantified finding. Where the document and the measured data disagree, that disagreement is
itself one of §1's more valuable findings: the account is reaching someone other than who it
thinks it is, and the creative is probably written for the wrong person.

If it is missing or older than 90 days, `audit-preflight` offers to build or refresh it. It never
blocks the run.

## What §1 must establish

From the commerce platform where possible, from the user where not, on a labelled assumption
otherwise:

- AOV, and how it varies by product and by acquisition source
- Gross margin, contribution margin (`contribution-margin`)
- CAC target, break-even CAC, break-even ROAS (`cac-and-roas`)
- LTV and repeat behaviour, from cohorts old enough to have repeated
- New vs returning customer economics
- Best-selling products, highest-margin products, **hero products** — and where those three
 disagree, which is common and important
- Promotional calendar — realised discounting, not intended
- Seasonality, from the account's own history and prior-year comparison
- Geographic priorities, and where shipping economics make a market unprofitable

## Where the three product lists disagree

Bestsellers, highest-margin products and hero products are usually not the same set, and the gap
is one of the most reliable sources of upside in a D2C audit.

The common pattern: spend concentrated on a bestseller with below-average contribution, while a
higher-margin product gets almost nothing. ROAS-based reporting cannot surface this — the
bestseller's ROAS looks fine — and it only becomes visible when margin is joined per SKU (§22).

## Seasonality before diagnosis

Check the prior-year comparison before calling a movement a finding. Q4 CPMs rising is not a
finding. A decline that matches last year's shape at the same point is the market, not the
account.

Conversely, an account that is *flat* year over year in a month it usually grows has a problem
that a month-over-month view will never show.

## Output

The commercial frame the whole audit is judged against: the one primary goal, the canonical
economics every other section consumes, the product priorities, and the named places where the
client's declared context and the measured data disagree.
