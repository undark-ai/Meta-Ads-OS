#!/usr/bin/env bash
# Create an audit run directory and open its coverage ledger.
#
# The ledger is opened NOW, with all 30 sections PENDING — not written at the end. A ledger
# written from memory afterwards is generous about what it checked, and an interrupted run
# leaves no record of how far it got.
set -euo pipefail
cd "$(dirname "$0")/.."

RUN_ID="${1:-$(date -u +%Y-%m-%d-%H%M)}"
LANE="${2:-audit}"

case "$LANE" in
  audit)     BASE="audits/$RUN_ID" ;;
  execution) BASE="changes/$RUN_ID" ;;
  *) echo "usage: $0 [run-id] [audit|execution]" >&2; exit 1 ;;
esac

if [ -e "$BASE" ]; then
  echo "refusing to overwrite an existing run at $BASE" >&2
  echo "runs are never overwritten — comparing audits depends on the old one surviving" >&2
  exit 1
fi

if [ "$LANE" = "execution" ]; then
  mkdir -p "$BASE"
  for f in change-plan approval applied rollback; do
    cp "templates/change-register.md" "$BASE/$f.md" 2>/dev/null || : > "$BASE/$f.md"
  done
  echo "execution run initialised at $BASE"
  echo "governed by EXECUTION-PROTOCOL.md — nothing is called before the plan is approved"
  exit 0
fi

mkdir -p "$BASE"/raw "$BASE"/normalized "$BASE"/findings \
         "$BASE"/reconciliations "$BASE"/agent-results

SECTIONS=(
 "Business & economics — GATE"
 "Tracking & measurement — GATE"
 "Reconciliation — MANDATORY"
 "Account structure"
 "Campaign performance & trend windows"
 "Bidding, delivery & learning phase"
 "Creative inventory & database"
 "Creative fatigue"
 "Creative angle & hook analysis"
 "Creative testing system"
 "Relevance & auction diagnostics"
 "Audience strategy"
 "Prospecting"
 "Retargeting"
 "Frequency & saturation"
 "Product catalog"
 "Advantage+ Shopping & Creative"
 "Placement analysis"
 "Funnel audit"
 "Landing pages & post-click CRO"
 "Offer audit"
 "Product & SKU economics"
 "Geographic & device economics"
 "New vs returning & the LTV loop"
 "Attribution"
 "Incrementality"
 "Competitive & Ad Library"
 "Hygiene, Business Manager & permissions"
 "Budget allocation & the next dollar"
 "Final output"
)

{
  echo "# Coverage — $RUN_ID"
  echo
  echo "0 FINDINGS · 0 CLEAN · 0 DEGRADED · 0 N/A · 0 BLOCKED · ${#SECTIONS[@]} PENDING (of ${#SECTIONS[@]})"
  echo
  echo "> Derive this tally from the rows programmatically; never write it from memory. A summary"
  echo "> line that drifts from the table beneath it discredits the ledger it summarises."
  echo
  echo "| § | Section | State | Sources | Note |"
  echo "|---:|---|---|---|---|"
  i=1
  for s in "${SECTIONS[@]}"; do
    printf '| %d | %s | PENDING | | |\n' "$i" "$s"
    i=$((i + 1))
  done
} > "$BASE/coverage.md"

for f in preflight source-capabilities scope assumptions; do
  : > "$BASE/$f.md"
done

echo "audit run initialised at $BASE"
echo "coverage.md opened with ${#SECTIONS[@]} sections PENDING"
