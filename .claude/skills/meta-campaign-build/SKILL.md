---
name: meta-campaign-build
description: When building campaigns, ad sets, ads and creatives on a live Meta account under the execution protocol — the build chain, the settings that matter, and the create-paused discipline. Use in an execution run when the user asks to "build this campaign," "launch these ads," "set this up in Meta." Execution lane only. For what to build and why, see meta-campaign-creation and meta-campaign-structure; this covers safely applying it.
lane: execution
---
# Campaign build

Load `meta-execution-protocol` first. Everything here operates inside it.

`meta-campaign-creation` and `meta-campaign-structure` decide *what* to build. This covers
building it on a live account without breaking anything.

## The chain

```
campaign  →  ad set  →  creative  →  ad
ads_create_campaign
             ads_create_ad_set
                          ads_create_creative
                                        ads_create_ad
```

Every one of these is a `write` tool. Every one is created `PAUSED`. Activation is a separate,
separately-approved step.

Build parent-first and verify each level exists before creating its children. A failed ad-set
creation followed by four ad creations produces four orphaned errors and a confusing log.

## Settings that are expensive to get wrong

| Setting | Why it matters | Reversible? |
|---|---|---|
| **Objective** | Cannot be changed after creation. A campaign built on the wrong objective is rebuilt, not edited | **No** |
| **Optimisation event** | Determines what Meta buys. `LINK_CLICKS` in a sales campaign buys clicks | Yes, resets learning |
| **Attribution setting** | Changes what the campaign reports, and breaks comparability with the rest of the account | Yes |
| **Budget level (CBO vs ABO)** | Structural. Switching later resets learning across the campaign | Yes, expensively |
| **Daily vs lifetime budget** | Lifetime cannot be changed to daily after the fact | **No** |
| **Audience exclusions** | Missing existing-customer exclusion silently inflates reported ROAS | Yes |
| **Placements** | Advantage+ Placements is the default for a reason; manual selection needs evidence | Yes, resets learning |
| **Advantage+ Creative enhancements** | Meta may alter the asset. You are then running an ad you did not fully author | Yes |

The three irreversibles — objective, lifetime budget, and campaign type — are checked against
the plan twice before the create call.

## Before activation

The create-paused rule exists so this check can happen:

1. **Budget against account history.** Not against the plan — against what this account normally
   spends. The plan can contain a typo; account history cannot.
2. **Preview every ad** (`ads_get_ad_preview`). Look at it. Broken text rendering, wrong aspect
   ratio and missing images are visible in one glance and invisible in a JSON response.
3. **Destination URL**, including UTM parameters, resolved through its redirect chain.
4. **Exclusions present**, especially existing customers on prospecting.
5. **Optimisation event** matches the objective and the §1 goal.

Then request approval for activation as a separate step.

## Creative upload

`ads_creative_upload_image|video` and the local-image finalise chain are writes. Upload before
creating the creative that references them, and log the returned hashes — a rollback that has to
find an orphaned upload later cannot.

## Naming

Build to the account's naming convention (§7, §28). This is not cosmetic here: rule-based
creative tagging runs off it, so an ad launched with an unparseable name is an ad that will not
appear in any future creative pattern analysis. The build is where compliance is cheap; the
audit is where non-compliance is expensive.

## Rollback

For a build, rollback is pausing and archiving what was created — not deleting it. Deleting
loses the delivery history, and if the build was correct and only mistimed, the history is worth
keeping.

Record every created entity id in `applied.md` as it returns. A build that dies halfway leaves
live entities, and the register is the only record of which ones.
