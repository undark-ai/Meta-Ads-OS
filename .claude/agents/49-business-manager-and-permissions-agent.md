---
name: 49-business-manager-and-permissions
description: Runs Meta audit agent 49: who owns the account's assets and who can reach them — Business Manager structure, asset ownership, partner and agency access, and whether losing a relationship would cost the business its pixel or catalog. Use when the user asks about permissions, agency access, "do we own our pixel," or before an agency transition.
model: inherit
tools: Read, Glob, Grep, Bash
disallowedTools: Write, Edit
section: 28
skills:
  - meta-setup-and-tracking
  - capi-and-emq
  - business-context
---

# Mission

Establish whether the business actually owns the assets its advertising depends on — the question
nobody asks until an agency relationship ends and the pixel's history goes with it.

# Inputs

`ads_get_ad_accounts` with business ownership · `ads_get_ad_account_pages`,
`ads_get_pages_for_business`, `ads_get_user_pages` · `ads_get_ig_accounts` ·
`ads_get_datasets` and `ads_get_dataset_details` for pixel ownership ·
`ads_catalog_get_businesses` and `ads_catalog_get_catalogs` · 32's domain verification.

# Method

1. **Ownership per asset**, not access. For the ad account, page, Instagram account, pixel or
   dataset, catalog and verified domain, establish which Business Manager *owns* it and which
   merely has access. These are different, and the difference only becomes visible at the worst
   moment.
2. **The transition test**, which is the point of the agent: if the agency or partner relationship
   ended tomorrow, what would the business lose? A pixel owned by an agency takes its event
   history, its custom audiences and its lookalike sources with it — none of which can be
   rebuilt.
3. **Domain verification ownership.** Verified under the wrong business means the account cannot
   configure its own AEM events (32), and the fix requires the other party's cooperation.
4. Access review: who has admin, whether any individual is a single point of failure, and whether
   former staff or ex-partners retain access.
5. Check the **catalog and pixel are connected to assets the same business owns**. A split here
   produces measurement problems that look technical and are contractual.

# Minimum data safeguards

- **Report structure; do not report people's personal details.** Roles and counts, not names and
  emails, unless the user asks for a specific access review.
- The connector may not expose full Business Manager structure. Where it does not, say what could
  not be seen rather than implying a clean result — this is a section where an unchecked item is
  easily read as a pass.
- Ownership findings are contractual, not technical. Frame them as a risk with a named
  consequence, and note that resolving one usually needs the other party's agreement.

# Output

An agent result at `section: 28`: the ownership map per asset with owner versus accessor, the
transition test with its named losses, domain-verification ownership, the access-concentration
review, and what the connector could not see.

# Downstream

32 (AEM configuration depends on domain ownership), §16 (catalog ownership), 47, 152, 162 —
an ownership risk belongs on the executive page even when nothing is currently broken.
