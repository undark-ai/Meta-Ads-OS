---
name: meta-audience-build
description: When creating or updating custom audiences, lookalikes and customer lists on a live Meta account under the execution protocol — including the hashing and consent rules for uploading customer data. Use in an execution run when the user asks to "upload my customer list," "create a lookalike," "build a value-based audience," or "set up exclusions." Execution lane only. For which audiences to build, see meta-audience-strategy and meta-high-value-audiences.
lane: execution
---
# Audience build

Load `meta-execution-protocol` first.

This skill covers the one execution area that handles other people's personal data, so it
carries rules the rest of the lane does not.

## Customer data — the non-negotiables

Before `ads_update_custom_audience_users` is called:

1. **The user has authorised this specific upload, this run.** Not "we agreed to build
   audiences". This list, these records, now.
2. **The data is hashed** as Meta requires — SHA-256, normalised (lowercased, trimmed) before
   hashing. **Never send raw email or phone.** If the pipeline cannot hash, it does not run.
3. **The lawful basis is the user's to assert.** Ask what it is, record the answer, and do not
   proceed on an assumption about consent. This is not the audit's judgement to make, and it is
   not one to skip.
4. **Log the audience id and the record count. Never log the records.** The change register is a
   file on disk; customer PII does not belong in it.
5. **Suppression lists are as sensitive as inclusion lists.** People who asked not to be
   contacted are a category that deserves more care, not less.

An upload that cannot satisfy all five does not happen, and the reason is reported.

## Value-based audiences

Value-based customer lists and lookalikes are among the highest-return audience work available
(`meta-high-value-audiences`), and they carry the same data rules plus one more: the **value**
column is commercially sensitive. Confirm the user intends to send per-customer value before
including it.

## Lookalike seeds

- A seed under Meta's minimum produces a poor lookalike, not an error. Check the seed size before
  creating.
- Seed quality beats seed size. 500 high-LTV customers outperform 50,000 all-buyers, and the
  build should say which was used.
- Record the seed audience id on the lookalike. A lookalike whose seed nobody can identify later
  cannot be refreshed or reasoned about.

## Exclusions

The most common audience finding in an audit is a missing exclusion, and the most common fix is
this. Two cautions when applying it:

- Adding an exclusion to a live ad set **resets learning**. State the cost in the plan.
- Excluding existing customers from prospecting will **lower reported ROAS**, because it removes
  the purchases that were flattering it. Tell the user this before the change, not when they ask
  why performance dropped. It is the change working, not failing.

## Updates versus creates

`ads_update_custom_audience_users` can add or remove. Removal is not reversible by re-adding —
the audience's history and its lookalike seeds are affected. Prefer creating a new audience over
mutating one that other ad sets depend on; check `ads_get_custom_audience_adsets` before
touching an audience to see what would be affected.

## Rollback

An audience that was created can be deleted, but a lookalike built from it and the ad sets using
it cannot be trivially restored. Rollback for audience work is usually "stop using it", not
"undo it" — say so in the plan, because it is one of the places where the protocol's rollback
promise is weaker than elsewhere.
