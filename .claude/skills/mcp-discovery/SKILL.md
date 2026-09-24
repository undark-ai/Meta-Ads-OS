---
name: mcp-discovery
description: When establishing which data sources are actually reachable for a Meta audit — walking the connector ladder, discovering real tool names and schemas at runtime, and recording which rung supplied each source. Use at the start of every audit and before any task that needs data. Never declare a source unavailable until every rung has been tried, and never inherit a previous run's verdict.
---
# Source discovery

Two rules, and both exist because breaking them silently deletes whole phases of an audit.

**Discover before use.** Never invent a tool name, schema, account id, dataset id or connector
capability. On Meta this is not pedantry: the connector's server id **differs per account**, so
the prefixed tool names (`mcp__<SERVER_ID>__ads_get_ad_entities`) cannot be known in advance.
Discover them, then use them.

**Walk the whole ladder.** A source is not `UNAVAILABLE` until every rung has failed.

## The connector ladder

| Rung | What it is |
|---|---|
| 1 | **Native connector** — the Meta Ads connector, a Shopify connector, a GA4 connector |
| 2 | **Composio** — the gateway. Supermetrics and similar aggregators sit here too, but check Composio first |
| 3 | **The commerce or analytics platform as a proxy** — Shopify's own reporting can answer questions about paid traffic when the ad platform cannot |
| 4 | **Approved third-party market intelligence** — Semrush and similar. Estimates, never revenue truth |
| 5 | **Browser observation** — `browser-inspection` for what is rendered, when no API reports it |
| 6 | **Ask the user** — an export, a screenshot, a figure they already know |
| 7 | `UNAVAILABLE` |

The gateway rung is not a fallback to reach for after the native one fails. **Check it first if
the account already uses one**, and check it every run. A source ruled out through one route is
frequently sitting authorised on another — a mistake made in production and recorded in
`FIELD-NOTES.md`.

**No native MCP for a source means go to Composio, in this order:**

1. `COMPOSIO_SEARCH_TOOLS` with the use case — the result names the toolkits and, in
   `toolkit_connection_statuses`, whether each already has an ACTIVE connection.
2. `COMPOSIO_MANAGE_CONNECTIONS` with `action: "list"` for the toolkit — this returns the
   **account ids**, which the next step needs.
3. Pick the account deliberately (see below), then execute through
   `COMPOSIO_MULTI_EXECUTE_TOOL`, passing `account` explicitly.

Two traps, both hit on a live account and both silent:

- **`account_selection: required` means the default is a guess.** A toolkit routinely holds more
  than one ACTIVE connection, and one connection can reach several properties or customers. On one
  run GA4 offered three properties under the right account — two of them sharing a name — and
  Google Ads offered three customer ids, two of which belonged to **other advertisers** and
  returned `USER_PERMISSION_DENIED`. Resolve the account by name and confirm it against something
  independent (timezone, currency, descriptive name) before pulling a figure from it. Record the
  chosen account id in `source-capabilities.md`, or the number cannot be traced later.
- **Some platforms refuse metrics in a manager context.** Google Ads returns
  `REQUESTED_METRICS_FOR_MANAGER` unless you resolve to a non-manager client first.

A gateway may hold **several authenticated accounts** for one platform. Enumerate them; the live
one is not always the one you were pointed at. Gateways also expose mutating tools — record them
during discovery and, in the audit lane, never call them.

## Never inherit a previous run's verdict

Connectors get authorised between runs. Re-checking is the cheapest test in the system, and
carrying forward an `UNAVAILABLE` from last month means an audit that quietly skips a section
the account can now supply.

## What to record

`audits/<run-id>/source-capabilities.md`:

| Source | Available | Authenticated | Rung | Real tool names | Authority | Date coverage | Notes |
|---|---|---|---|---|---|---|---|

The **real tool names** column is what stops downstream agents guessing. The **rung** column is
what makes a later `BLOCKED` verifiable.

## Meta-specific discovery

1. `ads_get_ad_accounts` — enumerate. Check `is_ads_mcp_enabled` as well as `is_queryable`;
 `false` on the first beats `true` on the second, and the failure otherwise surfaces deep into
 the run.
2. Confirm which account is live, and that it has spend in the intended window
 (`ads_get_ad_entities` at account level, wide range, monthly increments).
3. Confirm timezone, currency and the account's default attribution setting.
4. Probe field availability once at ad level before writing the full extraction — some fields
 return `"Not available"` for some accounts and objectives, and finding that out mid-pull
 wastes the quota.
5. `ads_get_datasets` — which pixel the account actually optimises against.
6. `ads_catalog_get_catalogs` — whether §16 and §17 have anything to audit at all.

## Tag every result, or the cache lies

A tool result that arrives untagged cannot be reused safely, and cannot be defended in a finding.
Tag each one at the point of retrieval:

```
source · tool · retrieval time · date range · account or store scope
attribution window · raw-or-normalized · confidence
```

The last three are what separate this from a filename. An untagged result and a result on a
different attribution window look identical downstream, which is the failure `data-cache` exists to
prevent.

## Retry behaviour

Retry a **transient** failure at most twice — a timeout, a 5xx, a rate-limit response that names a
retry-after. Back off between attempts.

**Never retry a validation error or a malformed argument without changing the request.** The
second identical call fails the same way and spends quota that a later section needs. An
unsupported field is not transient: read the error, which usually names the fields that *are*
supported at that level, and re-issue once against those.

A tool that reports itself unavailable for the account — not rolled out, not enabled — is not a
retry case at all. Record it as `UNAVAILABLE` with the reason, and degrade the sections that
depend on it rather than calling again.

## Rate limits

Meta rate-limits by account and by app. Heavy extraction can exhaust the budget for a period,
and it is shared. Batch queries, pull the smallest sufficient field set, and cache
(`data-cache`) so downstream agents reuse results rather than re-querying.

Expect late sections to close `DEGRADED` under limits rather than the run to fail. Say so in the
ledger, with what was not fetched.

## Discovery is not a phase you finish

If a section needs something discovery did not surface, check again before declaring it
blocked — including asking the user. The ladder's fourth rung is a real rung, and it is the one
most often skipped.
