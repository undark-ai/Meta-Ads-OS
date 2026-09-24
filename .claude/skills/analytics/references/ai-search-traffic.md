# Measuring AI Search Traffic

How to instrument and report traffic arriving from AI assistants, and how to join it to Search Console so organic and AI search sit in one view.

This is the tracking half. For what the numbers mean and how to measure whether a brand appears in AI answers at all, see the **ai-seo** skill's [GEO measurement reference](../../ai-seo/references/geo-measurement.md).

**The framing that keeps this honest:** referral clicks are not citations. A citation is the brand appearing as a source in an answer, and most citations produce no click — the user got their answer and left. Referral traffic requires a citation *and* a click, so it undercounts AI influence severely. Instrument it anyway; it's cheap, continuous, and it's the only AI signal that lands in analytics on its own. Just never report it as citation share.

---

## Why it needs configuring at all

Out of the box, GA4 files AI assistant traffic under Referral, scattered across a dozen hostnames, mixed in with genuine referral traffic from blogs and newsletters. Nobody looks at Referral. So a channel that may be a meaningful share of acquisition shows up as noise.

The fix is a source list and a channel group.

## The AI source list

Hostnames that appear as `session_source` / `page_referrer` for AI assistant traffic. Maintain this as a list you update — new engines and new hostnames appear regularly, and a stale list silently under-reports.

| Engine | Hostnames |
|--------|-----------|
| ChatGPT | `chatgpt.com`, `chat.openai.com` |
| Perplexity | `perplexity.ai`, `www.perplexity.ai` |
| Google Gemini | `gemini.google.com`, `bard.google.com` |
| Claude | `claude.ai` |
| Microsoft Copilot | `copilot.microsoft.com`, `bing.com/chat` |
| Others to watch | `you.com`, `phind.com`, `poe.com`, `grok.com`, `deepseek.com`, `mistral.ai` |

**Match on both exact hostnames and a substring pattern.** Exact matches keep the buckets clean; a substring fallback (`LIKE '%perplexity%'`) catches subdomains and regional variants you haven't enumerated. Report anything caught only by the fallback so you can add it to the exact list.

**Notable exclusions:** `google.com` and `bing.com` are traditional search even when the visit was influenced by an AI Overview — AI Overviews send traffic under the normal organic search source, and there is **no way to separate AI Overview clicks from ordinary organic clicks** in GA4 or Search Console. Don't invent a split. Say it isn't measurable, and use Search Console's overall impression-to-click ratio trend as the indirect signal instead.

## GA4 setup

**Custom channel group.** Admin → Data display → Channel groups → create a custom group with an "AI Search" channel defined as `Session source` matches regex against the hostname list. Place it above Referral in the ordering so it captures before Referral does. Custom channel groups apply retroactively to standard reports, which is why this is worth doing before anything else.

**Comparison segment.** Also build it as a comparison so you can slice any standard report by AI Search versus Organic Search without leaving the report.

**What to look at once it exists:** sessions, engagement rate, conversions, and revenue per session by engine. AI traffic frequently converts at a different rate from ordinary organic — often higher, because the assistant has already done the qualification — and that difference is the number worth reporting.

**Landing pages.** Which pages AI assistants send people to is the single most useful AI report you can build. It tells you which content is being cited in practice, which is the closest analytics gets to a citation signal.

## Warehouse queries

For a joined organic + AI view, the GA4 BigQuery export and a Search Console export are the two tables you need. These patterns hold on any SQL warehouse.

### Bucket AI versus traditional search

The split the whole report rests on:

```sql
CASE
  WHEN session_source IN ('chatgpt.com','chat.openai.com','perplexity.ai',
                          'gemini.google.com','claude.ai','copilot.microsoft.com')
    THEN 'AI'
  WHEN session_source IN ('google','bing','yahoo','duckduckgo',
                          'ecosia.org','search.brave.com')
    THEN 'Traditional'
  WHEN session_source LIKE '%perplexity%' OR session_source LIKE '%chatgpt%'
    THEN 'AI'
  WHEN session_source LIKE '%yahoo%'
    THEN 'Traditional'
  ELSE NULL
END AS bucket
```

`NULL` for everything else, deliberately — an `ELSE 'Other'` bucket that quietly collects direct, email, and paid traffic will be read as search traffic by whoever sees the chart.

### Current versus previous period in one query

Avoid two round-trips and an off-by-one on the comparison window. Shift the window back by `(end - start + 1)` days and tag rows:

```sql
SELECT
  CASE WHEN date >= DATE(@start_date) THEN 'current' ELSE 'previous' END AS period,
  SUM(sessions) AS sessions
FROM sessions_table
WHERE session_medium = 'organic'
  AND date >= DATE(@start_date) - (DATE(@end_date) - DATE(@start_date) + 1)
  AND date <= DATE(@end_date)
GROUP BY period
```

### Weighted average position

`AVG(position)` is wrong. It treats a query with 1 impression the same as one with 10,000, so it drifts with long-tail noise and moves for reasons nobody can explain:

```sql
SUM(position * impressions) / NULLIF(SUM(impressions), 0) AS avg_position
```

Use impression-weighting for every rate metric built from Search Console — position, CTR by group, anything averaged across queries.

### Top N per group

For "top landing pages within each bucket" without a window function, ClickHouse offers `LIMIT n BY dimension`. On BigQuery or Postgres use `ROW_NUMBER() OVER (PARTITION BY bucket ORDER BY sessions DESC)` and filter.

### Keep response sizes down

Daily granularity × every dimension over a long window overflows most API limits. Pre-filter dimensions in a CTE, then join:

```sql
WITH top_sources AS (
  SELECT session_source FROM sessions_table
  WHERE date BETWEEN @start_date AND @end_date
  GROUP BY session_source ORDER BY SUM(sessions) DESC LIMIT 12
)
SELECT date, session_source, SUM(sessions) AS sessions
FROM sessions_table
WHERE session_source IN (SELECT session_source FROM top_sources)
  AND date BETWEEN @start_date AND @end_date
GROUP BY date, session_source
```

---

## Reporting patterns that hold up

- **Lead with the plain-English insight, not the chart.** "AI engines sent 12.1K sessions — 8.1% of organic search traffic, up 318% on the prior 180 days" does more work than any visualization above it.
- **Current versus previous on every time series** — solid line for current, dashed grey for previous. A single line with no baseline invites a story that isn't there.
- **Report per engine, not one blended AI number.** ChatGPT and Perplexity behave differently enough that an average describes neither.
- **Absolute *and* share.** "8.1% of organic" is the number that survives a traffic-wide swing; the absolute alone doesn't.
- **State the window and state what's excluded.** Especially that AI Overview clicks are inside the traditional organic number and can't be separated out.

---

## Gotchas

| Symptom | Cause | Fix |
|---------|-------|-----|
| AI traffic looks like nothing | It's spread across Referral under a dozen hostnames | Build the custom channel group |
| A new engine's traffic missing | Hostname not on the list | Substring fallback plus a quarterly list review |
| Bounce rate per landing page, filtered by source, is unavailable | The GA4 export splits the source dimension from page-engagement metrics | Report top pages overall, or top AI landing pages with sessions only |
| No demographic breakdown | Demographic detail not enabled on the property | Use device / browser / OS instead — always available |
| Aggregate function nested inside another | Alias collision: `SUM(impressions) AS impressions` then dividing by `SUM(impressions)` | Rename the outer alias (`total_impressions`) |
| Rate metric returns NULL | `NULLIF` denominator hit zero | Correct behavior — handle it in presentation, not by removing the guard |
| Overlap analysis comes back empty | Joined on bid keywords instead of search terms | Use the search-terms report |
| AI referral numbers look implausibly low | They are. Most citations never produce a click. | Report it as referral traffic, not as citation share |

---

## What not to do

- **Don't report AI referral traffic as AI visibility.** It's a floor, not a measure.
- **Don't invent an AI Overview split.** It isn't measurable. Saying so is the correct answer.
- **Don't average positions unweighted.**
- **Don't pause paid terms off an overlap query.** Candidate list, then a holdout test.
- **Don't put a signed embed or API token in client-side code.** If a dashboard reads a warehouse, the credential stays server-side behind a proxy route. A URL with a bearer token in it reads the data for anyone who has the URL, until it's revoked.
- **Don't let the list go stale.** New engines appear; unmaintained regex silently under-reports and the trend line lies.

> **Removed on vendoring:** the paid/organic search-term overlap analysis that stood here was built on Google Ads search-term data. Meta has no search terms, so it could not run against this repository's only ad platform. See `ATTRIBUTION.md`.
