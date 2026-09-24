# Composio Quick Start

Get MCP access to 500+ marketing tools through a single integration.

## Prerequisites

- Node.js 18+
- Claude Code installed

## Install

```bash
npx @composio/mcp@latest setup
```

Verify by running `/mcp` in Claude Code — `composio` should appear in the server list.

## Connect a Tool

When you ask the agent to use a Composio-backed tool for the first time, it will provide a Connect Link. Open the link in your browser, authorize the app, and you're set. The connection persists across sessions.

```
You: "Get my top HubSpot contacts"
Agent: "Please connect HubSpot first: https://app.composio.dev/connect/..."
# Click the link → authorize → return to Claude Code
Agent: "Here are your top contacts: ..."
```

## Usage Examples

### Pull CRM contacts

```
"Show me my 10 most recent HubSpot contacts with their deal stages"
```

### Get ad performance

```
"What's my Meta Ads spend and ROAS for the last 7 days?"
```

### Write to a spreadsheet

```
"Add a row to my 'Campaign Tracker' Google Sheet with today's LinkedIn Ads metrics"
```

### Cross-tool workflow

```
"Find Salesforce leads from this week and post a summary in Slack #new-leads"
```

## Using Composio in an audit

Composio is **rung 2 of the connector ladder** (`.claude/skills/mcp-discovery`): where a source has
no native MCP, this is where the audit goes before declaring it `UNAVAILABLE`. In practice GA4 and
Google Ads are frequently already authorised here, and they are the two that decide whether §3
reconciliation and blended MER can be computed at all.

### The two pulls an audit actually needs

**GA4 — the neutral arbiter in §3.**

```
GOOGLE_ANALYTICS_LIST_ACCOUNT_SUMMARIES   → find the property
GOOGLE_ANALYTICS_GET_METADATA             → derive real apiNames; never hardcode from UI labels
GOOGLE_ANALYTICS_RUN_REPORT               → sessions, transactions, purchaseRevenue by channel
```

Dimension/metric compatibility is enforced server-side; `GOOGLE_ANALYTICS_CHECK_COMPATIBILITY`
settles a 400 faster than guessing. `metricValues` come back as **strings** — cast before summing.

**Google Ads — total ad spend, without which blended MER is wrong rather than partial.**

```
GOOGLEADS_LIST_ACCESSIBLE_CUSTOMERS       → candidate customer ids
GOOGLEADS_SEARCH_STREAM_GAQL              → SELECT metrics.cost_micros ... FROM campaign
                                             WHERE segments.date BETWEEN ... AND ...
```

`cost_micros` is micros — divide by 1,000,000. Metrics **cannot** be requested in a manager
context (`REQUESTED_METRICS_FOR_MANAGER`); resolve to a non-manager client first.

### Two traps that cost real time on a live run

**A toolkit can hold several ACTIVE accounts, and the default is a guess.** When the search result
says `account_selection: required`, enumerate before executing:

```
COMPOSIO_SEARCH_TOOLS      → read toolkit_connection_statuses
COMPOSIO_MANAGE_CONNECTIONS {action: "list"}   → account ids
COMPOSIO_MULTI_EXECUTE_TOOL {account: "<chosen id>"}   → always pass account explicitly
```

On one live run GA4 offered three properties under the right account, **two sharing a name**, and
Google Ads offered three customer ids of which **two belonged to other advertisers** and returned
`USER_PERMISSION_DENIED`. Resolve by name, confirm against something independent — timezone,
currency, descriptive name — and write the chosen account id into `source-capabilities.md` so the
figure can be traced back later.

**Composio exposes mutating tools.** Record them during discovery and, in the audit lane, never
call them. The execution-boundary rules in `CLAUDE.md` apply to gateway tools exactly as they apply
to the Meta connector's.

## Available Marketing Tools

See [marketing-tools.md](marketing-tools.md) for the full list of Composio toolkits mapped to marketing use cases.

Key tools with new MCP access (no native MCP server in this repo):
- **HubSpot** — contacts, deals, companies, lists
- **Salesforce** — SOQL queries, leads, opportunities
- **Meta Ads** — campaigns, ad sets, insights
- **LinkedIn Ads** — campaigns, analytics
- **Google Sheets** — read, write, create spreadsheets
- **Slack** — messages, channels
- **Notion** — pages, databases
- **Klaviyo** — profiles, lists, campaigns
- **ActiveCampaign** — contacts, automations

## Troubleshooting

### "Tool not found" error

The tool may not be connected yet. Ask the agent to connect it, or run:

```bash
npx composio apps list
```

### Expired authentication

OAuth tokens expire. If a tool stops working, re-authenticate:

```bash
npx composio connections list    # Find the connection
npx composio connections remove {id}  # Remove it
# Then ask the agent to use the tool again to trigger re-auth
```

### Rate limit errors

Composio has its own rate limits (free: 20K calls/mo, 10 req/sec). If you hit them:
- Reduce request frequency
- Upgrade your Composio plan
- Use native CLI tools for high-volume operations

### MCP server not appearing

Re-run the setup command:

```bash
npx @composio/mcp@latest setup
```

Then restart Claude Code.
