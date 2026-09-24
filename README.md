# Meta Ads Ecommerce OS

A Claude Code–native operating system for D2C e-commerce Meta ad accounts. It **audits** — 177
agents and 105 skills across a 30-section framework — and, under a separate fenced protocol, it
**executes**.

The premise, inherited from its Google counterpart: most audits fail not because nobody looked at
the account, but because they optimised numbers that were not true. So the run order is fixed —
**reconcile, measure, price, then scale.** Measurement and economics are gates, not chapters.

---

## Quickstart

### 1. Install

Two commands. The first registers the catalog, the second installs from it — adding the
marketplace alone installs nothing:

```
/plugin marketplace add undark-ai/Meta-Ads-OS
/plugin install meta-ads-os@meta-ads-os
```

**From a local clone** — same two commands, pointed at the directory instead of the repo. Use this
if you want to modify the system or work offline:

```
git clone https://github.com/undark-ai/Meta-Ads-OS.git
/plugin marketplace add ./Meta-Ads-OS
/plugin install meta-ads-os@meta-ads-os
```

Either way, run a full audit with:

```
/meta-ads-os:full-audit
```

Plugin skills are namespaced, so the `meta-ads-os:` prefix is part of the command. Asking in plain
language also works — *"Run the full Meta Ads audit on my account."*

Verify the install with `claude plugin details meta-ads-os`; it should report 105 skills and 177
agents.

### 2. Connect Meta

The one hard requirement is a **Meta Ads MCP connector on the account you want to audit**. Without
it there is no audit. Everything else is optional and degrades the run rather than stopping it —
[what a full audit needs](#what-a-full-audit-needs) gives the cost of each gap.

This repository deliberately does not ship a Meta server; see
[how Meta connects](#how-meta-connects-and-why-mcpjson-does-not-ship-a-server) for why, and what
to do if you add one.

### 3. Optionally, write the business context file

Preflight and several skills look for `.agents/product-marketing.md` — product, ICP, positioning,
margins, offers. **It is yours to write.** Nothing ships it, and it is gitignored so it never
leaves your machine. Skip it and the system asks those questions interactively instead; write it
once and it stops asking.

### 4. Run it

Preflight runs before any data is pulled and asks two things: do we know the business, and can we
see the data. **Preflight offers; it never blocks.** "Proceed as-is" is always valid and is
recorded, so a section that later closes `BLOCKED` reads as an accepted trade rather than an
oversight.

Then it sweeps. A full audit is one top-to-bottom pass over all 30 sections — long by design,
because it queries every section rather than stopping at the first missing input. On an
unfamiliar account the cheaper opening move is the foundational audit, which answers only *is
this account measurable, and is it economically viable?* — ask for it by name, or point Claude at
[`workflows/01-foundational-audit.md`](workflows/01-foundational-audit.md).

**An audit never touches your account.** Applying changes is a separate lane, entered
deliberately, with its own protocol and its own approvals.

### What you get

Output lands in `audits/<run-id>/`, one directory per run, never overwritten:

```
preflight.md            what was asked before the run, and what you chose
coverage.md             all 30 sections, each with its state
creative-database.csv   one row per ad — the creative spine
top-creatives.html      the Top Creatives dashboard
reconciliation.md       Meta's claim vs what the store banked
scorecard.md            per-category, against published weights
opportunity-matrix.md   what is broken, ranked in contribution
scale-matrix.md         where the next dollar goes
action-plan.md          30/60/90, sequenced so each change stays readable
executive-summary.md    the decision page
```

Narrower sequences live in `workflows/` — foundational audit, creative deep dive, weekly and
monthly cycles, scale decision, peak planning, execution run, quality control, executive review.

---

## What a full audit needs

You do not have to work this out first. `audit-preflight` runs before anything and asks which of
these to connect, saying what each one costs if you skip it. Connect nothing beyond Meta and the
audit still runs — it records what it could not see.

| Source | Standing | Without it |
|---|---|---|
| **Meta Ads connector** | Required | There is no audit |
| **Commerce platform** — Shopify, WooCommerce | Required | Revenue truth. Every ROAS stays a platform claim; reconciliation and margin both collapse |
| **GA4** or equivalent | Strongly recommended | The funnel's mid-stages, and the only neutral arbiter between two platforms that both over-claim |
| **Other paid channels** — Google, TikTok | Strongly recommended **in practice** | Blended MER needs *total* ad spend. Two platforms routinely claim the same order; you cannot see that with one connected |
| **Meta product catalog** | Required *if* catalog, DPA or Advantage+ Shopping runs | Feed quality, disapprovals, product diagnostics |
| **Email/CRM** — Klaviyo, Attentive | Recommended | The LTV loop: whether first-party value flows *back* into Meta |

## How Meta connects, and why `.mcp.json` does not ship a server

Meta is reached through the account's **configured connector**, not a server pinned in this repo.
Its MCP server id differs per account — tools arrive as
`mcp__<SERVER_ID>__ads_get_ad_entities` — which is exactly why *discover tools before use* is a
rule here rather than a convenience. Agents resolve the real prefixed names at runtime.

`.mcp.json` ships only Semrush (HTTP, optional competitive context). It deliberately does **not**
ship a self-hosted Meta server: third-party ones exist, but any server listed here executes
locally holding this account's Meta credentials, and none has been audited. If you add one,
**pin it to an immutable reference** — an unpinned spec re-resolves on every launch — or document
why it cannot be pinned.

---

## What makes this different

Three things separate this from
[`undark-ai/Google-Ads-OS`](https://github.com/undark-ai/Google-Ads-OS), and they shape everything
below.

**Creative is the lever.** Google is `Demand → Search → Product → Purchase`. Meta is
`Creative → Attention → Desire → Click → Product → Purchase → LTV`. A technically perfect account
with mediocre creative still struggles, so four of the thirty sections are creative and the
output is a **creative learning system** — which hook, angle, proof point, creator and offer win
*purchases* — not a list of winning ads.

**The connector can write.** The Google Ads MCP is read-only, so that system's safety story is
"we have no hands". This one has hands. The boundary is therefore enforced rather than asserted:
every one of the Meta connector's 102 tools is classified read or write, audit agents may call
only the 61 reads, and `scripts/validate-execution-boundary.py` fails the build if one so much as
references a write. Unclassified tools are treated as writes — fail closed.

**Meta grades its own homework.** Modelled conversions, view-through attribution, Aggregated Event
Measurement and the 7-day-click default mean Meta's reported figures are a *claim* until
reconciled. A modelled value never carries the `OBSERVED` evidence class, and Meta's assertions
about Meta — opportunity score, relevance rankings, EMQ — are `PLATFORM_STATED`: reportable,
never proof.

---

## The two lanes

| | Audit lane | Execution lane |
|---|---|---|
| Agents | 00–199 | 200+ |
| Meta tools | the 61 classified `read` | `read` + the 41 `write`, under the protocol |
| Output | findings, recommendations | applied changes + a change register |
| Entry | `/full-audit`, workflows 01–07, 09–10 | `workflows/08-execution-run` only |

**An audit never mutates as a side effect.** Not "usually", not "unless the user seems to want
it". An audit that fixes what it finds is describing an account that no longer exists by the time
anyone reads the report.

Every mutation obeys all seven rules in [`EXECUTION-PROTOCOL.md`](EXECUTION-PROTOCOL.md): a
written change plan with before-values, explicit per-run approval, preview before publish,
**create paused** with activation as a separate approval, a change log written as each call
returns, one material change at a time with a 14-day read window, and specific rules for customer
data.

---

## The 30 sections

Full definitions and their agent mapping: [`.claude/skills/full-audit/SKILL.md`](.claude/skills/full-audit/SKILL.md).
Sequence: [`workflows/02-full-account-audit.md`](workflows/02-full-account-audit.md).

| | |
|---|---|
| **1–3 Foundations** | Business & economics (gate) · Tracking & measurement (gate) · **Reconciliation** (mandatory, before any economic conclusion) |
| **4–6 Structure** | Account structure · Campaign performance & trend windows · Bidding, delivery & learning phase |
| **7–11 Creative** | Creative database → **Top Creatives dashboard** · Fatigue · Angle & hook analysis · Testing system · Relevance & auction diagnostics |
| **12–15 Audience** | Audience strategy · Prospecting · Retargeting · Frequency & saturation |
| **16–18 Catalog & delivery** | Product catalog · Advantage+ Shopping & Creative · Placements |
| **19–24 Post-click & economics** | Funnel · Landing pages & CRO · Offers · SKU economics · Geo & device · New vs returning and the LTV loop |
| **25–29 Truth & allocation** | Attribution · Incrementality · Competitive & Ad Library · Hygiene & permissions · Budget allocation |
| **30 Output** | Scorecard · opportunity matrix · **scale matrix** · 30/60/90 · quantified upside · executive page |

**§1 precedes everything economic. §2 precedes every attribution claim. §3 precedes any economic
conclusion. §30 runs last.** Everything else may run in parallel.

### Gates order the sweep; they never stop it

A `RED` measurement verdict lowers confidence on every downstream economic claim and is reported
prominently — it does not end the audit. Every other section still runs, findings are marked
`DEGRADED`, and only scale and kill recommendations that depend on the untrustworthy conversion
values are withheld. Most of a Meta audit never needed conversion value.

Missing margin never blocks a run either: derive it from the commerce platform, else ask without
stalling the sweep, else proceed on a labelled assumption and publish the range — stating whether
the recommendation changes across it. Usually it does not.

### Completeness

Every section closes labelled `FINDINGS`, `CLEAN`, `DEGRADED`, `N/A` or `BLOCKED` in a coverage
ledger, and the tally is derived from the rows programmatically. The reader has to be able to tell
"checked and fine" from "never looked", and `N/A` (the layer does not exist) from `BLOCKED` (an
input was unreachable).

---

## The creative spine

Section 7 writes `audits/<run-id>/creative-database.csv` once, against
[`schemas/creative-record.yaml`](schemas/creative-record.yaml) — one row per ad, carrying hook
rate, hold rate, video quartile retention, the parsed naming-convention tokens, the
classification, the funnel, the economics, and the measurement basis each number stands on.

**Sections 8–11, 19, 22 and 30 read that file. Nothing downstream re-queries Meta for creative
performance.** A dashboard and a findings list that disagree are worse than either alone, and
they disagree the moment two components pull with slightly different windows.

Section 7 also renders the **Top Creatives dashboard**: ad cards ranked by spend, purchases,
ROAS, hook rate or hold rate; Performance / Attention / Funnel tabs; a creative patterns table
(tag → ads, spend, purchases, CPA, ROAS) that section 9 consumes; and a per-ad drill-down with
the funnel path against account medians and the **promise-handoff score** against the landing
page.

Rule-based creative tagging runs off the account's ad-naming convention — which makes naming
compliance load-bearing rather than cosmetic: names that do not parse cannot be learned from. It
is reported spend-weighted, because ninety percent of *ads* parsing while the three biggest
spenders do not is a failing account.

---

## Structure

```
agents/     177 agents      ← 163 audit (00–162) + 14 execution (200–213). Orchestration 00–06,
                                       economics 07–20, measurement 21–36, reconciliation 37–42,
                                       structure & delivery 43–58, creative 59–78, relevance 79–82,
                                       audience 83–92, prospecting & retargeting 93–100,
                                       catalog 101–108, Advantage+ 109–114, placement 115–118,
                                       funnel & CRO 119–128, offer 129–133, geo & device 134–137,
                                       attribution & incrementality 138–144, competitive 145–147,
                                       trend & change 148–152, budget 153–155, output 156–162.
                                       Execution 200–213 — govern, operate, close
.claude/skills/      105 skills      ← 46 audit · 53 marketing · 6 execution
.claude-plugin/                     ← plugin / marketplace install path
tools/              162 files       ← connector registry, read on demand
  REGISTRY.md                         index of 93 tools × API / MCP / CLI / SDK
  integrations/      93 guides       auth, scopes, endpoints, operations
  clis/              64 scripts      read-only during an audit (see clis/README.md)
schemas/             12 files       ← contracts: finding, opportunity, reconciliation,
                                      creative-record, scale-matrix, tool classification
orchestration/        5 files       ← orchestrator, execution engine, data registry, manifest
workflows/           10 files       ← named sequences
templates/            5 files       ← finding, executive summary, change register, brief
scripts/              9 files       ← 8 validators + the run initialiser (run before committing)
CLAUDE.md                           ← the operating rules. Read this first.
EXECUTION-PROTOCOL.md               ← the mutation contract
AGENT-INDEX.md · SKILL-INDEX.md     ← the libraries and their bands/layers
AUTHORING.md                        ← how to add an agent or a skill
ATTRIBUTION.md · FIELD-NOTES.md     ← provenance; and defects found in live runs
```

Every agent must be mapped to one of the 30 sections or it will never run; `AGENT-INDEX.md`
holds that map, and `scripts/validate-section-map.py` checks it against the agents' own
frontmatter on every push.

---

## The three skill layers

They live in one directory and do **not** carry the same authority.

- **Audit skills (46)** establish what is true. Evidence-graded; may be cited in findings.
- **Marketing skills (53)** propose what to build. Advisory. A marketing skill's benchmark is
  **never** evidence for a quantified finding — a recommendation originating in one still needs a
  number, source, date range, formula, evidence class and confidence before it can be presented
  as one. Each carries a banner saying so.
- **Execution skills (6)** govern mutations, and may be loaded only in the execution lane.

Handoffs run audit → marketing, never the reverse. [`SKILL-INDEX.md`](SKILL-INDEX.md) maps all
three and the handoffs between them.

---

## Disciplines the system enforces

**Walk the connector ladder, every run.** Native connector → gateway or aggregator → the commerce
platform as proxy → ask the user → `UNAVAILABLE`. **A previous run's verdict is never inherited** —
connectors get authorised between runs, and re-checking is the cheapest test in the system.

**Reconcile before concluding.** Meta's claimed purchases and value are set against banked orders
before any economic conclusion. Blended MER uses **total** ad spend across every channel; computed
on Meta's alone it is wrong, not merely partial.

**Never average a ratio across entities.** CTR, ROAS, frequency, hook rate, CVR — recompute from
component sums. Averaging an ad-level ratio to an ad-set figure weights a 12-impression ad the
same as a 1.2-million-impression one, and the result looks entirely plausible.

**Volume gates conclusions.** Meta's learning threshold is ~50 conversions per ad set per week,
and ad-level purchase counts are small. Below the purchase floor the answer is
`INSUFFICIENT_DATA` and the next step is to buy more data — an ad killed at four purchases was
killed on a coin flip.

**Contribution, not ROAS.** Revenue, conversion value, MER and GMV are not profit.

[`FIELD-NOTES.md`](FIELD-NOTES.md) records where these came from: each is a defect found by
running a library against a real account.

---

## Validate

Eight checks, and CI runs all of them on every push and pull request
([`.github/workflows/validate.yml`](.github/workflows/validate.yml)):

```bash
python3 scripts/validate-references.py          # skill names, cross-refs, agent→skill resolution
bash    scripts/validate-agent-library.sh       # frontmatter, name↔filename, sections, read-only
bash    scripts/validate-skills.sh              # spec compliance, line limits, descriptions
python3 scripts/validate-docs.py                # README tree and counts against disk
python3 scripts/validate-section-map.py         # the section map against the agents' frontmatter
python3 scripts/validate-execution-boundary.py  # no audit agent references a write tool
python3 scripts/validate-doc-freshness.py       # core docs still describe the system
python3 scripts/audit-cli-writes.py --check     # tools/clis mutation surface still documented
```

Two of these exist because the failure they catch already happened. `validate-execution-boundary`
found the tool classification had drifted four tools from the connector, which — under
fail-closed — had silently made six read tools unavailable to every audit agent.
`validate-section-map` found sixteen agents claimed by two sections at once, because the map used
ranges that overlapped. Both are recorded in [`FIELD-NOTES.md`](FIELD-NOTES.md).

Then run `00-agent-quality-controller` for the judgement pass the validators cannot do — sample
floors, recomputed margins, duplicated work, agents mapped to no section.

## Provenance

Architecture from `undark-ai/Google-Ads-OS` (MIT). The `tools/` registry from
[`coreyhaines31/marketingskills`](https://github.com/coreyhaines31/marketingskills) (MIT, © 2025
Corey Haines). The Meta marketing family includes material adapted from
[`swan-gtm/gtm-skills`](https://github.com/swan-gtm/gtm-skills) (MIT, © 2026 Swan; original skills
by Ivan Falco / Frontal), plus concepts reviewed from
[`emilyhellqvist/meta-ads-skills`](https://github.com/emilyhellqvist/meta-ads-skills) by Emily
Hellqvist. The Top Creatives dashboard comes from an internal Undark skill and was genericised.

[`ATTRIBUTION.md`](ATTRIBUTION.md) records what was kept, dropped and modified file by file;
[`THIRD_PARTY_NOTICES.md`](THIRD_PARTY_NOTICES.md) retains the upstream notices. Licensed MIT —
see [`LICENSE`](LICENSE).
