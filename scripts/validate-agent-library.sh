#!/usr/bin/env bash
# Agent frontmatter, numbering, and section mapping.
#
# The check that matters most: every agent must map to one of the 30 audit sections. An agent
# no section owns will never run in a full audit, and will look present while doing nothing.
set -uo pipefail
cd "$(dirname "$0")/.." || exit 1

fail=0; count=0
seen_names=""

for f in agents/*.md; do
  [ -e "$f" ] || continue
  base="$(basename "$f")"
  count=$((count + 1))

  expected="${base%-agent.md}"
  fm_name="$(sed -n '/^name:/{s/^name: *//;s/^"//;s/"$//;p;q;}' "$f")"
  if [ "$fm_name" != "$expected" ]; then
    echo "FAIL  $base: frontmatter name '$fm_name' does not match filename (expected '$expected')"
    fail=$((fail + 1))
  fi

  case "$seen_names" in
    *" $fm_name "*) echo "FAIL  $base: duplicate agent name '$fm_name'"; fail=$((fail + 1)) ;;
  esac
  seen_names="$seen_names $fm_name "

  if ! printf '%s' "$base" | grep -Eq '^[0-9]+-'; then
    echo "FAIL  $base: filename must start with the agent number"; fail=$((fail + 1))
  fi

  for field in description model section; do
    grep -q "^$field:" "$f" || { echo "FAIL  $base: missing '$field:'"; fail=$((fail + 1)); }
  done

  section="$(sed -n 's/^section: *//p' "$f" | head -1)"
  if [ -n "$section" ] && { [ "$section" -lt 0 ] 2>/dev/null || [ "$section" -gt 30 ] 2>/dev/null; }; then
    echo "FAIL  $base: section '$section' is outside 0-30"; fail=$((fail + 1))
  fi

  # Audit agents are read-only. Never grant Write/Edit to an agent that inspects a live account.
  num="$(printf '%s' "$base" | sed -E 's/^([0-9]+)-.*/\1/')"
  if [ "$num" -lt 200 ] 2>/dev/null; then
    if grep -Eq '^tools:.*\b(Write|Edit)\b' "$f"; then
      echo "FAIL  $base: audit agent grants Write/Edit"; fail=$((fail + 1))
    fi
    grep -q '^disallowedTools:.*Write' "$f" || \
      echo "WARN  $base: audit agent does not declare 'disallowedTools: Write, Edit'"
  fi
done

echo
if [ "$fail" -gt 0 ]; then
  echo "$fail failure(s) across $count agents."
  exit 1
fi
echo "OK  $count agents valid"
