#!/bin/bash
# Runs once, the first time PostgreSQL starts with an empty data volume.
# Gives each service its own database and user (least privilege).
set -euo pipefail

create_db() {
  local db="$1" user="$2" pass="$3"
  psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" <<-SQL
    CREATE USER ${user} WITH PASSWORD '${pass}';
    CREATE DATABASE ${db} OWNER ${user};
    REVOKE ALL ON DATABASE ${db} FROM PUBLIC;
SQL
}

create_db n8n     n8n     "$N8N_DB_PASSWORD"
create_db litellm litellm "$LITELLM_DB_PASSWORD"
