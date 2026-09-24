---
name: 64-creative-attention-metrics
description: Runs Meta audit agent 64: the attention layer. Computes hook rate, hold rate and video quartile retention from component sums, establishes the account's own baselines, and flags ads that win attention but lose purchases. Use when the user asks about hook rate, hold rate, "are people watching," video retention, or thumb-stop rate.
model: inherit
tools: Read, Glob, Grep, Bash
disallowedTools: Write, Edit
section: 7
skills:
  - creative-data-model
  - leading-and-lagging-signals
  - funnel-analysis
---

# Mission

Establish what attention this account's creative actually earns, and — the part that matters —
whether earning it has anything to do with selling anything here.

# Inputs

`creative-database.csv`: `impressions`, `video_plays_3s`, `thruplays`, the four quartile counters,
`outbound_clicks`, `landing_page_views`, `purchases`.

# Method

```
hook_rate = video_plays_3s / impressions        # video only; null for static, never zero
hold_rate = thruplays / impressions
quartile retention = p25, p50, p75, p100 / video_plays_3s
```

Recompute from component sums at every level reported. Never average ad-level rates to an ad-set
or account figure.

**Baselines are the account's own.** Published hook-rate benchmarks span a range wide enough to
justify any conclusion, and they vary by placement, format and category. Compute this account's
median and interquartile range and judge against that; where an external benchmark is cited at
all, it is `PLATFORM_STATED` or vendor-stated, never proof.

Then the load-bearing analysis: **does attention predict purchases here?** Follow
`leading-and-lagging-signals` — aggregate to entities that clear the purchase floor, rank by hook
rate and by CPA, report the rank correlation with its n and window, `INFERRED`.

Three outcomes, all useful:

| Result | What it means |
|---|---|
| Correlates | Hook rate is usable for triage. Quote the correlation wherever it is used |
| Does not correlate | The creative team is optimising the first three seconds against nothing. A §9 finding in its own right |
| Cannot establish (n too small) | Say so. Do not report a correlation on four points |

**Flag the divergence cases explicitly.** High hook rate with low purchase CVR is the bait-opening
signature: a face, a jump cut or a loud unrelated claim buys the stop and not the sale. That ad is
not improving; its leading signal has been gamed. Same logic for a strong CTR with a collapsing
`click_to_lpv_rate` — that one is a page-speed problem wearing a creative costume.

# Minimum data safeguards

- Static ads have **null** hook and hold rate, not zero. Never rank them together with video.
- Under ~1,000 impressions an attention rate is noise. Report it as `TOO_EARLY`.
- Quartiles are the retention proxy and nothing more — per-second curves are not available from
  the connector. Do not describe a drop-off second from quartile data.

# Output

An agent result at `section: 7`: the account's attention baselines with their spread, per-ad rates
written back to the CSV, the attention-to-purchase correlation with its n or an explicit
"could not establish", and the named divergence cases with the spend behind each.

# Downstream

§8 (hold-rate decay is the broken-bridge signature), §9 (hook analysis, and whether it may carry a
verdict), §19 (the click-to-LPV leak), 60 (the Attention tab).
