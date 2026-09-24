# Checkout Audit Protocol

The full walk. Use this when the user wants a deep audit rather than a quick review. Every phase produces evidence you carry into the findings.

---

## Phase 0 — Setup

Establish before you touch the store:

- Website URL, checkout URL, brand, category, primary market, target customer
- Platform and plan (what is actually editable)
- Any supplied artifacts: screenshots, analytics exports, heatmaps, recordings, prior experiments, reviews, survey responses, product data

Use everything supplied. Where something is missing, name the gap — do not fill it with an assumption presented as fact.

---

## Phase 1 — The live walk

Run this twice: desktop at 1440px, mobile at 375px. Log an observation at every numbered step.

1. **Homepage** — what does a first-time visitor learn about legitimacy, shipping, and returns before they ever reach a product?
2. **Product page** — price clarity, shipping/delivery promise, returns visibility, stock status, variant selection, add-to-cart affordance
3. **Add to cart** — drawer, redirect, toast, or silence? Is the next step obvious?
4. **Cart** — editability, subtotal composition, shipping estimate, taxes, threshold messaging, competing CTAs, continue-shopping escape hatches
5. **Checkout entry** — is there an express wallet row above the form? Is there a guest path? Is the header still full site navigation (a leak)?
6. **Contact step** — field count, autofill behavior, newsletter checkbox and its default
7. **Shipping address** — field count and order, country/state control types, postal-code lookup, apartment field handling, address autocomplete
8. **Shipping method** — number of options, cost presentation, delivery dates vs. vague ranges, default selection
9. **Payment** — express options, card form quality, BNPL, billing-address defaulting, security messaging
10. **Review** — what's summarized, what's editable, whether the total is finally unambiguous
11. **Errors** — bad email, invalid postal code, malformed card, invalid coupon. Where does the message appear? Is the field preserved? Is it visible with the keyboard open on mobile?
12. **Interstitials** — every upsell, consent modal, or offer between cart and confirmation

Stop before completing payment unless the user has provided a test-order path.

Record for each observation: what you saw, on which viewport, and at which step. A finding without a location is not usable.

---

## Phase 2 — Business context

Answer these before recommending anything, from the store itself where possible:

| Question | Why it changes the audit |
|---|---|
| Typical order value | Low AOV cannot support high-friction checkout; high AOV can support more reassurance |
| Impulse or considered | Impulse rewards express wallets; considered rewards trust and specificity |
| New vs. returning mix | New-heavy checkouts are trust problems; returning-heavy ones are speed problems |
| Purchase frequency | Frequent repeat justifies accounts and subscriptions |
| Geographic markets | Drives payment mix, duties transparency, currency display |
| Shipping norms in category | Sets the free-shipping expectation you're measured against |
| Return stakes | Apparel and electronics need returns clarity at the payment step |
| Likely objections | Each one should be answered somewhere in the flow |
| Acquisition channels | Paid social traffic is colder and more mobile than email traffic |

State the implications explicitly. "Mobile-heavy paid social traffic at a £28 AOV means field count and express wallets outrank everything else in this audit" is analysis. Listing the facts is not.

---

## Phase 3 — Funnel map

```
Traffic → PDP → Add to Cart → Cart → Checkout Start →
Contact → Shipping → Shipping Method → Payment → Review → Purchase
```

For each transition, record:

- Observed friction
- Decisions demanded of the customer
- Trust gaps
- Information gaps (something they need to know and can't find)
- Distractions and exits
- Measured drop-off, if analytics exist

Mark which transitions you could measure and which are structural inference only.

---

## Phase 4 — Lens sweep

Work the ten lenses in `SKILL.md`. For each finding:

> **Observation → Problem → Why it matters → Recommendation → Expected impact → Test**

Two habits that keep this useful:

- Group findings by lens, then rank within lens. Do not interleave a font-size nit with a hidden-shipping-cost problem.
- Call out what's already working and should be preserved. A redesign that discards a working express-wallet row is a net loss.

---

## Phase 5 — Ideal desktop checkout blueprint

Write it section by section. For each section state: what should appear, what should disappear, what should move, what should be simplified, what should be emphasized.

A defensible default structure for a single-page or accordion checkout:

| # | Section | What belongs here |
|---|---|---|
| 1 | Header | Logo, a link back to cart, secure-checkout indicator. No site navigation, no search, no promo bar |
| 2 | Express payment row | Wallets first, above the form, visually separated with an "or" divider |
| 3 | Contact | Email only. Phone only if delivery genuinely requires it, with a reason shown |
| 4 | Shipping address | Country first, then address with autocomplete, minimum viable field set |
| 5 | Delivery options | 2–3 options maximum, real dates, sensible default preselected |
| 6 | Payment | Card form, BNPL if it fits the AOV, billing defaulted to shipping |
| 7 | Order summary | Always visible in a sticky column. Line items, shipping, tax, discount, final total |
| 8 | Trust and reassurance | Returns window, support contact, secure-payment statement — adjacent to the pay button, not in the footer |
| 9 | Cross-sell | Only if it doesn't compete with the CTA. Post-purchase is usually better |
| 10 | Terms | Linked, concise, not a blocking checkbox unless legally required |
| 11 | Purchase CTA | One primary action, unambiguous copy, total repeated on or beside it |

---

## Phase 6 — Ideal mobile checkout blueprint

Write this separately. It is not the desktop list reflowed.

| # | Section | Mobile-specific requirement |
|---|---|---|
| 1 | Header | Minimal. Reclaim vertical space |
| 2 | Express wallets | Apple Pay / Google Pay / Shop Pay first, thumb-reachable, before any typing is requested |
| 3 | Order summary | Collapsed by default with the total visible; expandable. Never force a scroll past the whole itemization |
| 4 | Form | One field per row. Correct `inputmode` and `autocomplete` on every field. Native pickers for country/state |
| 5 | Delivery options | Radio cards large enough to tap, dates not ranges |
| 6 | Payment | Numeric keypad for card number, card scanning enabled, no manual re-entry of billing address by default |
| 7 | Errors | Inline, above the field, and visible while the keyboard is open |
| 8 | Trust | Compressed to one line near the CTA — returns window and secure payment |
| 9 | Sticky CTA | Persistent pay button showing the total, above the safe-area inset |

Mobile-specific failures to look for: dropdowns where a native picker belongs, wrong keyboard type, autofill broken by custom inputs, tap targets under 44×44px, error messages hidden behind the keyboard, a total that requires scrolling to find, and a CTA that sits under the browser chrome.

---

## Phase 7 — Competitive benchmark

Where you can reach them, review 3–5 comparable stores and 2–3 best-in-class e-commerce checkouts.

Compare: checkout structure, form length, payment options, shipping transparency, trust treatment, mobile UX, upsell approach, CTA copy, coupon treatment, account requirement.

Look for **patterns repeated across successful stores**, not individual choices. One competitor's decision is noise; a pattern across five is a convention worth respecting or a deliberate one to break. Do not copy a competitor because they're bigger.

---

## Phase 8 — Synthesis

Produce, in order:

1. Cognitive load scorecard with justifications
2. Prioritized roadmap (P0–P3)
3. Top 10 changes, ranked, each with an A/B hypothesis
4. Ideal desktop and mobile blueprints
5. A/B testing roadmap — see `experiments.md`
6. Measurement plan — see `measurement.md`
7. 30-day action plan: five concrete steps, each with an owner type and a success signal

The executive summary is written last and goes first.
