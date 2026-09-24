---
name: meta-automated-rules
description: "When the user wants to automate account maintenance on Meta for an e-commerce or D2C brand — native Automated Rules or Marketing API automation that pauses losers, scales winners, watches frequency, or guards spend. Also use when the user mentions 'automated rules,' 'auto-pause,' 'auto-scale,' 'rule to kill bad ads,' 'automate my ad account,' 'spend safety net,' 'budget automation,' 'script to manage my ads,' or 'my account got restricted.' Covers the account-safety and rate-limit rules for any automation that touches a live ad account. For the thresholds the rules should encode, see meta-ads-operating-system. For the weekly manual cadence automation is meant to support, see meta-optimization-playbook. For API objects and fields, see meta-api-reference."
metadata:
 version: 1.0.0
---

> **Marketing layer — advisory, not evidence.** Every benchmark, threshold and rule of thumb
> below is build-time guidance. Per `CLAUDE.md`, a marketing skill's number is never evidence
> for a quantified finding: a recommendation that originates here still needs a number, source,
> date range, formula, evidence class and confidence from the audit layer before it can be
> presented as one. Handoffs run audit → marketing, never the reverse.


# Meta Automated Rules & Safe Automation — D2C E-commerce

Automated rules are the cheapest leverage in a Meta account and the fastest way to wreck one. A rule that fires on three days of thin data will pause your best ad before it has a chance; two rules that disagree will thrash an ad set until the algorithm gives up on it. This skill drafts rules, audits existing ones, and sets the safety rails for anything that writes to a live account.

## Before Starting

**Check for product marketing context first:**
If `.agents/product-marketing.md` exists (or `.claude/product-marketing.md`, or the legacy `product-marketing-context.md` filename, in older setups), read it before asking questions. Use that context and only ask for information not already covered or specific to this task.

Gather this context (ask if not provided):

- **Target CPA and break-even ROAS** — every threshold below is expressed as a multiple of Target CPA, so a rule cannot be written without it. Derive it as in meta-ads-operating-system: AOV, contribution margin per order, and the LTV-funded allowance.
- **Daily budget per campaign and the current number of active ads** — a rule's minimum-spend gate has to be reachable within its own time window.
- **What already runs** — existing rules, existing scripts, and whether anything currently has write access.

## Requires the Meta Ads MCP for Live Work

Auditing what already runs, and reading the delivery data a rule should be calibrated against, goes through the Meta Ads MCP: `ads_account_get_activity_logs` to see what has been changing the account, `ads_get_ad_entities` and `ads_get_ad_entities` for the spend and CPA distribution the thresholds must sit against, and `ads_get_errors` for delivery problems a rule might be reacting to. If the MCP isn't connected, say so and stop rather than fabricating account data — the rule recipes below still apply as drafts.

**This skill drafts and audits rules. It does not create them silently.** Every rule below spends or stops money. Output the rule specification for a human to enter or approve; never push a spend-affecting rule as a side effect of a conversation.

## How Rules Actually Evaluate

- **Evaluation frequency**: continuously (roughly every 30 minutes), hourly, or daily. Continuous is the default and the most dangerous, because it lets a rule act on an hour of data.
- **Conditions are AND-ed.** Every condition must be true at the same evaluation. This is your main safety tool: pair every performance condition with a minimum-spend or minimum-results condition.
- **The time window is separate from the evaluation frequency.** A rule can evaluate every 30 minutes against a 3-day window. Match the window to how long the metric needs to stabilize, not to how often you want to look.
- **Actions available**: turn off, adjust budget, adjust bid, or notify only. Notify-only is a first-class option and underused.
- **Always gate on volume.** A rule with no minimum-spend or minimum-results condition will fire on the first ad that gets unlucky in its first hour.

## Rule Recipes

Thresholds below match meta-ads-operating-system so automation and manual review never disagree. Substitute your own Target CPA.

| Rule | Conditions (all AND-ed) | Action | Caveat |
|---|---|---|---|
| **Pause underperformers** | Cost per purchase > Target CPA **and** spend > 3× Target CPA, over a rolling 3-day window, ad level | Turn off | Never let this fire before the learning phase exits. 3× Target CPA is the point at which zero purchases stops being bad luck — below it you are pausing noise. |
| **Scale a winner** | ROAS > target **and** cost per purchase ≤ Target CPA for 3 consecutive days **and** spend > a floor you set, ad set level | Increase budget 15–20% | Cap the increment. An uncapped percentage rule compounds daily and blows past the 30% learning-reset threshold within a week. Add a maximum-budget condition. |
| **Spend safety net** | Amount spent today > your hard daily cap, account or campaign level | Turn off | A backstop against a fat-fingered budget or a runaway scale rule, not a management tool. If this fires in normal operation, something else is broken. |
| **Frequency watch** | Frequency > 4 over a rolling 7-day window | **Notify only** | Never auto-pause on frequency. High frequency on a profitable ad is a rotation signal, not a kill signal — see creative-fatigue-detection. Auto-pausing here kills winners. |
| **Pacing check** | Spend < 50% of daily budget by a fixed hour | **Notify only** | Underspend has many causes (audience too small, bid too low, CBO concentration) and no single safe automated fix. Diagnose it, don't automate it. |

Two rules worth adding for D2C specifically:

- **Zero-delivery catch**: spend = $0 over the last 2 days at ad level, notify only. Catches rejected ads and broken creative before a week of budget quietly reroutes.
- **Catalog-driven campaign guard**: notify when an Advantage+ Shopping or dynamic-catalog campaign's spend jumps sharply, since a feed change can redirect delivery to products you didn't intend to push.

## Pitfalls: Rules That Do More Harm Than Good

1. **No minimum sample size.** The single most common failure. Any performance rule without a spend or results gate is a random-ad-killer.
2. **Continuous evaluation on a thin window.** Evaluating every 30 minutes against one day of data means the rule is reading variance. Match the window to the metric: purchases need days, not hours.
3. **Stacked conflicting rules.** A scale rule and a pause rule that can both be true on the same ad set will raise and cut budget in alternating evaluations, resetting learning every time. Audit for overlap before adding a rule.
4. **Ignoring attribution lag.** Meta restates conversion data for up to 7 days. A rule that reads yesterday's CPA is reading an incomplete number, and it will always look worse than reality. Never let a pause rule act on a window that ends today.
5. **Uncapped budget increases.** Percentage increases compound. Without a maximum-budget condition, a winning ad set walks itself into a learning reset.
6. **Rules nobody reviews.** A rule calibrated at a $25 Target CPA is wrong the moment margins or AOV change. Re-audit every rule when you re-set Target CPA.

## Rule Audit Checklist

When reviewing an account's existing rules:

1. List every rule with its conditions, action, window, and evaluation frequency. Pull `ads_account_get_activity_logs` to see which ones have actually fired and what they touched.
2. For each rule: does it have a volume gate? Does its window end today? Is the threshold still consistent with current Target CPA?
3. Look for pairs that can both be true on the same entity.
4. Flag every rule whose action spends or stops money but whose thresholds nobody can explain.
5. Downgrade anything ambiguous to notify-only rather than deleting it — you keep the signal and lose the risk.

## When Native Rules Aren't Enough: API Automation

Native rules can't join to store-side data, so they can't act on new-customer CAC, MER, or repeat rate — the metrics that actually matter here. That's the legitimate reason to write automation against the Marketing API. Rules for doing it safely:

- **System User token with the minimum scopes needed.** Never automate against a personal user token.
- **Read-heavy, write-light.** Compute the decision from reads; make the smallest possible write.
- **Exponential backoff on every error**, and batch writes rather than looping single calls.
- **Human-in-the-loop for anything that spends.** Automation can draft a change set and pause things; a budget increase should land in front of a person.
- **Throttle to human-plausible frequencies.** There is no reason for a management script to touch an account every minute.
- **Log every write** with its input data, so a bad decision is reconstructable.

## Account Safety

Automation is the most common way a working ad account gets restricted. The 2026 pattern:

- **Raw personal access tokens pointed at the Marketing API.** Use OAuth or an approved business-partner connector instead.
- **Bursty retry loops.** A failed call retried in a tight loop reads as bot activity regardless of intent. Back off.
- **Ungated write access.** Write scope that any script in the org can reach, with nothing gating what it changes.
- **Shared third-party developer apps.** Your account inherits the reputation of the app ID you run through.

Also: **Meta requires AI content to be labeled.** Since March 2026, undisclosed AI-generated creative is a leading rejection reason. If an ad's imagery or video is AI-generated, label it. This is a compliance requirement, not a preference, and it applies to every ad this suite helps you build.

## Common Mistakes

- Automating a decision you have never made manually. Run the rule as notify-only for two weeks first.
- Setting thresholds from a benchmark instead of the account's own Target CPA.
- Letting a rule act on today's data.
- Treating frequency or underspend as auto-pauseable.
- Automating your way around a creative supply problem. No rule produces a new concept.

## Related Skills

- **meta-ads-operating-system**: The Target CPA, kill, graduate and scale thresholds every rule here should encode. Rules automate that framework; they don't replace it.
- **meta-optimization-playbook**: The weekly manual cadence and the diagnosis order automation is meant to support.
- **creative-fatigue-detection**: What to do when the frequency watch fires — rotate, don't pause.
- **meta-api-reference**: Objects, fields and enums for anything written against the Marketing API.
- **full-audit**: The evidence-graded audit lane — 30 sections against live account data, where these benchmarks get tested rather than assumed.
