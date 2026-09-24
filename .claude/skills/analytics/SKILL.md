---
name: analytics
description: When the user wants to set up, improve, or audit analytics tracking and measurement. Also use when the user mentions "set up tracking," "GA4," "Google Analytics," "conversion tracking," "event tracking," "UTM parameters," "tag manager," "GTM," "analytics implementation," "tracking plan," "how do I measure this," "track conversions," "attribution," "Mixpanel," "Segment," "are my events firing," "analytics isn't working," "AI traffic," "ChatGPT referral traffic," "Perplexity traffic," "how much traffic is AI sending us," or "track AI search traffic." Use this whenever someone asks how to know if something is working or wants to measure marketing results. For A/B test measurement, see ab-testing. For a scored go/no-go on whether paid spend can be measured at all before scaling it, see paid-measurement-readiness. For Meta-specific attribution reconciliation and incrementality, see meta-attribution.
metadata:
 version: 2.2.0
---

> **Marketing layer — advisory, not evidence.** Every benchmark, threshold and rule of thumb
> below is build-time guidance. Per `CLAUDE.md`, a marketing skill's number is never evidence
> for a quantified finding: a recommendation that originates here still needs a number, source,
> date range, formula, evidence class and confidence from the audit layer before it can be
> presented as one. Handoffs run audit → marketing, never the reverse.


# Analytics Tracking

You are an expert in analytics implementation and measurement. Your goal is to help set up tracking that provides actionable insights for marketing and product decisions.

## Initial Assessment

**Check for product marketing context first:**
If `.agents/product-marketing.md` exists (or `.claude/product-marketing.md`, or the legacy `product-marketing-context.md` filename, in older setups), read it before asking questions. Use that context and only ask for information not already covered or specific to this task.

Before implementing tracking, understand:

1. **Business Context** - What decisions will this data inform? What are key conversions?
2. **Current State** - What tracking exists? What tools are in use?
3. **Technical Context** - What's the tech stack? Any privacy/compliance requirements?

---

## Core Principles

### 1. Track for Decisions, Not Data
- Every event should inform a decision
- Avoid vanity metrics
- Quality > quantity of events

### 2. Start with the Questions
- What do you need to know?
- What actions will you take based on this data?
- Work backwards to what you need to track

### 3. Name Things Consistently
- Naming conventions matter
- Establish patterns before implementing
- Document everything

### 4. Maintain Data Quality
- Validate implementation
- Monitor for issues
- Clean data > more data

---

## Tracking Plan Framework

### Structure

```
Event Name | Category | Properties | Trigger | Notes
---------- | -------- | ---------- | ------- | -----
```

### Event Types

| Type | Examples |
|------|----------|
| Pageviews | Automatic, enhanced with metadata |
| User Actions | Button clicks, form submissions, feature usage |
| System Events | Signup completed, purchase, subscription changed |
| Custom Conversions | Goal completions, funnel stages |

**For comprehensive event lists**: See [references/event-library.md](references/event-library.md)

---

## Event Naming Conventions

### Recommended Format: Object-Action

```
signup_completed
button_clicked
form_submitted
article_read
checkout_payment_completed
```

### Best Practices
- Lowercase with underscores
- Be specific: `cta_hero_clicked` vs. `button_clicked`
- Include context in properties, not event name
- Avoid spaces and special characters
- Document decisions

---

## Essential Events

### Marketing Site

| Event | Properties |
|-------|------------|
| cta_clicked | button_text, location |
| form_submitted | form_type |
| signup_completed | method, source |
| demo_requested | - |

### Product/App

| Event | Properties |
|-------|------------|
| onboarding_step_completed | step_number, step_name |
| feature_used | feature_name |
| purchase_completed | plan, value |
| subscription_cancelled | reason |

**For full event library by business type**: See [references/event-library.md](references/event-library.md)

---

## Event Properties

### Standard Properties

| Category | Properties |
|----------|------------|
| Page | page_title, page_location, page_referrer |
| User | user_id, user_type, account_id, plan_type |
| Campaign | source, medium, campaign, content, term |
| Product | product_id, product_name, category, price |

### Best Practices
- Use consistent property names
- Include relevant context
- Don't duplicate automatic properties
- Avoid PII in properties

---

## GA4 Implementation

### Quick Setup

1. Create GA4 property and data stream
2. Install gtag.js or GTM
3. Enable enhanced measurement
4. Configure custom events
5. Mark conversions in Admin

### Custom Event Example

```javascript
gtag('event', 'signup_completed', {
 'method': 'email',
 'plan': 'free'
});
```

**For detailed GA4 implementation**: See [references/ga4-implementation.md](references/ga4-implementation.md)

---

## Google Tag Manager

### Container Structure

| Component | Purpose |
|-----------|---------|
| Tags | Code that executes (GA4, pixels) |
| Triggers | When tags fire (page view, click) |
| Variables | Dynamic values (click text, data layer) |

### Data Layer Pattern

```javascript
dataLayer.push({
 'event': 'form_submitted',
 'form_name': 'contact',
 'form_location': 'footer'
});
```

**For detailed GTM implementation**: See [references/gtm-implementation.md](references/gtm-implementation.md)

---

## UTM Parameter Strategy

### Standard Parameters

| Parameter | Purpose | Example |
|-----------|---------|---------|
| utm_source | Traffic source | google, newsletter |
| utm_medium | Marketing medium | cpc, email, social |
| utm_campaign | Campaign name | spring_sale |
| utm_content | Differentiate versions | hero_cta |
| utm_term | Paid search keywords | running+shoes |

### Naming Conventions
- Lowercase everything
- Use underscores or hyphens consistently
- Be specific but concise: `blog_footer_cta`, not `cta1`
- Document all UTMs in a spreadsheet

### Meta Dynamic URL Parameters

Meta can write its own object names into the UTM string, so you never hand-tag an ad. Set this once in the ad account's default **URL Parameters** field and every new ad inherits it.

| Token | Resolves to |
|---|---|
| `{{campaign.name}}` / `{{campaign.id}}` | Campaign name / ID |
| `{{adset.name}}` / `{{adset.id}}` | Ad set name / ID |
| `{{ad.name}}` / `{{ad.id}}` | Ad name / ID |
| `{{placement}}` | The specific placement served |
| `{{site_source_name}}` | `fb`, `ig`, `an` or `msg` |

```
utm_source={{site_source_name}}
utm_medium=paid_social
utm_campaign={{campaign.name}}
utm_content={{ad.name}}
utm_term={{adset.name}}|{{placement}}
```

**Use `utm_medium=paid_social`, not `cpc`.** `cpc` is a Google Ads convention; on a social platform it tells you nothing and breaks channel grouping.

**Why Meta traffic shows up as "Organic Social" or "Unassigned" in GA4.** GA4 assigns Paid Social only when `utm_medium` matches a paid pattern (`cpc`, `ppc`, `paid`, `paid_social`, and similar) **and** `utm_source` matches a recognized social platform. Miss either condition and the session falls back to Organic Social — or to Unassigned if the source isn't recognized at all. This is the single most common reason a brand's GA4 shows almost no paid social traffic while Ads Manager reports thousands of clicks.

**The naming convention is the taxonomy.** Because ad, ad set and campaign names flow into the string, a sloppy ad name becomes a `utm_content` value you cannot group on, permanently — you cannot retag history. See **meta-campaign-structure** for the three-level convention.

**QA checklist:** confirm the parameters land on the real destination URL field, not a display link; click a live ad and read the resolved URL; check that names containing spaces or special characters encode cleanly; and verify the GA4 channel group before trusting a report.

---

## Choosing a Proxy Metric

When the outcome you care about is too slow to optimize on — repeat rate, LTV, payback — you optimize on a proxy. A proxy worth using is:

1. **Measurable** — you can pull it today, without a project.
2. **Moveable** — something the team can actually influence.
3. **Not an average** — averages hide the distribution that matters. Use a rate or a count.
4. **Correlated** — demonstrably tracks the real outcome in *your* data, not in a case study.
5. **Explicit about new vs. existing** — a metric that blends first-time and repeat customers will move for reasons unrelated to what you changed.
6. **Hard to game** — if the team can hit it without producing the outcome, they eventually will.

Template: *"the percentage of new customers who [specific action] within [window]."* For example: the share of new customers placing a second order within 60 days. If the proxy improves and the real outcome doesn't, the proxy is broken — replace it rather than defending it.

## AI Search Traffic

Traffic from AI assistants (ChatGPT, Perplexity, Gemini, Claude, Copilot) lands in GA4 as Referral by default, scattered across a dozen hostnames and mixed in with newsletter and blog referrals. Nobody looks at Referral, so a channel that may be a meaningful share of acquisition reads as noise.

The fix is a maintained source list plus a custom channel group that captures above Referral — and it applies retroactively to standard reports, so it's worth doing before anything else.

Two things to get right before reporting any of it:

- **Referral clicks are not citations.** Most AI citations produce no click at all; referral traffic requires a citation *and* a click, so it undercounts AI influence severely. Report it as referral traffic, never as citation share or "AI visibility."
- **AI Overview clicks cannot be separated from ordinary organic clicks.** They arrive under the normal `google` organic source in both GA4 and Search Console. There is no split to build. Saying it isn't measurable is the correct answer.

For the hostname list, the GA4 channel-group setup, warehouse query patterns (AI-vs-traditional bucketing, impression-weighted average position, current-vs-previous windows, paid/organic overlap), reporting patterns, and the common gotchas, see [references/ai-search-traffic.md](references/ai-search-traffic.md).

For measuring whether the brand appears in AI answers at all — which analytics cannot tell you — see the **ai-seo** skill.

---

## Debugging and Validation

### Testing Tools

| Tool | Use For |
|------|---------|
| GA4 DebugView | Real-time event monitoring |
| GTM Preview Mode | Test triggers before publish |
| Browser Extensions | Tag Assistant, dataLayer Inspector |

### Validation Checklist

- [ ] Events firing on correct triggers
- [ ] Property values populating correctly
- [ ] No duplicate events
- [ ] Works across browsers and mobile
- [ ] Conversions recorded correctly
- [ ] No PII leaking

### Common Issues

| Issue | Check |
|-------|-------|
| Events not firing | Trigger config, GTM loaded |
| Wrong values | Variable path, data layer structure |
| Duplicate events | Multiple containers, trigger firing twice |

---

## Privacy and Compliance

### Considerations
- Cookie consent required in EU/UK/CA
- No PII in analytics properties
- Data retention settings
- User deletion capabilities

### Implementation
- Use consent mode (wait for consent)
- IP anonymization
- Only collect what you need
- Integrate with consent management platform

---

## Output Format

### Tracking Plan Document

```markdown
# [Site/Product] Tracking Plan

## Overview
- Tools: GA4, GTM
- Last updated: [Date]

## Events

| Event Name | Description | Properties | Trigger |
|------------|-------------|------------|---------|
| signup_completed | User completes signup | method, plan | Success page |

## Custom Dimensions

| Name | Scope | Parameter |
|------|-------|-----------|
| user_type | User | user_type |

## Conversions

| Conversion | Event | Counting |
|------------|-------|----------|
| Signup | signup_completed | Once per session |
```

---

## Task-Specific Questions

1. What tools are you using (GA4, Mixpanel, etc.)?
2. What key actions do you want to track?
3. What decisions will this data inform?
4. Who implements - dev team or marketing?
5. Are there privacy/consent requirements?
6. What's already tracked?

---

## Tool Integrations

For implementation, see the [tools registry](../../tools/REGISTRY.md). Key analytics tools:

| Tool | Best For | MCP | Guide |
|------|----------|:---:|-------|
| **GA4** | Web analytics, Google ecosystem | ✓ | [ga4.md](../../tools/integrations/ga4.md) |
| **Mixpanel** | Product analytics, event tracking | - | [mixpanel.md](../../tools/integrations/mixpanel.md) |
| **Amplitude** | Product analytics, cohort analysis | - | [amplitude.md](../../tools/integrations/amplitude.md) |
| **PostHog** | Open-source analytics, session replay | - | [posthog.md](../../tools/integrations/posthog.md) |
| **Segment** | Customer data platform, routing | - | [segment.md](../../tools/integrations/segment.md) |

---

## Related Skills

- **ab-testing**: For experiment tracking
- **seo-audit**: For organic traffic analysis
- **cro**: For conversion optimization (uses this data)
- **checkout-cro**: For the e-commerce checkout event spec and funnel segmentation
- **revops**: For pipeline metrics, CRM tracking, and revenue attribution
- **ai-seo**: For whether the brand appears in AI answers at all — referral traffic is a floor, not a measure
- **google-ads-team**: For the PPC/SEO overlap framework the paid/organic overlap query feeds
