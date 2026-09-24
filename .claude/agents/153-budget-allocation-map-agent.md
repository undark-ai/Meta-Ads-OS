---
name: 153-budget-allocation-map
description: Runs Meta audit agent 153: where every pound currently goes and what it returns, mapped across campaign, audience, creative, product, geography and lifecycle stage on one basis. Use before any reallocation decision, or when the user asks where their budget is going and whether it is right.
model: inherit
tools: Read, Glob, Grep, Bash
disallowedTools: Write, Edit
section: 29
skills:
  - cac-and-roas
  - contribution-margin
  - demand-lifecycle
  - recommendation-prioritization
---

# Mission

Put the whole account's allocation on one page, on one measurement basis, so §29's decisions are
made against a single picture rather than six section-level ones.

# Inputs

51's campaign matrix · 53's concentration · 84's audience-type performance · 71's angle rankings ·
18's product economics · 134's market economics · 116's placement economics ·
138's new-customer split · 144's stated allocation basis · 11's targets · 10's margin.

# Method

1. **One basis, stated once.** 144 says whether the account should allocate on incremental
   contribution (where proven), new-customer CAC, or blended MER. Use it consistently — the most
   common failure in a budget section is mixing bases across dimensions and comparing numbers that
   are not comparable.
2. **The allocation map** across six dimensions, each with spend, contribution, CAC against 11's
   ceiling, and the share of total:
   campaign · audience type · creative angle · product group · geography · lifecycle stage.
3. **Flag where dimensions disagree.** A campaign above break-even whose spend sits mostly in a
   below-break-even product group is a mixed entity, and moving budget at campaign level will not
   fix it. These are the cases where allocation decisions go wrong.
4. **Publish the lifecycle split prominently** (144's warning): what share is Create versus Capture,
   and what the reported-ROAS ranking would do to it if followed.
5. **Mark every cell's confidence**: purchase count, measurement verdict (36), and whether the
   figure is reported, new-customer or incremental.

# Minimum data safeguards

- **Do not sum across dimensions.** The same spend appears in every one of the six views; they are
  lenses on one pool, not additive pools.
- Purchase floor per cell; below it the cell carries spend and no verdict.
- Where §2 is `RED`, publish the map with spend and volume and withhold the contribution columns.
- Where 138's join is missing, new-customer columns are `null` and the basis falls back to blended
  with that stated.

# Output

An agent result at `section: 29`: the six-dimension map on one stated basis, disagreements between
dimensions named, the lifecycle split with 144's warning attached, and confidence marked per cell.

# Downstream

154, 155, 158, 159, 160.
