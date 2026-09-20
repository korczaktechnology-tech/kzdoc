#!/usr/bin/env bash
set -euo pipefail

: "${MONGODB_URI:?MONGODB_URI deve estar definido}"
: "${MONGODB_DATABASE:=KZDocs}"
: "${BACKUP_DIR:=backups/mongodb}"

mkdir -p "$BACKUP_DIR"
STAMP="$(date -u +%Y%m%dT%H%M%SZ)"
mongodump --uri="$MONGODB_URI" --db="$MONGODB_DATABASE" --out="$BACKUP_DIR/$STAMP"
printf 'Backup criado em %s\n' "$BACKUP_DIR/$STAMP"
