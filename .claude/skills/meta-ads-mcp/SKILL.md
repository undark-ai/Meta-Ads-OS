---
name: meta-ads-mcp
description: When querying the Meta Ads connector for audit data — which call answers which question, the entity levels and fields, breakdown rules, and the read/write boundary. Use whenever an agent needs live account data from Meta. Covers the read tools only; the write tools are classified in schemas/meta-mcp-tool-classification.yaml and may be called solely by the execution lane under EXECUTION-PROTOCOL.md.
---
# Meta Ads connector

## The boundary, first

Audit agents call **read** tools only. Every Meta tool is classified in
`schemas/meta-mcp-tool-classification.yaml`, and **anything unclassified is treated as a write**.
Fail closed.

Write tools exist and work. They are the execution lane's, under `EXECUTION-PROTOCOL.md`, and
they are never called during an audit — not even when a request appears to ask for it.

## Tool names are per-account

The connector's server id differs per account: `mcp__<SERVER_ID>__ads_get_ad_entities`. Discover
it at runtime (`mcp-discovery`), never hardcode one from another account or another session.

## Which call answers which question

| Question | Call |
|---|---|
| Which accounts, and are they queryable? | `ads_get_ad_accounts` — check `is_ads_mcp_enabled`, not just `is_queryable` |
| Campaign / ad set / ad structure and performance | `ads_get_ad_entities` at `level=campaign|adset|ad` |
| Is anything blocking delivery? | `ads_get_errors` |
| Meta's own ranked recommendations | `ads_get_opportunity_score` — `PLATFORM_STATED` |
| Creative content: copy, headline, CTA, link, media | `ads_get_creatives` |
| What does the ad look like? | `ads_get_ad_preview` — renders inline in chat only |
| Who changed what, when? | `ads_account_get_activity_logs` — learning resets, budget and creative changes |
| Pixel health, EMQ, dedup | `ads_get_datasets`, `ads_get_dataset_quality`, `ads_get_dataset_stats` |
| Custom audiences, sizes, usage | `ads_get_ad_account_custom_audiences`, `ads_get_custom_audience`, `ads_get_custom_audience_adsets` |
| Catalog and feed health | `ads_catalog_get_diagnostics`, `ads_catalog_get_dynamic_ads_health`, `ads_catalog_get_product_feed_details` |
| Auction pressure and ad quality | `ads_insights_auction_ranking_benchmarks` |
| Vertical benchmarks | `ads_insights_industry_benchmark` — context, never a target |
| Performance trend and anomalies | `ads_insights_performance_trend`, `ads_insights_anomaly_signal` |
| What competitors are running | `ads_library_search` — public, and never evidence of profitability |
| Existing A/B tests and lift studies | `ads_experiment_list_tests`, `ads_experiment_abtest_get_test`, `ads_experiment_lift_get_test` |

## Query discipline

**Ask for the fields you need.** `ads_get_ad_entities` returns nothing you did not request. The
field list in `creative-data-model` is the difference between a creative analysis and a spend
report.

**`effective_status` is not `status`.** Rejections and limited-delivery states live in
`effective_status`. An ad `ACTIVE` but not delivering is a finding hiding in a column most pulls
skip.

**One breakdown dimension per call.** Meta rejects some combinations and silently changes totals
across others. Reconcile every breakdown against its parent total; if the rows do not sum, rows
are missing — say so rather than presenting a subset as the whole.

**One attribution window per run.** Stated in `scope.md` and in every dataset header. A row on a
different window is dropped, not silently included.

**Never average a ratio across entities.** Recompute from component sums at the level you want.

**Values come back as formatted strings** — `"$58,758.12 USD"`, `"1,694,974"`, `"1.55%"`,
`"Not available"`. Parse them, keep the raw. `"Not available"` is **null**, never zero.

**Filter for single-entity drill-downs** rather than pulling everything and filtering locally:
`filtering: [{field:"ad.id", operator:"IN", value:[adId]}]`, one `breakdowns` dimension per call.

## Rate limits

Limits are per account and per app, and shared. Pull the smallest sufficient field set, batch,
and cache with `data-cache`. Under pressure, expect late sections to close `DEGRADED` rather than
failing the run — and record what was not fetched.

## What the connector cannot give you

State these rather than designing an analysis that needs them:

- Per-second video retention curves, storyboards, transcripts, comment data. Quartiles
 (`p25`/`p50`/`p75`/`p100`) are the retention proxy.
- Who was already a customer. New-vs-returning requires the commerce-platform join.
- True incrementality. Reported ROAS is a claim; §26 measures the rest.
- Inline creative images inside an artifact — the sandbox blocks Meta's CDN.
- Anything for an account with `is_ads_mcp_enabled: false`.
