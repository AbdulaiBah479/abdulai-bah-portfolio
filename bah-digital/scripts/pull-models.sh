#!/usr/bin/env bash
# Downloads the starter local models (about 3 GB total). Needs the ollama service running.
set -euo pipefail
for m in qwen3:4b nomic-embed-text; do
  echo "Downloading $m ..."
  docker exec bah-ollama ollama pull "$m"
done
docker exec bah-ollama ollama list
