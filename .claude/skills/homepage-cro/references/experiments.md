# Homepage Experiment Library

**Read the powering problem first. It disqualifies half of what teams want to test on a homepage.**

---

## The powering problem

Homepage tests are the hardest tests in e-commerce to run credibly:

1. **Homepage sessions are a fraction of site sessions** — often 5–20%. You're testing on a slice, not the whole
2. **The conversion event is several steps downstream.** A homepage change influences a purchase that happens two or three pages later, so the effect is diluted by everything in between
3. **The audience is mixed.** Brand search, direct, returning customers, and cold traffic respond differently, and a blended result can be a flat average of one strong win and one loss
4. **Effect sizes are small.** Homepage changes rarely move site-wide conversion by the amounts a test can detect quickly

What follows from that:

- **Run the sample-size maths before committing.** See `../../ab-testing/references/sample-size-guide.md`. If a test needs 14 weeks, it isn't a test — it's a decision you should make on judgment and evidence
- **Use an intermediate primary KPI** where the terminal one is unreachable: product-view rate from the homepage, or homepage-assisted conversion rate. Keep revenue per session as the deciding secondary
- **Segment new vs. returning, and desktop vs. mobile**, always. Decide the segments before you start
- **Fix defects instead of testing them.** An out-of-stock hero, an expired promo, a broken nav link, or a 5-second LCP is a bug. Ship the fix
- **Prefer bigger swings.** Given the statistical constraints, a full hero or architecture change is more likely to produce a readable result than a button-colour test. Small homepage tests are usually a waste of runtime

---

## Hero and messaging

**1. Static hero replacing the carousel**
- Hypothesis: Rotation splits attention and later slides are effectively unpublished; one clear message outperforms five competing ones
- Control: Rotating hero, 3–5 slides
- Variant: Single static hero with the highest-priority message; displaced campaigns moved to their own measurable sections
- Primary: Product-view rate from homepage · Secondary: Revenue per session, LCP
- Risk: Internal, not customer — teams lose their slide. Bring per-slide engagement data to that conversation
- Priority: **P0** where a rotating hero exists

**2. Product-benefit hero vs. brand hero**
- Hypothesis: Naming the product and its outcome, with a proof anchor, converts better than a mood-led hero for cold and mixed traffic
- Control: Current brand/lifestyle hero
- Variant: WHO → WHAT → WHY → PROOF → ACTION hero, product visible, single CTA
- Primary: Product-view rate from homepage · Secondary: Revenue per session, bounce rate
- Risk: Brand dilution on a premium positioning — judge qualitatively too, not only on the numbers
- Priority: **P1**

**3. Single primary CTA**
- Hypothesis: Competing equal-weight CTAs mean no primary path; consolidating raises progression into the funnel
- Control: Multiple equally weighted hero CTAs
- Variant: One primary, others demoted to text links
- Primary: Product-view rate from homepage · Secondary: Revenue per session
- Risk: Low, unless the homepage genuinely serves two distinct audiences — check Rule 0 first
- Priority: **P1**

---

## Above the fold

**4. Collapse the promo bar stack**
- Hypothesis: Stacked promo bars steal the mobile fold and push all useful content below it; one message performs better than three
- Control: Two or more stacked bars, possibly rotating
- Variant: One static line — the single highest-value message
- Primary: Product-view rate from homepage (mobile) · Secondary: Promo code usage, revenue per session
- Risk: Reduced awareness of secondary offers
- Priority: **P0** where the stack pushes content below the fold at 375×667

**5. Proof above the fold**
- Hypothesis: A rating and review count in the first screen answers "is this brand real" before the visitor decides to leave
- Control: No proof above the fold
- Variant: Aggregate rating and review count near the hero CTA
- Primary: Bounce rate · Secondary: Product-view rate, revenue per session
- Risk: Counterproductive with low review volume or a weak rating
- Priority: **P1**

**6. Cap hero height on mobile**
- Hypothesis: A full-viewport mobile hero shows only an image; capping it so a headline, proof line, and CTA share the fold raises progression
- Control: Full-viewport hero
- Variant: Capped hero with headline, one proof line, and CTA visible at 375×667
- Primary: Product-view rate from homepage (mobile) · Secondary: Scroll depth, bounce rate
- Risk: Less visual impact
- Priority: **P1**

---

## Discovery and navigation

**7. Category tiles above the first content section**
- Hypothesis: Brand-search and returning visitors want routing, not persuasion; putting category routes high shortens the path
- Control: Categories below editorial or brand sections
- Variant: 3–6 category tiles directly under the hero
- Primary: Product-view rate from homepage · Secondary: Revenue per session, homepage exit rate
- Risk: Reads as less brand-led — weigh against positioning
- Priority: **P1**, and higher if Rule 0 shows a routing-led audience

**8. Need-based route alongside the product taxonomy**
- Hypothesis: Visitors who don't think in product categories need a situation-led route; adding one captures demand a product grid loses
- Control: Product taxonomy only
- Variant: Product taxonomy plus a "shop by need/use" module using customers' own language from search and reviews
- Primary: Product-view rate from homepage · Secondary: Revenue per session, module engagement
- Risk: Adding a route can dilute the primary one. Do not add a third
- Priority: **P2**

**9. Visible search input**
- Hypothesis: Search is a primary path for brand-search and returning traffic; an open input rather than an icon raises usage and progression
- Control: Search behind an icon
- Variant: Visible input in the header with suggestions
- Primary: Search usage rate · Secondary: Revenue per session for searchers, zero-result rate
- Risk: Low. Also instrument the zero-results state before running it, or you'll route more people into a dead end
- Priority: **P1** on catalogues above roughly 50 SKUs

**10. Reorder / returning-customer module**
- Hypothesis: A large returning-visitor share is being served a first-impression homepage; a reorder and new-since-last-visit module converts them faster
- Control: Same homepage for everyone
- Variant: Logged-in or recognized visitors see reorder, subscription management, and new arrivals first
- Primary: Revenue per returning session · Secondary: Repeat purchase rate, homepage exit rate
- Risk: Build cost; personalization needs the platform to support it
- Priority: **P1** where returning share is high — one of the most commonly missed opportunities

---

## Merchandising

**11. Ratings on product cards**
- Hypothesis: Rating and review count on cards provides proof at the point of selection, raising click-through to the right products
- Control: Cards with image, name, price
- Variant: Cards adding star rating and review count
- Primary: Product-view rate from homepage · Secondary: Add-to-cart rate, revenue per session
- Risk: Cards with no reviews look worse by comparison — decide the rule for low-volume products first
- Priority: **P1**

**12. Real best sellers instead of curated favourites**
- Hypothesis: Actual sales-ranked products outperform manually chosen ones, because they reflect what this audience already buys
- Control: Manually curated featured products
- Variant: Automated best-seller module, sales-ranked, in-stock filtered
- Primary: Revenue per session · Secondary: Product-view rate, module click-through
- Risk: Loses merchandising control over margin mix — check the margin of what surfaces
- Priority: **P2**

**13. Grid instead of horizontal carousel on mobile**
- Hypothesis: Off-screen carousel items get almost no engagement; a 2-up grid exposes more of the range
- Control: Horizontal scroll strip
- Variant: 2-up grid showing 4–6 products
- Primary: Product-view rate from homepage (mobile) · Secondary: Revenue per session
- Risk: More vertical space
- Priority: **P2**

---

## Promotions and capture

**14. Suppress the homepage email popup**
- Hypothesis: An early popup interrupts visitors before any intent is formed and costs more in progression than it returns in signups
- Control: Popup fires on homepage entry
- Variant: Suppressed on homepage, or delayed to exit intent, with an inline capture section lower down
- Primary: Revenue per session · Secondary: Email capture rate, bounce rate
- Risk: Capture rate will fall. Decide explicitly whether the list growth is worth the revenue — and note the two metrics usually have different owners
- Priority: **P1**

**15. Free-shipping threshold instead of a percentage discount**
- Hypothesis: A threshold raises AOV rather than cutting margin, and doesn't train discount-waiting
- Control: "10% off your first order" as the primary offer
- Variant: "Free shipping over £X" with the threshold stated
- Primary: Revenue per session · Secondary: AOV, conversion rate, shipping margin
- Risk: Conversion rate may dip while AOV and margin rise — judge on revenue and margin, not conversion
- Priority: **P1**

**16. Value-led vs. discount-led hero messaging**
- Hypothesis: For a brand with pricing power, leading with the guarantee or product benefit protects margin without costing conversion
- Control: Discount as the primary hero message
- Variant: Benefit or guarantee primary, offer demoted to secondary
- Primary: Revenue per session · Secondary: Full-price sell-through, discount code usage, AOV
- Risk: Short-term conversion dip. **Full-price sell-through is the metric that matters here** and it needs a longer window than the test
- Priority: **P1** for premium positioning

---

## Structure and performance

**17. Shorten the homepage**
- Hypothesis: Sections that answer no customer question dilute the path; removing them raises progression
- Control: Current section count
- Variant: The lowest-value sections removed, per the flow table and scroll data
- Primary: Product-view rate from homepage · Secondary: Revenue per session, scroll depth to CTA
- Risk: Removing something that was quietly working — use scroll and click data, not taste
- Priority: **P1**

**18. Optimize the hero asset**
- Hypothesis: The hero is the LCP element and its weight delays the first meaningful frame, raising bounce on mobile
- Control: Current hero image or autoplay video
- Variant: Modern format, correct dimensions, `fetchpriority="high"`, static poster instead of autoplay video
- Primary: LCP · Secondary: Bounce rate, product-view rate, revenue per session
- Risk: Low. This is usually a defect fix rather than a test — measure, ship, verify
- Priority: **P0** where LCP exceeds 2.5s

**19. Remove the interstitial / entry overlay**
- Hypothesis: An age gate, region selector, or campaign overlay before the homepage costs more than it returns
- Control: Overlay on entry
- Variant: Removed, or deferred until the action requires it
- Primary: Revenue per session · Secondary: Bounce rate
- Risk: Some overlays are legally required — verify before recommending removal
- Priority: **P1** where non-mandatory

**20. Proof adjacent to claims instead of a single block**
- Hypothesis: Proof placed immediately after the claim it supports does more than the same proof collected at the bottom of the page
- Control: One reviews section near the footer
- Variant: Relevant proof distributed to each claim, plus a shorter reviews section
- Primary: Product-view rate from homepage · Secondary: Revenue per session, scroll depth
- Risk: Fragmenting proof can weaken the aggregate impression — keep the rating visible high up
- Priority: **P2**

---

## Guardrails for every homepage test

Track alongside the primary: revenue per session, full-price sell-through (for any promotional change), email capture rate (for any popup change), AOV, bounce rate, LCP and CLS, and homepage exit rate.

And segment: **new vs. returning** and **desktop vs. mobile**, decided before the test starts. A blended homepage result is the most misleading number in e-commerce CRO.
