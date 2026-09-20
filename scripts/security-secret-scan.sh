#!/usr/bin/env bash
set -euo pipefail

PATTERN='AKIA[0-9A-Z]{16}|ghp_[A-Za-z0-9]{30,}|github_pat_[A-Za-z0-9_]{30,}|sk-[A-Za-z0-9]{20,}|-----BEGIN (RSA |EC |OPENSSH |DSA )?PRIVATE KEY-----'

echo 'Verificando arquivos rastreados...'
if git grep -nI -E "$PATTERN" -- . ':!scripts/security-secret-scan.sh'; then
  echo 'Possível credencial encontrada na árvore atual.' >&2
  exit 1
fi

echo 'Verificando histórico completo disponível...'
if git log --all --format= --patch -- . ':!package-lock.json' ':!*.lock' | grep -Eq "$PATTERN"; then
  echo 'Possível credencial encontrada no histórico do Git.' >&2
  exit 1
fi

echo 'Secret scan concluído sem padrões de credenciais de alta confiança.'
