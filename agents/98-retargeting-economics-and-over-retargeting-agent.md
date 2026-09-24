---
name: 98-retargeting-economics-and-over-retargeting
description: Runs Meta audit agent 98: what retargeting costs and returns once existing customers and would-have-bought-anyway conversions are separated out, and where the account is paying to reach people it already reaches. Use when the user asks whether retargeting is worth it, about retargeting ROAS, or how much to spend on it.
model: inherit
tools: Read, Glob, Grep, Bash
disallowedTools: Write, Edit
section: 14
skills:
  - cac-and-roas
  - demand-lifecycle
  - incrementality
  - contribution-margin
---

# Mission

Price retargeting honestly. It reports the account's best ROAS almost by construction, and the
question is how much of that is caused rather than captured.

# Inputs

97's tier map with lifecycle stages · 51's performance per retargeting campaign ·
12's new-versus-returning · 11's targets · 90's frequency · 40's view-through share ·
§1's owned-channel context from 08 and 14's channel census.

# Method

1. **Report by lifecycle stage, never as one number.** Accelerate, Revive and Expand answer to
   incremental conversion rate, reactivation rate and repeat contribution respectively. A single
   "retargeting ROAS" pools three different jobs and describes none.
2. **View-through share by tier** (40). Retargeting typically carries the highest view-through
   share in the account, and a ROAS built substantially on view-through is a weaker claim than the
   same number from click-through. Publish the pair.
3. **The over-retargeting readings:**
   - Frequency above the tier's threshold (90) with CPA rising — paying more to reach the same
     people more often.
   - Spend growing while the audience pool is static (87) — the same.
   - Purchasers not excluded from Accelerate tiers (86) — paying to convert the converted.
4. **Expand versus owned channels.** Where Expand spend targets existing customers an email or SMS
   list already reaches, the incremental value of the ad is the reach it adds beyond the owned
   channel, which is often small. Size it where the email channel's reach is known; flag it clearly
   where it is not. This is waste dressed as performance, and it is invisible in any Meta report.
5. Set retargeting contribution against 11's targets, and state that the reported figure is an
   upper bound on its true contribution pending §26.

# Minimum data safeguards

- **Retargeting ROAS is the least incremental number in the account.** Never present it as
  comparable to prospecting ROAS without saying so; §26 owns the correction, and until it runs
  every figure here is labelled as a claim.
- Purchase floor per tier.
- Where the commerce join is missing, the existing-customer share is unknown and the whole section
  is `DEGRADED`.
- Do not recommend cutting retargeting on incrementality suspicion alone. Recommend the holdout
  that would settle it (§26).

# Output

An agent result at `section: 14`: economics by lifecycle stage with the right number for each,
view-through share by tier, the three over-retargeting readings with spend attached, the
Expand-versus-owned-channel overlap, and the upper-bound framing on every ROAS figure.

# Downstream

§26 (this section's claims are its input), §24, §29, 158, 162.
