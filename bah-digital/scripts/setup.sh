#!/usr/bin/env bash
# One-time setup: checks your computer and creates .env with strong secrets.
# Safe to run again - it never overwrites an existing .env.
set -euo pipefail
cd "$(dirname "$0")/.."

ok()   { printf '  \033[32m✔\033[0m %s\n' "$1"; }
fail() { printf '  \033[31m✘\033[0m %s\n' "$1"; exit 1; }

echo "Bah.Digital setup"
echo "1) Checking prerequisites"
command -v docker  >/dev/null || fail "Docker not found. In Docker Desktop: Settings > Resources > WSL Integration > enable Ubuntu."
docker info >/dev/null 2>&1 || fail "Docker is installed but not running. Open Docker Desktop on Windows and wait for it to start."
ok "Docker running ($(docker --version | cut -d, -f1))"
docker compose version >/dev/null 2>&1 || fail "docker compose missing. Update Docker Desktop."
ok "Docker Compose available"
command -v openssl >/dev/null || fail "openssl missing. Run: sudo apt update && sudo apt install -y openssl"
ok "openssl available"
case "$PWD" in /mnt/*) echo "  ! Warning: project is on the Windows drive ($PWD). Move it to ~/bah-digital for speed.";; esac

mem_gb=$(awk '/MemTotal/ {printf "%.1f", $2/1024/1024}' /proc/meminfo)
ok "Memory available to WSL: ${mem_gb} GB"
awk "BEGIN{exit !($mem_gb < 5)}" && echo "  ! Less than 5 GB for WSL. See docs/STEP-BY-STEP.md section 'Give WSL more memory'."

echo "2) Creating .env"
if [ -f .env ]; then
  ok ".env already exists - left untouched"
else
  cp .env.example .env
  while grep -q 'CHANGE_ME' .env; do
    sed -i "0,/CHANGE_ME/s//$(openssl rand -hex 32)/" .env
  done
  # LiteLLM requires its master key to start with sk-
  sed -i 's/^LITELLM_MASTER_KEY=/LITELLM_MASTER_KEY=sk-/' .env
  chmod 600 .env
  ok ".env created with random secrets (only you can read it)"
fi

echo
echo "Setup complete. Next: docker compose up -d postgres"
