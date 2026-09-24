---
name: meta-campaign-structure
description: "When the user wants to structure Meta campaigns for an e-commerce or D2C brand — account architecture, prospecting/retargeting/retention layout, budget placement, consolidation rules, naming conventions, and the phased scaling roadmap from validation to Advantage+. Also use when the user mentions 'campaign structure,' 'account structure,' 'ABO vs CBO,' 'how many ad sets,' 'learning phase,' 'consolidate my campaigns,' or 'restructure my Meta account.' For building the campaigns on a live account, see meta-campaign-creation. For end-to-end campaign planning across channels, see ads-campaign-planning. For the e-commerce Meta hub, see meta-ads."
metadata:
 version: 1.1.0
---

> **Marketing layer — advisory, not evidence.** Every benchmark, threshold and rule of thumb
> below is build-time guidance. Per `CLAUDE.md`, a marketing skill's number is never evidence
> for a quantified finding: a recommendation that originates here still needs a number, source,
> date range, formula, evidence class and confidence from the audit layer before it can be
> presented as one. Handoffs run audit → marketing, never the reverse.


# Campaign Structure for D2C Meta Ads

How to structure a Meta account for e-commerce: the three phases (validation → creative scaling → Advantage+ automation), the recommended architecture, key settings, and the build order.

## Before Starting

**Check for product marketing context first:**
If `.agents/product-marketing.md` exists (or `.claude/product-marketing.md`, or the legacy `product-marketing-context.md` filename, in older setups), read it before asking questions. Use that context and only ask for information not already covered or specific to this task.

Gather this context (ask if not provided):

- AOV, contribution margin per order, and target CPA (needed for the minimum-budget formula)
- Current weekly purchase volume (determines which phase the account belongs in)

## The Three Phases

### Phase 1: Validation (ABO)

**Purpose:** Determine which audience sources produce profitable new customers before spending on creative testing. Use when launching a new account, product line, or market.

```
Campaign: [Brand] - Prospecting - Validation (ABO)
── Ad Set 1: 1% Customer-List Lookalike (best buyers)
── Ad Set 2: Value-based lookalike / engagement audience
── Ad Set 3: Broad (no targeting)
 └─ Same 3–4 ads in every ad set (isolate the audience variable)
```

Critical settings: ABO (not CBO — CBO would shift budget to the cheapest audience, which may not be the most profitable), equal budgets, same ads everywhere, Advantage+ audience expansion OFF, run 2–4 weeks.

**Validate in your order data, not Ads Manager:** new-customer rate, AOV per ad set, contribution margin per order, early repeat/LTV signal, post-purchase survey responses. Kill ad sets producing discount-hunters or low-AOV baskets; take winners to Phase 2. (Simpler test: broad vs. lookalike, two ad sets, pick the winner.)

### Phase 2: Creative Scaling (CBO)

**Purpose:** Scale the winning audience through creative concept testing. This is where most accounts live.

```
Campaign: [Brand] - Prospecting - CBO - [Winning Audience]
── Ad Set 1: UGC/testimonial concept (3–4 variations)
── Ad Set 2: Problem/solution concept (3–4 variations)
── Ad Set 3: Product demo / offer concept (3–4 variations)
```

Let CBO shift budget to winning concepts. Give each concept 7–10 days minimum. When a concept wins, produce more variations of it; when it dies, replace with a dramatically different concept. **Transition trigger to Phase 3: 50+ purchases/week consistently.**

### Phase 3: Automated Scaling (Advantage+ Shopping)

Proven offer, seasoned pixel, 50+ purchases/week. One Advantage+ shopping campaign with 5–10 proven creatives plus catalog, existing-customer budget cap set (10–20%). See meta-advantage-plus.

## Recommended Account Architecture

```
── Campaign 1: Retargeting (start here)
 ── Website visitors / viewed product / add-to-cart (7–30d)
 ── Engagers (IG/FB, video 50%+)
 ── Dynamic catalog ads (viewed or added, not purchased)
 Budget: 10–20% of total. Objective: Sales. Exclude purchasers 30–60d.

── Campaign 2: Prospecting - Validation (ABO, temporary)

── Campaign 3: Prospecting - Scaling (CBO or Advantage+)
 Main budget lives here (70–85%). Objective: Sales / Purchase.

── Campaign 4: Retention / VIP (optional, capped)
 ── Past purchasers: launches, replenishment, VIP offers
 Budget: 5–10%. Only if email/SMS can't reach them.
```

## Build Order

- **Month 1 — Retargeting:** lowest risk, warm traffic, proves the pixel and funnel work before committing prospecting budget. Small spend (audiences are small).
- **Month 2–3 — Prospecting:** Phase 1 validation (2–4 weeks) → Phase 2 creative scaling. This is where the majority of budget goes.
- **Month 4+ — Scale + Advantage+ + high-value segments:** move proven offers to Advantage+ at volume; add VIP/high-LTV plays (see meta-high-value-audiences).
- **Month 12+ — Expansion:** once your most in-market buyers are converted or aware, expand to colder segments. Message shifts from "buy now" offers to story-led ads that create demand.

Typical spend band per phase, so you can see which phase you are actually in regardless of the calendar: Month 1 **$500–2,000** · Month 2–3 **$2,000–5,000** · Month 4+ **$5,000–15,000** · scaling **$10,000–30,000** · mature **$20,000+**. A brand at $1,500/month running Advantage+ and three prospecting ad sets is running Month 4 structure on Month 1 budget, which is the most common structural error in young accounts.

**Don't launch on a Friday.** Learning runs through a weekend with nobody watching, and the first decision point lands on Monday with two days of unmonitored delivery already spent.

## Key Settings Reference

**Optimization events:**

| Event | When | Volume needed |
|-------|------|---------------|
| Purchase | Default for ecom | 50/week/ad set |
| Add to Cart / Initiate Checkout | Low purchase volume; temporary stepping stone | 50/week |
| Landing Page Views | New account, cold pixel only | 50/week |

Meta needs ~50 events/ad set/week to exit learning. If you can't hit 50 purchases, consolidate ad sets before downgrading the event — one big ad set beats three starving ones.

**Minimum daily budget = (Target CPA × 50) ÷ 7.**

**Minimum monthly budget by campaign type** — below these, the campaign type isn't wrong, it's unreachable:

| Campaign type | Monthly floor | Why |
|---|---|---|
| Retargeting | $500–1,500 | Small audience, high conversion rate; a little goes far, but under $500 frequency spikes before volume arrives |
| Prospecting (ABO) | $2,000–5,000 | Each ad set needs its own 50 weekly events; ABO multiplies the requirement by the ad set count |
| Prospecting (CBO) | $5,000–15,000 | One budget clears learning faster, but needs enough to feed several ads without starving any |
| Advantage+ Shopping | $5,000+ | Automation needs volume to learn from; below this it never leaves learning |

**Budget reallocation signals:**

| Signal | Action |
|---|---|
| One audience producing 3×+ better new-customer quality at similar CAC | Shift budget toward it, don't just note it |
| Learning phase not exiting after 2 weeks | Consolidate ad sets, raise the budget, or downgrade the optimization event — in that order |
| Retargeting share drifting above 20% of spend | Rebalance to prospecting; retargeting scales its reported ROAS, not the business |
| A campaign at its audience ceiling (frequency > 3.5, CPM climbing) | Stop adding budget here; add creative or widen the audience first |

**Cross-channel budget split by total spend** — how many channels you can actually run:

| Monthly paid budget | Split |
|---|---|
| $5–10K | 100% one channel. Spreading thin means nothing clears learning |
| $10–25K | 60–70% primary / 30–40% secondary |
| $25–50K | Three channels, with the third capped as a test |
| $50K+ | Full mix plus a standing test budget |

**Naming convention.** Campaign, ad set and ad names flow into the UTM string via dynamic parameters, so **the naming convention *is* your analytics taxonomy** — a sloppy ad name becomes a sloppy `utm_content` you can't group on for the life of the account. Three levels:

```
Campaign: [Brand] - [Funnel Stage] - [Budget Type] - [Audience/Detail]
 Brand - Prospecting - CBO - Broad
 Brand - Retargeting - CBO - ATC 14d

Ad set: [Audience Source] - [Targeting Detail]
 LAL1pct-VIP - AdvPlusPlacements
 Retarget-ATC14d - Broad

Ad: [Format] - [Concept] - [Offer] - [Date]
 UGC-Video - Founder-Story - NoOffer - 2026-08
 Static - BeforeAfter - 20pctFirstOrder - 2026-08
```

The **ad-level** convention is the one that pays off later: it is what makes format and concept rollups possible across the account (see creative-taxonomy). Retrofitting it is not possible — historical names are what they are.

**Cross-channel retargeting via UTM.** Build a website custom audience on `utm_source` contains a value, and you can retarget traffic from any other channel — Google Shopping, TikTok, an email click, a creator's link — on Meta. Those visitors were precision-targeted by the originating channel and already know the brand, so they typically convert at retargeting rates while costing far less to reach than a cold prospecting impression. Requires the UTM discipline above to be in place first; see **analytics** for the parameter setup.

## Dynamic Retargeting by Funnel Depth

One retargeting ad set for "site visitors" wastes the best signal you have. Segment by how far down the funnel they got, because the right message differs at each depth:

| Segment | Window | Message |
|---|---|---|
| Checkout initiated | 3–7 days | Remove the last obstacle: shipping, returns, payment options. Rarely needs a discount |
| Added to cart | 7–14 days | The product itself, plus one reason to act now |
| Viewed product | 14–30 days | Category-level or best-seller framing; they weren't close |

Rules:

- **Windows beyond 14 days risk serving ads for items already bought elsewhere** — or already bought from you, if exclusions are stale. Keep same-SKU purchaser exclusions current.
- **Collection and carousel beat single-image dynamic product ads** for e-commerce retargeting. A catalog ad that shows one product is a catalog ad wasting its catalog.
- **Frequency-cap retargeting separately from prospecting.** A small audience at prospecting frequency settings becomes an irritation within a week.

## What to Avoid

- Mixing prospecting and retargeting in one campaign (retargeting steals credit and budget)
- CBO during audience validation
- Editing campaigns mid-learning phase (resets the 50-conversion counter)
- More than 5–6 ad sets per campaign (dilutes signal)
- Optimizing for Link Clicks or Traffic — vanity events; optimize for Purchase
- Judging prospecting on blended ROAS — use new-customer CAC and MER

## Related Skills

- **analytics**: The UTM parameter setup that makes this naming convention readable downstream, and GA4 channel grouping.
- **meta-ads**: The e-commerce Meta hub — overall Meta strategy, audiences, creative, and optimization.
- **meta-campaign-creation**: Building this structure on a live account via the Meta Ads MCP — audiences, campaigns, ad sets, creatives, ads.
- **meta-advantage-plus**: When and how to hand a proven structure to Advantage+ shopping automation.
- **meta-high-value-audiences**: The VIP/high-LTV plays layered on in Month 4+.
- **ads-campaign-planning**: The end-to-end campaign plan (objectives, offers, budget, measurement) this structure executes.
