#!/usr/bin/env python3
"""Documented counts against what is actually on disk.

A README count that has drifted quietly misdescribes the system, and because counts are the
first thing a reader trusts, a wrong one discredits the prose around it. The same drift in
SKILL-INDEX or the manifests sends an author to a layer that no longer holds what they expect.

This checks the numbers. `validate-doc-freshness.py` checks that the prose still describes the
system rather than only counting it.
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent



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


def frontmatter(text):
    m = re.match(r"\A---\n(.*?)\n---", text, re.S)
    return m.group(1) if m else ""


def actual():
    skills_dir = ROOT / ".claude" / "skills"
    skills = sorted(d.name for d in skills_dir.iterdir() if d.is_dir())
    execution = {s for s in skills
                 if "lane: execution" in frontmatter((skills_dir / s / "SKILL.md").read_text())}
    manifest = json.loads((ROOT / "orchestration" / "manifest.json").read_text())
    audit = set(manifest["audit_skills"])
    return {
        "skills": len(skills),
        "audit": len(audit),
        "execution": len(execution),
        "marketing": len(skills) - len(audit) - len(execution),
        "agents": len(list((ROOT / ".claude" / "agents").glob("*.md"))),
        "integrations": len(list((ROOT / "tools" / "integrations").glob("*.md"))),
        "schemas": len(list((ROOT / "schemas").glob("*"))),
        "workflows": len(list((ROOT / "workflows").glob("*.md"))),
        "sections": 30,
    }


def main():
    a = actual()
    errors = []

    readme_name, readme = system_readme(ROOT)
    claude_md = (ROOT / "CLAUDE.md").read_text()
    skill_index = (ROOT / "SKILL-INDEX.md").read_text()
    attribution = (ROOT / "ATTRIBUTION.md").read_text()
    license_text = (ROOT / "LICENSE").read_text()
    notices_path = ROOT / "THIRD_PARTY_NOTICES.md"
    notices = notices_path.read_text() if notices_path.exists() else ""

    # --- counts stated in prose and in the structure tree ----------------------
    checks = [
        (readme_name, readme, rf"\b{a['skills']} skills\b", f"{a['skills']} skills"),
        (readme_name, readme, rf"\*\*Audit\b.*?\|\s*{a['audit']}\s*\||Audit skills \({a['audit']}\)",
         f"audit layer count {a['audit']}"),
        ("SKILL-INDEX.md", skill_index, rf"\b{a['skills']} skills in three layers\b",
         f"{a['skills']} skills in three layers"),
        ("SKILL-INDEX.md", skill_index, rf"Audit layer \({a['audit']}\)", f"Audit layer ({a['audit']})"),
        ("SKILL-INDEX.md", skill_index, rf"Marketing layer \({a['marketing']}\)",
         f"Marketing layer ({a['marketing']})"),
        ("SKILL-INDEX.md", skill_index, rf"Execution layer \({a['execution']}\)",
         f"Execution layer ({a['execution']})"),
        ("CLAUDE.md", claude_md, rf"\b{a['sections']}-section framework\b",
         f"{a['sections']}-section framework"),
    ]
    for fname, text, pattern, human in checks:
        if not re.search(pattern, text, re.S):
            errors.append(f"{fname}: does not state '{human}' — count has drifted from disk")

    # --- the structure tree in README -----------------------------------------
    tree = re.search(r"```\n(\.claude/agents/.*?)```", readme, re.S)
    if not tree:
        errors.append(f"{readme_name}: no structure tree found")
    else:
        block = tree.group(1)
        for label, n in (("skills", a["skills"]), ("agents", a["agents"]),
                         ("schemas", a["schemas"]), ("workflows", a["workflows"])):
            if not re.search(rf"{n}\s+{label}|{n}\s+files", block):
                errors.append(f"{readme_name} structure tree: '{label}' does not show {n}")

    # --- manifests agree with disk and with each other --------------------------
    m = json.loads((ROOT / "orchestration" / "manifest.json").read_text())
    am = json.loads((ROOT / "agent-manifest.json").read_text())
    if m != am:
        errors.append("agent-manifest.json and orchestration/manifest.json have diverged")
    if m.get("skills") != a["skills"]:
        errors.append(f"manifest: skills={m.get('skills')}, disk has {a['skills']}")
    if m.get("agents") != a["agents"]:
        errors.append(f"manifest: agents={m.get('agents')}, disk has {a['agents']}")
    if m.get("sections") != a["sections"]:
        errors.append(f"manifest: sections={m.get('sections')}, framework has {a['sections']}")

    # every skill named in a manifest layer list must exist
    skills_on_disk = {d.name for d in (ROOT / ".claude" / "skills").iterdir() if d.is_dir()}
    for key in ("audit_skills", "marketing_skills", "execution_skills"):
        for name in m.get(key, []):
            if name not in skills_on_disk:
                errors.append(f"manifest {key}: '{name}' does not exist on disk")
    listed = {n for key in ("audit_skills", "marketing_skills", "execution_skills")
              for n in m.get(key, [])}
    missing = skills_on_disk - listed
    if missing:
        errors.append(f"manifest: {len(missing)} skill(s) on disk in no layer list: "
                      f"{sorted(missing)[:5]}")

    # --- third-party attribution agrees with the material on disk ---------------
    corey = re.search(
        r"### Corey Haines-derived directories \((\d+)\).*?directories.*?:\n\n"
        r"(.*?)\n\nThe audit-layer directory",
        attribution,
        re.S,
    )
    if not corey:
        errors.append("ATTRIBUTION.md: Corey Haines-derived directory list is missing")
    else:
        stated = int(corey.group(1))
        corey_skills = re.findall(r"`([a-z0-9-]+)`", corey.group(2))
        if len(corey_skills) != stated:
            errors.append(
                f"ATTRIBUTION.md: Corey heading says {stated}, list contains {len(corey_skills)}"
            )
        absent = [name for name in corey_skills if name not in skills_on_disk]
        if absent:
            errors.append(f"ATTRIBUTION.md: credited Corey skill(s) missing from disk: {absent}")
        wrong_layer = [name for name in corey_skills if name not in set(m["marketing_skills"])]
        if wrong_layer:
            errors.append(
                f"ATTRIBUTION.md: credited Corey skill(s) not in marketing layer: {wrong_layer}"
            )
        if not re.search(rf"the {stated} marketing-skill directories", license_text):
            errors.append(f"LICENSE: does not state the verified Corey skill count {stated}")

    required_notices = (
        "Copyright (c) 2025 Corey Haines",
        "Copyright (c) 2026 Swan",
        "Ivan Falco / Frontal",
    )
    for notice in required_notices:
        if notice not in license_text and notice not in notices:
            errors.append(f"third-party notices: missing '{notice}'")
    if not notices_path.exists():
        errors.append("THIRD_PARTY_NOTICES.md: file is missing")

    for e in errors:
        print(f"FAIL  {e}")
    if errors:
        print(f"\n{len(errors)} documentation drift(s).")
        return 1
    print(f"OK  docs agree with disk — {a['skills']} skills "
          f"({a['audit']} audit / {a['marketing']} marketing / {a['execution']} execution), "
          f"{a['agents']} agents, {a['sections']} sections")
    return 0


if __name__ == "__main__":
    sys.exit(main())
