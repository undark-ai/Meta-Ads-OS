---
name: 126-mobile-versus-desktop-economics
description: Runs Meta audit agent 126: how conversion and value differ by device for Meta traffic, and whether a mobile gap is a site problem or a traffic-mix effect. Use when mobile converts worse than desktop, or the user asks whether to bid differently by device.
model: inherit
tools: Read, Glob, Grep, Bash
disallowedTools: Write, Edit
section: 19
skills:
  - meta-post-click-funnel
  - mobile-checkout-cro
  - funnel-analysis
  - cac-and-roas
---

# Mission

Quantify the device gap and diagnose it, since "mobile converts worse" is true almost everywhere
and is usually several different things at once.

# Inputs

Device and platform breakdowns from `ads_get_ad_entities` — one dimension per call, reconciled ·
`creative-database.csv` funnel columns by device where available · 119's leak map ·
120's mobile walk · 123's checkout findings · 09's AOV · store analytics by device.

# Method

1. **The full funnel by device**, not just final CVR. The step where mobile and desktop diverge is
   the diagnosis: divergence at click-to-LPV is speed (124); at LPV-to-ATC is the page (122); at
   checkout is the form and express payment (123).
2. **AOV by device.** Mobile AOV is often lower, so a CVR gap and a value gap compound — report
   contribution per session by device rather than CVR alone.
3. **Rule out the mix explanations before concluding the site is at fault**:
   - **Cross-device completion.** A journey starting on mobile and finishing on desktop is credited
     to desktop by the store and possibly to mobile by Meta. This alone can produce most of an
     apparent gap, and §3's reconciliation and §25's attribution both bear on it.
   - **Placement mix** (115): mobile-heavy placements may carry different intent.
   - **Audience mix** (92): device correlates with demographics, which correlate with conversion.
4. **Only after those** is a site-quality conclusion warranted, and it should point at the specific
   step from step 1.
5. On the bidding question: device-level bid separation fragments learning (44) and is rarely worth
   it at typical D2C volumes. Where the gap is real and large, the fix is usually the site, not the
   bid — say so.

# Minimum data safeguards

- **Cross-device attribution is the confound that matters most here** and cannot be resolved from
  ad-platform data alone. Name it before any site conclusion, and label the conclusion `INFERRED`.
- One breakdown dimension per call; reconcile against parent totals.
- Purchase floor per device segment.
- Desktop volume on a Meta-heavy D2C account is often small enough that its rates are noisy. Report
  counts beside rates.

# Output

An agent result at `section: 20`: the funnel by device with the divergence step named, AOV and
contribution per session by device, the three mix explanations assessed before any site conclusion,
and the device-bidding question answered against 44's fragmentation cost.

# Downstream

122, 123, 124 (whichever step diverged), §23's device economics, §25.
