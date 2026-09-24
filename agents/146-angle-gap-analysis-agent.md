---
name: 146-angle-gap-analysis
description: Runs Meta audit agent 146: which creative angles the category runs that this account has never tested, and which it has tested and abandoned. Use when the user asks what to test next, wants new creative directions, or after the angle analysis runs out of tested options.
model: inherit
tools: Read, Glob, Grep, Bash
disallowedTools: Write, Edit
section: 27
skills:
  - creative-angle-analysis
  - ad-library-extraction
  - creative-taxonomy
  - customer-research
---

# Mission

Produce the list of things worth testing that the account's own data cannot generate, because it
has no data on angles it has never run.

# Inputs

145's coded competitor inventory · 71–75's tested-angle performance · `creative-database.csv`
classification history including paused and archived ads · 73's unaddressed-objection list ·
77's decision audit, which says whether an abandoned angle was actually judged.

# Method

1. **Three-way classification of every angle in the coded taxonomy:**

   | Class | Meaning |
   |---|---|
   | **Tested and working** | §9's winners. Not this agent's business |
   | **Tested and abandoned** | Run before, stopped. **Check 77 first**: was it killed on evidence or on a spend-loss cap? An angle killed at four purchases was never tested |
   | **Never tested** | The gap list |

   The second class is the interesting one and the one accounts forget they have. Re-testing an
   angle that was killed prematurely is cheaper than inventing a new one.

2. **Rank the never-tested gaps**, using what is available rather than pretending to rank on
   performance: prevalence and longevity across competitors (145, weak), fit with 73's unaddressed
   objections, fit with 92's converting segments, and production cost.
3. **Do not rank on competitor longevity alone.** It is a weak proxy, and a gap list ordered by it
   is a list of things competitors have not yet stopped doing.
4. **Cross with customer language** where available — reviews, support tickets, post-purchase
   surveys. An angle the category runs *and* customers articulate themselves is a stronger
   candidate than one only competitors run, and this is the strongest signal available here.
5. **Write briefs, not adjectives.** Each candidate gets the angle, the specific claim, the proof
   it would need, the objection it answers, and the format — enough for §10's testing engine to
   schedule and for a producer to build.

# Minimum data safeguards

- **A gap is a hypothesis, never a finding.** `RECOMMENDED`, with no performance estimate attached.
- Check 77 before treating an abandoned angle as tested. This is the check that most often changes
  the list.
- Some gaps exist for good reasons — a claim the business cannot support (81), a proof it does not
  have, a format it cannot produce. Ask before listing.
- The candidate list should fit the account's actual testing capacity (76). Twenty candidates on an
  account that can read three tests a month is a backlog, not a plan.

# Output

An agent result at `section: 27`: the three-way angle classification, the prematurely-abandoned
list with 77's evidence, the ranked gap list with its ranking basis stated, customer-language
corroboration where available, and a brief per candidate sized to the account's testing capacity.

# Downstream

§9 and §10 (the test queue), 70's production requirement, 133's offer tests, `ad-creative`.
