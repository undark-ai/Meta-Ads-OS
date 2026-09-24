---
name: paid-measurement-readiness
description: "When the user wants to know whether their paid media can actually be measured before they spend more on it — a scored readiness check across dashboards, conversion tracking, web analytics and attribution, with a spend gate, plus the blended dashboard build and the baseline snapshot to take before scaling. Also use when the user mentions 'can we even measure this,' 'should we pause until tracking is fixed,' 'blended dashboard,' 'measurement audit,' 'we don't trust our numbers,' 'set a baseline before scaling,' 'MER dashboard,' or 'how do I report on paid across channels.' For event tracking implementation and GA4 setup, see analytics. For Meta-specific attribution and incrementality, see meta-attribution. For the Meta performance report itself, see meta-reporting."
metadata:
 version: 1.0.1
---

> **Marketing layer — advisory, not evidence.** Every benchmark, threshold and rule of thumb
> below is build-time guidance. Per `CLAUDE.md`, a marketing skill's number is never evidence
> for a quantified finding: a recommendation that originates here still needs a number, source,
> date range, formula, evidence class and confidence from the audit layer before it can be
> presented as one. Handoffs run audit → marketing, never the reverse.


# Paid Measurement Readiness

Most paid media problems presented as optimization problems are measurement problems. If you can't see new-customer CAC, you can't optimize for it, and no amount of creative testing rescues an account whose numbers nobody trusts. This skill scores whether an account is measurable, tells you whether to keep spending while you fix it, and specifies the blended dashboard that makes the rest of this library usable.

Cross-channel by design. Meta is usually the largest line, but the readiness question spans every paid channel plus the store.

## Before Starting

**Check for product marketing context first:**
If `.agents/product-marketing.md` exists (or `.claude/product-marketing.md`, or the legacy `product-marketing-context.md` filename, in older setups), read it before asking questions. Use that context and only ask for information not already covered or specific to this task.

Gather this context (ask if not provided):

- **Channels running and monthly spend per channel.**
- **Store platform and whether order-level export is available** — the dashboard below is built from it.
- **AOV, contribution margin per order, and any LTV data.** These are what the dashboard exists to expose.
- **What reporting exists today**, and who reads it.

## The Readiness Scorecard

Score each question 1–3. Be strict: score what exists and is used, not what is technically possible.

| # | Question | 1 | 2 | 3 |
|---|---|---|---|---|
| 1 | **Blended dashboard** — one view of total spend against total revenue | Nothing; numbers assembled ad hoc when asked | A spreadsheet updated manually and often stale | Automated, current, and the number people actually quote |
| 2 | **Per-channel dashboards** — spend and results by channel | Platform UIs only, read separately | Some channels consolidated, others not | Every paid channel in one comparable view |
| 3 | **Conversion tracking** | No pixel, or pixel not firing reliably | Pixel only | Pixel **plus** CAPI with server-side orders, and event match quality 6+ |
| 4 | **Web analytics** | Not installed or never opened | Installed, default config, no goals | Configured with the funnel events that matter, and reconciled against store orders |
| 5 | **Attribution, documented and agreed** | Nobody has decided; each person quotes a different number | A window is set but not written down or agreed | Documented view of platform ROAS vs MER vs survey data, including which one wins a disagreement |
| 6 | **Post-purchase survey** — "how did you hear about us?" and "is this your first purchase?" | Not running | Running, results never read | Running, read weekly, and used to correct platform attribution |

**Bands** (out of 18):

- **Under 7 — below average.** You are spending without visibility. Consider pausing or capping spend until at least question 3 reaches a 3. Scaling an account you can't measure multiplies a loss you can't see.
- **7–14 — average.** Spend, but fix the lowest score before increasing budget. Most accounts live here.
- **15–18 — above average.** Measurement is not your constraint. Go optimize.

**Always fix the lowest score first**, not the easiest one. A perfect dashboard fed by broken conversion tracking is a confidently wrong dashboard.

## The Blended Dashboard

One sheet or one warehouse view. Two inputs, one output.

**Input 1 — spend by channel by day.** One tab per channel or one long table: date, channel, spend. Pull it automatically; a manually-updated spend tab is a dashboard that goes stale in three weeks. See `tools/REGISTRY.md` for connectors that can feed this.

**Input 2 — orders.** An order-level export from the store, one row per order: order date, channel (from the post-purchase survey where you have it), new-vs-returning flag, order value, discount code, refund flag. The new-vs-returning flag is the single most valuable column and the one most often missing.

**Outputs** — aggregate both inputs to the same date grain and compute:

| Metric | Definition | Why it's here |
|---|---|---|
| Spend | Total paid spend | Denominator for everything |
| Orders | Total orders | Volume |
| New customers | Orders where the new-customer flag is true | The only growth number |
| CAC | Spend ÷ total customers | Blended cost |
| **New-customer CAC** | Prospecting spend ÷ new customers | The real cost of growth; the number most accounts have never seen |
| AOV | Revenue ÷ orders | Feeds break-even ROAS |
| **MER** | Total store revenue ÷ total ad spend | Account-level truth, immune to attribution games |
| Repeat rate (60/90-day) | Share of new customers placing a second order within the window | Whether acquisition is worth its price |
| Contribution profit | Revenue × margin − spend | Whether any of this made money |

Join spend and orders on channel and date. Refunds must be netted out or the whole model overstates. Keep the date range dynamic so nobody is reading a hardcoded month.

Build it wherever the team already works. A spreadsheet that gets read beats a warehouse view that doesn't.

## Take a Baseline Before You Change Anything

Before launching a new channel, restructuring an account, or starting a scaling push, snapshot the current state: AOV, new-customer CAC, 60/90-day repeat rate, MER, and contribution margin, over a trailing period long enough to be stable. Then set targets as **deltas** from that baseline over a stated horizon — for example, hold new-customer CAC flat while increasing new customers 30% over 90 days.

Without the snapshot you cannot tell later whether the change worked, and the whole team will argue about it from memory. This is the cheapest step in this skill and the most commonly skipped.

## Measurement Maturity

Readiness is a level, not a switch. Don't attempt level 3 work at level 1.

| Level | Timeline | What you can measure | What to build next |
|---|---|---|---|
| **1 — Basic** | Month 1–2 | Platform-reported spend and conversions | Pixel + CAPI, one blended spend-vs-revenue view |
| **2 — Intermediate** | Month 3–6 | MER, blended CAC, per-channel comparison | New-vs-returning split, post-purchase survey, order-level export |
| **3 — Advanced** | Month 6–12 | New-customer CAC, cohort repeat rate, contribution profit by channel | Payback-period tracking, LTV cohorts |
| **4 — Optimized** | Year 2+ | Incremental contribution | Holdout and geo-lift testing — see meta-attribution |

**Incrementality testing lives at level 4.** A lift test run on top of broken deduplication measures your instrumentation, not your marketing.

## Reporting Cadence

| Report | Audience | Cadence | Contents |
|---|---|---|---|
| Creative and ad dashboard | Whoever runs the account | Daily to weekly | Spend, CPA, ROAS, hook rate, frequency by ad |
| Channel performance | Marketing lead | Weekly | Spend, orders, CAC, MER, new-customer share by channel |
| Cohort and repeat report | Marketing lead | Monthly | Repeat rate and AOV by acquisition cohort and channel |
| Contribution and payback | Founder or CFO | Quarterly | Contribution profit, payback period, LTV:CAC |

Match the cadence to how fast the metric can actually move. A daily contribution-profit report invites decisions on noise.

## Reading the Trend

| Trend | Likely meaning | Action |
|---|---|---|
| Platform ROAS up, MER flat | Attribution shift, not growth | Split prospecting from retargeting; see meta-attribution |
| MER up, new-customer CAC up | Growth bought at a rising price | Check LTV and payback before accepting it |
| New-customer share falling | Acquisition being crowded out by retargeting or retention spend | Rebalance budget toward prospecting |
| Repeat rate falling on newer cohorts | Acquiring worse customers, usually via discount | Review offers and audience seeds |
| Contribution profit falling while revenue rises | Scaling past profitability | Stop scaling, fix unit economics |

## Common Mistakes

- Optimizing an account nobody can measure, then blaming the creative.
- Fixing the easiest score instead of the lowest one.
- A beautiful dashboard fed by an unreliable pixel.
- No new-vs-returning flag, so every CAC figure is blended and useless for growth decisions.
- Not netting refunds.
- Skipping the baseline snapshot, then arguing about whether a change worked.
- Running incrementality tests at maturity level 1.

## Related Skills

- **analytics**: Tracking plan, event naming, GA4 and GTM implementation, UTM strategy — the mechanics behind questions 3 and 4.
- **meta-attribution**: Attribution windows, why Meta and the store never match, and the holdout and geo-lift designs that live at maturity level 4.
- **meta-capi-and-events**: Getting question 3 to a 3 — Pixel plus CAPI, event match quality, deduplication.
- **meta-reporting**: The Meta-specific performance report and dashboard once the underlying measurement is sound.
- **google-ads-measurement**: The Google-side equivalent of questions 3–5 at account level — conversion-action integrity, purchase purity, and platform-vs-store-vs-cash reconciliation.
- **google-ads-economics**: Contribution margin, break-even ROAS and CAC ceilings for the Google line once it is measurable.
- **ads**: Cross-channel paid strategy and channel selection, including the reference playbooks for B2B and D2C.
- **ab-testing**: Experiment design and reading results, for the tests maturity level 4 unlocks.
