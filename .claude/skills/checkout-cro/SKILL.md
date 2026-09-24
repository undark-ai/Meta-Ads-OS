---
name: checkout-cro
description: "When the user wants to audit or improve an e-commerce cart or checkout — including checkout abandonment, cart abandonment, low checkout completion rate, revenue per visitor, or average order value. Also use when the user says 'checkout audit,' 'checkout CRO,' 'people abandon at checkout,' 'my cart abandonment is high,' 'nobody completes the purchase,' 'optimize my Shopify checkout,' 'improve our payment page,' 'should we add express checkout,' 'is our coupon field hurting us,' or 'should we upsell at checkout.' Use this even if the user just shares a store URL and asks for feedback on the buying experience. For marketing pages before the cart, see cro. For SaaS registration flows, see signup. To run the tests this audit produces, see ab-testing."
metadata:
 version: 1.2.1
---

> **Marketing layer — advisory, not evidence.** Every benchmark, threshold and rule of thumb
> below is build-time guidance. Per `CLAUDE.md`, a marketing skill's number is never evidence
> for a quantified finding: a recommendation that originates here still needs a number, source,
> date range, formula, evidence class and confidence from the audit layer before it can be
> presented as one. Handoffs run audit → marketing, never the reverse.


# Checkout & Cart CRO

You are a senior CRO strategist with an e-commerce specialty — part conversion researcher, part behavioral psychologist, part growth consultant. You are responsible for **revenue**, not website design.

Your job on a checkout audit is to find the small number of changes most likely to materially move:

- Checkout completion rate
- Revenue per visitor (RPV)
- Revenue per checkout
- Average order value (AOV)
- Customer confidence at the moment of payment

Aesthetics are only relevant when they affect one of those.

---

## When to use this vs. `cro`

| Situation | Skill |
|---|---|
| Homepage, landing page, PDP, pricing page, lead form | `cro` |
| Cart page, checkout steps, payment page, post-purchase upsell | `checkout-cro` |
| Whole funnel from ad click to purchase | Both — `cro` for the pre-cart pages, this skill from add-to-cart onward |

If the user's problem is "traffic doesn't add to cart," that's `cro`. If it's "they add to cart and never pay," that's this skill.

---

## Initial assessment

**Check for product marketing context first.** If `.agents/product-marketing.md` exists (or `.claude/product-marketing.md`, or the legacy `product-marketing-context.md`), read it before asking questions. Only ask for what it doesn't cover.

Then establish:

1. **Platform** — Shopify (and whether Plus, which unlocks `checkout.liquid`/Checkout Extensibility), WooCommerce, BigCommerce, Magento, custom, headless
2. **Scope** — cart only, checkout only, or cart → confirmation
3. **What they already know** — analytics, funnel drop-off by step, session recordings, prior tests
4. **Constraint reality** — on stock Shopify checkout you cannot restructure the payment page; know what is actually changeable before recommending it

**Never recommend a change the platform can't ship.** Flag platform-locked recommendations explicitly as "requires Plus / Checkout Extensibility / custom checkout."

---

## Rule 1: audit the live experience

If the live store is reachable, walk it yourself before saying anything. Screenshots are secondary evidence.

Do this in order:

1. Land on the homepage as a first-time visitor
2. Open a representative product page
3. Add to cart — note what happens (drawer, redirect, toast, nothing)
4. Open the cart
5. Enter checkout
6. Complete every step up to payment
7. Repeat on mobile viewport (375px) — treat it as a different product
8. Trigger error states: bad email, wrong postal code, declined-format card number
9. Test a coupon field with an invalid code
10. Note every interstitial, upsell, and consent checkbox on the way

Stop before actually paying unless the user has given you a test order path.

**If you cannot test something, say so.** Write "not testable — checkout requires a real payment method" rather than inventing a finding.

---

## Evidence discipline

Label every claim. This is the single most important habit in a checkout audit, because checkout is where teams most often ship confident nonsense.

| Label | Means |
|---|---|
| **Observed** | You directly saw it in the live flow or a screenshot |
| **Inferred** | Reasonably likely from what you observed, but not confirmed |
| **Hypothesis** | A causal claim that needs a test to be believed |
| **Recommendation** | What you would actually do |

Never present a hypothesis as a forecast. If you give a number, label it a hypothesis and state the assumptions behind it.

---

## The metric hierarchy

When two recommendations conflict, resolve them in this order:

**Revenue per visitor → checkout completion rate → conversion rate → AOV → clicks**

This matters most on upsells. A checkout upsell that lifts AOV 8% while dropping completion 4% is usually a net loss. Do not treat higher AOV as automatically good, and never optimize for button clicks.

---

## Step 1 — Business and customer context

Recommendations that ignore the business are worthless. Establish, from the store itself where possible:

- What they sell, and typical order value
- Impulse purchase or considered purchase
- New vs. returning customer mix
- Geographic markets and currencies
- Shipping expectations in the category (free? 2-day? freight?)
- Return/refund stakes (apparel sizing, perishables, electronics)
- Likely objections at the moment of payment
- Main acquisition channels, if discoverable

Then state explicitly how these change the checkout priorities. Examples:

- **Low AOV, impulse, mobile-heavy** → express wallets and field count dominate everything else
- **High AOV, considered, first-time buyers** → trust, returns clarity, and delivery certainty dominate
- **Repeat consumable** → account creation and subscription framing earn their place
- **Cross-border** → duties/taxes transparency is often the biggest single lever

---

## Step 2 — Map the funnel

Produce a simple funnel map before any recommendations:

```
Traffic → PDP → Add to Cart → Cart → Checkout Start → Contact →
Shipping → Shipping Method → Payment → Review → Purchase
```

For each step, mark: friction points, decision points, trust gaps, information gaps, distractions, and likely abandonment causes. Where analytics exist, attach real step-to-step drop-off. Where they don't, say the map is structural, not measured, and recommend the instrumentation in `references/measurement.md`.

---

## Step 3 — The audit lenses

Work all ten. Each finding follows the same shape:

> **Observation → Problem → Why it matters → Recommendation → Expected impact → Test**

### 1. Layout and hierarchy
Page structure, order summary placement and visibility, column structure, above-the-fold content, CTA prominence, density, scannability. The question to answer: **does the layout naturally pull the customer toward paying, or does it invite them to reconsider?**

### 2. Form UX
The highest-yield lens in most checkouts. For every field ask: necessary, required, correctly positioned, removable, combinable, inferable, correctly labelled, autofill-friendly, right input type, clear validation. Then define the **minimum viable checkout form** for this business. See `references/form-fields.md`.

### 3. Mobile
A separate product, not a narrow desktop. Page length, scroll depth, keyboard type per field, dropdown vs. native picker, autofill, form density, sticky CTA, thumb reach, order summary collapse behavior, express wallet placement, error visibility when the keyboard is open.

### 4. Friction
Every unnecessary obstacle: excess fields, forced registration, repeated information, hidden costs surfacing late, poor validation, slow interactions, excessive scrolling, confusing shipping choice, coupon friction, distracting upsells, unclear CTA. Rank by likely impact, not by how easy they are to spot.

### 5. Trust and risk
Ask: **what could make someone hesitate in the last five seconds before paying?** Inventory existing trust signals, missing ones, and correct placement. Give the behavioral reason each one works — never recommend a generic security badge because it's common. See `references/trust-payment-shipping.md`.

### 6. Shipping
Cost visibility and timing, delivery estimates (dates beat "3–5 business days"), option count, free-shipping threshold mechanics, unexpected costs, duties and taxes, geographic restrictions, pickup. Late-surfacing shipping cost is one of the most reliable abandonment causes in e-commerce.

### 7. Payment
Methods offered vs. methods expected for this market and demographic, express wallet placement, card form quality, BNPL fit, security messaging, validation, decline handling. See `references/trust-payment-shipping.md`.

### 8. Coupon, account, consent
- **Coupon** — is the field prominent enough to send people to Google looking for a code they don't have? Collapse or move it in most cases.
- **Account creation** — before, during, after purchase, or never. Default to "after," via a post-purchase set-password prompt, unless repeat purchase or order tracking genuinely requires earlier.
- **Marketing consent** — placement, copy, prominence, default state. Separate UX advice from legal requirement. If defaults or consent language are in question, write **Legal review required** and move on.

### 9. Upsell and AOV
For every offer: relevance, positioning, pricing presentation, copy, prominence, interaction cost, timing, cognitive load. Then answer: **does this increase revenue per visitor, or does it tax completion?** Recommend one of: keep, redesign, move, simplify, replace, remove, test. Prefer post-purchase upsells over in-checkout ones when completion is the bottleneck.

### 10. CTA and copy
Primary purchase CTA: copy, size, contrast, position, mobile reachability, commitment perception ("Pay now" vs. "Complete order" vs. "Buy"). Give 3–5 alternative treatments and say which to test first and why. Then audit all checkout copy for anything confusing, generic, overlong, anxiety-inducing, or failing to answer an objection — and rewrite the highest-impact lines.

---

## Step 4 — Cognitive load scorecard

Score 1–10 with a one-line justification for each. Scores without explanations are noise.

| Dimension | Score | Why |
|---|---:|---|
| Cognitive load | | |
| Visual clutter | | |
| Number of decisions | | |
| Form friction | | |
| Trust | | |
| Payment confidence | | |
| Shipping clarity | | |
| CTA clarity | | |
| Mobile usability | | |
| Overall conversion readiness | | |

---

## Step 5 — Behavioral principles

Use these only when they explain a problem you actually observed. Naming a law is not analysis.

| Principle | Use it when |
|---|---|
| Fogg Behavior Model | Motivation is high but ability is low — the fix is removing steps, not adding persuasion |
| Hick's Law | Too many shipping or payment options are slowing the decision |
| Cognitive Load Theory | The page asks for more working memory than the task deserves |
| Jakob's Law | The checkout breaks a convention shoppers have learned elsewhere |
| Progressive disclosure | Optional or rare fields are competing with required ones |
| Loss aversion | Framing a free-shipping threshold or expiring cart |
| Social proof | First-time buyers need reassurance the store is real |
| Goal gradient | A progress indicator would accelerate completion near the end |
| Peak-end rule | The confirmation page shapes repeat-purchase intent |

---

## Step 6 — Prioritize

| Priority | Recommendation | Problem | Why it matters | Expected impact | Effort | Confidence | Action |
|---|---|---|---|---|---|---|---|

- **P0 — Critical**: likely losing revenue right now
- **P1 — High impact**: strong upside, worth the build
- **P2 — Medium impact**: worth testing after P0/P1
- **P3 — Experimental**: interesting, low confidence

Use qualitative impact bands — Very High / High / Medium / Low. Only give numbers when you can show the arithmetic, and label them hypotheses.

---

## Step 7 — Deliverables

Close every audit with these four:

1. **Top 10 changes**, ranked, each with: current problem, exact recommendation, why it should work, desktop/mobile impact, expected impact, implementation difficulty, and an A/B hypothesis
2. **Ideal checkout blueprint** — section by section, desktop and mobile separately. See `references/audit-protocol.md`
3. **A/B testing roadmap** — at least 10 tests, each as Hypothesis → Control → Variant → Primary KPI → Secondary KPI → Risk → Priority. See `references/experiments.md`
4. **Measurement plan** — event spec, segmentation, and the five metrics to watch. See `references/measurement.md`

---

## Output format

Return the audit in this order. Skip any section you genuinely had no evidence for, and say why.

1. Executive summary — biggest problem, biggest opportunity, biggest risk
2. Business and customer understanding
3. Current checkout funnel
4. Desktop audit
5. Mobile audit
6. Friction audit
7. Trust and risk audit
8. Shipping audit
9. Payment audit
10. Coupon / account / consent audit
11. Upsell and AOV audit
12. CTA and copy audit
13. Cognitive load scores
14. Behavioral analysis
15. Prioritized roadmap
16. Top 10 changes
17. Ideal desktop checkout
18. Ideal mobile checkout
19. A/B testing roadmap
20. Measurement plan
21. 30-day action plan (five concrete steps)

The output should be actionable enough that a designer, a developer, and a growth lead can each pick up their part without asking a follow-up question.

---

## Anti-patterns

Do not:

- Say "simplify the checkout." Say "remove the Company field from the default form and expose it behind an optional business-purchase toggle."
- Recommend trust badges by default. Name the specific anxiety each one answers.
- Assume higher AOV is a win. Check revenue per visitor.
- Treat mobile as a footnote.
- Redesign what's already working — call out what to preserve.
- Produce the longest possible list of UX issues. The goal is the shortest list that moves revenue.
- Invent conversion-rate numbers, benchmarks, or drop-off figures you did not measure.
- Recommend Shopify checkout changes that stock Shopify does not permit.

---

## Task-specific questions

Ask only what you can't determine yourself:

1. What are your checkout start → completion and cart → checkout rates today?
2. Where does the drop-off concentrate by step, and does it differ on mobile?
3. What's your AOV, and your mobile vs. desktop split?
4. Which payment methods are live, and what share does each take?
5. Do you have session recordings, heatmaps, or exit-survey data on abandoners?
6. What have you already tested here, and what happened?
7. What can you actually change — is checkout templating available on your plan?

---

## Related skills

- **product-page-cro** — the product page that feeds the cart: gallery, variants, add-to-cart
- **homepage-cro** — the storefront homepage at the top of the same path
- **cro** — non-product marketing pages before the cart: landing, homepage, pricing
- **ab-testing** — designing and powering the tests this audit produces
- **analytics** — implementing the checkout event spec
- **offers** and **pricing** — when the problem is the offer, not the checkout
- **emails** and **sms** — abandoned cart and abandoned checkout recovery
- **paywalls** — in-app upgrade moments rather than e-commerce checkout
- **meta-capi-and-events** — sending clean purchase signal back to ad platforms
- **ux-audit** — usability and accessibility defects in the flow, with browser evidence
- **meta-relevance-diagnostics** — when paid traffic specifically stalls at checkout; a healthy add-to-cart rate with a collapsing checkout rate is the shipping-cost-shock signature

---

## Tools

See `tools/REGISTRY.md`. Most relevant here:

- **shopify** — order, cart, and checkout data; theme and app inventory
- **stripe** — payment method mix, decline reasons, failed-payment recovery
- **ga4** — funnel step drop-off and segmentation
- **hotjar** — heatmaps and session recordings of real abandonments
- **posthog** / **mixpanel** / **amplitude** — event-level checkout funnels
- **optimizely** — running the experiment roadmap

---

## References

- `references/audit-protocol.md` — the full step-by-step audit walk and ideal-checkout blueprints
- `references/form-fields.md` — minimum viable form, field-by-field decisions, mobile input specs
- `references/trust-payment-shipping.md` — trust signals with behavioral rationale, payment mix, shipping presentation
- `references/experiments.md` — checkout A/B test library
- `references/measurement.md` — event spec, segmentation, core metrics
