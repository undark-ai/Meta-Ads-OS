---
name: full-audit
description: Run the complete e-commerce Meta Ads account audit end to end across all 30 audit sections, using the Meta connector, commerce and analytics connectors, the Ad Library, browser inspection, specialist agents and persistent audit artifacts. Sweeps every section in one pass and records a coverage ledger rather than stopping at the first missing input. Also use when the user says "audit my Meta account," "full Facebook ads audit," "Meta ads account review," or "what's wrong with my Meta ads."
---
# Full account audit

A full audit is a **single top-to-bottom sweep of all 30 sections below**, not a conversation in
which depth is added only when the user asks for it. If the first pass leaves the user to
discover that creative, the pixel, the catalog or incrementality were never queried, the audit
failed — regardless of how good the findings that *were* produced are.

## What this audit is for

One question, and every section serves it:

> **Which creative + product + offer combinations are generating incremental profitable
> customers, and how much more can we scale them?**

Meta is `Creative → Attention → Desire → Click → Product → Purchase → LTV`. A technically
perfect account with mediocre creative still struggles, so four sections and roughly a third of
the effort go to creative — and the creative output is a **learning system**, not a list of
winning ads.

## The completeness rule

Every section carries one of these five states, and the state is **written down**:

| State | Meaning |
|---|---|
| `FINDINGS` | Ran; produced findings. |
| `CLEAN` | Ran; nothing wrong found. Say so explicitly — a clean result is a result. |
| `DEGRADED` | Ran on partial data. State what was missing and what the partial result still supports. |
| `N/A` | The layer does not exist in this account (e.g. no catalog, no retargeting). Not the same as blocked. |
| `BLOCKED` | An input is genuinely unavailable. Name the input, the reason, and what it would have answered. |

Never leave a section unstated. "I didn't get to it" is not one of the five.

## Setup

0. **Preflight (`audit-preflight`) — before anything else.** Two questions, asked up front and
 never after: does `.agents/product-marketing.md` exist and is it current, and are the
 connectors this audit needs actually connected? Preflight **offers, it never blocks** —
 "proceed as-is" is always valid and is recorded in `preflight.md`. Discovered mid-run these
 become caveats; asked up front they are the user's decision.
1. Create a unique audit run directory (`audit-artifacts`).
2. **Discover sources through the full connector ladder** (`mcp-discovery`). No source is
 `UNAVAILABLE` until the native connector, gateway/aggregator connectors, the commerce
 platform as proxy, and asking the user have all been tried. Record the rung that supplied
 each source.
3. **Confirm the account.** Most brands have one live account plus legacy and test accounts.
 `is_ads_mcp_enabled: false` beats `is_queryable: true` — an account can report queryable and
 still be un-queryable. Confirm the account has spend in the intended window before anything
 else runs; a dormant account is a preflight answer, not a §5 mystery.
4. Establish store, country, currency, **account timezone** (frequently not the store's),
 attribution setting and audit period. One attribution window for the whole run, stated in
 `scope.md` and in the header of every dataset.

## The 30 sections

| § | Section | Agents | What it must establish |
|---:|---|---|---|
| 1 | Business & economics — **gate** | **7**–16, 20 | One primary goal, and the canonical economics every other section consumes: AOV, gross and contribution margin, CAC target, break-even CAC and ROAS, LTV, new-vs-returning economics, hero and high-margin products, promo calendar, seasonality, geo priorities |
| 2 | Tracking & measurement — **gate** | 21–36 | Whether purchases are counted once, at the right value, with enough match quality to optimise on — pixel, CAPI, dedup, EMQ, purchase value and currency, content IDs, catalog matching, the funnel events, event priority and AEM, domain verification, attribution settings, UTMs |
| 3 | Reconciliation — **mandatory** | **37**–42 | Meta's claim against banked orders. Runs before any economic conclusion |
| 4 | Account structure | 43–46, 50 | Fragmentation, overlap, duplicated budgets, ABO/CBO placement, and whether consolidation would improve learning |
| 5 | Campaign performance & trend windows | 3, 4, 51–54, 148–150 | The full metric set per campaign across 7/30/90/365 and YoY, mapped onto change history (`campaign-rca` — which confirms a move is real before anything is root-caused). A trend without a change map is a chart, not a finding |
| 6 | Bidding, delivery & learning phase | 55–58 | Whether the bid strategy matches conversion volume and the §1 goal, and which ad sets are in learning (`bid-strategy-and-learning`) — an ad set that re-entered learning is not reporting a creative verdict |
| 7 | Creative inventory & database | **59**–64 | Builds `creative-database.csv` and renders the **Top Creatives dashboard**. Everything creative downstream reads this file and nothing re-queries |
| 8 | Creative fatigue | 65–70 | Which ads are decaying and which are evergreen; frequency, CTR decay, CPM rise, CPA rise, ROAS decline, performance by creative age; the refresh cadence the account actually needs |
| 9 | Creative angle & hook analysis | **71**–75 | Which hook, problem, benefit, product, proof point, objection, format, creator, opening three seconds, CTA, offer and persona win — and specifically which win *purchases* rather than clicks. **Includes `ad-copy-audit`**: the primary text, headline and CTA the account is actually running, scored and joined to what each ad earned, with rewrites where copy is the plausible constraint. Where an ad is below the purchase floor, `leading-and-lagging-signals` governs what a faster metric is allowed to conclude |
| 10 | Creative testing system | 76–78 | Whether a repeatable engine exists: concepts, hooks, angles, creators, formats and offers per month; iteration ratio; testing velocity and budget; winner and kill criteria (a spend-loss cap is a budget action, not a creative learning — `leading-and-lagging-signals`); whether learnings are written down |
| 11 | Relevance & auction diagnostics | 79–82 | Quality, Engagement Rate and Conversion Rate Ranking; auction overlap; ad quality; what is actually driving CPM |
| 12 | Audience strategy | 83–89, 92 | The audience layer and its hygiene, plus who actually converts (`audience-insights-mining`) — broad, Advantage+ Audience, interest, lookalikes, customer lists, website audiences, exclusions, overlap, size and saturation |
| 13 | Prospecting | 93–96 | Spend share, broad vs interest vs lookalike, new-customer CAC and ROAS, creative × audience interaction, and audiences that look strong but are not incremental. Classify the spend by the job it does (`demand-lifecycle`): Create and Capture are both "prospecting" and answer to different numbers |
| 14 | Retargeting | 97, 98 | Window laddering, existing-customer exclusion, frequency, retargeting CAC and ROAS, and whether the account is paying to reach people who were going to buy anyway. `demand-lifecycle` splits this into Accelerate, Revive and Expand — Expand spend competing with an owned email channel is waste dressed as performance |
| 15 | Frequency & saturation | 90, 91, 100 | Saturation by campaign, audience and creative. Distinct from §8: audience saturation and creative decay have different fixes |
| 16 | Product catalog | 101–108 | Feed health, disapprovals, product IDs, pixel↔catalog matching, product sets, out-of-stock exposure (`catalog-health`) — including item-ID stability, price parity and error trend, the three that break campaigns silently |
| 17 | Advantage+ Shopping & Advantage+ Creative | 109–114 | ASC structure, the existing-customer budget cap, new-customer acquisition, catalog integration — and **cannibalisation of manual campaigns**, checked first (`advantage-plus-audit`). A+ Creative enhancements audited separately: they change the creative you thought you tested |
| 18 | Placement analysis | 115–118 | Placement economics after CVR, AOV and new-customer rate, not last-click ROAS (`placement-economics`). Star / hidden gem / waste, and exclusion tested by duplication rather than an edit |
| 19 | Funnel audit | 119, 124, 126 | Impression → 3-sec → click → LPV → PV → ATC → IC → purchase, by campaign, creative, product and device. Leaks ranked by **absolute lost orders**, not by rate. **Also run the same funnel per channel from GA4** — Meta beside Google Ads and organic — because a leak present in every channel is the site, and one present in Meta alone is the traffic. Output includes rendered charts, not only tables |
| 20 | Landing pages & post-click CRO | 120–123, 125, 127, 128 | Creative→page message match, mobile UX, speed, photography, reviews, social proof, pricing, shipping, returns, trust, CTA, ATC and checkout |
| 21 | Offer audit | 129–133 | Discounts, bundles, free shipping, BXGY, volume, subscription, guarantees, urgency — and offer × creative × audience × product |
| 22 | Product & SKU economics | 17–19 | Spend, revenue, margin, repeat value and CAC by SKU, plus which products *acquire* customers worth keeping (19). "Which product" is one of the three axes of the core question |
| 23 | Geographic & device economics | 134–137 | Profitability by geography after shipping cost, and by device and platform. Both end in a profitability call, not a volume call |
| 24 | New vs returning & the LTV loop | 99, 138 | Whether reported ROAS is inflated by existing buyers, and whether first-party value data flows *back* into Meta — value-based lookalikes, customer lists, offline conversions. Revive and Expand economics from `demand-lifecycle` are read here, not against acquisition CAC |
| 25 | Attribution | 139–141 | Window choice, view-through share, modelled share, and Meta against GA4, Shopify and the CRM |
| 26 | Incrementality | **142**–144 | Demand created versus demand harvested. Geo tests, holdouts, conversion lift, organic and direct interaction, prospecting vs retargeting incrementality. **Create versus Capture (`demand-lifecycle`) is this distinction made structural** — map every campaign onto a stage before ranking anything on reported ROAS |
| 27 | Competitive & Ad Library | 145–147 | What competitors are running — angles, offers, formats, longevity — and the angle gaps this account has never tested |
| 28 | Hygiene, Business Manager & permissions | 47–49, 151, 152 | Old and duplicate campaigns and audiences, broken URLs, rejected ads, expired promos, wrong UTMs, naming conventions, permissions, BM setup, domain verification |
| 29 | Budget allocation & the next dollar | 153–155 | Underfunded winners, overfunded campaigns, diminishing returns, and where the next dollar goes — with `scaling-methods` for how to move it once the scale matrix says where |
| 30 | Final output | 5, 6, **156**–**162** | Scorecard, opportunity matrix, **scale matrix**, 30/60/90 plan, quantified upside, executive page |

Sections may run in parallel where they have no dependency, but **§1 precedes everything
economic, §2 precedes every attribution claim, §3 precedes any economic conclusion, and §30
runs last.**

## Gates that order, but never stop, the sweep

**Measurement (§2) precedes economics (§1's downstream use and §22).** If purchase truth is
materially compromised, that **lowers the confidence label on every downstream economic claim
and is reported prominently — it does not end the audit.** Continue and mark affected findings
`DEGRADED`.

Produce a measurement verdict:

- `GREEN` — purchase measurement is trustworthy enough to optimise on
- `YELLOW` — usable with explicit caveats
- `RED` — optimisation economics cannot be trusted

`RED` **orders** the audit; it does not end it. Continue every other section, but do not issue
scale or kill recommendations that depend on conversion values you have just shown to be
unreliable.

**Reconciliation (§3) is mandatory.** Load `cross-source-reconciliation`. Set Meta's claimed
purchases and value against banked orders from the commerce platform, and GA4 where present,
over the same window, timezone and currency. Align first — conversion date vs order date, gross
vs net, refunds, attribution window and model, which events count — then compute and publish:

| Measure | Definition |
|---|---|
| Order claim ratio | Meta-claimed purchases ÷ store orders |
| Value claim share | Meta-claimed value ÷ store revenue |
| Blended MER | store revenue ÷ **total** ad spend, all channels |
| Implied AOV | Meta-claimed value ÷ Meta-claimed purchases, against store AOV |
| Modelled share | share of Meta-claimed purchases Meta modelled rather than observed |

Blended MER uses **total** ad spend. Enumerate every paid channel first: computed on Meta's
spend alone it is wrong, not merely partial, and two platforms each claiming the same order is
only visible when their claims are summed.

Classify every compared metric `MATCH`, `EXPLAINED GAP`, `UNRESOLVED GAP` or
`INVALID COMPARISON`. **Never let an unreconciled ROAS reach the executive page.**

**Missing cost inputs never stop the run (§1).** Derive margin from the commerce platform; else
ask the user without stalling the sweep; else proceed on a clearly labelled assumption and
publish break-even ROAS as a range across the plausible margin band — stating whether the
recommendation changes across that range. Usually it does not, and the decision is safe without
the exact figure. Withhold only what genuinely depends on margin: break-even ROAS, CAC ceiling,
scale and kill calls.

## The creative spine

§7 writes `audits/<run-id>/creative-database.csv` once, against
`schemas/creative-record.yaml`. **Sections 8–11, 19, 22 and 30 read that file. Nothing
re-queries Meta for creative performance.** A dashboard and a findings list that disagree are
worse than either alone, and they disagree the moment two components pull their own data with
slightly different windows.

§7 also renders the **Top Creatives dashboard** (`creative-dashboard`) — cards ranked by spend,
purchases, ROAS, hook rate or hold rate; Performance / Attention / Funnel tabs; a creative
patterns table; and a per-ad drill-down with the funnel path against account medians and the
promise-handoff score against the landing page. Check its headline numbers equal §5's campaign
totals; if they diverge, something re-queried instead of reading the file.

Rule-based creative tagging runs off the account's **ad-naming convention**. Discover it in §7,
report spend-weighted compliance in §28, and treat non-compliance as load-bearing rather than
cosmetic: names that do not parse cannot be learned from. Where names do not parse, tag by
model and mark the classification source — a §9 conclusion built on model-inferred angles
carries lower confidence than one built on a parsed convention, and the reader must be able to
tell which they are reading.

## Coverage ledger

Write `audits/<run-id>/coverage.md` listing all 30 sections with their state, the sources used,
and — for `DEGRADED` and `BLOCKED` — the missing input and its consequence.

**Derive the tally from the rows; never write it from memory.** Count the states
programmatically and check the total is 30. A hand-written summary line drifts from the table
beneath it, and because it is the first thing a reader trusts, a wrong one discredits the
ledger it summarises. Where the ledger is also published elsewhere — the dashboard, a slide —
check the two agree.

## Sizing the pull

Completeness is about **sections covered**, not rows fetched.

- Reconcile every breakdown against its parent total. If ad rows do not sum to the campaign
 total, rows are missing.
- One breakdown dimension per call. Meta rejects some combinations and silently changes totals
 across others.
- Never average a ratio across entities. Recompute CTR, ROAS, frequency, hook rate and CVR from
 component sums at the level you want.
- One attribution window for the whole run. A row on a different window is dropped, not
 silently included.
- Batch queries; expect `DEGRADED` on late sections under rate limits rather than failing the
 run.

## Statistical honesty

Volume gates conclusions (`learning-phase-and-significance`). Meta's own learning threshold is
roughly 50 conversions per ad set per week; an ad with four purchases has not told you anything
about its angle. Below the purchase floor the verdict is `INSUFFICIENT_DATA`, and the next step
is to buy more data rather than act on what you have.

Most individual ads sit below that floor for their whole life, so `INSUFFICIENT_DATA` on every
ad would be an abstention rather than an audit. `leading-and-lagging-signals` is what runs
instead: a faster signal may rank and triage, but may only carry a verdict where it has been
**validated on this account** to predict purchases — correlation and n quoted at the point of
use, `INFERRED` and never `OBSERVED`. A leading signal improving while the lagging one worsens
is not a mixed result; it is evidence the leading signal was gamed.

Check learning-phase state before attributing any performance movement to creative. An ad set
that re-entered learning after an edit is reporting the edit, not the ad.

`ads_account_get_activity_logs` is not available on every account — Meta rolls it out gradually,
and an account without it returns an explanatory error rather than data. That does not excuse
skipping the check, and it does not stop the sweep. Degrade: derive what `created_time` and
`effective_status` support, say in each affected finding that movement cannot be tied to an edit,
cap decay and trend confidence at `MEDIUM`, and withhold kill calls that rest on decay alone. §6
closes `BLOCKED` where bid strategy and learning state cannot be read at all; §§5, 8 and 9 close
`DEGRADED` rather than `FINDINGS`. Record it in `source-capabilities.md` like any other source.

Modelled and inferred values are never presented as observed. Meta's assertions about Meta —
opportunity score, relevance rankings, EMQ, vendor lift estimates — are `PLATFORM_STATED`:
reportable, never proof.

## Deliverables

`preflight.md` · `coverage.md` · `creative-database.csv` · `top-creatives.html` ·
`reconciliation.md` · `scorecard.md` (156) · `opportunity-matrix.md` (157) ·
`scale-matrix.md` (158) · `action-plan.md` (159) · `quantified-upside.md` (160) ·
`executive-summary.md` (162) · evidence appendix.

This audit never changes the account. Where a finding warrants a change, the deliverable is a
recommendation; applying it is a separate, deliberately-started execution run governed by
`EXECUTION-PROTOCOL.md`.
