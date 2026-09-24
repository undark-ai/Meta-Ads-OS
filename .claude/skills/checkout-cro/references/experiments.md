# Checkout Experiment Library

Test ideas for cart and checkout, grouped by lever. Each is written to be lifted straight into a test brief.

**Format:** Hypothesis → Control → Variant → Primary KPI → Secondary KPI → Risk → Priority

**Primary KPI discipline:** checkout tests should be judged on **revenue per visitor** or **checkout completion rate**, not on clicks or step-advance rate. An upsell test judged on AOV alone will mislead you. See `../../ab-testing/SKILL.md` for powering these properly — checkout traffic is usually a fraction of site traffic, so runtimes are longer than teams expect.

---

## Express payment and payment mix

**1. Wallets above the form**
- Hypothesis: Placing express wallets above the contact form removes the typing task for mobile shoppers and lifts completion
- Control: Wallets below the card form, or absent
- Variant: Apple Pay / Google Pay / Shop Pay row directly above the email field, with an "or pay by card" divider
- Primary: Checkout completion rate (mobile) · Secondary: Revenue per visitor
- Risk: Wallet orders carry less marketing consent and less address-quality data
- Priority: P0 on mobile-heavy stores

**2. Add BNPL**
- Hypothesis: At this AOV, installments remove the affordability objection and increase completion enough to cover the provider fee
- Control: Cards and wallets only
- Variant: Klarna / Afterpay / Affirm offered at payment, with the per-instalment amount shown on the PDP
- Primary: Revenue per visitor net of fees · Secondary: AOV, completion rate
- Risk: Fee drag; possible cannibalization of full-price card orders
- Priority: P1 above roughly $75 AOV

**3. Remove a low-share payment method**
- Hypothesis: A payment option taking under 2% of orders adds choice cost without adding sales
- Control: All current methods
- Variant: Lowest-share method removed
- Primary: Checkout completion rate · Secondary: Payment step time
- Risk: The method may be disproportionately used by a high-value segment — segment before removing
- Priority: P2

---

## Form and friction

**4. Reduce to the minimum viable field set**
- Hypothesis: Removing Company and Phone from the default form, and combining first/last name, lifts completion
- Control: Current field set
- Variant: Minimum viable set; Company behind a business-order toggle, Phone optional with a stated reason
- Primary: Checkout completion rate · Secondary: Time to complete, field-level error rate
- Risk: Carrier or fulfilment dependency on phone — verify operationally first
- Priority: P0 where the form exceeds the minimum

**5. Address autocomplete**
- Hypothesis: Autocomplete removes the highest-typing-cost block on mobile and reduces address errors
- Control: Manual address entry
- Variant: Address autocomplete on line 1, auto-filling city, state, and postal code
- Primary: Checkout completion rate (mobile) · Secondary: Failed-delivery rate, address correction volume
- Risk: A custom widget that breaks browser autofill can be net negative — verify autofill still works
- Priority: P0 on mobile-heavy stores

**6. Guest checkout as the default path**
- Hypothesis: Forced or prominent registration blocks first-time buyers; a guest path lifts completion
- Control: Account creation required or visually dominant
- Variant: Guest checkout as the default; login as a secondary link; account creation offered on the confirmation page
- Primary: Checkout completion rate · Secondary: Account creation rate, repeat purchase rate at 90 days
- Risk: Lower account creation short-term — measure post-purchase capture to see if it offsets
- Priority: P0 where registration is forced

**7. Accordion vs. multi-step**
- Hypothesis: Consolidating a four-page checkout into an accordion reduces perceived length and lifts completion
- Control: Multi-page checkout
- Variant: Single-page accordion with a visible progress indicator
- Primary: Checkout completion rate · Secondary: Step-level drop-off
- Risk: Longer perceived page on mobile; needs careful section collapse
- Priority: P1

**8. Validation timing and message quality**
- Hypothesis: On-blur validation with fix-oriented messages reduces form abandonment versus on-submit or per-keystroke validation
- Control: Current validation behavior
- Variant: Validate on blur; inline, adjacent, actionable messages; field contents preserved on error
- Primary: Form completion rate · Secondary: Error rate per field, repeat-error rate
- Risk: Low
- Priority: P1

---

## Shipping and cost transparency

**9. Shipping cost surfaced before checkout**
- Hypothesis: Revealing shipping cost at the PDP or cart, rather than at payment, removes the late-surprise abandonment
- Control: Cost first shown at the shipping step
- Variant: Estimated cost or free-shipping statement on PDP and cart
- Primary: Checkout completion rate · Secondary: Add-to-cart rate, revenue per visitor
- Risk: Add-to-cart may fall if shipping is expensive — watch RPV, not ATC, and accept the trade if RPV rises
- Priority: P0 where cost appears late

**10. Named delivery dates**
- Hypothesis: "Arrives Tue 26 Aug" creates more delivery certainty than "3–5 business days" and lifts completion
- Control: Vague transit ranges
- Variant: Computed calendar dates from cutoff and carrier transit
- Primary: Checkout completion rate · Secondary: Expedited-shipping selection rate, WISMO support tickets
- Risk: Requires accurate cutoff logic; a missed promise costs more than a vague one
- Priority: P1

**11. Reduce shipping options to three**
- Hypothesis: Fewer, outcome-named options reduce decision cost at the step with the highest drop-off
- Control: Five or more carrier-named options
- Variant: Three options named by outcome and date, with the most-chosen preselected
- Primary: Shipping step completion · Secondary: Shipping revenue per order
- Risk: Loss of high-margin expedited selections — watch shipping revenue
- Priority: P1

**12. Free-shipping threshold progress in cart**
- Hypothesis: Showing the exact remaining amount plus a relevant add-on lifts AOV without hurting completion
- Control: Threshold stated statically or not at all
- Variant: "Add $12 for free shipping" with one relevant product suggestion priced near the gap
- Primary: Revenue per visitor · Secondary: AOV, completion rate, shipping margin
- Risk: Margin loss if the threshold is set below AOV
- Priority: P1

---

## Trust and reassurance

**13. Returns clarity beside the pay button**
- Hypothesis: The returns objection peaks immediately before payment; answering it there lifts completion
- Control: Returns policy linked in the footer only
- Variant: One line stating the returns window and whether returns are free, directly beside the CTA
- Primary: Checkout completion rate · Secondary: Return rate (watch for an increase)
- Risk: A prominent returns promise can raise return rate — measure net revenue, not gross
- Priority: P1

**14. Consolidate trust badges**
- Hypothesis: A badge cluster adds visual noise and competes with the CTA; one specific line outperforms it
- Control: Five or more badge logos
- Variant: One line — secure payment statement plus recognizable processor mark
- Primary: Checkout completion rate · Secondary: Payment step time
- Risk: Low; occasionally negative in categories where certification genuinely matters
- Priority: P2

**15. Persistent order summary**
- Hypothesis: A permanently visible itemized total removes hidden-cost anxiety and lifts completion
- Control: Summary collapsed or on a separate step
- Variant: Sticky summary column on desktop; collapsed-with-total-visible on mobile
- Primary: Checkout completion rate · Secondary: Summary expand rate
- Risk: Vertical space cost on mobile
- Priority: P1

---

## Coupon, upsell, CTA

**16. Collapse the coupon field**
- Hypothesis: A prominent coupon field prompts code-hunting and exit; collapsing it retains customers who have no code
- Control: Open coupon input in the form flow
- Variant: "Have a discount code?" text link inside the order summary
- Primary: Revenue per visitor · Secondary: Completion rate, coupon-open rate, discount rate
- Risk: Genuine code holders may struggle to find it — watch coupon application rate
- Priority: P1

**17. Move in-checkout upsell to post-purchase**
- Hypothesis: An upsell inside the checkout flow taxes completion more than it adds in AOV; post-purchase captures the same margin at near-zero risk
- Control: Upsell shown between checkout steps
- Variant: Checkout kept single-purpose; one-click upsell on the confirmation page
- Primary: Revenue per visitor · Secondary: Completion rate, upsell take rate
- Risk: Lower absolute upsell take rate post-purchase — the completion gain usually outweighs it
- Priority: P0 where an upsell interrupts the form flow

**18. CTA copy**
- Hypothesis: Copy naming the outcome rather than the transaction reduces commitment anxiety
- Control: "Pay now"
- Variant: Test "Complete order," "Place order," "Buy now — $84.00"
- Primary: Checkout completion rate · Secondary: Payment error rate
- Risk: Low. Do not test copy alone if a structural P0 is unfixed
- Priority: P2

**19. Sticky mobile CTA with total**
- Hypothesis: A persistent pay button showing the total removes the scroll-to-find-the-button cost on long mobile checkouts
- Control: CTA at natural page position
- Variant: Sticky bottom bar with total and pay button, above the safe-area inset
- Primary: Checkout completion rate (mobile) · Secondary: Scroll depth to purchase
- Risk: Obscures content on short viewports; can trigger accidental taps
- Priority: P1

**20. Remove site navigation from checkout**
- Hypothesis: Full navigation in the checkout header is a leak; a minimal header keeps committed customers in the flow
- Control: Standard site header with nav, search, and promo bar
- Variant: Logo, back-to-cart link, secure-checkout indicator only
- Primary: Checkout completion rate · Secondary: Exit rate from checkout
- Risk: Low
- Priority: P1

---

## Test hygiene for checkout

- **Power first.** Checkout traffic is a subset of site traffic. Run the sample-size math before committing — see `../../ab-testing/references/sample-size-guide.md`
- **Segment desktop and mobile.** Many checkout changes are positive on one and negative on the other. A blended result can hide both
- **Watch the guardrails.** Return rate, refund rate, shipping margin, payment fees, and support ticket volume. A completion win that raises returns 6 points is not a win
- **Never test two structural changes at once** in a low-traffic checkout. You will not be able to attribute the result
- **Fix P0 defects rather than testing them.** A card field using `type="number"`, an error message hidden behind the keyboard, or a broken autofill is a bug. Ship the fix; don't spend runtime proving the bug is bad
