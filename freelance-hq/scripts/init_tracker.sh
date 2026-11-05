#!/usr/bin/env bash
# Create your private tracker files from the examples (safe to run again; never overwrites).
set -euo pipefail
cd "$(dirname "$0")/../tracker"
for ex in *.example.csv; do
  live="${ex%.example.csv}.csv"
  if [ -e "$live" ]; then echo "keep   $live"; else cp "$ex" "$live"; echo "create $live"; fi
done
mkdir -p reviews
echo "Done. These files are git-ignored (private). Back them up in a PRIVATE place, not this public repo."
