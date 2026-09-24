# Hero, Messaging, and CTAs

The hero is the single most consequential communication area on the homepage — and the most frequently designed by committee.

---

## The 5-second test, weighted

Look only at the above-fold frame. Six questions:

| # | Question | Fails when |
|---|---|---|
| 1 | What brand is this? | Logo only, no context. Common and usually fine — brand-search visitors already know |
| 2 | What do they sell? | An abstract lifestyle image with a slogan. **The most damaging failure** — the visitor cannot form intent |
| 3 | Who is it for? | Copy that could describe any brand in the category |
| 4 | What makes them different? | Generic superlatives — "premium," "thoughtfully designed," "elevated essentials" |
| 5 | Why should I care? | No benefit or outcome stated anywhere above the fold |
| 6 | What do I do next? | No CTA, or four competing CTAs |

Score each 1–10 and justify.

**Weight by audience (Rule 0).** On a brand-search-and-returning-heavy homepage, #2 and #6 carry most of the commercial weight — those visitors already know the brand and need routing. On genuinely cold traffic, #3, #4, and #5 matter far more. Report the weighting, not just the scores; six equally-weighted scores imply every failure costs the same, and they don't.

---

## Hero rebuild framework

Reconstruct the hero as **WHO → WHAT → WHY → PROOF → ACTION**, then compare against what's there.

| Element | Job | Failure mode |
|---|---|---|
| **WHO** | Signals who this is for | Absent, or so broad it signals nothing |
| **WHAT** | Names the product or category concretely | Replaced by a mood or a slogan |
| **WHY** | The benefit or outcome | A feature, or a claim with no substance |
| **PROOF** | One credibility anchor — rating, count, press, guarantee | Missing above the fold entirely |
| **ACTION** | One primary CTA with clear destination | Multiple equal CTAs, or a vague "Explore" |

Then present:

- **Current message** — what the hero actually communicates to a stranger
- **Problem** — what's unclear or weak, and what it costs
- **Recommended message** — a concrete rewrite, not a direction
- **Why** — the mechanism by which it should perform better

### Three alternative directions

Always give three, and pick one to test first with a reason:

1. **Conversion-led** — names the product and the offer, single hard CTA into a collection or PDP. Highest expected short-term lift; the risk is brand dilution on a premium positioning
2. **Brand-led** — leads with positioning and the reason the brand exists. Right for a new or premium brand; the risk is that visitors don't learn what's for sale
3. **Product-benefit-led** — names the product and the outcome it delivers, with a proof anchor. Usually the safest first test and the most common winner for D2C

Recommend by **brand maturity and margin**, not by preference. A scaling brand with thin margin should test conversion-led first. An established identity brand with pricing power to protect should test product-benefit-led and treat conversion-led as the risk case.

---

## Hero carousels

If a rotating hero exists, treat it as its own finding.

**What goes wrong:**

- Engagement concentrates almost entirely on the first slide. Slides 3, 4, and 5 are effectively unpublished
- Rotation competes with reading. Text that moves while being read is text that isn't read
- Each slide's assets add page weight, and the hero is already the LCP element
- Reserving space for multiple slides, or swapping them, is a common layout-shift source
- Auto-rotation without pause controls is an accessibility failure, and keyboard and screen-reader access to later slides is usually broken
- Auto-rotating carousels almost never provide the single-pointer and keyboard alternatives their swipe interaction requires

**Why it exists anyway:** it is usually not a customer-driven decision. It's the artifact of several internal teams each needing their campaign above the fold. Say this plainly and diplomatically — the fix is an editorial decision about priority, not a design change. Naming the real cause is what makes the recommendation actionable.

**Default recommendation:** replace with a single static hero carrying the highest-priority message, and give the displaced campaigns their own sections further down where they can be measured individually. Frame it as a test with revenue per session as primary, and report per-slide engagement from the current carousel as the supporting evidence — that data usually wins the argument on its own.

**If it must stay:** cap at three slides, no auto-rotation (or pause on focus and hover, plus a visible pause control), visible position indicators, real previous/next buttons with keyboard access, first slide static on load, and all slides rendered in a readable final state under `prefers-reduced-motion`.

---

## Hero visual

| Check | The failure |
|---|---|
| Is the product visible? | Pure lifestyle imagery where the product is incidental or absent |
| Does it show the outcome? | Decorative image with no relationship to what's sold |
| Is text legible over it? | Light text over a photo where contrast fails somewhere in the frame — measure it, don't eyeball it |
| Does the mobile crop work? | Desktop crop centred on a subject that's cropped out at 375px |
| Is it the LCP element, and how heavy? | An unoptimized hero image or autoplaying video is the most common homepage LCP defect. See `../../ux-audit/references/ux-defects.md` |
| Video: does it earn its cost? | Autoplay video with no pause control, no poster, and no reduced-motion fallback. Measure the LCP cost before defending it |

---

## Copy audit

Sweep headlines, subheadlines, CTAs, section headings, benefit copy, promo copy, trust copy, brand story, and navigation labels.

| Problem | What to do |
|---|---|
| **Generic claims** — "premium quality," "thoughtfully designed," "elevated essentials" | Replace with something specific and falsifiable. If you can't substantiate it, cut it |
| **Unsupported claims** | Attach proof, or soften to something defensible |
| **Jargon and internal language** | Product line names and internal category labels mean nothing to a first-time visitor |
| **Feature-dumping** | Convert to benefit or outcome |
| **Repetition** | The same claim in the hero, the value bar, and three sections reads as having only one thing to say |
| **Excessive text** | Homepage copy is scanned. Cut to what survives a scan |
| **Weak navigation labels** | "Shop" and "Collections" have no information scent. Name what's inside |
| **Vague CTAs** | "Explore," "Discover," "Learn more" — name the destination |

Then rewrite the highest-impact copy: hero headline and subhead, primary CTA, and the two or three section headings carrying the most traffic.

---

## CTA hierarchy

Inventory every CTA on the page and classify:

- **Primary** — the action most visitors should take. There should be **one**, repeated consistently
- **Secondary** — a useful alternative for a different intent
- **Tertiary** — low-priority (account, newsletter, social)

Then judge:

| Check | The failure |
|---|---|
| Count | So many CTAs that nothing is primary |
| Hierarchy | Three buttons at identical visual weight |
| Consistency | The primary action worded differently in each section |
| Destination clarity | The visitor can't predict where the click goes |
| Intent match | A hard "Buy now" aimed at a visitor who arrived to browse |
| Repetition | On a long page, no CTA after the first screen |

Answer plainly: **does this homepage have one clear conversion path, or several competing ones?** Competing paths are the more common failure, and consolidating them is usually a cheap, high-confidence win — but verify against Rule 0 first. A homepage serving three genuinely different audiences may legitimately need two paths; it does not need five.
