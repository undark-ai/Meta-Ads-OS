#!/usr/bin/env python3
"""Enforce the audit/execution boundary.

The Google Ads MCP is read-only, so Google-Ads-OS's safety story is "we have no hands". The
Meta connector has write tools, so this repository needs the boundary enforced rather than
asserted. This script is that enforcement.

Fails the build when:
  - an audit agent (00-199) or an audit/marketing skill references a tool classified `write`
  - an execution agent (200+) is missing `lane: execution`, or does not load the protocol
  - any file references a Meta tool the classification file has never seen

Unclassified tools are treated as writes. Fail closed: if Meta ships a tool this repository
has not seen, the audit lane refuses it until a human has looked at what it does.

Some files legitimately NAME a write tool without calling it — the protocol itself, the
authoring guide, reference skills that document the API surface. Rather than a blanket
exemption, such a file must carry the marker below. It is greppable, auditable, and forces a
deliberate choice, which a hardcoded allowlist does not.
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CLASSIFICATION = ROOT / "schemas" / "meta-mcp-tool-classification.yaml"

DOCUMENTS_WRITES = "execution-boundary: documents-writes"
EXECUTION_LANE = "lane: execution"
PROTOCOL_SKILL = "meta-execution-protocol"

TOOL_RE = re.compile(r"\bads_[a-z0-9_]+\b")
FRONTMATTER_RE = re.compile(r"\A---\n(.*?)\n---", re.S)
# An entry may carry a trailing comment. Matching to end-of-line dropped those silently,
# which made classified tools look unknown — the failure this comment exists to prevent.
ENTRY_RE = re.compile(r"^\s+-\s+(ads_[a-z0-9_]+)\s*(?:#.*)?$")


def frontmatter(text):
    """Return the YAML frontmatter block, or empty string.

    Lane must be read from frontmatter, never from the body: an agent that *describes* the
    boundary rule — the quality controller does exactly that — would otherwise be flagged as
    declaring itself an execution agent.
    """
    m = FRONTMATTER_RE.match(text)
    return m.group(1) if m else ""


def load_classification():
    """Parse the read/write/retired lists without requiring PyYAML."""
    buckets = {"read": set(), "write": set(), "retired": set()}
    section = None
    for line in CLASSIFICATION.read_text().splitlines():
        stripped = line.strip()
        if stripped[:-1] in buckets and stripped.endswith(":"):
            section = stripped[:-1]
            continue
        if stripped and not line.startswith((" ", "\t")) and stripped.endswith(":"):
            section = None
            continue
        m = ENTRY_RE.match(line)
        if m and section:
            buckets[section].add(m.group(1))
    return buckets["read"], buckets["write"], buckets["retired"]


def scan(path, known, write_tools, retired, may_name_writes, errors):
    """Check one file's Meta tool references against its lane."""
    text = path.read_text()
    rel = path.relative_to(ROOT)
    found = set(TOOL_RE.findall(text))

    # A retired name gets its own message: the fix is to find the current tool, not to
    # classify the old one. Files that document the tool surface may name them; nothing else may.
    named_retired = found & retired
    if named_retired and not may_name_writes:
        errors.append(f"{rel}: references Meta tool(s) marked retired {sorted(named_retired)} — "
                      f"this repo believes these are superseded; verify against the live connector, "
                      f"then use the current name")

    # A file that documents the tool surface may name an unclassified tool for the same reason it
    # may name a write or a retired one: reporting the gap is how the gap gets closed. Without this
    # exemption FIELD-NOTES cannot record a newly-appeared tool until someone has already
    # classified it, which is backwards.
    unknown = found - known - retired
    if unknown and not may_name_writes:
        errors.append(f"{rel}: references Meta tool(s) absent from the classification: "
                      f"{sorted(unknown)} — classify them, or fix the reference")

    if not may_name_writes:
        writes = found & write_tools
        if writes:
            errors.append(f"{rel}: references write tool(s) {sorted(writes)} without the "
                          f"'{DOCUMENTS_WRITES}' marker")


def main():
    if not CLASSIFICATION.exists():
        print(f"FAIL: {CLASSIFICATION} not found")
        return 1

    read_tools, write_tools, retired_tools = load_classification()
    known = read_tools | write_tools
    if not write_tools or not read_tools:
        print("FAIL: classification file parsed no read or no write tools — check its format")
        return 1

    errors, marked = [], []

    # --- agents ----------------------------------------------------------------
    for path in sorted((ROOT / "agents").glob("*.md")):
        text = path.read_text()
        rel = path.relative_to(ROOT)
        num_match = re.match(r"^(\d+)-", path.name)
        if not num_match:
            errors.append(f"{rel}: filename does not start with an agent number")
            continue
        num = int(num_match.group(1))
        is_execution = EXECUTION_LANE in frontmatter(text)

        if num >= 200 and not is_execution:
            errors.append(f"{rel}: agent {num} is in the execution range but lacks "
                          f"'{EXECUTION_LANE}'")
        if num < 200 and is_execution:
            errors.append(f"{rel}: declares '{EXECUTION_LANE}' but is numbered in the audit range")
        if is_execution and PROTOCOL_SKILL not in text:
            errors.append(f"{rel}: execution agent does not load '{PROTOCOL_SKILL}'")

        may_name = is_execution or DOCUMENTS_WRITES in text
        if DOCUMENTS_WRITES in text:
            marked.append(str(rel))
        scan(path, known, write_tools, retired_tools, may_name, errors)

    # --- skills ----------------------------------------------------------------
    skills_dir = ROOT / ".claude" / "skills"
    execution_skills = set()
    for skill_md in skills_dir.glob("*/SKILL.md"):
        if EXECUTION_LANE in frontmatter(skill_md.read_text()):
            execution_skills.add(skill_md.parent.name)

    for path in sorted(skills_dir.glob("*/**/*.md")):
        skill = path.relative_to(skills_dir).parts[0]
        text = path.read_text()
        may_name = skill in execution_skills or DOCUMENTS_WRITES in text
        if DOCUMENTS_WRITES in text:
            marked.append(str(path.relative_to(ROOT)))
        scan(path, known, write_tools, retired_tools, may_name, errors)

    # --- workflows and root docs ----------------------------------------------
    for path in sorted((ROOT / "workflows").glob("*.md")) + sorted(ROOT.glob("*.md")):
        text = path.read_text()
        may_name = DOCUMENTS_WRITES in text
        if may_name:
            marked.append(str(path.relative_to(ROOT)))
        scan(path, known, write_tools, retired_tools, may_name, errors)

    for e in errors:
        print(f"FAIL  {e}")

    if errors:
        print(f"\n{len(errors)} boundary violation(s).")
        return 1

    print(f"OK  execution boundary intact — {len(read_tools)} read / {len(write_tools)} write "
          f"tools classified, {len(marked)} file(s) marked as documenting writes")
    return 0


if __name__ == "__main__":
    sys.exit(main())
