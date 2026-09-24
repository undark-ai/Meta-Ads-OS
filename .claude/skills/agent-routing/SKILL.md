---
name: agent-routing
description: When deciding which specialist agent or workflow answers a request — mapping a question to the section that owns it, choosing between a full audit and a narrower sequence, and knowing when a request belongs to the execution lane instead. Use when a user request does not obviously map to one agent, or when the orchestrator needs to sequence specialists.
---
# Agent routing

## Full audit, or a narrower sequence?

| The user says | Run |
|---|---|
| "Audit my account", "what's wrong", "review this account" | `02-full-account-audit` — all 30 sections |
| "Why is CPA up", "what changed", "performance dropped" | `04-weekly-operating-cycle`, then the section the diagnosis lands in |
| "Which creative is working", "creative analysis", "top creatives" | `03-creative-deep-dive` — §7–§11 plus §27 |
| "Where should I put more budget", "what should I scale" | `06-scale-decision` — §29 plus the scale matrix |
| "Is my tracking OK", "does Meta match Shopify" | §2 and §3 alone |
| "Build me a campaign", "change the budget", "pause these" | **The execution lane** — `08-execution-run`, not an audit |

A narrower sequence still preflights and still records coverage — for the sections it ran.

## Route a symptom to the section that owns it

Most requests arrive as symptoms, and the obvious section is frequently the wrong one:

| Symptom | Looks like | Usually is |
|---|---|---|
| "CPA is rising" | Creative fatigue (§8) | Could be §6 learning phase, §11 CPM, §15 saturation, §2 measurement, or seasonality (§5). Diagnose before routing |
| "Clicks but no sales" | Creative (§9) | §19/§20 post-click, or §2 if the purchase event is broken |
| "ROAS dropped" | Anything | §3 first — check the number is real before explaining it |
| "This ad stopped working" | §8 | §6 if the ad set re-entered learning; §15 if the whole set decayed |
| "CPMs are too high" | Auction pressure | §11 decomposition — relevance, mix shift, saturation and seasonality are separable |
| "Retargeting has amazing ROAS" | Good news | §26 — the least incremental spend reports the best numbers |
| "Which audience should I use" | §12 | §9 — on Meta, creative is closer to targeting than targeting is |

## Sequence, do not blend

One agent, one job. Where a request spans two, run them in order and say so, rather than
producing one unstructured answer that does neither well.

Common chains:

- **Performance dropped** → §3 (is the number real) → §6 (learning phase) → §8 (fatigue) → §15
 (saturation) → §11 (delivery)
- **New creative from scratch** → §9 (what wins today) → §27 (category gaps) → creative brief
- **A winner appeared** → §7 (confirm it is winning and on what) → §26 (is it incremental) →
 scale matrix (how much headroom)
- **Rising CAC** → §3 → §24 (new vs returning) → §13 (prospecting economics) → §29 (allocation)

## The gates route too

Before any scale or kill recommendation, regardless of which section produced it:

1. §2 verdict — is it `RED`?
2. §3 — is the number reconciled?
3. `learning-phase-and-significance` — is it above the floor?
4. §26 — does a retargeting claim have incrementality evidence?

An agent that skips these produces a recommendation the system will not stand behind.

## Never route to the execution lane from an audit

A request that means "change the account" is a different invocation, with its own approval. An
audit that discovers a fix writes a recommendation; it does not apply it. If a user asks
mid-audit for something to be changed, finish the audit and offer the execution run.
