#!/usr/bin/env bash
set -euo pipefail

: "${MONGODB_URI:?MONGODB_URI deve estar definido}"
: "${MONGODB_DATABASE:=KZDocs}"
: "${BACKUP_PATH:?BACKUP_PATH deve apontar para um dump do mongodump}"

mongorestore --uri="$MONGODB_URI" --nsFrom="$MONGODB_DATABASE.*" --nsTo="$MONGODB_DATABASE.*" "$BACKUP_PATH"
printf 'Restauração concluída a partir de %s\n' "$BACKUP_PATH"
