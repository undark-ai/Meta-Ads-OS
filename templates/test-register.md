# Test register

One row per test. A test without a kill number is a launch.

| Test | Type | Hypothesis | Variable | Baseline | Primary metric | Guardrail | Min sample | Kill number | Review date | Resets learning? | Result | Decision | Learning recorded? |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|

## Rules

- **One variable.** Two make the result unreadable, and the account paid for a test it cannot
  learn from.
- **Minimum sample in purchases, not clicks** (`learning-phase-and-significance`). Below the
  floor the decision is `INSUFFICIENT_DATA`.
- **Kill number agreed before the test runs.** Negotiated afterwards is how losers get one more
  week and winners get killed for being volatile.
- **Guardrail metric named.** A variant that lifts conversion 12% and drops AOV 15% lost money.
- **Learning-phase cost stated up front** where the change resets it — roughly a week of stable
  delivery.
- **`Learning recorded?` is the column that matters.** A result nobody wrote down gets re-tested
  next quarter, and the account pays for the same lesson twice.

## Decisions

`WIN` · `LOSE` · `INCONCLUSIVE` · `RUNNING` · `KILLED_EARLY`

`INCONCLUSIVE` is a legitimate outcome and must not be recorded as `LOSE`. An under-powered test
that could never have detected the effect is not evidence the change does not work — check the
minimum detectable effect before concluding anything (`cro-experiment-design`).
