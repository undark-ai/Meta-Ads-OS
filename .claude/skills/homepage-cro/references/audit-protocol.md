# Homepage Audit Protocol

The full walk, plus the architecture you produce from it.

---

## Phase 0 — Traffic reality

Before opening the site. This gate determines what the rest of the audit is even about.

| Question | Where to get it | Why it decides the audit |
|---|---|---|
| Homepage share of total sessions | GA4 landing-page report | If it's 6% of sessions, homepage work is not the top growth priority — say so |
| Source split of homepage sessions | GA4 landing page × source/medium | Brand search and direct want routing; paid social wants convincing |
| New vs. returning split | GA4 landing page × user type | A returning-heavy homepage optimized for cold visitors gets worse |
| Homepage-assisted revenue | Path exploration / assisted conversions | Distinguishes "hub that works" from "pretty dead end" |
| Next-page distribution | GA4 path exploration | Tells you which module is actually carrying discovery |
| Exit rate from homepage | GA4 | A high exit rate on brand-search traffic is a routing failure |

If none of this exists, the audit runs on structural inference. State that explicitly, name the assumption you're making about the audience, and put "instrument this" first in the action plan. Do not quietly assume cold traffic — that assumption produces confident recommendations that harm returning-customer revenue.

---

## Phase 1 — The live walk

Desktop 1440px and mobile 375px, separately. Log the viewport with every observation.

| # | Step | What to record |
|---|---|---|
| 1 | Above-fold capture | Screenshot before any scroll, both viewports |
| 2 | Fold accounting | Measure what consumes the fold: promo bar(s), cookie banner, nav, hero. How much useful content survives at 375×667? |
| 3 | Header | Logo, nav, search, account, cart. Is search visible or hidden behind an icon? |
| 4 | Promo bar | How many messages? Rotating? Dismissible? Is the offer current? |
| 5 | Hero | Headline, subhead, visual, CTA count. If it rotates, watch every slide and time the interval |
| 6 | First trust signal | How far down before any proof appears? |
| 7 | Navigation | Open every desktop dropdown and the full mobile menu tree. Count levels and items |
| 8 | Search | Use it. Search a product you'd expect. Then search a typo. Then search something they don't sell — check the zero-results state |
| 9 | Full scroll | Log every section in order with its apparent purpose |
| 10 | Discovery click-through | Click a category, a collection, and a product card. Does the scent hold, or does the label promise something the destination doesn't deliver? |
| 11 | Product cards | Image quality and consistency, name, price, rating, review count, swatches, badges, quick add, hover behaviour |
| 12 | Popups | Trigger, timing, dismissibility, whether it fires before any content is seen, whether it re-fires for subscribers |
| 13 | Decay check | Out-of-stock or discontinued hero products, expired promos, stale "New Arrivals," wrong-season creative, dead links, sold-out featured collections |
| 14 | Floating elements | Chat, back-to-top, accessibility widget, sticky bars — and what each covers at 375×667 |
| 15 | Footer | Is it doing navigation work, or is it a link dump? Are policies and contact reachable? |

Note everything you couldn't test, and why.

---

## Phase 2 — Brand and business context

| Question | Why it changes the audit |
|---|---|
| Catalogue size | 3 SKUs and 900 SKUs need opposite homepages — one converts, one routes |
| Brand maturity | A new brand must establish; an established one must merchandise |
| Competes on price, product, or identity? | Decides how much promotional prominence is acceptable |
| AOV and margin | High margin can absorb brand-building space; thin margin can't afford a homepage that doesn't route |
| Repeat purchase rate | High repeat means returning customers are a large share — build for them |
| Subscription or consumable? | Reorder and subscription management belong on the homepage |
| Seasonality | Determines the maintenance cadence the page needs |
| Category familiarity | A novel product needs education before desire; a known one doesn't |

State the implications, don't just list facts. "A 4-SKU identity brand at £95 AOV with 38% repeat purchase means the homepage's job is brand plus reorder, not catalogue navigation" is analysis.

---

## Phase 3 — Name the job

Pick one primary job (see the table in `SKILL.md`), name at most one secondary, and judge the architecture against that. If the page is serving four jobs, that is the finding — say which to pick and what to cut.

---

## Phase 4 — Section-by-section flow

| Section | Purpose | User question it answers | Business objective | Performing? | Verdict | Priority |
|---|---|---|---|---|---|---|

Verdict is one of **keep / improve / move / combine / remove**.

Rules:

- A section answering no customer question is a removal candidate, however good it looks
- Combine before you add. Two weak modules saying the same thing are one strong module
- Use scroll and click data where it exists — a module nobody reaches is not a content problem, it's a position problem
- Judge the narrative: does it run **problem → desire → product → proof → brand → action**, or lurch between disconnected blocks? Name the abrupt transitions

---

## Phase 5 — Ideal architecture by archetype

Do not apply a 17-section template. Most underperforming D2C homepages are too long. Pick the archetype that matches the job, then adapt.

### A. Product discovery hub — larger catalogue, brand-search heavy

| # | Section | Why here |
|---|---|---|
| 1 | Slim value bar | One message — shipping threshold or returns. Not a promo stack |
| 2 | Header with visible search | Search is a primary path for this audience |
| 3 | Hero | Seasonal or best-selling category, one primary CTA into a collection |
| 4 | Category tiles | 3–6 routes, labelled how customers shop. The workhorse of this archetype |
| 5 | Best sellers | Social proof and discovery in one module. Ratings on cards |
| 6 | Compressed trust strip | Rating, review count, one guarantee — one row, not a badge wall |
| 7 | New arrivals | The reason returning visitors came |
| 8 | Shop by need / use case | Second discovery route for people who don't think in categories |
| 9 | Brand differentiator | One block. Why this brand, with proof |
| 10 | UGC or reviews | Real customers, linked to products |
| 11 | Email capture | Inline, not a popup, if the popup is being removed |
| 12 | Footer | Genuine secondary navigation |

### B. Direct conversion — 1–3 SKUs

| # | Section | Why here |
|---|---|---|
| 1 | Slim value bar | Shipping and returns reassurance |
| 2 | Header | Minimal. Cart visible |
| 3 | Hero = the product | Product, price, rating, add-to-cart or shop CTA. Behaves like a PDP hero |
| 4 | Three benefits | Outcome-led, strongest first and last |
| 5 | Proof | Rating, review count, press, UGC |
| 6 | How it works | Where the product needs explaining |
| 7 | Comparison | Against the alternative the customer is actually considering |
| 8 | Reviews | Depth, with photos |
| 9 | FAQ | The real pre-purchase objections |
| 10 | Final CTA with risk reversal | Returns window and guarantee restated |
| 11 | Footer | |

### C. Brand establishment — new brand, unfamiliar category

Same spine as A, but sections 3–5 become: hero that states who this is for and why the brand exists → the problem the category gets wrong → the product as the answer, with proof. Route to product by section 5. **A brand-establishment homepage that hasn't shown a product by the second scroll is a brochure.**

### D. Returning-customer hub — high repeat, subscriptions, consumables

Lead with reorder and account access, then new-since-last-visit, then subscription management, then discovery. Personalize where the platform allows. This archetype is the one most commonly missed, and it's the correct one more often than teams assume — check Rule 0.

---

## Phase 6 — Mobile blueprint

Write separately.

| Requirement | Detail |
|---|---|
| Fold discipline | Promo bar, nav, and hero must leave real content visible at 375×667. One promo line maximum |
| Hero height | Capped. A full-viewport hero on mobile means the visitor sees only an image |
| Nav | Menu reachable in one tap, no more than two levels before products, search prominent inside the menu |
| Category tiles | 2-up grid beats a horizontal scroll strip — off-screen items get almost no engagement |
| Horizontal carousels | If used, show a partial next item so scrollability is visible, and provide buttons plus keyboard access |
| Product cards | 2-up. Rating and price legible at real size. Tap targets ≥44×44px |
| Section count | Fewer than desktop. Cut, don't stack — mobile scroll depth is not free |
| Popups | Never before the visitor has seen content. Must be dismissible with a real target, not a 12px × |
| Floating elements | Check chat, accessibility, and sticky bars don't cover CTAs or content |
| Media | Hero video is usually the wrong call on mobile — measure it before defending it |

Mobile failures to look for: promo stack plus cookie banner plus hero leaving nothing above the fold; horizontal category strips hiding most options; a hamburger menu three levels deep; hero text illegible over the image at small size; a newsletter popup firing at 2 seconds.

---

## Phase 7 — Competitive benchmark

Review 3–5 comparable D2C brands plus 2–3 best-in-class ones. Compare hero strategy, navigation depth, category taxonomy, discovery modules, proof placement, merchandising, promotional prominence, mobile layout, CTA hierarchy, section count.

Answer: **what do strong brands in this category consistently do that this homepage doesn't?** Patterns across several are signal; one brand's choice is noise. Note where a competitor's approach is wrong for *this* brand's positioning — a discount-led homepage is correct for an outlet and destructive for a premium brand.

---

## Phase 8 — Synthesis

1. Cognitive load scorecard with justifications
2. Prioritized roadmap by Impact × Confidence ÷ Effort
3. Top 15 changes, ranked
4. Ideal architecture — desktop and mobile
5. A/B roadmap — see `experiments.md`
6. Measurement plan — see `measurement.md`
7. 30-day action plan: concrete steps, each with an owner type and a success signal. Include the maintenance cadence and its owner — homepage decay is a recurring problem, not a one-off fix

Executive summary is written last and goes first.
