# Running an audit

The short version, for someone who wants to start one.

## Start it

```
/full-audit
```

or ask: *"Run the full Meta Ads audit on my account."*

`audit-preflight` runs first and asks two questions before any data is pulled. Answer them, or
say "proceed as-is" — that is always valid and is recorded.

## What happens

1. **Preflight** — business context, connectors, and confirmation of which account is live and
   whether it has spend in the window.
2. **Discovery** — the connector ladder, and the real tool names (they differ per account).
3. **Scope** — currency, account timezone, window, and one attribution setting for the whole run.
4. **The 30 sections**, in one pass. §1 economics and §2 measurement are gates; §3 reconciles
   Meta's claim against banked orders before any economic conclusion. §7 builds the creative
   database and the Top Creatives dashboard; §§8–11 read it.
5. **§30** — scorecard, opportunity matrix, scale matrix, 30/60/90 plan, executive page.

## What you get

Everything lands in `audits/<run-id>/`, one directory per run, never overwritten:

```
coverage.md            all 30 sections, each with its state
creative-database.csv  one row per ad
top-creatives.html     the dashboard
reconciliation.md      Meta's claim vs what the store banked
scorecard.md           per-category, against published weights
opportunity-matrix.md  what is broken, ranked in contribution
scale-matrix.md        where the next dollar goes
action-plan.md         30/60/90
executive-summary.md   the decision page
```

## Narrower runs

| You want | Run |
|---|---|
| A quick verdict on an unfamiliar account | `workflows/01-foundational-audit` |
| The creative learning system only | `workflows/03-creative-deep-dive` |
| The weekly read | `workflows/04-weekly-operating-cycle` |
| Where the next dollar goes | `workflows/06-scale-decision` |
| To apply changes | `workflows/08-execution-run` — a separate, deliberate invocation |

## Two things worth knowing before you read the output

**A `RED` measurement verdict does not mean the audit failed.** It means scale and kill
recommendations that depend on conversion value are withheld, and everything else still ran.
Most of a Meta audit never needed conversion value.

**Some recommendations lower reported ROAS while improving the business** — excluding existing
customers from prospecting, fixing a purchase event that was double-counting. The report flags
these. Applying them and then reverting when the dashboard drops is the most common way an audit
gets undone.
