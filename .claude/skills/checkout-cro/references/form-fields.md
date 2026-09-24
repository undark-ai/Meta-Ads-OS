# Checkout Form Fields

Form UX is the highest-yield lens in most checkouts. Every field is a tax. This file is the decision framework for which taxes are worth paying.

---

## The minimum viable checkout form

The shortest form that can legally and operationally fulfil a physical order to a single address:

1. Email
2. Country / region
3. Full name
4. Address line 1
5. City
6. State / province (where the country requires it)
7. Postal code
8. Payment details

That's it. Everything else must justify itself. For a digital product the list collapses to email and payment.

Before recommending a field set, ask what the fulfilment operation genuinely needs — not what the form currently has.

---

## Field-by-field decisions

| Field | Default position | Notes |
|---|---|---|
| **Email** | First, alone | Required. Type `email`, `autocomplete="email"`, `inputmode="email"`. This is the abandoned-checkout recovery hook — capture it before anything that can fail |
| **First / last name** | Combine into one "Full name" field unless fulfilment or a payment processor needs them split | Two fields where one would do is a common, cheap win |
| **Phone** | Optional by default | Only required when the carrier genuinely needs it (freight, same-day, some international). If required, say why inline: "For delivery updates only." Use `inputmode="tel"` |
| **Company** | Remove from the default form | Expose behind an optional "This is a business order" toggle. B2B buyers will find it; consumers shouldn't have to skip it |
| **Country** | First field of the address block | It determines the shape of everything below it. Native `<select>` on mobile. Default to the store's primary market, or geolocate |
| **Address line 1** | After country | Use address autocomplete where available. It is one of the highest-ROI checkout changes on mobile |
| **Apartment / unit** | Optional, secondary, visually subordinate | Never required. Label it "Apartment, suite, etc. (optional)" |
| **City** | Auto-fill from postal code where the country supports it | Manual re-entry of derivable data is pure friction |
| **State / province** | Only render for countries that use it | A US-format state dropdown shown to a UK customer is a credibility hit |
| **Postal code** | Auto-derive city/state where possible | `inputmode` should match the format — numeric for US, text for UK/CA. Validate format, not existence, client-side |
| **Billing address** | Default to "same as shipping," collapsed | Only expand when the customer unchecks it |
| **Account password** | Remove from checkout | Offer account creation on the confirmation page instead — the order is already banked |
| **Marketing consent** | One line, honest copy, correct default for the jurisdiction | See consent notes below |
| **Order notes / gift message** | Collapsed link, not an open textarea | An empty textarea reads as an obligation |

---

## The five questions for any field

For each field, in order:

1. **Can it be removed?** Does anyone downstream actually use this data?
2. **Can it be inferred?** Postal code → city/state. IP → country. Card BIN → card type.
3. **Can it be combined?** Full name instead of first + last.
4. **Can it be deferred?** Account password, gift message, phone → post-purchase.
5. **Can it be made optional?** And if it's optional, is it visually subordinate to the required fields?

Only after all five fail does the field earn its place — and then optimize its label, input type, and validation.

---

## Input attributes that matter

Most "mobile checkout friction" is a missing HTML attribute, not a design problem. Check every field for:

| Field | `type` | `inputmode` | `autocomplete` |
|---|---|---|---|
| Email | `email` | `email` | `email` |
| Full name | `text` | — | `name` |
| Address 1 | `text` | — | `address-line1` |
| Address 2 | `text` | — | `address-line2` |
| City | `text` | — | `address-level2` |
| State | `text` / select | — | `address-level1` |
| Postal code | `text` | `numeric` (US) / `text` (UK, CA) | `postal-code` |
| Country | select | — | `country-name` |
| Phone | `tel` | `tel` | `tel` |
| Card number | `text` | `numeric` | `cc-number` |
| Card expiry | `text` | `numeric` | `cc-exp` |
| Card CVC | `text` | `numeric` | `cc-csc` |

Two failures worth checking specifically:

- **`type="number"` on a postal code or card field.** It triggers spinner arrows, breaks leading zeros, and rejects valid international formats. Use `type="text"` with `inputmode="numeric"`.
- **Custom-built inputs that break browser and password-manager autofill.** A fancy address widget that defeats autofill costs more than it earns.

---

## Labels, placeholders, validation

**Labels:** always visible. Placeholder-only labels disappear the moment someone types, forcing them to delete text to remember what a field wanted. Floating labels are acceptable; placeholder-as-label is not.

**Placeholders:** use for format hints only ("Apt 4B"), never to carry the field's name.

**Validation:**
- Validate on blur, not on every keystroke — mid-typing errors read as being scolded
- Show the error inline, adjacent to the field, and describe the fix: "Enter a 5-digit ZIP code," not "Invalid input"
- Never clear the field on error
- Never reset the whole form on a failed submit
- On mobile, the error must be visible with the keyboard open — an error above the fold of a covered viewport is invisible
- Show a summary at the top only when multiple fields failed, and link each item to its field

---

## One page, accordion, or multi-step

There is no universal winner. Choose on the specifics:

| Pattern | Fits when |
|---|---|
| **Single page** | Short form, high-intent traffic, returning-customer heavy |
| **Accordion** | Medium form, needs a sense of progress, keeps context visible. The safest default |
| **Multi-step** | Long form, complex shipping or configuration, mobile-heavy. Requires a real progress indicator |

Whichever you recommend, non-negotiables:

- A visible progress indicator on anything multi-step (goal gradient)
- Back navigation that preserves entered data
- Never re-ask for something already given
- The running total must be reachable at every step

If the platform can't switch patterns, say so and optimize within the one it has.

---

## Guest checkout and account creation

Forced registration before purchase is one of the most reliable abandonment causes in e-commerce. Default recommendation:

1. Guest checkout as the visible default path
2. Login offered as a small, secondary link for returning customers — not a wall
3. Account creation offered on the confirmation page, pre-filled, one click to set a password

Deviate only when repeat purchase, subscription management, or order-tracking support genuinely depends on an account existing before payment — and then say what you're trading for it.

---

## Coupon field

The coupon field creates a specific behavior: a customer who has no code sees the field, concludes a discount exists, and leaves to find one. Some come back. Some buy from a coupon site's affiliate link instead.

Default recommendation:

- Collapse it behind a text link labelled "Have a discount code?"
- Place it in the order summary, not the primary form flow
- Never make it the most visually prominent element on the page
- Show applied discounts clearly in the summary once used

Exception: if the store's acquisition strategy depends on codes (influencer, podcast, direct mail), a discoverable field is correct — but still not prominent.

Always frame the recommendation as testable: coupon-field prominence is a clean A/B test with revenue per visitor as the primary KPI.

---

## Marketing consent

- One line, plainly worded, near the email field or after the address block
- Never pre-checked in jurisdictions requiring explicit opt-in
- Never bundled with terms acceptance
- Never a blocking modal
- SMS consent needs its own explicit opt-in, separate from email

Separate the UX recommendation from the legal question. Where default state, wording, or jurisdiction is in play, write **Legal review required** and give the UX recommendation alongside it.
