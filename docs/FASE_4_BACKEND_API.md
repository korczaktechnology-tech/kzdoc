# FASE 4 — BACKEND / API

## Objetivo

A Fase 4 transforma a estrutura preparada nas fases anteriores em uma API de negócio utilizável pelo frontend e pelas futuras aplicações desktop e mobile.

A API utiliza FastAPI, mantém o versionamento em `/api/v1/` e separa modelos de entrada, respostas, rotas, serviços, repositórios, validações e persistência.

## Itens 60–84

### 60. Aplicação backend
A aplicação FastAPI está configurada em `backend/src/korczak_documents/main.py`, com documentação OpenAPI, tratamento centralizado de erros e registro das rotas.

### 61. API v1
Todas as rotas de negócio ficam sob `/api/v1/`. O endpoint raiz de saúde permanece disponível para infraestrutura.

### 62. Saúde do sistema
`GET /api/v1/health` e o health raiz permitem verificar se a aplicação está respondendo.

### 63–66. Autenticação, sessão e recuperação
Foram criados:
- `POST /api/v1/auth/register`
- `POST /api/v1/auth/login`
- `POST /api/v1/auth/logout`
- `POST /api/v1/auth/recovery`

As sessões usam tokens opacos armazenados somente como hash no MongoDB. A recuperação possui resposta neutra para não revelar se um e-mail está cadastrado.

### 67. Usuários
Foram criados:
- `GET /api/v1/users/me`
- `PATCH /api/v1/users/me`
- `GET /api/v1/users` para administração.

A senha nunca é devolvida pela API.

### 68–69. Documentos e versões
A API permite criação, consulta, atualização, exclusão lógica, restauração, exclusão definitiva e criação/consulta de versões.

### 70. Pastas
A API permite criar, listar, renomear, mover e excluir pastas, validando a pasta pai dentro do mesmo proprietário.

### 71. Etiquetas
A API permite criar, listar, aplicar, remover e excluir etiquetas.

### 72–74. Favoritos, recentes e lixeira
Favoritos ficam associados ao documento por usuário. Recentes são registrados por eventos de abertura. A lixeira usa exclusão lógica antes da exclusão definitiva.

### 75. Pesquisa
`GET /api/v1/search` pesquisa por nome e tipo, com filtro opcional de pasta e estado.

### 76–77. Grupos e permissões
Foi adicionada a coleção `grupos` como suporte à API. A API permite criar grupos, adicionar/remover membros e consultar/alterar permissões documentais, com alteração de permissões reservada ao administrador.

### 78. Auditoria
Operações relevantes geram eventos na coleção `eventos`. `GET /api/v1/audit` oferece paginação e filtro por tipo.

### 79. Notificações
Foram criadas consulta e marcação de notificações como lidas.

### 80. Validação
Modelos de entrada usam Pydantic com campos obrigatórios, limites de tamanho e rejeição de campos desconhecidos. Erros de validação são padronizados.

### 81–83. Respostas, erros e logs
A API possui contrato de erro consistente:
```json
{
  "error": {
    "code": "validation_error",
    "message": "Dados de entrada inválidos"
  }
}
```

Erros de aplicação, validação e falhas internas possuem tratamento centralizado. As ações importantes registram eventos de auditoria.

### 84. Testes
A Fase 4 possui:
- inventário automatizado de todas as rotas previstas;
- testes de validação;
- teste do contrato de erros;
- teste de integração real com MongoDB;
- fluxo ponta a ponta de cadastro, login, sessão, usuários, documentos, versões, pastas, etiquetas, favoritos, recentes, lixeira, pesquisa, grupos, permissões, auditoria e notificações;
- validação do build e dos testes do frontend no mesmo workflow.

## Critério de conclusão

A Fase 4 é considerada concluída quando o workflow `Fase 4 - Backend API` passa no branch `main`, incluindo os testes unitários/contratuais e o teste de integração com MongoDB real.

**Status atual: concluída e validada.** O workflow da Fase 4 passou integralmente no `main`. A validação cobre o contrato das rotas, autenticação, persistência, isolamento entre usuários, documentos, versões, pastas, etiquetas, favoritos, recentes, lixeira, pesquisa, grupos, permissões, auditoria, notificações e recuperação de sessão. Os workflows das Fases 1, 2 e 3 também estão verdes no mesmo estado do repositório.

## Observação

A implementação desta fase prepara a superfície de negócio da API. Endurecimentos específicos de segurança, incluindo políticas avançadas de senha, rate limiting, proteção contra abuso, revisão de segredos e demais itens da Fase 5, permanecem deliberadamente na fase correspondente.
