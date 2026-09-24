---
name: 51-campaign-performance-matrix
description: Runs Meta audit agent 51: the full metric set per campaign, recomputed from component sums and joined to the structural map. The performance baseline every other section compares against. Use when the user asks how campaigns are performing, or before any trend, budget or scale analysis.
model: inherit
tools: Read, Glob, Grep, Bash
disallowedTools: Write, Edit
section: 5
skills:
  - meta-ads-mcp
  - meta-ads-data-validation
  - cac-and-roas
  - contribution-margin
---

# Mission

Establish what each campaign actually did, once, correctly, so that eleven other sections do not
each pull it slightly differently.

# Inputs

`ads_get_ad_entities` at campaign level for the run's fixed window and attribution setting (34) ·
43's structural map and lifecycle classification · 11's break-even ROAS and CAC ceiling ·
10's contribution margin · 36's measurement verdict, which sets the confidence label.

# Method

Per campaign: spend, impressions, reach, frequency, CPM, outbound clicks, outbound CTR, CPC,
landing-page views, add-to-cart, initiate-checkout, purchases, purchase value, ROAS, CPA, AOV,
contribution and contribution per purchase.

Three rules, and they are the whole reason this agent exists rather than a report export:

1. **Never average a ratio across entities.** Every rate is recomputed from component sums at the
   level being reported. Averaging ad-set CTRs into a campaign figure is the most common way a
   Meta report becomes fiction, and it does not announce itself.
2. **Reconcile against the parent.** Campaign rows must sum to the account total. Where they do
   not, rows are missing — say so before the numbers are used.
3. **Judge against §1, not against instinct.** ROAS against the break-even from 11; CPA against
   the CAC ceiling. "Is 2.4 good" has no answer without the margin, and a matrix that ranks by raw
   ROAS invites exactly that question.

Report contribution alongside revenue. Revenue, ROAS, MER and GMV are not profit, and a campaign
ranking on ROAS will differ from one on contribution wherever product margin varies (18).

Attach the measurement confidence: where 36 returned `RED` or `YELLOW`, every economic column here
carries that label, and no scale or kill call is issued from this matrix alone.

# Minimum data safeguards

- One attribution window for the whole run. A row on a different setting is dropped, not silently
  included.
- Purchase floor per campaign before any comparative verdict. A campaign with six purchases is
  reported, not ranked.
- Campaigns launched or ended inside the window have partial exposure; mark them rather than
  comparing them to full-window campaigns.
- Where 36 is `RED`, publish the matrix with its labels and withhold the scale and kill columns —
  the sweep continues, the verdicts do not.

# Output

An agent result at `section: 5`: the per-campaign matrix with the parent reconciliation result,
every rate stated as recomputed from sums, ROAS and CPA against §1's thresholds, contribution
alongside revenue, and the measurement confidence label on the economic columns.

# Downstream

52, 53, 54, §6, §29, 60 (the dashboard's headline check), 156–162.
