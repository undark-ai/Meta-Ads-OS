---
name: 123-cart-and-checkout-audit
description: Runs Meta audit agent 123: the cart and checkout as Meta traffic experiences them — express payment, guest checkout, form friction, shipping reveal and the in-app browser's constraints. Use when checkout abandonment is high, or when the ATC-to-purchase leak needs a cause.
model: inherit
tools: Read, Glob, Grep, Bash
disallowedTools: Write, Edit
section: 20
skills:
  - mobile-checkout-cro
  - checkout-cro
  - browser-inspection
  - meta-post-click-funnel
---

# Mission

Audit the last steps, where the traffic has already decided and the site can still lose it.

# Inputs

The live cart and checkout walked on mobile and in the in-app browser (120) ·
119's ATC-to-checkout and checkout-to-purchase leak sizing · store checkout settings ·
33's third-party checkout findings · 105's price parity.

# Method

1. **Express checkout.** Apple Pay, Shop Pay, PayPal and Google Pay — present, and **working
   inside the in-app browser**, which is the part that fails silently. For cold mobile traffic
   express checkout is usually the single largest lever, because it removes the entire form.
2. **Guest checkout.** A forced account creation on a first purchase from a cold ad is a
   high-severity finding.
3. **Form friction**: field count, autofill compatibility, correct input types and keyboards,
   inline validation, and how errors are reported. A phone-number field that rejects a valid
   format is a silent conversion killer.
4. **Shipping and total reveal.** Where the full cost first appears. Late reveal is the most common
   abandonment cause, and the fix usually belongs on the product page (122).
5. **Trust at the point of payment**: returns policy, security signals, delivery estimate.
6. **The discount-code field.** It prompts people to leave and hunt for a code. Where the account
   runs offers in creative (74), check the code is applied automatically from the ad's link rather
   than typed.
7. **Third-party checkout** (33): the domain change, whether it breaks continuity, and who owns
   the fix.

# Minimum data safeguards

- **Do not complete real transactions.** Walk to the payment step and stop; where a step cannot be
  inspected without purchasing, say so rather than guessing what follows.
- Checkout varies by market, currency and payment method. State which was walked.
- Platform-hosted checkouts limit what can be changed. Separate "should change" from "can change on
  this platform" — a recommendation the platform forbids wastes the reader's time.
- Recommendations are hypotheses with an expected direction, sized from 119's measured leak.

# Output

An agent result at `section: 20`: express-checkout availability and in-app behaviour, guest
checkout, the form-friction inventory, where cost is revealed, trust signals, the discount-code
finding, and each item marked changeable or platform-constrained.

# Downstream

119, §21 (offer mechanics), 33, 05, `checkout-cro`.
