# Agent index

Agents are addressed **by number** — workflows, the orchestrator and the dependency map all
reference them that way, so numbers are stable and existing agents are never renumbered.

Run order is not numeric order. The orchestrator runs the 30 sections defined in
[`.claude/skills/full-audit/SKILL.md`](.claude/skills/full-audit/SKILL.md): business context and
economics first, then the **measurement** gate, then the mandatory **reconciliation**, then the
diagnostic bands, with the output band last. A scale recommendation built on untrustworthy
conversion data is worse than no recommendation — so the gates order the sweep, and never stop
it. See [`workflows/02-full-account-audit.md`](workflows/02-full-account-audit.md).

**Every agent maps to one of the 30 sections.** An agent no section owns will never run in a full
audit, and will look present while doing nothing — which is why `section:` is a required
frontmatter field and `scripts/validate-agent-library.sh` checks it.

## The two lanes

<!-- execution-boundary: documents-writes -->
<!-- the execution shipped table names the write surface each operator owns. -->

| Range | Lane | Meta tools | Frontmatter |
|---|---|---|---|
| 00–199 | **Audit** — read-only | the 61 classified `read` | `tools: Read, Glob, Grep, Bash` · `disallowedTools: Write, Edit` |
| 200+ | **Execution** — mutates | `read` + the 41 `write`, under the protocol | `lane: execution` · loads `meta-execution-protocol` |

`scripts/validate-execution-boundary.py` fails the build if an audit agent so much as references
a write tool. Unclassified tools are treated as writes — fail closed.

## Bands

| Band | # | Owns sections | Purpose |
|---|---|---|---|
| Meta / QC | 00 | — | Library quality control. Reviews the other agents; never an ad account |
| Orchestration | 01–06 | 0, 5, 30 | Full-audit orchestrator, preflight, delivery blockers, opportunity score, quick wins, audit report |
| Context & economics — **gate** | 07–20 | 1, 22 | The one primary goal, and the canonical economics every other section consumes |
| Measurement — **gate** | 21–36 | 2 | Pixel, CAPI, dedup, EMQ, event priority, AEM, domain verification, attribution settings, UTMs |
| Reconciliation | 37–42 | 3 | Meta's claim against banked orders. Runs before any economic conclusion |
| Structure | 43–50 | 4, 28 | Fragmentation, overlap, ABO/CBO, hygiene, Business Manager, permissions |
| Delivery & bidding | 51–58 | 5, 6 | Bid strategy, learning phase, budget constraint, delivery blockers |
| Creative | 59–78 | 7, 8, 9, 10 | The creative database, the dashboard, fatigue, angle analysis, the testing engine |
| Relevance | 79–82 | 11 | Quality / Engagement / Conversion Rate Ranking, auction overlap, CPM decomposition |
| Audience | 83–92 | 12, 15 | Broad, Advantage+, interest, lookalike, custom lists, exclusions, overlap, saturation |
| Prospecting & retargeting | 93–100 | 13, 14, 24 | New-customer economics, window laddering, over-retargeting, the LTV loop |
| Catalog | 101–108 | 16 | Feed health, disapprovals, product IDs, pixel↔catalog matching, out-of-stock exposure |
| Advantage+ | 109–114 | 17 | ASC structure, existing-customer cap, A+ Creative, cannibalisation of manual campaigns |
| Placement | 115–118 | 18 | Placement economics after CVR and AOV; exclusion tests that don't reset learning |
| Funnel & CRO | 119–128 | 19, 20 | Leak sizing in lost orders, message match, mobile UX, PDP, cart, checkout |
| Offer | 129–133 | 21 | Discounts, bundles, thresholds, subscription; offer × creative × audience × product |
| Geo & device | 134–137 | 23 | Profitability after shipping cost, by geography and by device |
| Attribution & incrementality | 138–144 | 25, 26 | Window choice, view-through, modelled share; demand created vs harvested |
| Competitive | 145–147 | 27 | Ad Library angle inventory and the gaps this account has never tested |
| Trend & change | 148–151 | 5, 28 | 7/30/90/365 and YoY, mapped onto change history |
| Budget allocation | 152–155 | 29 | Underfunded winners, diminishing returns, where the next dollar goes |
| Output | 156–162 | 30 | Scorecard, opportunity matrix, **scale matrix**, 30/60/90, quantified upside, executive page |
| **Execution** | 200–213 | — | Build, audience, budget, catalog and rules operations under the protocol |

Creative carries 20 agents and measurement 16 — which is where this library's shape differs most
from its Google counterpart, and it is deliberate: a third of a Meta audit is creative, and
measurement is what everything else is judged on.

## Shipped (Phase 1)

| # | Name | File | Section | Depends on | Declared skills |
|---:|---|---|---:|---|---|
| 00 | `00-agent-quality-controller` | [`00-agent-quality-controller-agent.md`](agents/00-agent-quality-controller-agent.md) | — | — | `full-audit` |
| 01 | `01-full-account-audit` | [`01-full-account-audit-agent.md`](agents/01-full-account-audit-agent.md) | — | 02 | 21 skills — the orchestrator's full context |
| 02 | `02-audit-preflight` | [`02-audit-preflight-agent.md`](agents/02-audit-preflight-agent.md) | — | — | `audit-preflight`, `mcp-discovery`, `meta-ads-mcp` |
| 03 | `03-delivery-blockers` | [`03-delivery-blockers-agent.md`](agents/03-delivery-blockers-agent.md) | 5 | — | `meta-ads-mcp`, `meta-ads-data-validation` |
| 04 | `04-opportunity-score` | [`04-opportunity-score-agent.md`](agents/04-opportunity-score-agent.md) | 5 | — | `meta-ads-mcp`, `delivery-diagnostics` |
| 05 | `05-quick-win-ranking` | [`05-quick-win-ranking-agent.md`](agents/05-quick-win-ranking-agent.md) | 30 | diagnostic sections | `recommendation-prioritization`, `14-day-change-control`, `contribution-margin` |
| 06 | `06-audit-report` | [`06-audit-report-agent.md`](agents/06-audit-report-agent.md) | 30 | 05, 156–162 | `coverage-ledger`, `recommendation-prioritization`, `scale-matrix`, `cross-source-reconciliation` |

## Shipped (Phase 3) — the execution lane (200–213)

The band that can change a live account. Every agent here declares `lane: execution` in
frontmatter and loads `meta-execution-protocol`; `scripts/validate-execution-boundary.py` fails
the build otherwise, and fails it the other way if an audit agent so much as names a write tool.

**Govern (200–203). No write tool is called until all four have run.**

| # | Name | Owns |
|---:|---|---|
| 200 | `200-execution-preflight-and-gate` | The account confirmation and the five refusal gates — reconciled, volume, measurement, incrementality, recoverable. **The agent whose main output is frequently "no"** |
| 201 | `201-change-plan-author` | `change-plan.md`, with the current values **captured first** — a rollback written from memory afterwards is a wish |
| 202 | `202-approval-and-scope-control` | Approval per run, recorded verbatim with exclusions, and the boundary held mid-run. Scope creep is how this protocol gets broken while appearing to be followed |
| 203 | `203-preview-and-dry-run` | Previews per placement and a field-level diff **including unchanged fields**, shown *with* the approval request |

**Operate (204–211). Each writes its own `applied.md` line as the call returns, never batched.**

| # | Name | Write surface |
|---:|---|---|
| 204 | `204-campaign-builder` | `ads_create_campaign` — **`PAUSED`, always** |
| 205 | `205-ad-set-builder` | `ads_create_ad_set` — exclusions set at creation, learning-threshold sanity checked |
| 206 | `206-creative-and-ad-builder` | Media upload → creative → ad, named to the account's convention, destination parameters carried intact |
| 207 | `207-audience-builder` | Audiences and customer lists. **Rule 7 lives here**: per-upload authorisation, hashing verified, lawful basis asked, records never logged |
| 208 | `208-budget-and-bid-operator` | Budgets and bids, stepped, with the learning-reset cost stated before the call |
| 209 | `209-status-and-pause-operator` | Status. **Pause rather than delete**, and check what a pause takes with it |
| 210 | `210-catalog-operator` | The catalog write family — and fixes applied at the layer that survives the next sync |
| 211 | `211-measurement-and-experiment-operator` | Pixel configuration and experiments. **The highest-consequence agent in the band** — its changes are the ones rollback cannot undo |

**Close (212–213).**

| # | Name | Owns |
|---:|---|---|
| 212 | `212-activation-gate` | The **only** caller of `ads_activate_entity`, after a pre-activation check against *account history* and a separate approval. This is what create-paused bought |
| 213 | `213-change-register-and-rollback` | The register's integrity, `rollback.md` written during the run, the applied-versus-approved reconciliation, and what rollback cannot restore |

**The connector exposes no automated-rules write tool**, so there is no rules-deployer agent.
`meta-rules-deploy` supplies the thresholds and guardrails; a human deploys them in Ads Manager.
Recorded in `FIELD-NOTES.md` rather than papered over with an agent that cannot act.

## Shipped (Phase 2) — attribution, incrementality, competitive, trend, budget and output (138–162)

**§24, §25 and §26 — new vs returning, attribution, incrementality (138–144).**

| # | Name | Section | Determines |
|---:|---|---:|---|
| 138 | `138-new-vs-returning-attribution` | 24 | New-customer share per campaign, with the **modelled share reported as unknown** rather than distributed |
| 139 | `139-attribution-window-and-model` | 25 | The window matched to 13's buying cycle, with each option's figures published — and what a window change does **not** fix |
| 140 | `140-cross-source-attribution-comparison` | 25 | Four sources on one alignment, each assigned to the decisions it is fit for rather than one declared correct |
| 141 | `141-attribution-verdict` | 25 | The confidence statement — observed, modelled, view-through, unexplained — and the caveat set in quotable form |
| 142 | `142-incremental-roas` | 26 | **Create versus Capture made structural.** Names the evidence class available first, and never applies a synthetic incrementality factor |
| 143 | `143-incrementality-test-design` | 26 | The test that would settle each open question, sized — and the ones the account is too small to read, said plainly |
| 144 | `144-incrementality-verdict` | 26 | Proven / Inferred / Unknown. **Most accounts have an empty Proven column**, and that is the finding |

**§27 — competitive (145–147).** Everything here is context; a competitor's ad is never evidence.

| # | Name | Determines |
|---:|---|---|
| 145 | `145-ad-library-competitive-inventory` | Competitor creative coded in **61's taxonomy**, with longevity reported as the weak proxy it is |
| 146 | `146-angle-gap-analysis` | Never-tested versus **prematurely abandoned** — checked against 77, because an angle killed at four purchases was never tested |
| 147 | `147-competitive-position-verdict` | Variety, coverage and production level, with the section's limits stated prominently |

**§5 and §28 — trend, change and hygiene (148–152).**

| # | Name | Section | Determines |
|---:|---|---:|---|
| 148 | `148-change-history-mapping` | 5 | The change map — including the site, store and other-channel changes the activity log cannot see, which is where the real cause usually lives |
| 149 | `149-anomaly-detection` | 5 | What is actually a movement, with four artefacts ruled out before any cause is considered |
| 150 | `150-root-cause-analysis` | 5 | Eight layers worked in order, contributions sized where separable, `INSUFFICIENT_DATA` where not |
| 151 | `151-trend-and-change-verdict` | 28 | Direction of travel, self-inflicted versus external, and **how many periods were readable at all** |
| 152 | `152-hygiene-verdict` | 28 | Costing money / costing learning / risk — three lists with different owners |

**§29 — budget allocation (153–155).**

| # | Name | Determines |
|---:|---|---|
| 153 | `153-budget-allocation-map` | Six dimensions on **one stated basis**, with the warning that they are lenses on one pool and never additive |
| 154 | `154-diminishing-returns-and-headroom` | Four ceilings per candidate, the binding one named, headroom in weekly spend — never extrapolated past the observed range |
| 155 | `155-next-dollar-allocation` | Destinations capped at headroom, sources of funds, and the Create/Capture flag when the ranking would drain growth |

**§30 — output (156–162).**

| # | Name | Determines |
|---:|---|---|
| 156 | `156-scorecard` | Weights published **before** scores and derived from §1's goal; unmeasurable categories excluded, never scored zero |
| 157 | `157-opportunity-matrix` | One currency, **de-duplicated** — the same wasted pound appears in three sections by design, and summing them inflates the total |
| 158 | `158-scale-matrix` | The core question answered, through five gates. Most cells will not clear them, and saying so is the point |
| 159 | `159-action-plan` | Dependency order before priority, long-lead work started early, and the deliberate omissions named |
| 160 | `160-quantified-upside` | Three bands, the conservative one led with, and an explicit list of what could not be sized |
| 161 | `161-coverage-and-evidence-appendix` | All 30 sections closed with a **derived** tally, plus the evidence table and contradiction log |
| 162 | `162-executive-summary` | The decision page. Opens with §1's goal, answers the core question, states what is not proven prominently |

## Shipped (Phase 2) — funnel, post-click CRO, offer and geo (119–137)

**§19 and §20 — funnel and post-click (119–128).**

| # | Name | Section | Determines |
|---:|---|---:|---|
| 119 | `119-funnel-map-and-leak-sizing` | 19 | Leaks ranked by **absolute lost orders** against the account's own best segment. A step that is not measured is `BLOCKED`, not zero |
| 120 | `120-mobile-and-in-app-browser-experience` | 20 | What the page does inside the IG/FB webview, where the traffic actually arrives and desktop testing never looks |
| 121 | `121-promise-handoff-scoring` | 20 | Claim, visual and offer continuity scored per ad, written into the creative database — and the offer mismatch checked against 47, 105 and 15 before it is written up as copy |
| 122 | `122-landing-page-and-pdp-audit` | 20 | The page in the order a stranger meets it, with recommendations marked as hypotheses rather than sized uplifts |
| 123 | `123-cart-and-checkout-audit` | 20 | Express checkout **working inside the webview**, guest checkout, form friction, and where cost is first revealed |
| 124 | `124-page-speed-and-technical-delivery` | 19 | The click-to-LPV gap — usually the largest quick win, and invisible from inside Meta's reporting. Rules out the measurement explanation first |
| 125 | `125-trust-and-social-proof` | 20 | Trust for a cold first-time buyer, which does work here that search traffic never needs |
| 126 | `126-mobile-versus-desktop-economics` | 19 | The device gap, with cross-device attribution named as the confound before any site conclusion |
| 127 | `127-cro-test-design-and-priority` | 20 | Testable / too-slow-to-test / not-worth-testing. The too-slow set is routed to judgement, not queued behind a test that will never conclude |
| 128 | `128-post-click-verdict` | 20 | Whether the constraint is the site or the ads, from a three-way comparison rather than an assertion |

**§21 — offers (129–133).**

| # | Name | Determines |
|---:|---|---|
| 129 | `129-offer-inventory` | The four surfaces — creative, site, checkout, catalog — and where they contradict each other |
| 130 | `130-offer-economics` | Offers priced by applying the discount **to the margin**, never ranked on conversion rate |
| 131 | `131-offer-creative-and-audience-fit` | Offer × lifecycle stage, where Create needs none and Accelerate carries the highest subsidy risk |
| 132 | `132-promotional-cadence` | Whether customers have learned to wait, and how discount-acquired cohorts repeat |
| 133 | `133-offer-verdict-and-test-list` | Coherent / priced / targeted, with mechanical fixes separated from strategic ones |

**§23 — geography and device (134–137).**

| # | Name | Determines |
|---:|---|---|
| 134 | `134-geographic-economics` | Contribution per market after shipping, duty, returns and FX — each against **its own** ceiling, not the account's |
| 135 | `135-geo-targeting-and-coverage` | Spend in markets the store cannot ship to, and the location-type setting that buys tourists |
| 136 | `136-device-and-platform-economics` | Platform framed as a **placement-mix** comparison, and the modelled share published beside every iOS reading |
| 137 | `137-geo-device-verdict` | Per-market actions with reallocation **capped by receiving-market headroom** |

## Shipped (Phase 2) — catalog, Advantage+ and placement (101–118)

**§16 — product catalog (101–108).** `N/A` where the account runs no catalog, with what that
forecloses stated — `N/A` is a real result and is not `BLOCKED`.

| # | Name | Determines |
|---:|---|---|
| 101 | `101-catalog-inventory-and-sync` | Which catalog is connected, its feed route and owner, and sync recency — a feed that last succeeded three weeks ago advertises a three-week-old catalogue and nothing says so |
| 102 | `102-product-diagnostics-and-disapprovals` | Blocked products **ranked by revenue at risk**, with clustered themes where one fix covers many |
| 103 | `103-feed-quality-and-attributes` | The feed judged as creative, because in a dynamic ad it is. Custom labels are the highest-value gap in most feeds |
| 104 | `104-product-sets-and-segmentation` | Whether the catalog is divided the way the account needs to **spend**, not the way the store is merchandised |
| 105 | `105-catalog-price-and-availability-parity` | Price and stock against the live site — and the **sync latency**, which is the durable finding rather than any single mismatch |
| 106 | `106-dynamic-ads-performance` | Dynamic retargeting and prospecting separated, on new-customer economics, with view-through share published alongside every ROAS |
| 107 | `107-catalog-and-pixel-integration` | The join dynamic retargeting depends on entirely, with Meta's match rate set against 25's direct ID comparison |
| 108 | `108-catalog-verdict` | Servable / findable / sellable, and unreachable contribution sized with long-blocked products excluded rather than counted at full value |

**§17 — Advantage+ (109–114).** 110 runs before any performance verdict.

| # | Name | Determines |
|---:|---|---|
| 109 | `109-asc-structure-and-budget` | Structure, creative supply, catalog integration, and the **existing-customer budget cap** against §1's goal |
| 110 | `110-asc-versus-manual-cannibalisation` | Whether ASC finds new customers or re-credits ones manual campaigns would have won — asked **first**, and answered `INFERRED` unless a real holdout exists |
| 111 | `111-asc-performance-and-new-customer-mix` | ASC's economics with 110's caveat carried inline, never on reported ROAS alone |
| 112 | `112-advantage-plus-creative-enhancements` | What Meta changed after upload — and the confidence consequence for §9, since an enhanced ad is not the ad that was authored |
| 113 | `113-advantage-plus-audience-and-placement` | The automation inside otherwise-manual campaigns. Advantage+ Audience makes §12 and §13's audience labels unreliable, and that caveat travels |
| 114 | `114-advantage-plus-verdict` | `EARNING` / `UNPROVEN` / `MISCONFIGURED` / `UNDERPERFORMING`. **`UNPROVEN` is the conclusion**, and its recommendation is the holdout, not a budget change |

**§18 — placement (115–118).**

| # | Name | Determines |
|---:|---|---|
| 115 | `115-placement-inventory-and-delivery` | Where impressions actually land versus where anyone intended, and format-versus-surface fit |
| 116 | `116-placement-economics` | Contribution after CVR, AOV and new-customer rate. **Never excludes a placement on last-click ROAS** — the most common placement mistake |
| 117 | `117-placement-exclusion-testing` | Duplication rather than editing, because a placement edit resets learning and destroys the read; and the explicit not-worth-testing verdict where the arithmetic says so |
| 118 | `118-placement-verdict` | Creative **fit** versus placement **economics** — opposite fixes, sized separately, never summed |

## Shipped (Phase 2) — relevance, audience, prospecting and retargeting (79–100)

**§11 — relevance and auction diagnostics (79–82).**

| # | Name | Section | Determines |
|---:|---|---:|---|
| 79 | `79-relevance-rankings` | 11 | The three rankings read as a **triage**, not a grade — each pattern routes to a different owner, and a third of ads are below average by construction |
| 80 | `80-cpm-decomposition` | 11 | Mix, relevance, self-competition, narrowing, season — then outside competition as a **residual**, not a first explanation |
| 81 | `81-ad-quality-and-feedback` | 11 | Rejection patterns and claim risk as a register, not a legal opinion. Negative feedback is `INFERRED` here, not measured |
| 82 | `82-relevance-verdict-and-cpm-opportunity` | 11 | Cost problem versus fit problem, sized against the account's **own** well-ranked median CPM |

**§12 and §15 — audience and saturation (83–92, 100).**

| # | Name | Section | Determines |
|---:|---|---:|---|
| 83 | `83-audience-inventory` | 12 | The layer with lookalike **lineage** — a lookalike is only as good as a seed nobody has refreshed |
| 84 | `84-audience-type-performance` | 12 | Targeting types ranked on new-customer CAC, because a ROAS ranking recommends the audiences that grow the business least |
| 85 | `85-lookalike-and-value-source` | 12 | What each lookalike actually models, and the LTV data sitting unused as a seed |
| 86 | `86-exclusions-and-audience-hygiene` | 12 | What each missing exclusion costs — checked for freshness, not just presence |
| 87 | `87-audience-size-and-headroom` | 12 | The ceiling, from measured reach-versus-spend rather than Meta's bucketed estimate |
| 88 | `88-customer-list-and-first-party-audiences` | 12 | Whether the business's own customer data reaches Meta at all — coverage, match rate, segmentation, refresh |
| 89 | `89-placement-and-device-audience-fit` | 12 | Creative **fit** versus placement **economics** — opposite fixes, and §18 must know which |
| 90 | `90-frequency-by-audience` | 15 | Frequency per audience against its own threshold, spend-weighted, with cross-audience exposure estimated |
| 91 | `91-saturation-and-reach-curve` | 15 | The account's own diminishing-returns curve, with the **observed spend range** as an explicit boundary |
| 92 | `92-converting-audience-profile` | 12 | Who converts by **over-indexing**, framed as a creative input rather than a targeting instruction |
| 100 | `100-frequency-and-saturation-verdict` | 15 | Audience exhaustion versus creative decay, sized and sequenced by lead time |

**§13, §14 and §24 — prospecting, retargeting and the LTV loop (93–99).**

| # | Name | Section | Determines |
|---:|---|---:|---|
| 93 | `93-prospecting-economics` | 13 | **Create and Capture reported separately**, because ranking them together on ROAS defunds the only thing making the account grow |
| 94 | `94-prospecting-audience-and-creative-fit` | 13 | The awareness mismatch — offer creative asking cold traffic for a step it has not taken |
| 95 | `95-broad-versus-targeted-verdict` | 13 | A verdict that states which comparison class it rests on, or the test that would settle it |
| 96 | `96-prospecting-scale-readiness` | 13 | Four gates — economics, headroom, returns, creative supply — and the binding one is the answer |
| 97 | `97-retargeting-structure-and-windows` | 14 | Whether retargeting is a ladder or a pile, and whether each tier has a distinct message |
| 98 | `98-retargeting-economics-and-over-retargeting` | 14 | By lifecycle stage, with view-through share published alongside every ROAS — and Expand spend competing with an owned email channel |
| 99 | `99-ltv-loop-and-first-party-feedback` | 24 | Four links, and the loop is broken at whichever fails first. Fixing link 4 while link 2 is broken achieves nothing |

## Shipped (Phase 2) — structure, hygiene, performance and delivery (43–58)

**§4 and §28 — structure and hygiene (43–50).**

| # | Name | Section | Determines |
|---:|---|---:|---|
| 43 | `43-campaign-inventory-and-structure` | 4 | The three-level map, reconciled against parent totals, with each campaign classified by `demand-lifecycle` stage once so four sections do not derive it four ways |
| 44 | `44-fragmentation-and-consolidation` | 4 | Events per ad set per week as a distribution, and which ad sets are **structurally** learning-limited — a structural finding, not a creative one |
| 45 | `45-audience-overlap-and-self-competition` | 4 | Where the account outbids itself, and the missing exclusions that cause it. Rules out self-competition before 65 blames the outside auction |
| 46 | `46-budget-structure-abo-cbo` | 4 | Whether Meta or the operator decides allocation — and whether anyone chose. Starved segments inside campaign-budget campaigns |
| 47 | `47-account-hygiene-inventory` | 28 | Debris ranked by spend at risk, customer-facing first. Expired promos still running outrank forty archived audiences |
| 48 | `48-destination-and-link-health` | 28 | Whether spend lands somewhere, checked on mobile and in the in-app browser, including redirects that silently drop `fbclid` and UTMs |
| 49 | `49-business-manager-and-permissions` | 28 | Ownership versus access per asset, and **the transition test**: if the agency relationship ended tomorrow, what would the business lose |
| 50 | `50-structure-verdict-and-consolidation-plan` | 4 | The two-axis verdict — learning versus legibility — and a sequence that keeps each change readable |

**§5 — campaign performance and trend windows (51–54).** 148–151 map movements onto change
history; these four establish what moved.

| # | Name | Section | Determines |
|---:|---|---:|---|
| 51 | `51-campaign-performance-matrix` | 5 | The full metric set, every rate **recomputed from component sums**, judged against §1's break-even rather than against instinct |
| 52 | `52-trend-windows-and-yoy` | 5 | 7/30/90/365 and **matched-week** year over year, seasonally adjusted, with each movement decomposed into the metric driving it |
| 53 | `53-spend-concentration` | 5 | What the account is exposed to at every level, plus the lifecycle split against §1's goal and the thin tail that is dissipated rather than tested |
| 54 | `54-budget-pacing-and-utilisation` | 5 | Budget-constrained versus delivery-constrained versus blocked versus losing the auction — four states that look alike and have different fixes |

**§6 — bidding, delivery and learning (55–58).**

| # | Name | Section | Determines |
|---:|---|---:|---|
| 55 | `55-bid-strategy-audit` | 6 | Every cap against realised cost and against 11's ceiling. Deliberately conservative: a bid change costs roughly two weeks of readable performance |
| 56 | `56-learning-phase-state` | 6 | **The invalidation list** — every ad set that reset inside the window, which §5, §8, §9 and §11 must all check before attributing a movement to anything they own |
| 57 | `57-optimisation-event-and-window` | 6 | The instruction Meta actually follows, against §1's goal — and whether an unvalidated mid-funnel proxy is being optimised toward |
| 58 | `58-delivery-diagnostics` | 6 | Seven causes of underdelivery worked in order because they masquerade as each other, and the §6 verdict with its binding constraint named |

## Shipped (Phase 2) — the measurement gate, §2 (21–36)

The gate every economic claim in the repository inherits. It exists in this commit because §3
shipped able to *size* a reconciliation gap and unable to *diagnose* one — 41's diagnosis rows now
name the agent that owns each check instead of pointing at a band that did not exist.

Structure follows the five layers in `.claude/skills/capi-and-emq/SKILL.md`. The agents apply it;
they do not restate it.

| # | Name | Layer | Determines |
|---:|---|---|---|
| 21 | `21-dataset-and-signal-inventory` | 1 — arrival | Which dataset is optimised against, which are *receiving*, volume trend against the change map, freshness, browser/server split. **Browser-only Purchase is a serious finding** |
| 22 | `22-funnel-event-coverage` | 1 | Which funnel events fire, configured against arriving, and whether the volumes are physically possible |
| 23 | `23-capi-implementation` | 1 | The server-side route — platform app, server container, gateway, direct, partner — and what it makes fixable versus structurally capped |
| 24 | `24-purchase-event-payload` | 2 — payload | `value`, currency, single-fire. **The highest-impact payload check in the audit**; its implied-AOV arithmetic is what §3's value rows resolve to |
| 25 | `25-content-ids-and-catalog-matching` | 2 | Whether Meta can connect an event to a product, at variant grain |
| 26 | `26-custom-conversions-and-event-definitions` | 2 | What the account's custom conversions actually count, read literally, validated against store orders |
| 27 | `27-event-deduplication` | 3 — dedup | `event_id`/`event_name` parity, dedup rate, timing window, and the **corrected claim ratio** §3 needs |
| 28 | `28-consent-and-signal-loss` | 3 | The events that never fire — a bound on the verdict, not a defect to be fixed to zero |
| 29 | `29-event-match-quality` | 4 — EMQ | The score **and coverage per key**. An EMQ of 6.2 on email alone is a different account from 6.2 on six partial keys |
| 30 | `30-identifier-capture-and-hashing` | 4 | What the site has versus sends; advanced matching; `external_id`; and the silent hashing failure — high coverage with low EMQ |
| 31 | `31-click-id-persistence` | 4 | `fbclid` → `fbc` → server event, traced step by step, **in the in-app browser**. The most common single EMQ cause |
| 32 | `32-domain-verification-and-aem` | 5 — AEM | Verification, and **`Purchase` at priority 1**. Lower-priority events are under-reported by design, not broken |
| 33 | `33-third-party-checkout-measurement` | 5 | What changes off-domain, and **who owns each fix** — a recommendation sent to the wrong party does not get done |
| 34 | `34-attribution-settings-audit` | — | The setting per campaign, and the **one window** the whole run uses. Establishes; 40 sizes; §25 chooses |
| 35 | `35-utm-and-link-tracking` | — | Whether anything outside Meta can see paid traffic. Untagged spend is why §3's claim share is a **bound rather than a measurement** |
| 36 | `36-measurement-verdict` | — | **GREEN / YELLOW / RED**, weighted by consequence rather than count, plus §3's routed answers and the ranked fix list |

`RED` orders the audit and never stops it: every other section still runs, findings are marked
`DEGRADED`, and no scale or kill call is issued on conversion values just shown to be unreliable.

## Shipped (Phase 2) — the economics and reconciliation gates, §§1, 3, 22

The two gates `CLAUDE.md` says precede economic conclusions. They exist early because the creative
band above cites "the canonical margin from §1" and "break-even ROAS from §1" throughout, and
without them every creative verdict is a ranking rather than a contribution.

**§1 and §22 — context and economics (07–20).** 10 and 11 are the canonical producers: no other
agent in the repository computes margin or the ROAS and CAC thresholds.

| # | Name | Section | Depends on | Determines |
|---:|---|---:|---|---|
| 07 | `07-primary-goal-and-business-frame` | 1 | — | **The one primary goal**, its number, constraint and horizon — and stated against revealed |
| 08 | `08-product-and-icp-context` | 1 | 07 | Product, ICP, positioning and offer, reconciled against measured data. Context is never evidence |
| 09 | `09-aov-and-order-economics` | 1 | — | Gross, realised and post-refund AOV, the distribution, and the **population definition** §3 reuses |
| 10 | `10-contribution-margin-builder` | 1 | 09 | **The canonical contribution margin**, with coverage stated. Computed once, never recomputed |
| 11 | `11-cac-and-roas-targets` | 1 | 10, 12, 13 | **Break-even ROAS, CAC ceiling, target ROAS, payback** — plus the break-even chain by funnel stage |
| 12 | `12-new-vs-returning-economics` | 1 | 09, §3 join | New-customer CAC against blended, and the gap between them |
| 13 | `13-ltv-and-repeat-economics` | 1 | 09, 10 | Cohort contribution curves and the payback horizon a ceiling can honestly use |
| 14 | `14-total-ad-spend-census` | 1 | — | **Every paid channel enumerated.** Blended MER on Meta's spend alone is wrong, not partial |
| 15 | `15-promo-calendar-and-seasonality` | 1 | — | The calendar every trend and creative comparison is checked against, plus confounded windows |
| 16 | `16-geo-and-market-priorities` | 1 | 10 | Contribution per order by market, and the CAC ceiling each market would have to clear |
| 17 | `17-hero-product-identification` | 22 | 10 | Revenue, contribution, repeat-driver and **entry-product** rankings, and the spend mismatch |
| 18 | `18-sku-economics-builder` | 22 | 10, 11, 17 | Per-product economics against each product's own break-even, never the account's |
| 19 | `19-sku-repeat-and-ltv` | 22 | 13, 17 | Which products acquire customers worth keeping — loss-leaders and one-and-dones |
| 20 | `20-margin-assumption-and-sensitivity` | 1 | 10, 11 | Every assumed input banded, and every affected recommendation `ROBUST` / `SENSITIVE` / `UNAVAILABLE` |

**§3 — reconciliation (37–42).** Run order is not numeric order here: **38 runs before 37.**

| # | Name | Section | Depends on | Determines |
|---:|---|---:|---|---|
| 38 | `38-reconciliation-alignment` | 3 | 09 | Date basis, timezone, currency, window, model, event set, refunds, population. **An unaligned comparison is not a reconciliation** |
| 37 | `37-meta-vs-commerce-reconciliation` | 3 | 38 | The gate: order claim ratio, value claim share, implied AOV against the **Meta-attributed** store AOV |
| 39 | `39-blended-mer-and-channel-census` | 3 | 14, 38 | Blended MER on total ad spend and on contribution, plus cross-platform double-claiming |
| 40 | `40-modelled-and-view-through-share` | 3 | 38 | How much of Meta's claim is modelled or view-through, per campaign type, written per row into the creative database |
| 41 | `41-gap-diagnosis-and-classification` | 3 | 37, 39, 40, §2 | `MATCH` / `EXPLAINED GAP` / `UNRESOLVED GAP` / `INVALID COMPARISON`, with the cause only as far as evidence reaches |
| 42 | `42-ga4-triangulation` | 3 | 38 | GA4 as a third reading — after testing whether GA4 itself is trustworthy enough to arbitrate |

Where §2 has not yet run, 41 still classifies and sizes each gap but marks the **diagnosis**
`DEGRADED`, naming the measurement check that would settle it. The measurement band lands next and
upgrades those labels rather than changing the numbers.

## Shipped (Phase 2) — the creative band, §§7–10

Written first, ahead of numeric order: it carries a third of the audit's value and produces the
dashboard, so it should be runnable and reviewable before the long tail exists.

**§7 — the creative database and the dashboard.** 59 writes the file; nothing downstream re-queries.

| # | Name | Section | Depends on | Determines |
|---:|---|---:|---|---|
| 59 | `59-creative-database-builder` | 7 | 02, §2 | Writes `creative-database.csv` against `schemas/creative-record.yaml` — one window, one attribution setting, reconciled against parent totals |
| 60 | `60-creative-dashboard-builder` | 7 | 59, §5, §20 | Renders `top-creatives.html` and the Chrome snapshot, and checks its headlines against §5's totals |
| 61 | `61-creative-classifier` | 7 | 59, 62 | Fills the classification columns, rule-based then model, recording `*_source` per field |
| 62 | `62-naming-convention-parser` | 7 | 59 | Infers the convention, sets `parse_status`, reports compliance **spend-weighted** |
| 63 | `63-creative-mix-and-concentration` | 7 | 59, 61 | Mix by spend share, top-ad concentration, single points of failure |
| 64 | `64-creative-attention-metrics` | 7 | 59 | Hook rate, hold rate, quartiles — and whether attention predicts purchases *here* |

**§8 — fatigue.** 65 is a differential diagnosis, not a score.

| # | Name | Section | Depends on | Determines |
|---:|---|---:|---|---|
| 65 | `65-creative-fatigue-diagnosis` | 8 | 59, 64 | Which of seven named causes is degrading each ad, and why not the other six |
| 66 | `66-creative-age-and-lifespan` | 8 | 59 | The account's own creative lifespan by format, with survival rates |
| 67 | `67-evergreen-vs-iteration-candidates` | 8 | 65, 66 | Protect / iterate / retire / insufficient, and never edit an evergreen in place |
| 68 | `68-fatigue-vs-saturation-separation` | 8 | 65, §12 | Creative decay or audience exhaustion — the two have opposite fixes |
| 69 | `69-creative-decay-curve` | 8 | 65, 66, §1 | The decay rate, current exposure, and fatigue sized in contribution |
| 70 | `70-creative-refresh-requirement` | 8 | 66, 67, 68 | Concepts needed per month, against readable test capacity |

**§9 — which dimension wins purchases.**

| # | Name | Section | Depends on | Determines |
|---:|---|---:|---|---|
| 71 | `71-creative-angle-winner-decomposition` | 9 | 61, §1 | The winning dimension on contribution, with seven confounds ruled out or named |
| 72 | `72-hook-and-first-three-seconds` | 9 | 64, 61 | Three separate rankings — stop, hold, sell — and the gaps between them |
| 73 | `73-proof-objection-and-persona` | 9 | 61, 92 | Which proof, which objection, which persona; and the objections never addressed |
| 74 | `74-offer-in-creative` | 9 | 61, §1 | Offers ranked on **contribution**, not conversion rate |
| 75 | `75-creative-audience-interaction` | 9 | 61, §12, §18 | Where the account-level answer is wrong for a specific audience |

**§10 — is there an engine.**

| # | Name | Section | Depends on | Determines |
|---:|---|---:|---|---|
| 76 | `76-creative-testing-velocity-and-budget` | 10 | 59 | Velocity against **readable capacity** — testing more than you can read is noise |
| 77 | `77-test-read-and-graduation` | 10 | 76, §1 | Which past kills were verdicts, which were spend-loss caps, which were coin flips |
| 78 | `78-creative-learning-documentation` | 10 | 71–77 | Whether learning compounds, and the §10 verdict with its binding constraint |

**The library is complete: 177 agents.** 163 audit agents (00–162) covering all 30 sections, and
the 14-agent execution band (200–213) governed by `EXECUTION-PROTOCOL.md`.
Until an agent exists, its section still closes with a state — `DEGRADED` or `BLOCKED`, naming
what was missing — because a section that silently does not run is a defect, not an omission.

## The pivotal agents

Named because the rest hang off them:

| # | Name | Why it matters |
|---:|---|---|
| 01 | full-audit orchestrator | Drives the 30-section sweep and owns the coverage ledger |
| 07 | primary-goal-and-business-frame | Names the one KPI every later section is judged against |
| 37 | meta-vs-commerce-reconciliation | The mandatory §3 gate — no economic conclusion precedes it |
| **59** | creative-database-builder | Writes `creative-database.csv` once. Nothing downstream re-queries Meta |
| **60** | creative-dashboard-builder | Renders the Top Creatives dashboard from that file |
| 61 | creative-classifier | Rule-based tagging from the naming convention, model fallback, source recorded |
| 71 | creative-angle-winner-decomposition | Which dimension wins **purchases**, with its confounds ruled out |
| 142 | incremental-roas | Reported versus incremental — the number scaling should use |
| **158** | scale-matrix | Creative × product × offer × audience, ranked by incremental contribution |
| 162 | executive-summary | The decision page |

## Adding an agent

`AUTHORING.md` has the full contract. The three that are easy to get wrong:

1. **Map it to a section**, or it never runs.
2. **State a sample floor** and say what to return when it is not met. Meta's ad-level purchase
   counts are small enough that an agent without a floor will produce confident nonsense as the
   normal case, not the edge case.
3. **Consume the canonical values** — contribution margin and break-even ROAS from §1,
   significance from `learning-phase-and-significance`, creative fields from
   `creative-record.yaml`. An agent that recomputes margin will disagree with the executive page,
   and the reader has no way to tell which is right.
