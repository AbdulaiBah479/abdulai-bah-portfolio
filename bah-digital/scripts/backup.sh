#!/usr/bin/env bash
# Backs up all databases and your config into backups/<date>/.
# Keeps the last 7 backups. Usage: ./scripts/backup.sh
set -euo pipefail
cd "$(dirname "$0")/.."
set -a; . ./.env; set +a

dest="backups/$(date +%Y-%m-%d_%H%M)"
mkdir -p "$dest"

docker exec bah-postgres pg_dumpall -U "$POSTGRES_USER" | gzip > "$dest/postgres.sql.gz"
echo "✔ PostgreSQL saved"

if docker ps --format '{{.Names}}' | grep -qx bah-qdrant; then
  docker run --rm -v bah_qdrant-data:/data -v "$PWD/$dest":/out alpine \
    tar czf /out/qdrant.tar.gz -C /data .
  echo "✔ Qdrant saved"
fi

tar czf "$dest/config.tar.gz" config infrastructure .env
chmod 600 "$dest"/*
echo "✔ Config saved (contains secrets - keep backups private)"

ls -1dt backups/20* | tail -n +8 | xargs -r rm -rf
echo "Backup complete: $dest"
