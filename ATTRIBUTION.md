# Attribution

What in this repository came from somewhere else, what was changed, and what was deliberately
left behind. Kept file-level rather than summary-level so an upstream re-sync stays traceable.

---

## Sources

| Source | License | What it gave this repo |
|---|---|---|
| [`undark-ai/Google-Ads-OS`](https://github.com/undark-ai/Google-Ads-OS) | MIT © 2026 undark-ai | The architecture: agent numbering and bands, the coverage-ledger discipline, the evidence contract, the gates-order-but-never-stop rule, the connector ladder, the validator suite, the plugin layout |
| [`coreyhaines31/marketingskills`](https://github.com/coreyhaines31/marketingskills) | MIT © 2025 Corey Haines | The `tools/` connector registry (93 integration guides, 64 CLIs, the Composio layer), by way of Google-Ads-OS; and the 15 marketing-skill directories named below |
| Internal Undark marketing-skill library | Internal Undark source; mixed provenance traced below | The `meta-*` marketing skill set and the CRO/offer/copy skills; the `meta-ads-team` role references that seed the agent bodies |
| [`swan-gtm/gtm-skills`](https://github.com/swan-gtm/gtm-skills) (`skills/ivan-falco`) | MIT © 2026 Swan; original skills by Ivan Falco / Frontal | Paid-ads frameworks and wording adapted from B2B onto e-commerce economics, both through the internal D2C skill pack and directly into the audit layer |
| [`emilyhellqvist/meta-ads-skills`](https://github.com/emilyhellqvist/meta-ads-skills) | MIT stated in the upstream README; the reviewed revision has no standalone license file or copyright notice | Ideas and checks from Emily Hellqvist's Meta Ads skill set: scored audit dimensions, the ASC-vs-manual self-competition red flag, placement/overlap/pacing checks |
| Internal Undark `creative-analysis-dashboard` skill | Original Undark work | The Top Creatives dashboard and both HTML templates, genericised from an internal account-specific implementation |
| [Curtis Howland's Meta DTC benchmark publications](https://newsletter.curtishowland.com/p/ive-spent-100m-on-meta-ads-in-the) | Factual practitioner observations, cited rather than vendored | The external benchmark context in `BENCHMARKS.md`; every figure remains attributed and labelled self-reported |

---

## Carried from Google-Ads-OS

**Near-verbatim, deliberately.** The evidence contract is the part worth keeping identical
across both systems — an agent author who has worked in one should not have to relearn it:

- `schemas/agent-run.schema.json`
- `schemas/opportunity-schema.yaml`, `finding-schema.yaml`, `agent-contract.yaml`,
  `reconciliation-schema.yaml`, `test-schema.yaml` — each extended, never restructured
- `tools/` in full (see below)
- `LICENSE`, `.gitignore` (extended with `changes/`)

**Extended for Meta:**

| File | What changed |
|---|---|
| `agent-contract.yaml` | Added `section` (1–30), `coverage_state`, and `measurement_basis` — because Meta reports modelled conversions and a result has to say what it stands on |
| `finding-schema.yaml` | Added the `PLATFORM_STATED` evidence class for Meta's assertions about Meta; added `severity` and `verification` |
| `reconciliation-schema.yaml` | Added `alignment_checked`, `INVALID_COMPARISON`, and the five mandatory headline measures including `modelled_share` |
| `opportunity-schema.yaml` | Added `overlaps_with` and `time_to_read_days`; made `impact_currency` explicitly nullable so a `FLAG` cannot acquire a fabricated value |
| `run-state.schema.json` | Added `lane`, the per-section coverage map, and the gate verdicts |
| `test-schema.yaml` | Added `learning_phase_safe` and `learning_recorded` |

**Structurally new here, with no Google counterpart:**

- `EXECUTION-PROTOCOL.md` and the execution lane. The official Google Ads MCP is read-only, so
  that system's safety story is "we have no hands". The Meta connector has write tools, so this
  one needs a protocol instead of an absence.
- `schemas/meta-mcp-tool-classification.yaml` — the read/write classification the boundary
  validator enforces.
- `schemas/creative-record.yaml` and `schemas/scale-matrix.yaml`.
- `scripts/validate-execution-boundary.py`.

**Not carried:** the Google-specific agent library (search terms, keywords, Quality Score,
Merchant Center feed rules, PMax) and the Google-specific audit skills. The section framework
was rebuilt from scratch around Meta's levers rather than translated.

---

## `tools/` registry

Vendored whole from Google-Ads-OS, which vendored it from `coreyhaines31/marketingskills`.
93 integration guides, 64 CLIs, the Composio layer.

Changed: `tools/README.md` rescoped to Meta's source hierarchy; `tools/clis/README.md` rewritten
around the **two-lane** boundary rather than a blanket read-only rule, since this repository has
an execution lane and the old wording would have been false.

Non-Meta entries are kept deliberately. `shopify`, `stripe` and `paddle` back the economics
gate; `google-ads`, `tiktok-ads` and `linkedin-ads` are what make blended MER computable at all;
`klaviyo` and `attentive` back the LTV loop; `hotjar`, `posthog` and `optimizely` back the funnel
and CRO bands.

---

## Marketing skills

Vendored from an internal Undark marketing-skill library. That set's `meta-*` skills are already
scoped to D2C e-commerce, which is this repository's scope, so they needed rescoping far less
than Google-Ads-OS's marketing layer did.

Changed on vendoring:

- Cross-references rewritten to point at skills that exist **in this repository**. An upstream
  pointer to a skill that was not carried misleads routing at trigger time, and
  `validate-references.py` fails the build on it.
- Any threshold presented as a rule is marked advisory. Per `CLAUDE.md`, a marketing skill's
  benchmark is not evidence for a quantified finding.
- References to the upstream repo's own file layout removed.

### Corey Haines-derived directories (15)

These directories descend from the MIT-licensed `coreyhaines31/marketingskills` tree. The whole
directory is covered, including any retained references, assets and evals:

`ab-testing`, `ad-creative`, `analytics`, `competitor-profiling`, `copy-editing`, `copywriting`,
`cro`, `customer-research`, `emails`, `marketing-psychology`, `offers`, `popups`, `pricing`,
`product-marketing`, `signup`.

The audit-layer directory named `attribution` is this repository's work. It shares a name with an
upstream Corey Haines skill but does not descend from that file. The previous `LICENSE` count of
17 was inherited from Google-Ads-OS and was wrong for this repository.

---

## `meta-ads-team`

Its 24 role references were the strongest single input to the agent library, and they are used
as **seeds for agent bodies** rather than vendored as one mega-skill — this OS addresses
specialists by number, and a role table inside a skill cannot be sequenced by an orchestrator or
mapped to a coverage ledger.

Specifically carried into agent bodies: the seven-layer account health check and its 0–100
weighted scorecard, the severity tiers, the seven named fatigue diagnoses, the campaign RCA
"confirm the move is real first" step, the five-layer pixel/EMQ audit, the placement
star/hidden-gem/waste framework, the scaling methods and saturation-ceiling detection, and the
hook/iteration creative frameworks.

`references/meta-platform-reference.md` became the platform-behaviour rules in
`schemas/canonical-data-model.md` and `CLAUDE.md`: never average ratios, breakdown
incompatibilities, attribution-window alignment, rate limits.

**Second pass.** All 24 role references were read in full on a later pass, and seven audit skills
were written from them to cover sections that had no skill at all:

| Role reference | Became |
|---|---|
| `campaign-rca` | `campaign-rca` — including its "confirm the move is real" step, which now gates every §5 trend claim |
| `fatigue-diagnostic` | The seven named diagnoses in `frequency-and-saturation` |
| `pixel-attribution-audit` | The per-match-key EMQ thresholds in `capi-and-emq` |
| `bidding-strategist` | `bid-strategy-and-learning` |
| `placement-optimizer` | `placement-economics` — star / hidden-gem / waste, and exclusion-by-duplication |
| `catalog-health` | `catalog-health` — including item-ID stability, price parity and error *trend* |
| `scaling-playbook` | `scaling-methods` — the readiness gate and the four methods |
| `audience-insights-miner` | `audience-insights-mining` — the clicks-versus-purchases gap |
| `funnel-analyzer` | The starting stage ranges in `funnel-analysis` |
| `account-health-check` | The §30 scorecard's published-weights discipline and severity tiers |
| `hook-generator`, `iteration-brief`, `creative-brief-writer`, `copywriting-frameworks` | The creative brief template and `creative-testing-engine`'s iteration hierarchy (Angle > Offer > Persona > Format > Hook) |

The remaining roles — `ad-analyzer`, `daily-health-monitor`, `performance-reporting`,
`experiment-reader`, `launch-preflight`, `persona-builder`, `competitor-research`,
`retention-analyzer`, `seasonal-planner`, `creative-type-rollup` — map to agents in bands not yet
written, and are recorded here so Phase 2 has a source rather than starting from a blank page.

---

## `ivan-falco`

All 44 skills reviewed. The set is written for **B2B SaaS lead generation**; this repository is
D2C e-commerce only, so the split is by transferability rather than by quality.

**Adapted rather than vendored under the same paths.** None of the Swan files is present as an
unchanged file, but "ideas only" was too strong: a repository-wide comparison found retained
phrasing, tables and structures in the D2C rewrites. Ivan Falco / Frontal therefore receives
author credit here, and Swan's MIT copyright notice is retained in `LICENSE` and
`THIRD_PARTY_NOTICES.md`.

The first internal D2C pack based on this material became these 21 marketing skills:

`ads-campaign-planning`, `creative-cadence-operating-system`, `creative-fatigue-detection`,
`lead-capture-optimization`, `message-validation`, `meta-ads-operating-system`, `meta-ads`,
`meta-advantage-plus`, `meta-api-reference`, `meta-audience-strategy`, `meta-campaign-creation`,
`meta-campaign-structure`, `meta-capi-and-events`, `meta-creative-strategy`,
`meta-high-value-audiences`, `meta-offer-strategy`, `meta-optimization-playbook`, `meta-overview`,
`meta-reporting`, `meta-setup-and-tracking`, `meta-third-party-conversion-tracking`.

Further material was folded into audit-layer skills that this repository owns:

| Source skill | Where it went |
|---|---|
| `ads-scaling-quadrant` | The budget × effort lever table in `scaling-methods` |
| `advantage-plus` | `advantage-plus-audit` (the audit side) and the vendored `meta-advantage-plus` (the build side) |
| `creative-cadence-operating-system`, `creative-fatigue-detection`, `message-validation` | Vendored through the internal skill library; their ancestry still runs to the Ivan Falco / Frontal source set |
| `ads-budget-allocation`, `ads-offers-strategy` | Folded into `recommendation-prioritization` and the vendored `meta-offer-strategy` |
| `ad-copywriting`, `ad-personas` | Folded into `creative-taxonomy`'s persona axis and the vendored `ad-creative` |

From `meta-ads-operating-system`: the two-campaign 80/20 scaling-versus-testing split, the
stage-1/stage-2 decision tree, the swap rules, the frequency fatigue triggers and the
tests-per-week production formula — all re-based onto break-even ROAS and new-customer CAC in
`creative-testing-engine` and `frequency-and-saturation`. Every threshold in that skill is
expressed against **Target CPL**, a lead-gen quantity this repository does not compute, so a
direct vendoring would have imported a metric with nothing behind it.

**Adapted from B2B to D2C, after an earlier version of this document dropped them.** The first
pass recorded `ads-optimization-signals` and `demand-lifecycle` as "do not transfer, built on a
B2B pipeline model". That was wrong, and the reasoning was lazy: the B2B *metrics* (CPMQL,
pipe-to-spend, cost per opportunity) are the replaceable part, not the framework carrying them.

| Source skill | Carried as | What was re-based |
|---|---|---|
| `demand-lifecycle` | `demand-lifecycle` (audit layer) | Create / Capture / Accelerate / Revive / Expand kept whole; the stages re-hung on awareness level L1–L5 (already a field in `schemas/creative-record.yaml`) and on D2C offers and numbers — new-customer CAC, reactivation rate, repeat rate, contribution per customer — instead of pipeline stages. **Create versus Capture is the incrementality distinction**, which §26 asks about and nothing else here maps campaigns onto; §13/§14's prospecting-versus-retargeting split is cruder and misses Revive and Expand entirely |
| `ads-optimization-signals` | `leading-and-lagging-signals` (audit layer) | The leading/lagging discipline and the break-even chain. The B2B lag is a 2–24 month sales cycle; the D2C lag is **sparsity per entity** — an account banks plenty of purchases, almost none of its ads do. `break-even CPL = deal size × close rate` becomes the D2C chain break-even CPA → cost per checkout → per ATC → per LPV → CPC → CPM, computed off the account's own §19 step-through rates. The non-performer and maintenance pause rules are carried explicitly as **spend-loss caps, not significance tests** — a pause logged as a budget action, never as a creative learning. Added rather than carried: the requirement that a leading signal be validated to correlate on *this* account before it may carry a verdict, and the gaming failure mode (bait openings lift hook rate and depress purchase CVR) |

**Reviewed and genuinely superseded:** `ads-measurement-scorecard`. Verified against the file
rather than asserted — `paid-measurement-readiness` carries the same 1–3 scoring across the same
dimensions, plus a spend gate and a fix-the-lowest-score-first rule; §30's scorecard adds
published weights and excludes what it could not measure rather than scoring it zero.

**Not carried,** as out of scope under D2C-only: `meta-b2b-overview`, `abm-on-meta`,
`abm-measurement-framework`, `abm-retargeting-framework`, `1-to-1-abm-ads`,
`linkedin-abm-1to1-few-many`, `linkedin-ads`, `linkedin-ads-abm-guide`,
`linkedin-ads-audience-guide`, `account-selection-framework`, `persona-mapping-framework`,
`scale-b2b-qualified-pipeline`, `lead-form-optimization`, `ads-outbound-signaling-guide`,
`google-ads`, `ads-channel-selection`.

---

## `emilyhellqvist/meta-ads-skills`

21 skills by **Emily Hellqvist** reviewed. The repository README labels the project MIT, but the
reviewed revision has no standalone `LICENSE` file or formal copyright notice. No complete file is
vendored here; the credit below is for concepts and checks that were re-expressed. Its lead-gen audit is out of scope; the rest folded into the matching agent
bands rather than being carried as separate skills, since this repository already has a section
that owns each subject.

**Carried as ideas:** `meta-ads-audit-ecommerce`'s weighted scoring dimensions (into the §30
scorecard) and its **ASC + manual Shopping self-competition** red flag (into §17 — a genuinely
good catch that the other sources miss); `meta-ads-placement-mining` (§18),
`meta-ads-audience-overlap` (§12), `meta-ads-budget-pacing` (§6/§29),
`meta-ads-anomaly-detection` (§5), `meta-ads-exclusions` (§12/§14),
`meta-ads-utm-generator` (§2), `meta-ads-segmentation` (§12), `meta-ads-automated-rules`
(execution lane).

**Not carried:** `meta-ads-audit-leadgen`.

---

## `creative-analysis-dashboard`

The source was an internal Undark skill, not an external package. The skill and both HTML
templates were carried into `.claude/skills/creative-dashboard/`; their copyright is covered by
the repository's `undark-ai` notice.

Changed:

- **Genericised.** The account-specific `ANGLES` / `THEMES` regexes, `LP_GENOMES` landing-page
  summaries and `destFor()` keyword routing were hardcoded for one brand. They are now an
  account config the audit derives — from the real naming convention in §7 and the real landing
  pages in §20 — rather than something a human hand-edits per client.
- **Fed by the audit rather than re-querying.** The template pulled its own data from the
  connector. It now reads `audits/<run-id>/creative-database.csv`, so the dashboard and the
  findings cannot disagree.
- **Hook rate, hold rate and quartile retention promoted** out of the template into
  `schemas/creative-record.yaml`, so §8 and §9 compute from the same numbers the cards show.

Kept verbatim because they are hard-won: the platform limits. The artifact sandbox blocks
Meta's CDN so inline thumbnails do not render; `thumbnail_url` is 64px and expires; signed URLs
cannot be upscaled; `ads_get_ad_preview` renders inline in chat only; per-second retention
curves, storyboards, transcripts and comment data are not available from the connector; accounts
with `is_ads_mcp_enabled: false` cannot be queried regardless of `is_queryable`. These are
recorded in the skill and in `FIELD-NOTES.md`.

---

## License

MIT — see `LICENSE`. `THIRD_PARTY_NOTICES.md` keeps the upstream notices and authorship details in
one place. Vendored or adapted material retains its upstream license; where an upstream license
differs, it governs that material.
