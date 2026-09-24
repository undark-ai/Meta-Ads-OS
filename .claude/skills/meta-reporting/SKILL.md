---
name: meta-reporting
description: "When the user wants Meta Ads performance analysis or reporting for an e-commerce or D2C store — pull live insights, read them like an operator (ROAS vs break-even, new-customer CAC, MER vs vanity signals), and produce a branded dashboard or a written performance report a client or founder can act on. Also use when the user mentions 'weekly ad report,' 'Meta dashboard,' 'how are my ads doing,' 'ROAS report,' 'client-ready report,' 'performance recap,' or 'ad account rollup.' The deliverable here is the report or dashboard itself; for evidence-graded live-account analysis, see full-audit. For fixing what the report surfaces, see meta-optimization-playbook. For why Meta's numbers don't match Shopify or GA4, attribution windows, and incrementality testing, see meta-attribution."
metadata:
 version: 1.1.0
---

> **Marketing layer — advisory, not evidence.** Every benchmark, threshold and rule of thumb
> below is build-time guidance. Per `CLAUDE.md`, a marketing skill's number is never evidence
> for a quantified finding: a recommendation that originates here still needs a number, source,
> date range, formula, evidence class and confidence from the audit layer before it can be
> presented as one. Handoffs run audit → marketing, never the reverse.


# Meta Ads Reporting and Dashboards — D2C E-commerce

Turn raw Meta numbers into a decision. This skill pulls live performance, analyzes it like an operator, and renders a clean, client-ready output.

## Before Starting

**Check for product marketing context first:**
If `.agents/product-marketing.md` exists (or `.claude/product-marketing.md`, or the legacy `product-marketing-context.md` filename, in older setups), read it before asking questions. Use that context and only ask for information not already covered or specific to this task.

Gather this context (ask if not provided):

- AOV and contribution margin per order — needed to compute break-even ROAS, the anchor for every judgment in the report.
- The reporting window and audience for the output (internal weekly review vs client/founder deliverable), plus the store's name/logo if branding a dashboard.

## Requires the Meta Ads MCP

Live-account work in this skill calls the Meta Ads MCP (tools like `ads_get_ad_accounts` to resolve the account, `ads_get_ad_entities` for campaign and ad structure, `ads_get_ad_entities` for spend, purchases, revenue, ROAS, CPA, CTR, CPM, and frequency over the reporting window, `ads_insights_performance_trend` for period-over-period movement, and `ads_insights_anomaly_signal` to surface unexpected swings). If the MCP isn't connected, say so and stop rather than fabricating account data or performance numbers — the metric definitions and report structure below still work with data the user supplies.

## What this covers

1. **Performance analysis** - pull live spend, purchases, revenue, ROAS, CPA, CTR, CPM, frequency at account and campaign level, then read it like an operator (leading vs vanity signals).
2. **Reporting** - weekly or period-over-period rollups: what changed, what is working, what to fix first.
3. **Dashboards** - a self-contained HTML dashboard you can open in a browser or send to a client/founder: KPI tiles (spend, purchases, revenue, ROAS, CPA, AOV, CTR, CPM) plus a per-campaign table sorted by spend. Brand it with the store's logo and name.

Pull data at both account and campaign level for the same window (last 7 days and last 30 days are the standard cuts), extracting purchases and purchase revenue as the outcome metrics and treating impressions, reach, and CPM as context.

## The D2C metric stack

- **ROAS** = attributed revenue ÷ spend (in-platform, inflated by retargeting - read prospecting and retargeting separately).
- **Break-even ROAS** = AOV ÷ contribution margin per order. A 2.0 ROAS is great for a 60%-margin brand and a loss for a 30%-margin brand. Never judge ROAS without knowing break-even.
- **CPA / new-customer CAC** - cost per purchase, ideally split new vs returning. CAC is judged against first-order margin and LTV, not in a vacuum.
- **MER (blended)** = total revenue ÷ total ad spend, from the store's own numbers. The check on in-platform attribution: if Meta ROAS rises but MER falls, Meta is taking credit for sales it didn't drive.
- **AOV** - watch it alongside CPA; a discount-heavy funnel can hold CPA flat while eroding margin.

## How to analyze (not just report)

Reporting is describing the numbers. Analysis is deciding what to do. Always:

1. **Lead with the outcome metric, not vanity.** Purchases, ROAS vs break-even, and new-customer CAC first. Impressions, reach, and CPM are context, never the headline.
2. **Separate leading from lagging signals.** CTR and CPM move first; CPA and ROAS confirm. A rising CPM with stable ROAS is fine; ROAS sliding below break-even is the alarm. Thumbstop/hook rate on video is the earliest creative signal.
3. **Read at the right altitude.** Account → campaign → ad set → ad. Find the level where the money is leaking before recommending a fix. Split prospecting vs retargeting before averaging anything - a blended 3.5 ROAS hiding a 0.9 prospecting ROAS is a scaling trap.
4. **Tie every number to an action.** "CPA up 40% week over week, driven by the prospecting campaign fatiguing (frequency 4.2, CTR down 35%). Action: rotate in the next creative batch, refresh the hook." Not "CPA went up."
5. **Cross-check with blended numbers.** Reconcile Meta-reported purchases against the store's orders and MER for the same period. Report both; flag the gap.
6. **Never fabricate a benchmark.** If you don't have the account's own history, say so. Category benchmarks are reference ranges, labeled as such - the account's own break-even ROAS and trailing 30-day baseline beat any industry table.

## Report structure

- **Wins first**, then concerns, with week-over-week numbers at the campaign level.
- Headline block: spend, purchases, revenue, ROAS (vs break-even), CPA, MER.
- Then: what changed and why (creative fatigue, CPM inflation, promo effects, tracking gaps), and the top 3 actions in priority order.
- Seasonality note where relevant (promos, holidays, stock-outs) so period comparisons are honest.

## Output standards

- Dashboards are client-ready: clean, branded, no jargon, no source citations.
- Written reports are decision documents, not data dumps: every section ends in an action or an explicit "no action needed."
- Plain language. No AI slop, no emoji.

## Related Skills

- **full-audit**: The evidence-graded audit lane — 30 sections against live account data, where these benchmarks get tested rather than assumed.
- **meta-optimization-playbook**: The decision trees and kill/optimize/scale rules for acting on what the report surfaces.
- **meta-ads-operating-system**: The standing decision framework the Monday review feeds — Target CPA, graduation, scaling thresholds.
- **meta-ads**: The e-commerce Meta hub — audience strategy, campaign structure, and creative testing across the full suite.
- **analytics**: Cross-channel measurement and attribution beyond the Meta account.
