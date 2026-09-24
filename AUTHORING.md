# Authoring agents and skills

How to add to this library so new work loads correctly and holds the same evidence standard as
the rest. Validate with `scripts/` before committing — see [Validation](#validation).

Three kinds of unit, with different jobs:

| | Audit agents (`.claude/agents/`, 00–199) | Skills (`.claude/skills/`) | Execution agents (`.claude/agents/`, 200+) |
|---|---|---|---|
| Answers | "What is true about this account?" | "How do I do this well?" | "Apply this approved change" |
| Invoked | By the orchestrator, or by name | By trigger phrase | By `workflows/08-execution-run` only |
| Output | A finding set against a contract | Guidance, drafts, checklists | Applied changes + a change register |
| Evidence | Required — every number sourced | Not evidence; advisory only | Cites the finding it implements |
| Meta tools | `read` only | audit/marketing: `read` only | `read` + `write` under the protocol |

---

## Adding an audit agent

### 1. Number and name it

Files are `NNN-short-name-agent.md`, numbered into the existing bands — see `AGENT-INDEX.md`
for the authoritative ranges. Take the next free number in the right band; where a new agent
belongs to no existing band, append a new band after the last rather than inserting into a
range. **Do not renumber existing agents** — workflows and the orchestrator reference them by
number.

A new agent must also be mapped to one of the **30 audit sections** in
`.claude/skills/full-audit/SKILL.md` **and** in `workflows/02-full-account-audit.md`, and the
section it declares in frontmatter must match both — `scripts/validate-section-map.py` fails the
build otherwise. Write the row as an exact list rather than a range that reaches into a
neighbouring section's numbers; overlapping ranges are how sixteen agents ended up claimed by two
sections at once (`FIELD-NOTES.md`). An agent no section owns will never run in a full audit,
and will look present while doing nothing.

Frontmatter `name` is the filename without `-agent.md`: `61-creative-classifier-agent.md`
declares `name: 61-creative-classifier`. Lowercase, hyphens, unique across the library.

### 2. Write the frontmatter

```yaml
---
name: 163-example
description: Runs Meta Ads ecommerce audit agent 163: <one line on what it determines>. Use when the orchestrator or user requests this specialist analysis.
model: inherit
tools: Read, Glob, Grep, Bash
disallowedTools: Write, Edit
section: 12
skills:
  - meta-ads-mcp
  - statistical-confidence
---
```

- `description` is what routing keys on. Say what the agent **determines**, not what topic it is
  about.
- `tools` — the narrowest set that works. Audit agents are read-only: `Read, Glob, Grep, Bash`,
  with `disallowedTools: Write, Edit`. Never grant `Write`/`Edit` to an agent that inspects a
  live account.
- `section` — which of the 30 this agent reports into.
- `skills` — only skills the agent actually loads. Every entry must resolve to a
  `.claude/skills/` directory; `scripts/validate-references.py` enforces it. An audit agent may
  not declare an execution skill.

### 3. Write the body

Read `59-creative-database-builder-agent.md` for a dataset producer and
`01-full-account-audit-agent.md` for the orchestrator. Sections that must be present:

- **Mission** — the decision this agent exists to inform. One sentence, and it names a decision,
  not a topic.
- **Inputs** — named fields from named sources, with the date range they need.
- **Minimum data safeguards** — what makes the analysis invalid. State the sample floor and say
  what to return when it is not met. An agent with no floor will produce confident nonsense on
  thin data, and on Meta that happens constantly because ad-level purchase counts are small.
- **Method** — the formula in full. Reuse the canonical definitions rather than recomputing:
  contribution margin and break-even ROAS from section 1, significance from
  `learning-phase-and-significance`, creative fields from `creative-record.yaml`. An agent that
  recomputes margin from its own assumptions will disagree with the executive page.
- **Output** — against `schemas/agent-contract.yaml`, including `measurement_basis` and the
  `coverage_state` it contributes.
- **Dependencies** — which agents must run first, and what this one does if they were blocked.
  "Fails" is not an answer; degrade and say so.

### 4. Honour the output contract

`schemas/agent-contract.yaml` requires `agent_id`, `agent_name`, `section`, `status`,
`coverage_state`, `period`, `scope`, `data_sources`, `data_quality`, `measurement_basis`,
`key_findings`, `recommendations`, `confidence`, `limitations`, `dependencies`.

Findings follow `schemas/finding-schema.yaml`. The classification field is the point, not
paperwork:

- A modelled or inferred number must never be emitted as `OBSERVED`.
- Meta's own assertions about Meta — opportunity score, relevance rankings, EMQ, vendor lift
  estimates — are `PLATFORM_STATED`. Reportable, never proof.
- If impact cannot be defensibly quantified, the finding is a `FLAG` with **no** currency value.
  Never invent one to fill the field.

`measurement_basis` is not optional. An agent that omits it is asserting its figures are
observed, and on Meta that is usually false.

### 5. Register it

Add a row to `AGENT-INDEX.md` (number, name, band, section, dependencies, declared skills) and
update the band table if the agent opens a new band. Bump `agent_count` in
`agent-manifest.json` and `orchestration/manifest.json`. Map the agent to its section in
`.claude/skills/full-audit/SKILL.md` and add it to `workflows/02-full-account-audit.md`, plus
any other named sequence it belongs to. Update the counts in `README.md` — they appear in prose,
in the structure tree, and `scripts/validate-docs.py` checks all
of them against disk.

---

## Adding an execution agent

Same shape, plus:

```yaml
---
name: 214-example-executor
description: Applies <specific approved change type> to a live Meta ad account under EXECUTION-PROTOCOL.md.
model: inherit
tools: Read, Write, Glob, Grep, Bash
lane: execution
section: 0
skills:
  - meta-execution-protocol
---
```

- `lane: execution` is mandatory and is what `validate-execution-boundary.py` keys on.
- The body must restate the seven rules it is bound by, or load `meta-execution-protocol` and
  say it does. An execution agent that does not mention approval, preview, create-paused,
  logging and rollback is not finished.
- It must name **which write tools it calls**, and they must all be classified `write` in
  `schemas/meta-mcp-tool-classification.yaml`. A write tool that is not in that file yet gets
  added there first.
- It writes to `changes/<run-id>/`, never to `audits/`.

An execution agent may never be invoked by the audit orchestrator. If you find yourself wanting
that, the thing you actually want is a recommendation.

---

## Adding a skill

```
.claude/skills/<name>/
  SKILL.md          required
  references/       optional — depth loaded on demand
  assets/           optional — templates, HTML, images
  scripts/          optional
  evals/evals.json  optional — trigger tests
```

Constraints (enforced by `scripts/validate-skills.sh`):

- `name`: 1–64 chars, lowercase letters, numbers and hyphens, **identical to the directory
  name**. A mismatch makes the skill silently fail to load — invisible by inspection, which is
  why it is validated.
- `description`: 1–1024 chars.
- `SKILL.md`: under 500 lines. Past that, move depth into `references/` and route to it from a
  table.

```yaml
---
name: example-skill
description: When the user wants to <task>. Also use when the user mentions "<phrase>," "<phrase>," or "<phrase>." For <adjacent task>, see <other-skill>.
---
```

Write descriptions for retrieval, not for reading. Name the trigger phrases someone would
actually type. Cross-reference sibling skills so routing between them is explicit — and only
name skills that exist; `validate-references.py` fails the build on a pointer to a removed
skill.

### Which layer does a new skill belong to?

- **Audit skill** — establishes what is true, cites sources, grades evidence, consumed by
  agents. `cross-source-reconciliation`, `modeled-conversions`, `creative-data-model`.
- **Marketing skill** — proposes what to build. Prescriptive, advisory. `meta-creative-strategy`,
  `cro`, `offers`.
- **Execution skill** — governs or performs mutations. `meta-execution-protocol`,
  `meta-campaign-build`.

Precedence, per `CLAUDE.md`: audit skills establish facts; marketing skills propose actions;
execution skills apply approved ones. **A marketing skill's benchmark is never evidence for a
quantified finding.** If a new skill would be cited as proof of a number, it belongs in the
audit layer and needs source and confidence discipline.

A new audit skill is added to `SKILL-INDEX.md`, to `audit_skills` in both
`agent-manifest.json` and `orchestration/manifest.json`, and to the counts in `README.md` and
`CLAUDE.md`.

---

## Validation

Run all of these before committing. They are cheap and they catch the failures that are
invisible by inspection:

```bash
python3 scripts/validate-references.py          # skill names, links, agent→skill resolution
bash    scripts/validate-agent-library.sh       # frontmatter, name↔filename, uniqueness, sections
bash    scripts/validate-skills.sh              # spec compliance, line limits, description quality
python3 scripts/validate-docs.py                # README tree + counts vs disk
python3 scripts/validate-section-map.py         # the section map vs the agents' frontmatter
python3 scripts/validate-execution-boundary.py  # no audit agent references a write tool
python3 scripts/validate-doc-freshness.py       # README still describes the system, not just counts it
python3 scripts/audit-cli-writes.py --check     # tools/clis mutation surface still documented
```

Then run `00-agent-quality-controller` for a judgement pass on rubric, calculation rigour and
dependency clarity. It reads without mutating.

## House rules that override style preference

From `CLAUDE.md`, and not negotiable in new work:

1. Audit agents are read-only. Every mutation goes through `EXECUTION-PROTOCOL.md`.
2. Discover tools before use. Never invent a tool name, schema, account id or pixel id.
3. Every material finding carries a number, source, date range, formula, evidence class,
   confidence and next action. Otherwise it is a `FLAG`, not a `FIX`.
4. Modelled, estimated or inferred values are never presented as observed. Meta's claims about
   Meta are `PLATFORM_STATED`.
5. Never average a ratio across entities. Recompute from component sums.
6. Volume gates conclusions. Under the purchase floor, the answer is `INSUFFICIENT_DATA`.
7. Measurement precedes economics; economics precedes scaling.
8. One material change at a time, with a 14-day read window.
