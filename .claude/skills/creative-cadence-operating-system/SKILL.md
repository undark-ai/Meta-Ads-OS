---
name: creative-cadence-operating-system
description: "When the user wants a creative production and iteration system for an e-commerce or D2C Meta account — the iteration priority hierarchy, concept sourcing from reviews and post-purchase surveys, image-first validation, testing volume math, format lifespans, and refresh cadence. Also use when the user mentions 'creative cadence,' 'how many ads should I test,' 'creative production,' 'creative iteration,' 'creative pipeline,' 'hook rate,' or 'how often should I refresh creative.' For diagnosing when live ads are dying and rotation thresholds, see creative-fatigue-detection. For the angles and concepts themselves, see meta-creative-strategy. For bulk ad copy generation, see ad-creative."
metadata:
 version: 1.1.0
---

> **Marketing layer — advisory, not evidence.** Every benchmark, threshold and rule of thumb
> below is build-time guidance. Per `CLAUDE.md`, a marketing skill's number is never evidence
> for a quantified finding: a recommendation that originates here still needs a number, source,
> date range, formula, evidence class and confidence from the audit layer before it can be
> presented as one. Handoffs run audit → marketing, never the reverse.


# Creative Cadence Operating System — D2C Meta

The system for what creative to build, when to build it, how to iterate, and when to retire it. Creative accounts for the majority of ad performance on Meta post-Andromeda: the algorithm uses your creative as the primary signal for who to serve. **Your creative is your targeting. Your hook is your filter. Your iteration velocity determines your scaling ceiling.**

## Before Starting

**Check for product marketing context first:**
If `.agents/product-marketing.md` exists (or `.claude/product-marketing.md`, or the legacy `product-marketing-context.md` filename, in older setups), read it before asking questions. Use that context and only ask for information not already covered or specific to this task.

Gather this context (ask if not provided):
- Monthly testing budget and target CPA (needed for the production math)
- Current creative library: how many proven ads, what formats, how old

## 1. The Iteration Priority Hierarchy

When iterating on a winning ad, change elements in this order:

| Priority | Element | Impact |
|---|---|---|
| 1 | **Hook** (first 3 seconds / first line) | Highest — ~90% of viewers decide in 3 seconds. Changing the hook changes who the ad reaches. |
| 2 | **Visual treatment** | High — faces lift engagement; 4:5 typically outperforms other Feed ratios. The visual stops the scroll. |
| 3 | **Format** (static/video/carousel/UGC) | Medium — format changes read as a "new ad" to the algorithm and change lifespan. |
| 4 | **Body copy / CTA** | Lower — once hooked, body copy matters less than the capture. |

**Hook targets:** hook rate (3s views ÷ impressions) 20-25%+. Below 15%, the ad will never perform regardless of body quality. Swapping the hook on a winner can extend its life 2-4 weeks.

**Hooks that work for D2C:** provocative question ("Why does your 'clean' detergent have 12 unpronounceable ingredients?"), specific pain ("Your leggings go see-through at squat depth"), counterintuitive claim ("Cheap sunscreen is why your serum isn't working"), social-proof lead ("47,000 five-star reviews later…"), number-first (numbers in the first line lift CTR 20-30%). For named headline techniques to generate hook variants, see ad-headline-techniques.

## 2. Concept Sourcing System

Source 15-25 customer situations before creating ads. Priority order:

| Source | Signal |
|---|---|
| Organic/creator winners (last 12 months) | Market-validated message — repurpose as paid |
| Post-purchase surveys | "What almost stopped you?" = objections; "what convinced you?" = hooks |
| Product reviews (yours + competitors') | Real customer language, verbatim |
| Support tickets & DMs | Active pain points and confusion |
| Meta Ad Library | Competitor ads running 3+ months are likely profitable — steal angles, not creative |
| TikTok/Reddit/community threads | How your category is actually talked about |

### Image-First Concept Validation

Test new concepts as static images before investing in video: statics take hours not days, so you test more concepts per cycle. A concept that fails as an image would likely fail as video too. Once an image concept proves itself (delivers, produces purchases at acceptable CAC), iterate it into video, carousel, and UGC versions and scale the best format. **Skip image-first** for inherently video-native concepts: UGC testimonials, demos, texture/ASMR content.

### The 50/30/20 Production Split

50% of production = iterations on top performers; 30% = iterations on other performers; 20% = completely new concepts. Plan ~10 variations per proven ad over its lifespan.

## 3. Production Math

- **Tests per month** ≈ testing budget ÷ (3 × target CPA). Each test needs ~3x target CPA in spend before judging.
- **Win rates:** iterations on winners ~25% (1 in 4); brand-new concepts ~10% (1 in 10); blended ~1 in 6.
- **Proven ads needed:** each proven ad absorbs only so much monthly spend before frequency causes fatigue — you cannot scale budget ahead of creative supply. If you want to double spend, first close the creative deficit.

## 4. Format Playbook

| Format | Lifespan | Notes |
|---|---|---|
| Static image | 14-28 days | 4:5 for Feed, 9:16 for Stories. Refresh headline on same visual = 7-14 extra days. Meta flags near-duplicates — changes must be visually distinct. |
| Video (<30s) | 21-35 days | Captions always on (most watch muted). <30s prospecting, up to 60s retargeting. Swap the opening hook to extend life. |
| Carousel | 21-35 days | 3-5 cards; first card must stand alone. Reordering cards reads as "new" to the algorithm. |
| UGC / creator | 28-42 days (longest) | Authenticity fatigues slower. Record 3-5 creators at once; edit into 10+ hook/cut variations = built-in rotation. |

## 5. The Production Pipeline

Testing volume is a throughput problem, and throughput fails on handoffs rather than on ideas.

**Brief → design → review → launch → log.** Five stages, each with an owner and a definition of done:

| Stage | Done when |
|---|---|
| Brief | The concept, hook, format, offer and the persona/situation it targets are written down. A brief without a named situation is a mood board |
| Design | Assets exist for every placement group the ad set runs — no auto-cropping |
| Review | Claims are substantiated, copy passes house style, AI-generated imagery is labeled |
| Launch | Built paused, previewed, then activated. Naming convention applied at ad level |
| Log | The row below is filled in, the day it launches, not retroactively |

**Asset tracking schema.** One row per test, in whatever the team already uses:

`test name · hypothesis · concept/angle · format · offer · channel · launch date · budget spent · result · learning`

The `learning` column is the only one that compounds. A log with results and no learnings is a spreadsheet of dead ads.

**Hypothesis template:** *"If we do X, then I believe Y, as measured by Z."* If Z isn't a metric you can pull, the test isn't a test.

**Prioritize the backlog with RICE**, each dimension 1–5 (Reach, Impact, Confidence, Effort — where 1 is *low* effort). Score, sort, pull from the top. Without a scored backlog, production defaults to whatever was suggested most recently.

**Avoid the activity trap.** Shipping tests is not the goal; accumulating learnings is. A month of 20 launches with no recorded learning is a month with no progress, and it looks identical to a productive month on every dashboard.

**Budget-derived ad count.** Every ad needs enough daily spend to generate **3–4 clicks a day** or it gathers no signal at all. Don't create more ads than the budget can serve — this is the same constraint as the ad-count ceiling in meta-ads-operating-system, expressed from the production side.

## 6. The Testing Cadence

| Action | Frequency |
|---|---|
| Check delivery on new tests (is spend distributing?) | Day 5-7 after launch — swap ads getting under half their fair share |
| Launch iterations on top performers (hook first) | Every 2 weeks |
| Launch completely new concepts (as statics) | Monthly minimum |
| Retire depleted ads | When CTR drops 30%+ from peak or frequency > 5 |
| Check fatigue signals (frequency, CTR, CPM trends) | Weekly — see creative-fatigue-detection for the full diagnostic |
| Full refresh: re-audit customer situations, new angles | Quarterly |

Judge tests on cost per new customer / ROAS vs break-even — not CTR or CPC. Minimum 3x target CPA in spend and ~14 days runtime before verdicts.

### What to Build When an Ad Fails

| Failure | Build Next |
|---|---|
| No delivery | Different hook/visual/format — the audience never saw your copy |
| Clicks but no purchases | Wrong audience or broken promise — change the pain point or fix the ad-to-PDP match |
| Purchases but CAC too high | Right angle, wrong execution — same angle, new hook/format |
| Buyers but low AOV / no repeats | Attracting deal-seekers — reduce discount-led framing, add product-value angles |
| Fatigue | New hook + different format + different creator/colorway |

## Related Skills

- **meta-creative-strategy**: The angles and concepts this system produces and iterates — creative-as-targeting, customer situations, concept types.
- **creative-fatigue-detection**: The diagnostic side — fatigue signals, frequency thresholds, and rotation rules for the ads this system feeds.
- **message-validation**: Scoring ads by the customer quality they produce (AOV, repeat rate) before scaling variations.
- **meta-ads**: The e-commerce Meta hub — campaign structure, audiences, and account-level strategy around the creative engine.
- **ad-creative**: Bulk, platform-agnostic ad copy and headline generation to fill the production pipeline.
