# Meta Ads Ecommerce OS

## What this repository is

An evidence-first operating system for D2C e-commerce Meta ad accounts. It audits, and — under
a separate, fenced protocol — it executes. The two are different lanes with different rules,
and the boundary between them is enforced, not advisory.

Everything the system does serves one question:

> **Which creative + product + offer combinations are generating incremental profitable
> customers, and how much more can we scale them?**

## The two lanes

**Audit lane (agents 00–199, audit skills).** Read-only. Establishes what is true. May call
only tools classified `read` in `schemas/meta-mcp-tool-classification.yaml`. An audit that
discovers a fix writes a recommendation; it does not apply it, and it never mutates as a side
effect. `scripts/validate-execution-boundary.py` fails the build if an audit agent so much as
references a write tool.

**Execution lane (agents 200+, execution skills).** May mutate a live ad account, under
`EXECUTION-PROTOCOL.md` and nothing less: a written change plan, explicit per-run approval,
preview before publish, create-paused, a logged change register, a rollback note. An audit run
and an execution run are separate invocations and never share a run id.

Unclassified tools are treated as writes. Fail closed.

## Operating rules

- **Discover tools before using them.** Never invent a tool name, schema, account id, pixel id
  or connector capability. The Meta connector's server id differs per account, so the prefixed
  tool names must be discovered at runtime rather than hardcoded — which is exactly why
  discovery is a rule and not a convenience.
- **Meta grades its own homework.** Modelled conversions, view-through attribution, Aggregated
  Event Measurement and the 7-day-click default all mean Meta's reported figures are a claim
  until reconciled. A modelled or inferred value is never emitted as `OBSERVED`. Meta's
  assertions about Meta — opportunity score, relevance rankings, EMQ, vendor lift estimates —
  are `PLATFORM_STATED`: reportable, never proof.
- **Reconcile before concluding.** Section 3 sets Meta's claimed purchases and value against
  banked orders from the commerce platform, and GA4 where present, **before any economic
  conclusion**. Publish order claim ratio, value claim share, blended MER, implied AOV against
  store AOV, and modelled share. Never let an unreconciled ROAS reach a recommendation.
- **Separate brand from generic before comparing search to paid social.** Always. Brand search
  harvests demand paid social often created, so a blended search figure is partly Meta's own work
  priced as Google's — and because brand carries most of the transactions on a fraction of the
  spend, blending does not overstate search slightly, it inverts the ranking. Generic is the only
  valid comparison. Split by campaign or search term, never by GA4's channel group, and attribute
  each platform's spend to the segment its sessions landed in — PMax is cross-network, not search.
- **Blended MER uses total ad spend.** Every paid channel, enumerated first. Computed on Meta's
  spend alone it is wrong, not merely partial — and two platforms each claiming the same order
  is only visible when their claims are summed.
- **Every material finding carries** a number, source, date range, formula, evidence class,
  confidence and one next action. If it cannot be defensibly quantified it is a `FLAG`, not a
  `FIX`, and it carries no invented currency value.
- **Never average a ratio across entities.** CTR, ROAS, frequency, hook rate, CVR — recompute
  from component sums at the level you want. Averaging ad-level ratios to an ad-set figure is
  the most common way a Meta report becomes fiction. Breakdowns do not compose either: one
  breakdown dimension per call, and reconcile each against its parent total.
- **Volume gates conclusions.** Meta's own learning threshold is ~50 conversions per ad set per
  week; a creative kill or scale call under the purchase floor in
  `learning-phase-and-significance` is variance, not a verdict. Under the floor, the answer is
  `INSUFFICIENT_DATA` and the next step is to buy more data.
- **Learning phase invalidates reads.** An ad set that re-entered learning after an edit is not
  reporting a creative verdict. Check `ads_account_get_activity_logs` before attributing a
  performance movement to the creative. **Where the change map is unavailable** — the tool is not
  rolled out to the account, or returns nothing — degrade rather than skip: derive what
  `created_time` and `effective_status` support, state in the finding that movement cannot be
  attributed to creative, cap the confidence of every decay and trend conclusion at `MEDIUM`, and
  withhold kill recommendations that rest on decay alone. A missing change map lowers confidence;
  it never silently becomes an unqualified creative verdict.
- **Contribution, not ROAS.** Revenue, conversion value, ROAS, MER and GMV are not profit. Use
  the canonical contribution margin from section 1; never recompute it per agent.
- **Re-walk the connector ladder every run.** Native connector → **Composio** (and comparable
  aggregators) → the commerce platform as a proxy → ask the user → `UNAVAILABLE`. No native MCP
  for a source means go to Composio rather than declaring the source missing. Never inherit a prior run's `UNAVAILABLE`; connectors get authorised between
  runs and re-checking is the cheapest test in the system. Gateways hold several authenticated
  accounts per platform — enumerate them, and prefer the platform's native query surface.
- **One material change at a time, with a 14-day read window,** wherever a causal read is
  intended. Respect conversion lag before calling recent performance a failure.
- **Read `.agents/product-marketing.md` first** if it exists; it carries product, ICP,
  positioning and offer context. If it is missing, offer the `product-marketing` skill rather
  than interrogating the user for basics on every task.
- **Run `audit-preflight` before any audit or task.** Check the business-context document
  exists and is current — missing, or older than 90 days, or contradicted by measured data means
  **ask** whether to refresh it (via `feel-brand-strategy`, researching the live site and public
  presence first, then asking only what research could not answer) or proceed as-is. Then
  enumerate the connectors the work needs — Meta, the commerce platform, Composio, GA4, Google Ads
  and every other paid channel, GSC, Merchant Center, the Meta catalog, Semrush, email/CRM — and
  ask in **one batched question** which to connect before the run. Scale both checks down to what
  a single task actually needs: if nothing is missing and the context is current, ask nothing and
  start. Preflight offers and records; it never blocks.

## Creative is the lever

Google is `Demand → Search → Product → Purchase`. Meta is
`Creative → Attention → Desire → Click → Product → Purchase → LTV`. A technically perfect
account with mediocre creative still struggles, so roughly a third of the audit is creative and
the run order reflects it.

The creative sections do not produce a list of winning ads. They produce a **creative learning
system**: which hook, problem, benefit, product, proof point, objection, format, creator,
opening three seconds, CTA, offer and persona win — and specifically which win *purchases*
rather than clicks.

That work is built on one dataset, `audits/<run-id>/creative-database.csv`
(`schemas/creative-record.yaml`), written once by agent 59. **Nothing downstream re-queries Meta
for creative performance.** The Top Creatives dashboard renders that file; so do the fatigue,
angle and scale analyses. A dashboard and a findings list that disagree are worse than either
alone, and they disagree the moment two components pull their own data with slightly different
windows.

Rule-based creative tagging runs off the account's ad-naming convention, which is why naming
compliance is a load-bearing finding here rather than a cosmetic one: names that do not parse
cannot be learned from. Report it spend-weighted.

## Skill layers

All three live in `.claude/skills/`, and they do not carry the same authority.

- **Audit skills** establish what is true. Evidence-graded; may be cited in findings.
- **Marketing skills** propose what to build. Advisory build-time guidance; they never override
  the operating rules above. A marketing skill's benchmark, threshold or rule of thumb is not
  evidence — a recommendation originating in one still needs a number, source, date range,
  formula, evidence class and confidence before it can be presented as a finding.
- **Execution skills** govern mutations. They may be loaded only in the execution lane.

Handoffs run audit → marketing, never the reverse. `SKILL-INDEX.md` maps all three layers and
the handoffs between them.

## Run order

A full audit is the **30-section framework** in `.claude/skills/full-audit/SKILL.md`, run top to
bottom in **one pass**. Each section names its owning agents there; the sequence is in
`workflows/02-full-account-audit.md`.

```
0.  audit-preflight — business-context freshness and connector gaps, offered to the user
1.  /full-audit, or agents/01-full-account-audit-agent.md
2.  Source discovery through the full connector ladder
3.  §1  Business & economics — names the ONE primary goal. Gate.
4.  §2  Tracking & measurement — pixel, CAPI, dedup, EMQ, AEM. Gate.
5.  §3  Reconciliation — Meta's claim vs Shopify and GA4. Mandatory, before any economics.
6.  §4–§29  Structure, bidding, creative (§7–§11), audiences, catalog, Advantage+, placements,
    funnel, landing pages, offers, SKU economics, geo/device, LTV loop, attribution,
    incrementality, Ad Library, hygiene, budget allocation
7.  §30 Scorecard, opportunity matrix, scale matrix, 30/60/90 plan, quantified upside,
    executive page
```

**§1 precedes everything economic. §2 precedes every attribution claim. §3 precedes any
economic conclusion. §30 runs last.** Sections with no dependency between them may run in
parallel.

## Gates order the sweep; they never stop it

A `RED` measurement verdict lowers the confidence label on every downstream economic claim and
is reported prominently — it does not end the audit. Continue every other section and mark the
affected findings `DEGRADED`, but do not issue scale or kill recommendations that depend on
conversion values you have just shown to be unreliable.

Missing cost inputs never block a run. Derive margin from the commerce platform; if that fails,
ask the user without stalling the sweep; if they skip, continue on a clearly labelled
assumption and show the sensitivity. Withhold only the figures that genuinely require margin —
break-even ROAS, CAC ceiling, scale and kill calls. Waste, structure, creative, measurement,
catalog, audiences and CRO findings are all still delivered in full.

## Completeness

A full audit is a complete top-to-bottom sweep of all 30 sections in one pass. Every section
ends labelled `FINDINGS`, `CLEAN`, `DEGRADED`, `N/A` or `BLOCKED`, written to
`audits/<run-id>/coverage.md`. **Never leave a section silently unrun** — the reader cannot tell
"checked and fine" from "never looked" unless you say which it was. Derive the tally from the
rows programmatically; a hand-written summary line drifts from the table beneath it and
discredits the ledger it summarises.

## Persistent artifacts

Audit outputs go under `audits/<run-id>/`; never overwrite a prior run. Every full run produces
`preflight.md`, `coverage.md`, `creative-database.csv`, `top-creatives.html`,
`reconciliation.md`, `scorecard.md`, `opportunity-matrix.md`, `scale-matrix.md`,
`action-plan.md`, `quantified-upside.md` and `executive-summary.md`, plus the evidence appendix.

Execution outputs go under `changes/<run-id>/`. Both directories are gitignored: they hold
account ids, spend, creative and order data.

## Connectors

`tools/REGISTRY.md` and `tools/integrations/*.md` are the connector reference — auth, scopes,
MCP availability, real operations. Consult them instead of guessing, but **runtime discovery
wins over anything written there.**

The Meta connector is the one source this OS cannot run without. It is reached through the
account's configured connector rather than a server pinned in `.mcp.json`, because its server id
is per-account. If you add a self-hosted MCP server to `.mcp.json`, **pin it to an immutable
reference** — an unpinned spec re-resolves on every launch and would execute new code locally
holding this account's Meta credentials. Pin it, or document why it cannot be pinned.

`tools/clis/*` is read-only during an audit; the mutating surface is enumerated in
`tools/clis/README.md`. Changes to a live account go through the execution lane, never through
these scripts — reaching for `meta-ads.js` mid-audit bypasses every safeguard in
`EXECUTION-PROTOCOL.md`.

## Adding to the library

`AUTHORING.md` holds the frontmatter rules, output contract and validators for new agents and
skills. Run every validator in `scripts/` before committing.
