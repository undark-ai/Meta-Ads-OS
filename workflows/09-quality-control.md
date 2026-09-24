# Quality control

Reviews the library, not an account. Run before a release, and after adding agents or skills.

## Sequence

| Step | What |
|---|---|
| 1 | Run every validator in `scripts/` and read the output |
| 2 | Run `00-agent-quality-controller` for the judgement pass the validators cannot do |
| 3 | Fix `CRITICAL` and `HIGH` findings before the release; triage the rest |

## What the validators catch

Mechanical failures that are invisible by inspection: a skill whose frontmatter `name` does not
match its directory silently fails to load; a pointer to a removed skill misleads routing at
trigger time; a README count that has drifted from disk quietly misdescribes the system.

```bash
python3 scripts/validate-references.py          # skill names, links, agent→skill resolution
bash    scripts/validate-agent-library.sh       # frontmatter, name↔filename, uniqueness, sections
bash    scripts/validate-skills.sh              # spec compliance, line limits, descriptions
python3 scripts/validate-docs.py                # README tree and counts vs disk
python3 scripts/validate-execution-boundary.py  # no audit agent references a write tool
python3 scripts/audit-cli-writes.py --check     # tools/clis mutation surface still documented
python3 scripts/validate-doc-freshness.py       # README describes the system, not just counts it
```

## What only the review catches

- An agent with a plausible method and **no sample floor** — it will produce confident nonsense on
  thin data, and Meta's ad-level purchase counts make that the common case rather than the edge
  case
- An agent that recomputes contribution margin instead of consuming §1's
- A findings template that invites a fabricated currency value
- Two agents computing the same thing from different inputs — they will disagree inside one
  report, which is the failure that costs an audit its credibility
- An agent mapped to no section, which will never run while looking present
- An execution agent whose body does not actually address approval, preview, create-paused,
  logging and rollback

## Release gate

No release with an open `CRITICAL`. A `CRITICAL` here means the library will produce a wrong
number or breach the execution boundary — both are worse than shipping late.
