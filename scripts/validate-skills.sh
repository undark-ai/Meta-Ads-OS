#!/usr/bin/env bash
# Skill spec compliance.
#
# The failures here are invisible by inspection, which is why they are validated rather than
# reviewed: a skill whose frontmatter `name` does not match its directory silently fails to
# load — it looks present and never triggers.
set -uo pipefail
cd "$(dirname "$0")/.." || exit 1

fail=0; warn=0; count=0

for dir in .claude/skills/*/; do
  name="$(basename "$dir")"
  skill="$dir/SKILL.md"
  count=$((count + 1))

  if [ ! -f "$skill" ]; then
    echo "FAIL  $name: no SKILL.md"; fail=$((fail + 1)); continue
  fi

  fm_name="$(sed -n '/^name:/{s/^name: *//;s/^"//;s/"$//;p;q;}' "$skill")"
  if [ "$fm_name" != "$name" ]; then
    echo "FAIL  $name: frontmatter name is '$fm_name' — a mismatch makes the skill fail to load silently"
    fail=$((fail + 1))
  fi

  if ! grep -q '^description:' "$skill"; then
    echo "FAIL  $name: no description — routing has nothing to key on"; fail=$((fail + 1))
  fi

  # name spec: lowercase letters, digits, hyphens
  if ! printf '%s' "$name" | grep -Eq '^[a-z0-9-]{1,64}$'; then
    echo "FAIL  $name: directory name must be 1-64 chars of [a-z0-9-]"; fail=$((fail + 1))
  fi

  lines="$(wc -l < "$skill")"
  if [ "$lines" -gt 500 ]; then
    echo "FAIL  $name: SKILL.md is $lines lines (limit 500) — move depth into references/"
    fail=$((fail + 1))
  fi

  # A description with no trigger phrasing works only when an agent loads the skill by name.
  desc="$(sed -n 's/^description: *//p' "$skill" | head -1)"
  if [ "${#desc}" -lt 60 ]; then
    echo "WARN  $name: description is ${#desc} chars — too terse to route on"
    warn=$((warn + 1))
  fi
done

echo
if [ "$fail" -gt 0 ]; then
  echo "$fail failure(s), $warn warning(s) across $count skills."
  exit 1
fi
echo "OK  $count skills valid ($warn warning(s))"
