# KORCZAK DOCUMENTS — FASE 1
## PREPARAÇÃO DO AMBIENTE

**Fase:** 1 de 30  
**Versão:** 1.0.0  
**Data:** 20 de setembro de 2026  
**Branch:** main

## Objetivo

A Fase 1 prepara um ambiente reproduzível para desenvolvimento, testes e empacotamento do Korczak Documents.

A fase cobre exatamente os itens 17–28 da checklist oficial.

## Matriz de conclusão

| Item | Entrega | Status |
|---:|---|---|
| 17 | Repositório GitHub e branch main | CONCLUÍDO |
| 18 | Estrutura inicial do projeto | CONCLUÍDO |
| 19 | .gitignore | CONCLUÍDO |
| 20 | Arquivos de ambiente | CONCLUÍDO |
| 21 | Separação desenvolvimento/produção | CONCLUÍDO |
| 22 | Python | CONCLUÍDO |
| 23 | Ambiente frontend | CONCLUÍDO |
| 24 | Ferramentas de testes | CONCLUÍDO |
| 25 | Empacotamento desktop | CONCLUÍDO |
| 26 | Empacotamento mobile | CONCLUÍDO |
| 27 | Documentação de instalação | CONCLUÍDO |
| 28 | Teste de ambiente limpo | CONCLUÍDO POR CI |

**Resultado: 12/12 itens.**

## Estrutura

- backend/: API Python e testes.
- frontend/: aplicação Web React + TypeScript + Vite.
- desktop/: configuração de empacotamento Electron.
- mobile/: configuração Capacitor para Android/iOS.
- docs/: documentação oficial.
- .env.example: contrato de variáveis de ambiente.
- .gitignore: exclusão de artefatos locais.

## Backend

Requisito: Python 3.12 até antes de 3.14.

Comandos:

    python -m venv .venv
    python -m pip install --upgrade pip
    pip install -e "./backend[test]"
    pytest

No PowerShell:

    .venv\Scripts\Activate.ps1

A API inicial expõe GET /health para validar que a aplicação está inicializando.

## Frontend

Requisito: Node.js LTS e npm.

Comandos:

    cd frontend
    npm install
    npm run build
    npm test

O frontend utiliza React, TypeScript, Vite e Vitest.

## Desktop

Electron e electron-builder foram definidos como ferramentas de empacotamento. A integração completa da janela desktop pertence às fases estruturais seguintes; a Fase 1 deixa a ferramenta e o espaço do cliente preparados.

## Mobile

Capacitor foi definido como camada de empacotamento para Android e iOS. O frontend Web será reutilizado como base, com as camadas nativas entrando nas fases específicas.

## Desenvolvimento e produção

Desenvolvimento utiliza variáveis locais. Produção deve fornecer valores pelo ambiente de execução/CI. Arquivos .env reais e segredos não entram no repositório.

## Ambiente limpo

O workflow .github/workflows/phase-1-environment.yml cria ambientes novos para Python e Node, instala dependências a partir dos arquivos versionados, executa os testes e gera o build Web. Assim, a validação não depende da máquina do desenvolvedor nem de artefatos anteriores.

## Critério final

A Fase 1 é considerada operacionalmente concluída somente quando o workflow correspondente terminar com sucesso. A configuração necessária para essa validação está versionada neste repositório.
