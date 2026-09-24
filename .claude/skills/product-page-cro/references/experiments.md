# PDP Experiment Library

Test ideas for product pages, grouped by lever. Written to lift straight into a test brief.

**Format:** Hypothesis → Control → Variant → Primary KPI → Secondary KPI → Risk → Priority

**KPI discipline:** never judge a PDP test on add-to-cart rate alone. ATC is trivially easy to move in the wrong direction — hiding price, burying shipping, or an aggressive sticky bar all lift it while pushing unqualified shoppers into an abandoned cart. **Pair every ATC primary with checkout initiation or revenue per visitor as a secondary**, and treat a rise in ATC with flat revenue as a failure, not a partial win.

See `../../ab-testing/references/sample-size-guide.md` for powering. Single-PDP traffic is usually thin — most of these need to run across a product template, not one page.

---

## Above the fold

**1. Price and title above the gallery fold on mobile**
- Hypothesis: A full-bleed gallery consuming the mobile fold hides the title and price, so shoppers can't complete the 10-second test and bounce
- Control: Gallery at current height
- Variant: Gallery capped so title, rating, price, and one benefit line share the first viewport
- Primary: PDP conversion rate (mobile) · Secondary: Bounce rate, scroll depth
- Risk: Smaller hero image may reduce product appeal — watch gallery interaction rate
- Priority: **P0** where the fold test fails on mobile

**2. Benefit summary above the variant selector**
- Hypothesis: Three specific benefit lines between price and variants give shoppers the value proposition before they're asked to decide, lifting qualified add-to-carts
- Control: Feature list, or nothing, above the selector
- Variant: 3 benefit/outcome lines, strongest first and last
- Primary: Add-to-cart rate · Secondary: Checkout initiation, revenue per visitor
- Risk: Low. Cheapest high-value PDP test there is
- Priority: **P1**

**3. Rating and review count next to the title**
- Hypothesis: Surfacing the rating in the first viewport provides social proof before evaluation begins
- Control: Rating only in the reviews section
- Variant: Star rating and count beside the title, anchor-linked to reviews
- Primary: Add-to-cart rate · Secondary: Review section engagement
- Risk: Counterproductive with very low review volume or a poor rating
- Priority: **P1** where review volume supports it

---

## Gallery

**4. Add the missing question-answering images**
- Hypothesis: Shoppers abandon because scale, contents, or fit is unanswerable from the current gallery
- Control: Current image set
- Variant: Add scale/context, what's-included, and dimension images (whichever are missing)
- Primary: Add-to-cart rate · Secondary: Return rate, gallery interaction depth
- Risk: More images means more weight — ship optimized formats or you'll trade LCP for clarity
- Priority: **P1**

**5. Reorder the gallery**
- Hypothesis: Leading with an in-use or in-context shot rather than a clean studio hero communicates value faster for this category
- Control: Studio hero first
- Variant: In-use or on-model shot first
- Primary: Add-to-cart rate · Secondary: Gallery interaction rate
- Risk: Category-dependent — technical products usually want the clean hero first
- Priority: **P2**

**6. Customer photos in the gallery**
- Hypothesis: UGC answers colour and scale questions the studio set can't, raising confidence
- Control: Brand photography only
- Variant: A labelled customer-photo section in or beneath the gallery
- Primary: Add-to-cart rate · Secondary: Return rate, review engagement
- Risk: Inconsistent image quality can cheapen a premium brand — curate
- Priority: **P2**

---

## Variants and configuration

**7. Swatches instead of dropdowns**
- Hypothesis: Visible options remove a tap and let shoppers choose the colour they can see, lifting completion of the selection step
- Control: Dropdown selectors for colour and size
- Variant: Visual swatches for colour, chips for size, with per-option availability
- Primary: Add-to-cart rate (mobile) · Secondary: Variant selection rate, time to add
- Risk: Space cost with large option sets
- Priority: **P0** where colour or size is a dropdown

**8. Inline size guidance**
- Hypothesis: Sizing uncertainty blocks purchase and causes returns; inline guidance addresses both
- Control: Size guide behind a modal or PDF link
- Variant: Inline measurements, model height and worn size, plus a review-sourced fit signal
- Primary: Add-to-cart rate · Secondary: **Return rate** (the real prize), exchange rate
- Risk: None material. Measure returns over a full return window before calling it
- Priority: **P0** where "wrong size" leads return reasons

**9. Compatibility checker**
- Hypothesis: Shoppers who can't confirm the product works with what they own don't buy
- Control: Compatibility listed in a spec table
- Variant: A two-input compatibility tool with a clear yes/no result
- Primary: Add-to-cart rate · Secondary: Return rate, pre-purchase support volume
- Risk: Build cost; a wrong answer is worse than no tool
- Priority: **P1** for technical categories

---

## Add-to-cart module

**10. Delivery date beside the CTA**
- Hypothesis: A named arrival date resolves delivery uncertainty at the decision point better than a vague range
- Control: "Ships in 3–5 business days," or nothing
- Variant: "Order in the next 4 hours for delivery Tuesday 26 Aug," computed from real cutoff and transit
- Primary: Add-to-cart rate · Secondary: Revenue per visitor, WISMO ticket volume
- Risk: Requires accurate cutoff logic. A missed promise costs more than a vague one
- Priority: **P1**

**11. Shipping and returns adjacent to the CTA**
- Hypothesis: Shipping cost and returns window discovered at checkout instead of the PDP causes late abandonment
- Control: Policies in the footer or a separate page
- Variant: One compact line — shipping cost or threshold, delivery date, returns window — beside the button
- Primary: Checkout initiation · Secondary: Checkout completion rate, revenue per visitor
- Risk: ATC may *fall* while revenue rises, as unqualified shoppers self-select out. That is a win — set the primary KPI accordingly
- Priority: **P0** where shipping cost is not discoverable on the PDP

**12. Cart drawer instead of silent add or redirect**
- Hypothesis: Unambiguous confirmation plus a visible path to checkout raises checkout initiation
- Control: Silent add, toast, or redirect to cart page
- Variant: Slide-out cart drawer with cart contents and a clear checkout CTA
- Primary: Checkout initiation · Secondary: Items per order, revenue per visitor
- Risk: Redirect-to-cart may suit single-item catalogues better — segment by basket size
- Priority: **P0** where the add is silent

**13. Sticky CTA with variant and price**
- Hypothesis: On a long mobile PDP, a persistent CTA showing the selected variant and price removes the scroll-back cost
- Control: CTA only at its natural position
- Variant: Sticky bottom bar with variant, price, and add-to-cart, above the safe-area inset
- Primary: Add-to-cart rate (mobile) · Secondary: Scroll depth, review engagement
- Risk: Obscures content; check against reviews and footer at 375×667
- Priority: **P1**

**14. Buy Now alongside Add to Cart**
- Hypothesis: A single-item express path shortens the route to purchase for decided shoppers
- Control: Add to cart only
- Variant: Add to cart primary, Buy Now (express wallet) secondary
- Primary: Revenue per visitor · Secondary: Items per order, conversion rate
- Risk: Real — it can suppress basket-building and lower AOV. Watch items per order closely
- Priority: **P2**

---

## Trust and proof

**15. Review content surfaced up-page**
- Hypothesis: The most decision-relevant review sentence quoted near the variant selector does more than the same review 4000px down
- Control: Reviews only in the bottom section
- Variant: One or two pulled quotes near the decision, plus attribute ratings
- Primary: Add-to-cart rate · Secondary: Review section engagement
- Risk: Cherry-picking perception if quotes look curated — use the most helpful-voted ones
- Priority: **P1**

**16. Extended returns window**
- Hypothesis: A longer, clearly stated returns window is a costly signal that reduces perceived risk enough to lift conversion beyond its return cost
- Control: Current returns window
- Variant: Extended window, stated prominently near the CTA
- Primary: Revenue per visitor net of returns · Secondary: Conversion rate, **return rate**
- Risk: Genuine — returns will rise. Measure net over a full return cycle, not gross conversion
- Priority: **P2**

**17. Consolidate trust badges**
- Hypothesis: A badge cluster adds noise and competes with the CTA; one specific claim outperforms it
- Control: Five or more badges
- Variant: One line — returns window and a real, recognized guarantee or certification
- Primary: Add-to-cart rate · Secondary: Time on page
- Risk: Low; occasionally negative where certification genuinely drives the category
- Priority: **P2**

---

## Distraction and cross-sell

**18. Move cross-sell below the decision**
- Hypothesis: Related products adjacent to the CTA split attention at the decision point
- Control: Cross-sell beside or above the add-to-cart module
- Variant: Cross-sell moved below the description, or into the cart drawer
- Primary: Revenue per visitor · Secondary: Add-to-cart rate, items per order
- Risk: Cross-sell click-through will fall — judge on RPV, not on cross-sell engagement
- Priority: **P1**

**19. Suppress the newsletter popup on PDPs**
- Hypothesis: A discount popup interrupting an in-progress purchase decision converts buyers into code-hunters and depresses revenue per visitor
- Control: Popup fires on PDPs as elsewhere
- Variant: Suppressed on PDPs, or delayed until exit intent
- Primary: Revenue per visitor · Secondary: Email capture rate, add-to-cart rate
- Risk: Email capture will fall — decide explicitly whether the list growth is worth the revenue
- Priority: **P1**

**20. Reduce the promo banner stack**
- Hypothesis: Stacked promo bars steal the mobile fold and push the decision content below it
- Control: Multiple stacked announcement bars
- Variant: One line, or none
- Primary: PDP conversion rate (mobile) · Secondary: Promo code usage
- Risk: Reduced promo awareness
- Priority: **P1** where the stack pushes price below the fold

---

## Test hygiene for PDPs

- **Test the template, not the page.** One PDP rarely has the traffic. Run across a product template or a category and segment afterwards
- **Segment desktop and mobile.** Many PDP changes are positive on one and negative on the other; a blended result hides both
- **Wait out the return window** on anything touching sizing, imagery, or returns messaging. A conversion win that raises returns 8 points is a loss, and you cannot see it inside two weeks
- **Guardrails:** return rate, items per order, checkout completion, support ticket volume, LCP
- **Fix defects, don't test them.** A dropdown for colour, a silent add-to-cart, a 3MB hero image, or an out-of-stock dead end are bugs. Ship the fix; don't spend runtime proving a bug is bad
- **Watch for novelty on gallery changes** — image reordering often shows an early lift that decays. Run the full cycle
