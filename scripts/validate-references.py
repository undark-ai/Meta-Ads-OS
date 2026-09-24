#!/usr/bin/env python3
"""Skill names, cross-references, and agent-to-skill resolution.

Two failures this catches, both invisible by inspection:
  - an agent declaring a skill that does not exist — it silently loads nothing
  - a "see <skill>" pointer to a skill that was removed or never carried, which misleads
    routing at trigger time and sends a reader somewhere that isn't there
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILLS_DIR = ROOT / ".claude" / "skills"
AGENTS_DIR = ROOT / ".claude" / "agents"

FRONTMATTER_RE = re.compile(r"\A---\n(.*?)\n---", re.S)
SEE_RE = re.compile(r"\bsee ([a-z0-9]+(?:-[a-z0-9]+)+)\b")

# Prose that happens to look like a hyphenated skill name.
NOT_SKILL_NAMES = {
    "new-customer", "break-even", "post-click", "first-party", "third-party",
    "value-based", "view-through", "one-pager", "day-to-day", "add-to-cart",
    "cost-per-acquisition", "click-through", "in-app",
}


def frontmatter(text):
    m = FRONTMATTER_RE.match(text)
    return m.group(1) if m else ""


def declared_skills(fm):
    """Parse the `skills:` list from an agent's frontmatter."""
    out, in_list = [], False
    for line in fm.split("\n"):
        if line.startswith("skills:"):
            in_list = True
            continue
        if in_list:
            m = re.match(r"^\s+-\s+([a-z0-9-]+)\s*$", line)
            if m:
                out.append(m.group(1))
            elif line.strip() and not line.startswith(" "):
                break
    return out


def main():
    skills = {d.name for d in SKILLS_DIR.iterdir() if d.is_dir()}
    errors = []

    # --- agent -> skill resolution --------------------------------------------
    checked = 0
    for path in sorted(AGENTS_DIR.glob("*.md")):
        for skill in declared_skills(frontmatter(path.read_text())):
            checked += 1
            if skill not in skills:
                errors.append(f"{path.relative_to(ROOT)}: declares skill '{skill}', "
                              f"which does not exist in .claude/skills/")

    # --- cross-references between skills --------------------------------------
    refs = 0
    for path in sorted(SKILLS_DIR.glob("*/**/*.md")):
        text = path.read_text()
        for ref in set(SEE_RE.findall(text)):
            if ref in NOT_SKILL_NAMES or ref in skills:
                continue
            # Only flag names that plausibly are skill pointers: the repo's own skills all
            # appear elsewhere, so an unknown hyphenated name after "see" is a dead pointer.
            refs += 1
            errors.append(f"{path.relative_to(ROOT)}: 'see {ref}' does not resolve to a skill")

    # --- internal file links ---------------------------------------------------
    link_re = re.compile(r"\]\((?!https?:|#|mailto:)([^)#]+)")
    for path in sorted(ROOT.glob("*.md")) + sorted((ROOT / "workflows").glob("*.md")):
        for target in link_re.findall(path.read_text()):
            resolved = (path.parent / target).resolve()
            if not resolved.exists():
                errors.append(f"{path.relative_to(ROOT)}: link to '{target}' does not exist")

    for e in errors:
        print(f"FAIL  {e}")
    if errors:
        print(f"\n{len(errors)} unresolved reference(s).")
        return 1
    print(f"OK  {len(skills)} skills; {checked} agent skill declarations resolve; "
          f"cross-references and internal links intact")
    return 0


if __name__ == "__main__":
    sys.exit(main())
