# Data registry

Which dataset is produced by whom, read by whom, and under what key. The orchestrator uses this
to schedule; agents use it to find data rather than re-fetching it.

The rule underneath: **a dataset has one producer.** Two producers means two versions, and two
versions means two sections of the same report disagreeing with no way to tell which is right.

## Datasets

| Dataset | Path | Producer | Consumers | Schema |
|---|---|---|---|---|
| Ad / ad set / campaign entities and insights | `raw/entities/` | §5 | Nearly everything | — |
| **Creative database** | `creative-database.csv` | **59** | 60–78, 119–128, 134–135, 156–162, dashboard | `creative-record.yaml` |
| Creative content | `raw/creatives/` | §7 | §9, §20 | — |
| Activity log | `raw/activity-log/` | §5 | §6, §8, §9, §25 | — · **may be UNAVAILABLE** — `ads_account_get_activity_logs` is rolled out per account. Consumers degrade (confidence capped at `MEDIUM`, no decay-only kills) rather than skip |
| Dataset quality / pixel state | `raw/datasets/` | §2 | §3, §25 | — |
| Commerce orders and line items | `raw/commerce/` | §1 | §3, §22, §24 | — |
| GA4 funnel and pages | `raw/ga4/` | §19 | §3, §20 | — |
| Catalog diagnostics | `raw/catalog/` | §16 | §17 | — |
| Ad Library results | `raw/ad-library/` | §27 | §9 | — |
| Landing page genomes | `normalized/lp-genomes.json` | §20 | §7 dashboard, §19 | — |
| Reconciliations | `reconciliations/` | §3 | §25, §26, §30 | `reconciliation-schema.yaml` |
| Findings | `findings/` | every section | §30 | `finding-schema.yaml` |
| Agent results | `agent-results/` | every agent | orchestrator | `agent-contract.yaml` |
| Opportunity matrix | `opportunity-matrix.md` | 157 | 159, 162 | `opportunity-schema.yaml` |
| **Scale matrix** | `scale-matrix.md` | 158 | 159, 162 | `scale-matrix.yaml` |

## Cache keys

A cached result is reusable only if it was pulled on the same terms:

```
source · entity level · date range · attribution window · breakdown dimension · field set
```

A hit on a different attribution window is **not** a hit. Returning it is worse than re-querying,
because the mismatch is invisible downstream.

## Canonical values

Computed once in §1, consumed everywhere. An agent that recomputes one of these will disagree
with the executive page:

`gross_margin_pct` · `contribution_margin_pct` · `contribution_per_order` ·
`break_even_roas` · `cac_ceiling` · `new_customer_cac` · `payback_period`

Each carries its basis — `DERIVED`, `USER_SUPPLIED` or `ASSUMED` — so a consumer can tell a
measurement from an assumption.

## Never across runs

Each run pulls fresh. The one legitimate cross-run read is prior-run output for comparison — a
previous scorecard or coverage ledger — read as history, explicitly dated, never as current
state.
