# Fase 12 — Auditoria e Histórico

## Objetivo

Fechar a rastreabilidade do Korczak Documents. Toda operação relevante deve registrar quem executou a ação, o que ocorreu, qual recurso foi afetado, quando ocorreu, o resultado e se o registro permanece íntegro, sem transformar a auditoria em cópia dos dados privados.

## Checklist oficial — itens 195–204

**195. Registrar criação.** Documentos, pastas, etiquetas, grupos e usuários geram eventos quando a criação é concluída.

**196. Registrar edição.** Alterações de documentos, pastas, versões e usuários geram eventos com os campos alterados quando aplicável, sem registrar valores sensíveis.

**197. Registrar exclusão.** Exclusões lógicas, definitivas e remoções são registradas.

**198. Registrar restauração.** Documentos, pastas e versões restaurados geram eventos próprios.

**199. Registrar alterações de permissão.** Alterações de permissões de documentos e pastas registram ator, recurso, política e resultado.

**200. Registrar alterações administrativas.** Operações administrativas sobre usuários e grupos são rastreáveis.

**201. Registrar autenticações relevantes.** Cadastro, login, falha de login, logout e recuperação são registrados quando houver informação suficiente para associação segura.

**202. Criar consulta de eventos.** `GET /api/v1/audit` oferece consulta paginada.

**203. Criar filtros de auditoria.** A consulta aceita tipo, documento, ator, recurso, resultado e período, inclusive combinados.

**204. Garantir integridade dos registros.** Cada evento possui SHA-256 calculado sobre uma representação canônica dos campos essenciais; a consulta recalcula o hash e retorna `integrity_valid`.

## Modelo do evento

A coleção `eventos` é append-only no nível da aplicação. Não existe endpoint para editar ou excluir eventos.

Cada registro contém `id`, `user_id`, `actor_id`, `type`, `action`, `resource`, `resource_id`, `result`, `payload` redigido, `created_at` em UTC e `integrity_hash`.

O hash cobre esses campos lógicos. Alteração posterior de ator, ação, recurso, resultado, payload ou data invalida o registro.

## Privacidade e redaction

O payload passa por redaction recursiva. Chaves contendo `password`, `token`, `secret`, `authorization`, `cookie`, `api_key` ou `content` são substituídas por `[REDACTED]`, inclusive em objetos e listas aninhados.

A auditoria guarda identificadores e metadados necessários para rastreabilidade, mas não senhas, tokens, cookies, chaves de API, autorizações ou o conteúdo integral dos documentos.

## Eventos cobertos

- documentos: criação, edição, salvamento, exclusão, exclusão definitiva, restauração, versões e abertura;
- pastas: criação, edição, exclusão e restauração;
- permissões de documentos e pastas;
- usuários e grupos, incluindo membros;
- cadastro, login, falha de login, logout e recuperação;
- etiquetas e favoritos.

## Consulta e autorização

Administradores e gestores podem consultar a visão global. Usuários comuns ficam restritos aos próprios eventos. A API rejeita consulta de outro ator por usuário comum.

A paginação aceita no máximo 100 registros por página e ordena os eventos do mais recente para o mais antigo. A coleção possui índices para usuário+data, ator+data e recurso+data.

## Validação

A fase valida criação, edição, exclusão, restauração, versões, permissões, operações administrativas, autenticação, paginação, filtros combinados, isolamento entre atores, acesso global autorizado, redaction, presença do hash e detecção de adulteração.

O workflow da Fase 12 também executa a regressão do backend e o build/teste do frontend.

## Critério de conclusão

Os itens **195–204** são considerados concluídos somente quando implementação, testes de integração e workflow específico da Fase 12 passam sem regressões.

**Estado: 🟢 Concluída**
