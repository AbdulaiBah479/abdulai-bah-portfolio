#!/usr/bin/env bash
# Shows whether each Bah.Digital service is up. Run any time:  ./scripts/health.sh
cd "$(dirname "$0")/.."
set -a; [ -f .env ] && . ./.env; set +a

check() { # name, command
  if eval "$2" >/dev/null 2>&1; then printf '  \033[32m● UP  \033[0m %s\n' "$1"
  elif docker ps -a --format '{{.Names}}' | grep -qx "bah-$1"; then printf '  \033[31m● DOWN\033[0m %s  (see: docker compose logs %s)\n' "$1" "$1"
  else printf '  \033[90m○ not installed yet\033[0m %s\n' "$1"; fi
}

echo "Bah.Digital health"
check postgres   "docker exec bah-postgres pg_isready -U ${POSTGRES_USER:-bah_admin}"
check qdrant     "curl -sf http://127.0.0.1:6333/healthz"
check ollama     "curl -sf http://127.0.0.1:11434/api/version"
check open-webui "curl -sf http://127.0.0.1:3000/health"
check n8n        "curl -sf http://127.0.0.1:5678/healthz"
check litellm    "curl -sf http://127.0.0.1:4000/health/liveliness"
echo
docker stats --no-stream --format '  {{.Name}}: {{.MemUsage}}' 2>/dev/null | grep bah- || true
