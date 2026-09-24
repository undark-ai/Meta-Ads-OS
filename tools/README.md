# Connector registry

Runtime context for the data sources a Meta Ads audit touches: what each tool offers
(API / MCP / CLI / SDK), how authentication works, and which operations exist. Agents read
this instead of guessing at connector capabilities — the first rule in `CLAUDE.md` is
*discover tools before use, never invent a tool name or schema*.

| Path | Contents |
|---|---|
| `REGISTRY.md` | Index of all 93 tools with capability columns and links |
| `integrations/` | One guide per tool: auth, scopes, endpoints, common operations, limits |
| `clis/` | 64 zero-dependency Node CLIs — **read the boundary rule in `clis/README.md` first** |
| `composio/` | MCP access layer for OAuth-only tools without native MCP servers |

## Primary sources for this OS

Everything else in the registry is available, but these are the sources the audit agents
actually depend on:

| Source | Role in an audit | Authority |
|---|---|---|
| `meta-ads` | Campaign, ad-set, ad, creative, placement, audience and activity-log data | Media metrics |
| `ga4` | Behaviour, funnels, landing pages, source/medium | Behaviour |
| `shopify` (or the connected commerce source) | Orders, SKUs, refunds, inventory, customer status | Revenue truth |
| `stripe` / `paddle` | Settlement and payment reconciliation | Banked revenue |
| Meta product catalog (via the Meta connector) | Feed attributes, diagnostics, disapprovals | Feed truth |
| Meta Ad Library (via the Meta connector) | Live competitor creative, angles, offers, longevity | Competitive context |
| `semrush` | Competitor, demand and market context | Third-party estimate |
| `browserbase` / `firecrawl` | Rendered landing page, product page, cart and checkout UX — the post-click half of every paid-social finding | Rendered UX |
| `supermetrics` / `coupler` | Reporting pipelines out of the platforms above | Derived |

The Meta Ads connector is the one source this OS cannot run without; everything else is
connector-dependent. Discover each source's real tool schema at runtime rather than assuming a
particular MCP is present, and walk the full connector ladder in `CLAUDE.md` before calling
anything `UNAVAILABLE`.

## Source-of-truth hierarchy

Registry entries do not override the hierarchy in `CLAUDE.md`. First-party transaction data
wins for revenue and orders; Meta is authoritative for media metrics and for its own delivery,
relevance and auction diagnostics; the Meta product catalog for feed state; GA4 for behaviour;
the browser for rendered UX; Semrush and the Ad Library are third-party or competitive
*context*, never observed fact about this account.

Meta-specific: a conversion figure that Meta **modelled** is not an observed fact either, and
never carries the `OBSERVED` class no matter which registry entry supplied it.

## Provenance

This registry is vendored from [`coreyhaines31/marketingskills`](https://github.com/coreyhaines31/marketingskills)
(MIT) by way of `undark-ai/Google-Ads-OS`. See `ATTRIBUTION.md`. Non-Meta entries are kept
deliberately — `shopify`, `stripe` and `paddle` back the economics gate; `google-ads` /
`tiktok-ads` / `linkedin-ads` are what make **blended MER** computable at all, since MER on one
platform's spend is wrong rather than merely partial; `klaviyo` / `attentive` back the LTV loop;
and `hotjar` / `posthog` / `optimizely` back the funnel and CRO bands.
