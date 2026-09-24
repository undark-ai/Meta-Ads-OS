# Field notes

Defects found by running this library against real accounts, and what changed in the repository
because of them. Each entry names the failure, not just the fix — a rule with no story attached
gets relaxed by the next person who finds it inconvenient.

Google-Ads-OS keeps the same file for the same reason. Several of its entries transfer directly,
and are recorded here as **inherited** rather than rediscovered, so nobody has to pay for the
same lesson twice.

---

## Found while building

### Overlapping ranges in the section map, and the same bug twice

*Found 2026-08-26, QA sweep before the first live run.*

`full-audit/SKILL.md` maps each of the 30 sections to the agents that own it. Written as ranges —
`43–50`, `83–92`, `97–99` — which read cleanly and quietly overlap: §4 and §28 both claimed
43–50, §12 and §15 both claimed 90–92, §14 and §24 both claimed 99. Sixteen agents were claimed
by two sections at once, and eight rows disagreed with the agents' own `section:` frontmatter.

**This is the second time.** The first was three post-click agents mapped to §19 when §19's range
had no room for them; that got patched as a one-off. It was not a one-off — it was this, and
patching the symptom left the cause in place to bite again.

The fix is structural rather than editorial. The frontmatter is authoritative:
`validate-agent-library.sh` requires a `section:` on every agent, and the orchestrator runs
sections rather than ranges. So the map is a **derived view**, and `scripts/validate-section-map.py`
now checks it against its source on every push — every agent's section appears in that section's
row, no row claims an agent that declares another section, no agent is claimed twice. The map
itself was regenerated from the frontmatter rather than hand-corrected.

Verified by reintroducing the original §19 range and confirming the validator produced eight
failures naming exactly the three double-claimed agents and the two omitted ones.

**The general lesson.** A range is a compression of a list, and compressions drift silently
against the thing they compress. Where a document restates machine-checkable state, either derive
it or check it — a hand-maintained restatement will be wrong eventually, and it will be trusted
while it is wrong.

---

### A shipped skill with no tool behind it: automated rules

*Found 2026-08-26, building the execution band.*

`meta-rules-deploy` is one of the six execution skills — thresholds, guardrails, notify-only
first. The original Phase 3 plan listed a rules-deployer agent to go with it. Checking the
classification before writing it: **the connector exposes no rules-writing tool at all.** Not
classified as a write, not classified as a read — absent.

So there is no rules-deployer agent. Agent 200's capability check states the gap explicitly:
automated rules are deployed in Ads Manager by a human, and the skill supplies what to encode.

**The temptation worth naming.** The obvious move was to write the agent anyway, describing rules
in prose and letting it "recommend" them — which would have looked like a complete band and been
an agent that cannot act. A repository that claims a capability it does not have is worse than
one with a stated gap, because the gap gets discovered mid-run on a live account.

The general check: before writing an agent around a skill, confirm a tool exists for what it
does. A skill can be pure guidance; an agent in the execution band is a promise to act.

---

### The tool classification had drifted from the connector, and fail-closed made it bite

*Found 2026-08-26, writing agent 25 (`content-ids-and-catalog-matching`).*

<!-- execution-boundary: documents-writes -->

`scripts/validate-execution-boundary.py` failed on a reference to `ads_catalog_list_products` — a
real, read-only connector tool that was absent from
`schemas/meta-mcp-tool-classification.yaml`. Because the file's `unclassified_default` is `WRITE`,
an unlisted read tool is treated as a mutation and audit agents are blocked from calling it.

Diffing the whole file against the connector's live tool list found the classification carried 98
tools against an actual 102:

- **Six reads missing** — `ads_catalog_get_businesses` and the whole catalog `list_*` family.
  All six were silently unavailable to every audit agent in the repository.
- **One write missing** — `ads_creative_upload_media`.
- **Three entries that no longer exist** — `ads_creative_upload_local_image`,
  `ads_finalize_local_ad_image_upload`, `ads_delete_local_ad_image`. Superseded by the
  `upload_image` / `upload_video` / `upload_media` family.

Corrected to 61 read / 41 write, and the counts in `README.md` and `AGENT-INDEX.md` updated with
them.

**What this says about fail-closed.** The default is right — an unclassified tool must never be
callable by an audit agent, because a wrong guess in the other direction is a mutation on a live
account. But its cost is that connector drift presents as a *capability gap* rather than as an
error: the tools were not refused loudly, they were simply never used, and nothing would have
surfaced that until an agent happened to name one. So the diff itself is the thing worth keeping —
compare the classification against the live tool list when the connector changes, rather than
waiting for a validator to trip on it by luck.

---

## Known before the first run

These come from the sources this repository vendored — the platform limits and behaviours that
were already documented, and that would otherwise be rediscovered expensively.

### Ratio averaging silently corrupts every rollup

*Source: `meta-ads-team/references/meta-platform-reference.md`.*

Averaging ad-level CTR, ROAS, frequency or CVR to get an ad-set or campaign figure weights a
12-impression ad the same as a 1.2-million-impression one. The result is not approximately
right — it is wrong in a direction nobody can predict from the output, and it looks entirely
plausible. Every rollup recomputes from component sums.

**Changed:** the rule is in `CLAUDE.md`, in `schemas/canonical-data-model.md`, and the creative
record stores components alongside every derived ratio so a rollup can always be recomputed.

### Breakdowns do not compose, and the totals move

Meta rejects some breakdown combinations and silently returns different totals across others.
A placement × age × device pull is not a valid decomposition of the account.

**Changed:** one breakdown dimension per call, and every breakdown is reconciled against its
parent total. If the rows do not sum, rows are missing and the audit says so rather than
presenting a subset as the whole.

### `is_ads_mcp_enabled: false` beats `is_queryable: true`

*Source: `creative-analysis-dashboard`.*

An account can report as queryable and still be un-queryable, because Meta's MCP rollout gates
it separately. A run that trusts the wrong flag fails deep into the sweep rather than at
preflight, after the user has been told it started.

**Changed:** preflight probes both flags, and confirms the account has spend in the intended
window before anything else runs. A dormant account is a preflight answer, not a §5 mystery.

### Meta returns numbers as formatted strings

`"$58,758.12 USD"`, `"1,694,974"`, `"1.55%"`, `"Not available"`. Naive parsing turns
`"Not available"` into `0`, and a zero is a claim — it says "we looked and there were none",
which is the opposite of what the field meant.

**Changed:** the nullability rule in `schemas/creative-record.yaml`. A missing value is null and
stays null. A null hook rate on a static ad and a 0.0 hook rate on a video nobody stopped for
mean opposite things, and a ranking that conflates them puts the wrong ads at the top.

### Creative thumbnails cannot be relied on as durable assets

`thumbnail_url` is 64px and expires in weeks; signed URLs cannot be upscaled (editing `stp=`
returns a signature mismatch); the artifact sandbox blocks Meta's CDN entirely; and
`ads_get_ad_preview` renders inline in chat only, with short-lived URLs that require the viewer
to be logged in to Facebook.

**Changed:** the dashboard uses styled placeholders plus Preview and Ads Manager deep links, the
Chrome snapshot is explicitly regenerable rather than permanent, and the deliverable never
promises an image will still be there next month.

### Ad Library longevity is not evidence of profitability

A competitor's ad running for six months means it is running. It does not mean it works —
plenty of accounts leave losers on.

**Changed:** §27 classifies every Ad Library observation as competitive *context*, and
`finding-schema.yaml` has no evidence class that would let it become proof.

---

## Inherited from Google-Ads-OS

These were found on Google Ads accounts, and the failure mode is the platform-agnostic part.

### A source ruled out on one route was authorised on another

The connector ladder exists because a source was called `UNAVAILABLE` after the native route
failed, while sitting authorised on a gateway the whole time. Whole phases of an audit were
deleted silently.

**Changed:** the ladder is walked every run, the rung that supplied each source is recorded in
`source-capabilities.md`, and **a previous run's `UNAVAILABLE` is never inherited**. Re-checking
is the cheapest test in the system.

### Blended MER computed on one platform's spend

MER on Meta's spend alone is not a partial MER. It is a different, wrong number — and it hides
the case it exists to reveal, which is two platforms each claiming the same order.

**Changed:** §3 enumerates every paid channel before computing MER, and the reconciliation
schema makes total-spend basis a required property of the measure.

### A hand-written coverage tally drifted from its own table

The summary line said 25 sections covered; the table beneath it showed otherwise. Because the
summary is the first thing a reader trusts, a wrong one discredits the ledger it summarises.

**Changed:** the tally is derived from the rows programmatically and checked against the section
count. Where the ledger is also published elsewhere — an artifact, a slide — the two are checked
against each other.

### Missing margin inputs stopped an entire audit

A run stalled on an unanswered COGS question and delivered nothing, when the great majority of
its findings — waste, structure, creative, measurement, audiences, CRO — never needed margin at
all.

**Changed:** the escalation ladder in `CLAUDE.md`. Derive margin from the commerce platform,
else ask without stalling the sweep, else proceed on a labelled assumption and publish the
sensitivity. Withhold only the figures that genuinely require margin.

---

## Found in Meta runs

*Add entries here rather than quietly patching a rule — the story is what stops the rule being
relaxed later.*

### The split was applied to the tables and not to the charts

*Run: 2026-08-27 · same account · also caught by the account owner*

Immediately after the brand/generic rule was written and merged, the corrected audit still shipped
a **blended "Paid Search" bar** in its session→add-to-cart chart, and blended per-channel funnel
charts beside it. The prose table below them was correctly split; the charts were not. A caveat
paragraph had been added above the chart saying the bar was "brand and generic mixed together".

That is the same failure the new rule had just been written to prevent, one layer down. A reader
takes the funnel's *shape* from the chart and frequently never reaches the table, so the chart is
the more dangerous half of the output — and a caption asking the reader to mentally correct a bar
is not a correction.

**Changed:** `funnel-analysis`'s chart section now states that the split applies to every chart,
that captioning a blended bar is not a fix, and that if a segment is not fit for the table it is
not fit for a bar. PMax is named too — GA4 files it under `Cross-network`, where a channel-group
chart hides it entirely.

### Comparing blended search to paid social inverted the ranking

*Run: 2026-08-27 · Account type: apparel D2C, Israel · caught by the account owner, not by the
library*

The first cross-channel funnel run reported that paid search acquired a customer for **₪101**
against paid social's **₪263**, and that paid social converted session→ATC at 14.5% against paid
search's 38.8%. Both figures were published with a caveat that search was "mostly brand" — and the
caveat was worthless, because the blended numbers were still in the table being compared.

Separating brand from generic reversed the finding entirely:

| Segment | Sessions | Sess→ATC | Spend | GA4 txn | CAC | ROAS |
|---|---:|---:|---:|---:|---:|---:|
| Brand search | 414 | **54.6%** | ₪506 | 31 | **₪16** | 20.09 |
| **Generic search** | 206 | **10.2%** | ₪1,380 | 3 | **₪460** | **0.46** |
| Meta paid social | 10,388 | 14.5% | ₪38,411 | 146 | **₪263** | 1.23 |

Generic search — the only segment comparable to paid social — costs **₪460 per customer against
Meta's ₪263** and converts *worse* at session→ATC. Meta was roughly 1.7× better than comparable
Google traffic, not 2.6× worse. Brand carried 31 of the 34 paid-search transactions on 27% of the
search spend, and it was dragging every blended average with it.

The error compounds: **blending does not overstate search a little, it inverts the ranking**,
because brand carries most of the transactions on a fraction of the spend. And the recommendation
that followed — move budget from paid social toward paid search — was the exact opposite of what
the data supported.

A second defect rode along. The ₪101 also counted **PMax spend as search spend**, because GA4 puts
PMax in `Cross-network` while the Google Ads campaign list looks like one Google total. Attributing
platform spend to a different segment than its sessions understated search CAC twice over.

A third, found while fixing it: **both platforms over-claim against GA4 by about the same factor** —
Meta 2.09×, Google search 2.21×. Any cross-channel CAC table built from each platform's own
conversion counts is comparing attribution aggressiveness, not performance.

**Changed:** `funnel-analysis` gains a mandatory brand/generic/shopping split with a table of what
may and may not be compared, the rule that GA4's channel group is **not** a valid splitter (it mixes
brand and generic, and hides PMax in cross-network), and the requirement to attribute spend to the
segment its sessions landed in. `CLAUDE.md` carries it as a standing rule beside blended-MER.
`cross-source-reconciliation` gains the shared-numerator rule. `incrementality` gains the reading
that brand search is a meter for demand *other* channels created, which is what makes it the
cheapest incrementality signal an account already has.

### Preflight had been reduced to half of what Google-Ads-OS asks

*Found 2026-08-27, comparing this repository against `undark-ai/Google-Ads-OS`, which it was
built from.*

`audit-preflight` here was 66 lines. The same skill in Google-Ads-OS is 134, and the difference is
not Meta-versus-Google specifics — it is content that was dropped in the port:

- The **staleness table**. Google's has four states (missing · ≤90 days · >90 days · contradicted
  by measured data) with a different question for each. Ours asked one flat question.
- **Reading `last_updated` from inside the document**, not only the filesystem mtime, "because a
  file touched by a git checkout is not a file whose contents were reviewed."
- **"Age is not the only trigger"** — a new product line, a price change, a repositioning, a new
  market, a change of primary customer.
- **The `feel-brand-strategy` handoff**, by name, with the note that it is a plugin skill rather
  than vendored and what to fall back to when it is absent.
- **"Research before interrogating"** — read the live site and public presence, arrive with a
  draft, ask only what research could not answer. Ours said "research the live site" in passing.
- **Half the connector matrix**: Google Search Console, Merchant Center, Composio as a named row,
  Semrush, and the "usually forgotten" list — Tag Manager, payment/finance, BigQuery, the
  customer-list sources behind value-based audiences.
- **The entire "scaling preflight to a single task" table** — task → does it need business
  context → which connectors to ask about. Ours had three sentences.

The consequence showed up on the first live run: preflight never asked about Google Ads, GSC or
Merchant Center, and §3 then discovered mid-run that blended MER needed a channel nobody had been
asked to connect. The question that should have been asked up front became a caveat in the report,
which is precisely the failure the skill's own opening paragraph describes.

**Changed:** `audit-preflight` rewritten to Google's structure with Meta's specifics — the
four-state table, the `feel-brand-strategy` handoff, research-before-interrogating, the full
connector matrix including GSC/Merchant/GTM/BigQuery/CRM/payments, and the per-task scale-down
table. `CLAUDE.md`'s preflight rule now states the staleness threshold and the batched-question
requirement rather than gesturing at them.

### The ladder had no retry policy and no provenance tagging

*Found 2026-08-27, same comparison.*

Google-Ads-OS splits discovery across two skills: `mcp-discovery` walks the ladder, and
`mcp-orchestration` governs what happens to a result once you have it. Meta kept the first and
dropped the second. Two things went with it.

**Retry behaviour.** Google's says retry a transient failure at most twice and never retry a
validation error without changing the request. Ours said nothing, and on the live run an
unsupported-field error was re-issued unchanged before the error text was read properly — the
error names the fields that *are* supported at that level, which is the actual fix.

**Result tagging.** Google's requires every tool result to carry source, retrieval time, date
range, scope, query, raw-or-normalized status and confidence. Ours had none of it. `data-cache`
covers the cache key well — better than Google's, since it includes the attribution window — but a
cache key is not provenance, and an untagged result cannot be defended in a finding.

Also dropped: two ladder rungs. Google's has *approved third-party market intelligence* and
*browser observation* as explicit rungs before inference. Ours collapsed to native → gateway →
commerce proxy → ask the user, which left `browser-inspection` and `ad-library-extraction` as
skills with no position on the ladder.

**Changed:** `mcp-discovery` gains a retry policy, a result-tagging block, and the two missing
rungs. A tool that reports itself unavailable for the account is now explicitly *not* a retry case.

### Nothing said which source was allowed to be believed about what

*Found 2026-08-27, same comparison.*

Google-Ads-OS carries `schemas/source-adapter-registry.yaml`, giving each source a `mode`,
`discovery_required` flag and an `authority`. Meta had no equivalent. On the first live run three
sources disagreed about the same 90 days and nothing in the repository stated which one wins for
which metric — the auditor reasoned it out correctly, but from first principles rather than from a
contract.

**Changed:** added `schemas/source-authority.yaml`, with `authority` and an
`evidence_class_ceiling` per source — Meta capped at `PLATFORM_STATED`, Semrush at `INFERRED`, the
commerce platform at `OBSERVED`. It also records the two things the live run learned the hard way:
Shopify's per-order referrer field is not an attribution source, and GA4 undercounts the commerce
platform by roughly 5-15%.

### No skill read the ad copy the account was actually running

*Found 2026-08-27 · Account type: apparel D2C, 89 ads*

`creative-record.yaml` carries `primary_text`, `headline`, `description` and `cta_type` — the words
of every live ad. Nothing read them. `creative-dashboard`'s template rendered them; no skill
analysed them.

The library could say which *angle* won (`creative-angle-analysis`), which *format* won, and how to
generate more copy (`ad-creative`), but could not answer "is the copy we are running any good, and
what should it say instead" — which is what an operator looking at a 1.19-ROAS ad actually asks.
`copywriting` covers pages, `copy-editing` edits a document you hand it, `ad-writing-style` governs
voice, and `message-validation` scores messages on customer value. None of them reads the account.

**Changed:** added `ad-copy-audit` — reads the copy columns from the creative database, scores six
craft dimensions with the weak line quoted, joins each score to measured purchases, finds the
winning copy *decision* rather than the winning ad, and rewrites only where the ad carries real
spend, copy is the plausible constraint, and there is a specific quotable weakness. The purchase
floor governs it exactly as it governs creative: below the floor a copy score is unvalidated and
says so.

### The funnel could not tell a bad site from bad traffic

*Found 2026-08-27 · same account*

`funnel-analysis` mapped Meta's funnel well — including the two stages Google has no equivalent
for — but only Meta's. On the live run the account lost 79 of every 100 ad-driven landing-page
views before add-to-cart, and the audit could not say whether that was a site problem or a
paid-social traffic-quality problem, because it had nothing to compare against.

Those have opposite fixes. One is a §20 job; the other is §13 targeting and creative. The
distinction is available for free in GA4, which measures every channel the same way.

**Changed:** `funnel-analysis` gains a cross-channel section — the same stages by
`sessionDefaultChannelGroup`, paired with each platform's own spend so the comparison ends in cost
per outcome rather than rate — plus a reading table (all channels drop at the same stage means the
site; one channel alone means that channel). It also now **requires rendered charts** rather than
tables alone, with the rule that a rate is never charted without its denominator beside it.

### A mandatory rule rested on a tool the account did not have

*Run: 2026-08-26 · Account type: small-spend apparel D2C, Israel, ~₪38k / 90 days*

`CLAUDE.md` required checking `ads_account_get_activity_logs` before attributing any performance
movement to creative. On the first live account the tool answered: *"This tool is new and is being
gradually rolled out across ad accounts."* Meta ships it per account, and this account did not have
it.

The rule was stated unconditionally with no stated behaviour on absence, so four sections that
depend on the change map — §5, §6, §8, §9 — had no defined way to proceed. §6 closed `BLOCKED`
outright. The auditor invented a reasonable answer (cap confidence, withhold decay-based kills),
which is exactly the judgement a framework exists to remove.

The shape generalises: the library degrades well when **data** is missing — the margin ladder, the
connector ladder, gates-order-but-never-stop — and had no equivalent for a missing **field or
tool**.

**Changed:** `CLAUDE.md`, `full-audit/SKILL.md` and `orchestration/data-registry.md` now carry the
degradation path — derive what `created_time` and `effective_status` support, state that movement
cannot be tied to an edit, cap decay and trend confidence at `MEDIUM`, withhold decay-only kills,
and close `DEGRADED` rather than `FINDINGS`.

### The creative schema asked for a field the connector would not serve at ad level

*Run: 2026-08-26 · Account type: as above, 89 ads / 66 of them video*

`creative-record.yaml` sourced `hook_rate` from `3_second_video_plays`. The creative database is
one row per ad, so the field has to come back at ad level — and the connector rejected it there
(`Unsupported fields: 3_second_video_plays`) while accepting it at account level. The documented
substitute, `video_continuous_2_sec_watched_actions`, returned `null` on the same ads. `hook_rate`
was null for all 89 rows in an account that was two-thirds video.

The nullability rule held — nothing was filled in with a zero — and `creative-dashboard` already
said not to render a metric the account cannot supply. But that guidance was written for *the
account has no video ads*, and this was *the connector withheld the field*: same symptom, opposite
meaning to the reader.

**Changed:** `creative-record.yaml` gains a fallback ladder and a `video_plays_3s_source` column
recording which rung supplied the value; `creative-dashboard` now separates the two "cannot supply"
cases (`N/A` versus `DEGRADED`, hide versus state the reason) and withdraws the hook-rate sort when
the column is null; `creative-data-model` carries the caveat.

### The ladder named two gateways and recommended the wrong one

*Run: 2026-08-26*

Rung 2 read "Composio, Supermetrics and similar", and `tools/REGISTRY.md` went further —
"**Agent recommendation**: Supermetrics for pulling data from multiple marketing platforms". On the
live account, Composio already held authorised GA4 **and** Google Ads connections, and those two
were exactly what §3 needed: GA4 as the neutral arbiter, Google Ads for the total spend without
which blended MER is wrong rather than partial. Supermetrics was never needed.

Naming two gateways as equals gave the agent no rule, and the registry pointed at the one that was
not the answer. The skill also said the gateway rung is "not a fallback to reach for after the
native one fails" without saying **how to enumerate it** — that had to be invented mid-run.

Two traps surfaced and cost real time: GA4 offered three properties under the right account, two of
them sharing a name; Google Ads offered three customer ids, two belonging to **other advertisers**
(`USER_PERMISSION_DENIED`). Trusting either default would have put another company's spend in this
account's reconciliation.

**Changed:** the rule is now explicit — no native MCP means go to Composio — with the enumeration
procedure in `mcp-discovery`, the multi-account and manager-context traps written down, the
Supermetrics recommendation removed from `tools/REGISTRY.md`, and `tools/composio/README.md`
extended past setup into the GA4 and Google Ads pulls an audit actually makes.

### Three validators could not pass on a vendored install

*Run: 2026-08-26*

`README.md` documents "copying in" as a supported install — clone the library into the project you
want to audit. Doing exactly that and running the eight validators the README tells you to run
produced **15 failures across three of them**, on a library that was provably intact: they read
`README.md` as *this system's* document, and in a vendored layout that file necessarily describes
the host project.

The library passed every check that mattered. But an operator following the README's own
instructions saw red on a clean install, which trains people to ignore validator output — and
validator output is where the execution-boundary check lives.

**Changed:** `validate-docs.py` and `validate-doc-freshness.py` resolve the system document through
`system_readme()` — `docs/SYSTEM.md`, then `UPSTREAM-README.md`, then `README.md`. Upstream is
unaffected; a vendored copy that keeps `UPSTREAM-README.md` now validates in place. On the install
that found this, the three went from 15 failures to 0.

### The boundary validator could not be told about a tool it did not know

*Run: 2026-08-26*

The live connector exposed 106 `ads_*` tools; the classification named 105. The one gap,
`ads_log_ui_interaction`, defaulted to WRITE and was correctly refused — fail-closed worked.

Writing that up was the problem. `validate-execution-boundary.py` exempted files carrying the
`execution-boundary: documents-writes` marker from the write and retired checks, but computed
`unknown = found - known - retired` and reported it **regardless of the marker**. So the document
whose job is to report an unclassified tool could not name it without failing the build. The gap
could not be recorded until it was closed — backwards, and directly against the classification
file's own note that the list is "kept so the change is auditable and so FIELD-NOTES can name
them".

Separately, three tools sat in `retired:` under the comment "Names the connector once exposed and
no longer does […] they are NOT callable" — and the live connector was **still serving all three**,
alongside the `ads_creative_upload_media` that supposedly superseded them. The validator stated it
as fact: "the connector no longer exposes these".

**Changed:** the `unknown` branch is gated on `may_name_writes` like the other two;
`ads_log_ui_interaction` is classified; the retired bucket now says it records this repo's belief
rather than a fact about any account, and the message asks the reader to verify against the live
connector.

### A funnel denominator that the library had already got right

*Run: 2026-08-26 · recorded as a near-miss, not a defect*

Building §19, the click → landing-page-view step was first computed against Meta's `clicks` and
read **53.6%** — which ranked as the account's largest leak and would have sent the client to fix a
page-speed problem that did not exist. `clicks` counts likes, comments and profile taps; 41.1% of
this account's clicks were non-outbound. Against `outbound_clicks` the step is **91.0%** and
healthy, and the real leak was three stages deeper at LPV → add-to-cart.

The library had already anticipated this. `creative-record.yaml` defines
`click_to_lpv_rate = landing_page_views / outbound_clicks` with the note "a low value here is a
page-speed or redirect problem, not a creative one", and `funnel-analysis` carries the band
`LPV / outbound clicks | 40–70%` — which would have flagged 53.6% on sight. The rule was written;
it was simply not read before the number was computed.

**Changed:** nothing in the rule, because the rule was right. Recorded here because the near-miss
is the argument for the check: a documented denominator is easy to skip, and
`meta-ads-data-validation` is the natural home for enforcing it —
`lpv / clicks < 70%` while `lpv / outbound_clicks > 85%` means the wrong denominator is in use.

Template:

```markdown
### <One-line description of what went wrong>

*Run: <date> · Account type: <e.g. mid-spend apparel D2C>*

What happened, what the output claimed, and why it was wrong.

**Changed:** the file and rule that now prevent it.
```
