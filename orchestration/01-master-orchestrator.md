# Master orchestrator

The execution model behind `.claude/agents/01-full-account-audit-agent.md`. That agent is the
entry point; this describes how a run is driven, so an interrupted or partial run behaves
predictably.

## Run lifecycle

```
initialized → preflight → discovering → acquiring → reconciling → analyzing → synthesizing
                                                                        ↓
                                                        completed | partial | failed
```

State lives in `orchestration/runs/<run-id>/run-state.json` against
`schemas/run-state.schema.json`. It carries the lane (`audit` or `execution`), the per-section
coverage map, and the gate verdicts — so a resumed or inspected run does not depend on anything
being remembered.

## Section scheduling

The 30 sections form a dependency graph, not a queue.

**Hard ordering:**

- §1 before anything economic
- §2 before any attribution claim
- §3 before any economic conclusion
- §7 before §§8–11, and before the creative parts of §19, §22 and §30
- §30 last

Everything else may run in parallel. A section whose dependencies are `BLOCKED` still runs — on
what it can see — and closes `DEGRADED` with the missing input named.

## Gate semantics

Gates **order** the sweep. They never halt it.

| Gate | Verdict | Effect |
|---|---|---|
| §2 measurement | `RED` | Confidence lowered on every economic claim; scale and kill recommendations that depend on conversion value are withheld. **Every section still runs** |
| §3 reconciliation | `UNRESOLVED GAP` | The gap qualifier travels with every dependent figure, including onto the executive page |
| §1 economics | margin `ASSUMED` | Dependent figures published as a range across the plausible band, with a statement of whether the recommendation changes across it |

A gate that halts the run delivers nothing, and most of a Meta audit's findings never needed
conversion value in the first place.

## Agent invocation

- Invoke only agents whose required inputs exist. Record a skipped agent as `skipped`, with its
  reason, in `agent-results/`.
- **A skipped agent does not skip its section.** The section still closes with a state that
  explains why.
- Validate each agent's return against `schemas/agent-contract.yaml`. A result missing
  `measurement_basis` is `invalid_output`, not a result — it is asserting its numbers are
  observed, and on Meta that is usually false.
- Where two agents disagree, reconcile the underlying data before publishing either
  (`conflict-resolution`).

## The creative dataset is a barrier

§7 is the only place creative performance is fetched. Agents 60–78, and the creative parts of
§§19, 22 and 30, wait for `creative-database.csv` and read it.

This is deliberate scheduling, not caching convenience: two components fetching their own
creative data with slightly different windows produce a dashboard and a findings list that
disagree, and that failure is invisible until someone adds up two tables.

## Rate limits

Meta limits per account and per app, and the budget is shared. The orchestrator batches, pulls
the smallest sufficient field set, and caches to `raw/` (`data-cache`).

Under pressure, late sections close `DEGRADED` with what was not fetched named. The run does not
fail.

## Interruption

`coverage.md` is opened at the start with all 30 sections `PENDING` and updated as each closes.
An interrupted run therefore still shows exactly what it reached, and `run-state.json` carries
enough to resume.

Never write the ledger at the end from memory.

## The boundary

The orchestrator is an **audit** driver. It cannot invoke an execution agent, and no path
through it reaches a write tool. Where a finding warrants a change, the output is a
recommendation and an offer to run `workflows/08-execution-run` — a separate invocation the user
starts.
