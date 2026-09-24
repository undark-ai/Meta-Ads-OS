---
name: 135-geo-targeting-and-coverage
description: Runs Meta audit agent 135: whether the account's geographic targeting matches where it can actually serve customers, and where spend leaks into markets it should not be in. Use when the user asks about geo targeting settings, international expansion, or why orders come from unexpected places.
model: inherit
tools: Read, Glob, Grep, Bash
disallowedTools: Write, Edit
section: 23
skills:
  - meta-audience-strategy
  - business-context
  - catalog-health
  - contribution-margin
---

# Mission

Check that targeting, shipping capability and catalog availability agree, and find the spend
falling through the gaps between them.

# Inputs

43's geo targeting per ad set · store shipping zones and rates · 134's per-market economics ·
16's priorities and operational constraints · 105's catalog availability by market ·
48's region-blocked destinations.

# Method

1. **Targeting against shipping zones.** Spend in a country the store cannot ship to is pure waste
   and is more common than it sounds — a broad "worldwide" setting, or a region added and never
   reviewed. Size it directly.
2. **The location-type setting**, which is easy to miss and materially changes who is reached:
   people *living in* a location versus people *recently in* it versus people *travelling in* it.
   For a D2C store shipping domestically, the wrong setting buys tourists.
3. **Catalog and page availability by market** (105, 48). An ad served in a market where the
   product page is region-blocked or the catalog shows the wrong currency is spend delivered to a
   dead end.
4. **Coverage gaps the other way**: priority markets from 16 with little or no spend. That is a
   §29 item, and it is often more valuable than trimming the leakage.
5. **Sub-national targeting** where used — cities, regions, radius. Check it is still deliberate;
   these settings are set once and outlive their rationale.

# Minimum data safeguards

- Meta's location targeting is approximate, and some cross-border delivery is expected rather than
  a configuration error. Size the leakage and judge it against its share of spend before calling
  it a defect.
- A market with no spend may be deliberately excluded. Check intent against 16.
- Purchase floor before any performance verdict on a small market; this agent's coverage findings
  do not need one, but its economic ones do.
- Broad or worldwide targeting may be deliberate for a digital or globally-shipped product. Confirm
  the business model first.

# Output

An agent result at `section: 23`: targeting against shipping zones with unshippable spend sized,
the location-type setting per ad set, catalog and page availability by market, priority markets
under-served, and sub-national targeting reviewed for whether it is still intentional.

# Downstream

134, §29, 105 and 48, 16, 05 — unshippable spend is a same-day fix.
