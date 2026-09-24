#!/usr/bin/env python3
"""Check the section-ownership map against the agents' own frontmatter.

This class of defect has bitten twice. Both times the map in full-audit/SKILL.md used a
*range* that quietly overlapped a neighbouring section's range, so two sections claimed the
same agents and nobody could tell which owned them. The first time it surfaced as three
post-click agents mapped to a section that had no room for them; the second time as sixteen
agents double-claimed across seven section pairs.

The agents' frontmatter is authoritative — validate-agent-library.sh already requires a
`section:` on every agent, and the orchestrator runs sections, not ranges. So the map is a
derived view, and a derived view that drifts from its source is worse than no view: it reads
as authoritative and is not.

Checks, against .claude/skills/full-audit/SKILL.md and workflows/02-full-account-audit.md:
  1. every agent's declared section appears in that section's row
  2. no row claims an agent that declares a different section
  3. no agent is claimed by more than one row
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
FULL_AUDIT = ROOT / ".claude" / "skills" / "full-audit" / "SKILL.md"
WORKFLOW = ROOT / "workflows" / "02-full-account-audit.md"


def declared_sections():
    """agent number -> section, from frontmatter only."""
    out = {}
    for path in sorted((ROOT / ".claude" / "agents").glob("*.md")):
        num = re.match(r"(\d+)-", path.name)
        if not num:
            continue
        m = re.search(r"^section: *(\d+)", path.read_text(), re.M)
        if m:
            out[int(num.group(1))] = int(m.group(1))
    return out


def parse_cell(cell):
    """Expand '43–46, 50' and '**59**, **60**, 61–64' into a set of agent numbers."""
    text = cell.replace("**", "")
    found = set()
    for r in re.finditer(r"(\d{1,3})\s*[–-]\s*(\d{1,3})", text):
        lo, hi = int(r.group(1)), int(r.group(2))
        if 0 < lo <= hi <= 213:
            found.update(range(lo, hi + 1))
    for r in re.finditer(r"\b(\d{1,3})\b", re.sub(r"\d{1,3}\s*[–-]\s*\d{1,3}", "", text)):
        v = int(r.group(1))
        if 0 <= v <= 213:
            found.add(v)
    return found


def claimed(path, agents_col):
    """section -> set of agent numbers the map claims for it."""
    out = {}
    for line in path.read_text().splitlines():
        cells = [c.strip() for c in line.split("|")[1:-1]]
        if len(cells) <= agents_col or not cells[0].isdigit():
            continue
        sec = int(cells[0])
        if 1 <= sec <= 30:
            out[sec] = parse_cell(cells[agents_col])
    return out


def check(path, agents_col, declared, errors):
    rel = path.relative_to(ROOT)
    if not path.exists():
        errors.append(f"{rel}: missing")
        return
    rows = claimed(path, agents_col)
    if len(rows) != 30:
        errors.append(f"{rel}: parsed {len(rows)} section rows, expected 30")

    seen = {}
    for sec, nums in sorted(rows.items()):
        for n in sorted(nums):
            if n not in declared:
                continue  # a number that is not an agent — prose, a threshold
            if declared[n] != sec:
                errors.append(
                    f"{rel} §{sec}: claims agent {n}, which declares section {declared[n]}"
                )
            if n in seen and seen[n] != sec:
                errors.append(f"{rel}: agent {n} claimed by both §{seen[n]} and §{sec}")
            seen[n] = sec

    for num, sec in sorted(declared.items()):
        if sec == 0:
            continue  # orchestration and execution agents own no audit section
        if num not in rows.get(sec, set()):
            errors.append(f"{rel} §{sec}: agent {num} declares this section but the row omits it")


def main():
    declared = declared_sections()
    if not declared:
        print("FAIL: no agents parsed")
        return 1

    errors = []
    check(FULL_AUDIT, 2, declared, errors)
    check(WORKFLOW, 3, declared, errors)

    for e in errors:
        print(f"FAIL  {e}")
    if errors:
        print(f"\n{len(errors)} section-map drift(s).")
        return 1

    mapped = sum(1 for s in declared.values() if s)
    print(f"OK  section map agrees with frontmatter — {mapped} agents across 30 sections, "
          f"{len(declared) - mapped} unsectioned (orchestration and execution)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
