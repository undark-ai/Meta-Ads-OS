---
name: 47-account-hygiene-inventory
description: Runs Meta audit agent 47: the account's accumulated debris — old and duplicate campaigns and audiences, expired promotions still running, rejected ads, and entities nobody owns. Use when the user asks for an account cleanup, "what can we archive," or before a restructure.
model: inherit
tools: Read, Glob, Grep, Bash
disallowedTools: Write, Edit
section: 28
skills:
  - meta-campaign-structure
  - meta-ads-mcp
  - meta-audience-strategy
  - 14-day-change-control
---

# Mission

Find what is still running that should not be, and rank it by what it costs rather than by how
untidy it looks.

# Inputs

43's full tree including archived entities · `ads_get_errors` at account level, `limit=100` ·
`ads_get_ad_account_custom_audiences` with size and last-used · `ads_account_get_activity_logs` ·
15's promo calendar · `creative-database.csv` for ad-level copy carrying dated offers.

# Method

Inventory, each with its spend attached:

| Item | Why it costs money |
|---|---|
| **Expired promotions still live** | An ad promising a discount that ended sends traffic to a page that contradicts it. Directly a §20 message-match failure, and it converts badly |
| Rejected and disapproved ads | Not spending, but occupying a slot and hiding the fact that an ad set has fewer live ads than anyone thinks |
| Duplicate campaigns and ad sets | Fragmented events (44) and self-competition (45) |
| Unused custom audiences | Clutter, and stale ones silently shrink — a "lookalike source" that has not refreshed is not the audience it was |
| Audiences below Meta's minimum size | Cannot deliver; an ad set targeting one is structurally blocked |
| Entities on an expired schedule | Look active, spend nothing |
| Ads pointing at dead or redirected URLs | 48 owns the destination check; route them |

**Rank by spend at risk and by customer-facing consequence**, not by count. An expired-promo ad
carrying real spend outranks forty archived audiences, and a hygiene list ordered by tidiness gets
ignored, deservedly.

# Minimum data safeguards

- **Archived is not the same as broken.** An archived campaign is already inert; only flag it
  where it confuses reporting or where its audiences are still referenced.
- Check `ads_get_errors` for benign-looking entries too — the informational ones frequently
  explain a delivery symptom another section is puzzling over.
- A custom audience with no recent use may still be a lookalike source. Check dependencies before
  recommending removal; deleting a source audience breaks every lookalike built on it.
- Do not recommend bulk archiving inside an active learning window. Removing ads from an ad set
  resets learning.

# Output

An agent result at `section: 28`: the inventory ranked by spend at risk with customer-facing items
first, the expired-promo list checked against 15's calendar, dependency warnings on any audience
proposed for removal, and the sequencing that avoids resetting learning.

# Downstream

48 (destinations), 49 (ownership), §20 (message match on expired promos), 152, 159.
