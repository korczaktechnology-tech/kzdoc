# Fase 13 — Integração Frontend ↔ Backend

**Itens:** 205–222  
**Estado:** 🟢 Concluída

## Objetivo

Garantir que a interface do Korczak Documents seja uma camada de apresentação da aplicação real. Nenhuma operação apresentada ao usuário pode depender de dados fictícios, estado inventado ou botão sem comportamento definido.

## Checklist 205–222

- [x] **205 — Login e cadastro:** autenticação usa os endpoints reais e persiste somente o token da sessão.
- [x] **206 — Sessão:** a aplicação valida a sessão com `/api/v1/users/me`, limpa a sessão inválida e envia o token nas requisições autenticadas.
- [x] **207 — Dashboard:** documentos, notificações e contadores exibidos vêm da API.
- [x] **208 — Documentos:** criação, leitura, edição, movimentação, exclusão, restauração e exclusão definitiva usam a API real.
- [x] **209 — Editor:** salvamento cria versão no servidor e trata conflito de versão sem apagar o rascunho local.
- [x] **210 — Pastas:** criação, renomeação, exclusão lógica, restauração e permissões usam a API.
- [x] **211 — Favoritos e recentes:** estado é persistido no backend e carregado novamente.
- [x] **212 — Pesquisa:** pesquisa rápida e avançada usam consulta server-side, filtros, ordenação e paginação reais.
- [x] **213 — Usuários:** criação, edição e ativação/desativação respeitam os endpoints administrativos e os perfis do servidor.
- [x] **214 — Grupos:** criação e gerenciamento de membros usam a API e são exibidos somente quando autorizados.
- [x] **215 — Permissões:** políticas de documentos e pastas são carregadas e gravadas no backend; a autorização definitiva continua no servidor.
- [x] **216 — Auditoria e histórico:** histórico documental e auditoria global consultam eventos reais, com filtros e paginação.
- [x] **217 — Perfil e configurações:** alterações do perfil e tema persistem corretamente; encerramento remove o token local.
- [x] **218 — Tratamento de erros:** respostas HTTP são convertidas em `ApiError`, 401 encerra a sessão local e falhas de rede/timeout recebem mensagem controlada.
- [x] **219 — Identificadores:** parâmetros de recursos enviados pela interface são codificados antes de formar URLs.
- [x] **220 — Controles sem implementação:** ações fictícias de upload, digitalização, assinatura, OCR, backup, projetos e armazenamento foram removidas da interface nesta fase em vez de simular funcionalidades ainda inexistentes.
- [x] **221 — Estado e feedback:** ações críticas aguardam a resposta da API, exibem erro quando necessário e recarregam o estado persistido quando a operação termina.
- [x] **222 — Validação de integração:** workflow dedicado executa testes backend com MongoDB, suíte frontend e build de produção.

## Regras de engenharia

### Fonte de verdade

O frontend não replica regras de autorização. O backend permanece responsável por identidade, propriedade, ACL, perfis e validação de operações.

### Cliente HTTP

O serviço `frontend/src/services/api.ts` centraliza comunicação com a API. A camada:

- adiciona o Bearer token quando existir;
- envia JSON somente quando há corpo;
- interpreta respostas JSON e respostas vazias;
- converte erros HTTP para `ApiError`;
- remove a sessão local em 401;
- encerra requisições que ultrapassem 30 segundos;
- diferencia timeout e falha de rede;
- codifica identificadores usados em caminhos.

### Integração do editor

O salvamento utiliza `base_version_id`. Quando o servidor responde 409, a aplicação recarrega a versão atual e preserva o rascunho local. O frontend não tenta sobrescrever silenciosamente uma alteração concorrente.

### Dados fictícios

Não são utilizados dados de demonstração para representar operações concluídas. Onde o backend ainda não fornece uma funcionalidade — por exemplo upload binário, OCR, assinatura digital ou armazenamento — a interface não apresenta uma ação operacional falsa.

### Validação

A fase somente permanece concluída enquanto o workflow específico passar com:

1. MongoDB real em serviço de CI;
2. testes de contrato e integração do backend;
3. teste específico da integração;
4. build do frontend;
5. testes do frontend.

## Critério de aceite

A Fase 13 está concluída porque os 18 itens 205–222 foram implementados ou validados, não apenas documentados. As fases 14–30 permanecem responsáveis pelas capacidades que a arquitetura reservou para elas, especialmente responsividade, publicação, clientes nativos, sincronização, desempenho, segurança final e release.
