# Trust, Payment, and Shipping

The three things a customer is actually deciding about in the last ten seconds before paying: *is this store real, can I pay the way I want, and do I know what I'm getting and when.*

---

## Trust signals

### The rule

Never recommend a trust signal because it's common. Name the specific anxiety it answers and where it must appear to answer it. A security badge in the footer answers nothing, because nobody scrolls to the footer while holding a credit card.

### Anxiety → signal map

| Customer anxiety | Signal that answers it | Where it belongs |
|---|---|---|
| "Is this a real business?" | Physical address, phone or chat, company registration, real About content | Footer plus a compressed line in checkout |
| "Will my card details be stolen?" | Visible padlock/HTTPS, "Secure checkout" wording, recognizable processor marks (Stripe, Shop Pay, PayPal) | Adjacent to the card fields |
| "What if it doesn't fit / doesn't work?" | Returns window stated in plain language, free-returns statement if true | Beside the pay button — this is where the doubt peaks |
| "When will it actually arrive?" | Named delivery dates, not "3–5 business days" | Shipping method step, repeated in the summary |
| "Is the product genuine?" | Authorized-retailer statement, warranty, brand authorization | PDP and order summary |
| "Is anyone else buying this?" | Review count and score, recent-purchase count if honestly sourced | PDP, and a compressed form in the cart |
| "What if I need help?" | Support hours, response time, contact route | Checkout header or near the CTA |
| "Am I being charged something hidden?" | Full itemized total including tax, shipping, and duties before the pay button | Order summary, permanently visible |

### Placement rules

- Trust content that matters goes **within thumb-and-eye distance of the pay button**, not in a footer or a separate policies page
- Compress it: one line each for returns window, secure payment, and support beats a badge wall
- Real, specific claims outperform generic ones. "30-day free returns, no questions" beats "Satisfaction guaranteed"
- Never fabricate scarcity, live-viewer counts, or purchase tickers. If a count is shown, it must be current and real. Fake urgency is a trust liability, and increasingly a regulatory one

### What to remove

- Badge clusters of five or more logos — they read as compensating for something
- Expired or unrecognizable certification marks
- Generic stock "SSL Secured" graphics that aren't tied to a real certificate
- Anything that competes visually with the purchase CTA

---

## Payment

### Method coverage

Coverage is a market question, not a preference question. The right set depends on geography and demographic, not on what the developer finds easiest.

| Market / segment | Expected beyond cards |
|---|---|
| US | Apple Pay, Google Pay, PayPal, Shop Pay; BNPL at AOV above roughly $75 |
| UK | Apple Pay, Google Pay, PayPal, Klarna / Clearpay |
| EU (DE, AT, NL) | SEPA direct debit, iDEAL (NL), Klarna, invoice/Rechnung in DE — cards alone underperform badly here |
| Nordics | Klarna, Swish (SE), MobilePay (DK) |
| LATAM | Pix (BR), OXXO (MX), installments (widely expected) |
| APAC | Alipay, WeChat Pay, GrabPay, PayNow depending on country |
| Mobile-heavy any market | Wallets are not optional — they remove the entire typing task |
| High AOV / considered | BNPL and installments shift the affordability objection |

**Express wallets are the single highest-leverage payment change on mobile.** They eliminate the form, the address entry, and the card entry in one tap. If they exist but sit below the form, moving them above it is a cheap, high-confidence change.

### Card form quality

- Card number: `type="text"`, `inputmode="numeric"`, `autocomplete="cc-number"`
- Auto-format with spaces as they type; auto-advance between expiry and CVC
- Detect and display card brand from the BIN rather than asking the customer to pick it
- Never require a separate card-type selector
- Explain CVC location if you ask for it
- Support card scanning on mobile where the platform allows it

### Decline and error handling

Declines are a revenue leak most audits skip entirely. Check:

- Does a decline preserve the entered data, or reset the form?
- Is the message actionable ("Your bank declined this card — try another card or use PayPal") or opaque ("Payment failed")?
- Is an alternative payment method offered immediately at the point of failure?
- Are 3DS / SCA challenges handled inline, or do they break the flow in a popup that mobile browsers block?
- Are soft declines retried, and are failed payments followed up by email?

Pull actual decline reasons from Stripe or the processor where available. Decline-code distribution frequently reveals a fixable configuration problem rather than a UX one.

### Separate confidence levels

Split payment recommendations explicitly:

- **High confidence** — add Apple Pay and Google Pay above the form on a mobile-heavy store; fix a card field using `type="number"`; make a decline message actionable
- **Hypothesis, needs testing** — whether adding BNPL lifts revenue per visitor net of fees; whether reordering wallet options changes mix; whether removing a low-share method reduces choice paralysis

---

## Shipping

Late-surfacing shipping cost is one of the most reliable abandonment causes in e-commerce. Most shipping findings are about *when* information appears, not what it costs.

### What to audit

| Item | The failure to look for |
|---|---|
| Cost visibility | First appearing at the payment step, after the customer has invested effort |
| Delivery estimates | "3–5 business days" instead of "Arrives Tue 26 Aug" |
| Option count | Five options where two would do — Hick's Law applies |
| Default selection | Most expensive option preselected, or nothing preselected |
| Free-shipping threshold | Not surfaced, or surfaced without the gap to it ("Add $12 for free shipping") |
| Unexpected costs | Handling fees, insurance opt-ins defaulted on, surcharges appearing at review |
| Duties and taxes | Cross-border orders where DDU means a surprise bill on delivery — state it before payment |
| Geographic restrictions | Discovered only after the address is entered |
| Pickup / local delivery | Available operationally but not offered in checkout |

### Recommendations that usually hold

- Surface a shipping cost or a free-shipping statement **on the PDP and in the cart**, before checkout starts
- Show real dates, computed from cutoff times and carrier transit, not vague ranges
- Cap options at three; name them by outcome ("Arrives Tue 26 Aug — free") rather than by carrier service code
- Preselect the option most customers choose, not the most expensive
- Show threshold progress in the cart with the exact remaining amount, and make the suggestion actionable with a relevant add-on
- State duties handling explicitly for cross-border: DDP (prepaid) or DDU (customer pays on delivery)
- Never default-check paid shipping insurance or protection. It is a short-term margin gain and a long-term trust cost, and in several jurisdictions a compliance problem

### Free shipping thresholds

A threshold is a loss-aversion mechanic and it works, but only if:

- The gap to the threshold is visible with the exact amount remaining
- The suggested add-on is genuinely relevant and priced near the gap
- The threshold sits above AOV but within reach — roughly 15–30% above typical order value. Too high reads as unattainable and does nothing

Model the margin before recommending a threshold change. A threshold that lifts AOV 10% while giving away shipping on 40% more orders can be net negative.

---

## Upsell and cross-sell at checkout

The test for any checkout offer is **revenue per visitor, net of its effect on completion** — never AOV alone.

| Placement | Risk to completion | Best used for |
|---|---|---|
| Cart page | Low | Relevant accessories, threshold nudges |
| In-checkout, inside the form flow | **High** | Rarely worth it — it interrupts a committed customer |
| Order summary sidebar | Low–medium | One small, relevant add-on |
| Post-purchase (confirmation page, one-click) | Near zero | The best place for almost every upsell — the order is already banked |

Default recommendation when completion is the bottleneck: move in-checkout upsells to post-purchase, and keep the checkout itself single-purpose.

For each existing offer, decide: **keep, redesign, move, simplify, replace, remove, or test** — and say which, with the reason.
