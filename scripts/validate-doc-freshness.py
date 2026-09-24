#!/usr/bin/env python3
"""Does the README still describe the system, or has it decayed into counting it?

`validate-docs.py` checks the numbers. This checks something a count cannot: that the prose
still explains the concepts a reader needs, and that a concept named in one core doc has not
been silently dropped from the others.

A README that lists file counts and nothing else passes every mechanical check and tells a new
reader nothing about why the system is shaped the way it is.
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# Concepts this system cannot be understood without. Each must appear in the README, because
# a reader who misses one will misread every output the system produces.
README_CONCEPTS = {
    "the two lanes": r"audit lane|two lanes|Audit lane",
    "the write boundary": r"classified read or write|fail closed|read-only",
    "reconciliation before economics": r"[Rr]econcil\w+ (?:before|precedes)|before any economic conclusion",
    "gates that do not stop the sweep": r"never stop|does not end the audit|order the sweep",
    "the five coverage states": r"FINDINGS.*CLEAN.*DEGRADED",
    "modelled is not observed": r"modelled|PLATFORM_STATED",
    "blended MER on total spend": r"total\*{0,2} ad spend|blended MER",
    "never average a ratio": r"[Nn]ever average a ratio|component sums",
    "the volume floor": r"volume gates|purchase floor|INSUFFICIENT_DATA",
    "contribution not ROAS": r"[Cc]ontribution, not ROAS|are not profit",
    "the creative spine": r"creative-database\.csv|creative spine",
    "connector discovery": r"differs per account|discover tools before use|runtime",
}

# Concepts that must stay consistent across the core docs — a rule stated in one and dropped
# from another is how a library starts contradicting itself.
CROSS_DOC = {
    "EXECUTION-PROTOCOL.md": ["create.paused", "approval", "rollback", "change plan"],
    "AUTHORING.md": ["section", "sample floor|minimum data", "lane: execution"],
    "CLAUDE.md": ["30-section", "PLATFORM_STATED", "connector ladder", "coverage"],
}

MIN_PROSE_RATIO = 0.45  # a doc that is mostly tables and code has stopped explaining



def system_readme(root):
    """The document that describes *this system*.

    The README documents "copying in" as a supported install: clone the library into the project
    you want to audit. In that layout `README.md` describes the **host** project, not this system,
    and these checks would fail on a correct install — training operators to ignore validator
    output, which is exactly where the execution-boundary check lives.

    So prefer an explicit system doc when one is present. A vendored copy keeps
    `UPSTREAM-README.md` (or `docs/SYSTEM.md`) and its own `README.md`; upstream has only
    `README.md` and is unaffected.
    """
    for name in ("docs/SYSTEM.md", "UPSTREAM-README.md"):
        p = root / name
        if p.exists():
            return name, p.read_text()
    return "README.md", (root / "README.md").read_text()


def prose_ratio(text):
    lines = [l for l in text.split("\n") if l.strip()]
    if not lines:
        return 0.0
    structural = sum(1 for l in lines
                     if l.lstrip().startswith(("|", "```", "#", "-", "*", ">", "1.", "2."))
                     or l.startswith("    "))
    return 1 - (structural / len(lines))


def main():
    errors, warnings = [], []

    readme_name, readme = system_readme(ROOT)
    for concept, pattern in README_CONCEPTS.items():
        if not re.search(pattern, readme, re.S | re.I):
            errors.append(f"{readme_name}: no longer explains '{concept}'")

    for fname, patterns in CROSS_DOC.items():
        text = (ROOT / fname).read_text()
        for p in patterns:
            if not re.search(p, text, re.I):
                errors.append(f"{fname}: does not cover '{p}'")

    for fname in (readme_name, "CLAUDE.md", "EXECUTION-PROTOCOL.md", "AUTHORING.md"):
        text = (ROOT / fname).read_text()
        ratio = prose_ratio(text)
        if ratio < MIN_PROSE_RATIO:
            warnings.append(f"{fname}: {ratio:.0%} prose — mostly tables and lists; "
                            f"check it still explains rather than only enumerates")
        if len(text.split()) < 400:
            errors.append(f"{fname}: {len(text.split())} words — too thin to orient a reader")

    # A README that points at files which no longer exist misleads on the first click.
    for target in re.findall(r"\]\((?!https?:|#)([^)#]+)\)", readme):
        if not (ROOT / target).exists():
            errors.append(f"{readme_name}: links to '{target}', which does not exist")

    for w in warnings:
        print(f"WARN  {w}")
    for e in errors:
        print(f"FAIL  {e}")
    if errors:
        print(f"\n{len(errors)} freshness failure(s).")
        return 1
    print(f"OK  core docs still describe the system "
          f"({len(README_CONCEPTS)} concepts present, {len(warnings)} warning(s))")
    return 0


if __name__ == "__main__":
    sys.exit(main())
