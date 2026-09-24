---
name: 33-third-party-checkout-measurement
description: Runs Meta audit agent 33: what changes when checkout sits on a domain the business does not control — verification, AEM, cookie access and click-id persistence all behave differently. Use when the store uses a hosted or third-party checkout, a payment-provider domain, or the user asks why tracking breaks at checkout.
model: inherit
tools: Read, Glob, Grep, Bash
disallowedTools: Write, Edit
section: 2
skills:
  - meta-third-party-conversion-tracking
  - capi-and-emq
  - browser-inspection
---

# Mission

Handle the case that breaks the standard measurement model, and say who can actually fix each
part of it.

# Inputs

The checkout journey, walked: which domain each step sits on, which cookies are readable where ·
31's traced click-id chain · 32's verification status · 23's implementation route · the
platform or provider's own documented capabilities.

# Method

1. **Map the domains.** Landing, cart, checkout and confirmation may span two or three. Where the
   order is created determines where the `Purchase` event can fire.
2. Per constraint, establish the position and the owner:

   | Constraint | Question |
   |---|---|
   | Domain verification | Which domain is verified, and is it the one the conversion happens on |
   | AEM configuration | Whose configuration applies to the checkout domain |
   | Cookie access | Can `_fbc` and `_fbp` be read where the order is created |
   | Server events | Can the provider send them, and with which identifiers |
   | Order data | Does the business receive enough back to reconcile in §3 |

3. **Prefer the server-side route.** Where the browser cannot fire a usable event on a third
   party's domain, a server event from the business's own backend — where the order is recorded —
   is usually both possible and better matched. Say so concretely rather than describing the
   constraint.
4. **Name the owner of each gap.** Some are the provider's, some the platform's, some the
   account's. A recommendation addressed to the wrong party is a recommendation that does not get
   done, and this is the section where that failure is most common.

# Minimum data safeguards

- Where checkout is on the business's own domain, this agent is **`N/A`** — a clean result, stated
  explicitly so the reader can tell it was checked.
- Provider capabilities change; check current documentation rather than relying on what was true
  at a previous audit, and cite what was checked.
- Do not assume a hosted checkout cannot be measured. Many can, through the platform's own Meta
  integration; the question is whether this account has it configured.

# Output

An agent result at `section: 2`: the domain map, each constraint with its position and owner, the
recommended route with its expected effect, and what §3 can and cannot reconcile as a result.

# Downstream

31, 32, 23, 36, and §19 — a checkout the audit cannot measure is a funnel step it cannot size.
