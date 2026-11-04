#!/usr/bin/env bash
# Create a private client workspace: bash scripts/new_client.sh "Client Name"
set -euo pipefail
[ $# -ge 1 ] || { echo "Usage: $0 \"Client Name\""; exit 1; }
slug=$(printf '%s' "$1" | tr '[:upper:]' '[:lower:]' | sed -E 's/[^a-z0-9]+/-/g; s/^-+|-+$//g')
[ -n "$slug" ] || { echo "Invalid name"; exit 1; }
root="$(cd "$(dirname "$0")/.." && pwd)"
dir="$root/clients/$slug"
[ ! -e "$dir" ] || { echo "Already exists: $dir"; exit 1; }
mkdir -p "$dir"/{brief,deliverables,comms}
cp "$root/templates/client-intake-questionnaire.md" "$dir/brief/intake.md"
cp "$root/templates/scope-of-work.md" "$dir/brief/scope.md"
printf '# %s\n\nStarted: %s\n\n## Comms log\n\n## Decisions\n\n## Next actions\n' "$1" "$(date +%F)" > "$dir/README.md"
echo "Created $dir (git-ignored: never commit client data)"
