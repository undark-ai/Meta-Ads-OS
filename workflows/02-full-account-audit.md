# Full account audit

One top-to-bottom sweep of all 30 sections. Section definitions and their agent mapping live in
`.claude/skills/full-audit/SKILL.md`; the orchestrator is
`.claude/agents/01-full-account-audit-agent.md`.

## Sequence

| Step | § | Section | Agents |
|---:|---:|---|---|
| 0 | — | Preflight, run directory, source discovery through the full ladder, scope | 02 |
| 1 | 1 | Business & economics — **gate** | 7–16, 20 |
| 2 | 2 | Tracking & measurement — **gate** | 21–36 |
| 3 | 3 | Reconciliation: Meta claim vs commerce platform and GA4 — **mandatory** | 37–42 |
| 4 | 4 | Account structure | 43–46, 50 |
| 5 | 5 | Campaign performance & trend windows | 3, 4, 51–54, 148–150 |
| 6 | 6 | Bidding, delivery & learning phase | 55–58 |
| 7 | 7 | Creative inventory & database → **Top Creatives dashboard** | 59–64 |
| 8 | 8 | Creative fatigue | 65–70 |
| 9 | 9 | Creative angle & hook analysis | 71–75 |
| 10 | 10 | Creative testing system | 76–78 |
| 11 | 11 | Relevance & auction diagnostics | 79–82 |
| 12 | 12 | Audience strategy | 83–89, 92 |
| 13 | 13 | Prospecting | 93–96 |
| 14 | 14 | Retargeting | 97, 98 |
| 15 | 15 | Frequency & saturation | 90, 91, 100 |
| 16 | 16 | Product catalog | 101–108 |
| 17 | 17 | Advantage+ Shopping & Advantage+ Creative | 109–114 |
| 18 | 18 | Placement analysis | 115–118 |
| 19 | 19 | Funnel audit | 119, 124, 126 |
| 20 | 20 | Landing pages & post-click CRO | 120–123, 125, 127, 128 |
| 21 | 21 | Offer audit | 129–133 |
| 22 | 22 | Product & SKU economics | 17–19 |
| 23 | 23 | Geographic & device economics | 134–137 |
| 24 | 24 | New vs returning & the LTV loop | 99, 138 |
| 25 | 25 | Attribution | 139–141 |
| 26 | 26 | Incrementality | 142–144 |
| 27 | 27 | Competitive & Ad Library | 145–147 |
| 28 | 28 | Hygiene, Business Manager & permissions | 47–49, 151, 152 |
| 29 | 29 | Budget allocation & the next dollar | 153–155 |
| 30 | 30 | Final output | 5, 6, 156–162 |

**§1 precedes everything economic. §2 precedes every attribution claim. §3 precedes any economic
conclusion. §30 runs last.** Sections with no dependency between them may run in parallel.

## Rules

- **Gates order the sweep; they never stop it.** A `RED` measurement verdict or a missing margin
  input lowers confidence on the affected findings and is reported prominently — the remaining
  sections still run.
- **Every section closes with a state** — `FINDINGS`, `CLEAN`, `DEGRADED`, `N/A` or `BLOCKED` —
  written to `audits/<run-id>/coverage.md`. An unrun section is a defect, not an omission.
- **§7 writes the creative database once.** §§8–11, 19, 22 and 30 read it. Nothing re-queries
  Meta for creative performance, including the dashboard.
- The orchestrator skips agents whose inputs do not exist, but the **section** still closes with
  a state explaining why.
- **This workflow never mutates the account.** Changes go through `08-execution-run`.

## Deliverables

`preflight.md` · `coverage.md` · `creative-database.csv` · `top-creatives.html` ·
`top-creatives-chrome.html` · `reconciliation.md` · `scorecard.md` · `opportunity-matrix.md` ·
`scale-matrix.md` · `action-plan.md` · `quantified-upside.md` · `executive-summary.md` ·
evidence appendix.
