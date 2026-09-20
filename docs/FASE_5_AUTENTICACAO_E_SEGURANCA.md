# FASE 5 — AUTENTICAÇÃO E SEGURANÇA

## Objetivo

Esta fase endurece a autenticação e as fronteiras de segurança da API sem depender de serviços pagos. A implementação usa recursos nativos do backend, MongoDB e GitHub Actions.

## Itens 85–100

### 85–87 — Contas, login e logout
- Cadastro cria usuários com e-mail normalizado e senha validada no servidor.
- Login usa comparação do hash da senha e retorna sessão opaca.
- Logout revoga a sessão em vez de apenas apagar uma referência local.

### 88 — Gerenciamento de sessão
As sessões armazenam somente o hash do token, possuem expiração de 24 horas e `revoked_at`. O MongoDB recebe índice TTL para limpeza automática após a expiração.

### 89 — Proteção de rotas
As rotas autenticadas usam `current_user` e recusam requisições sem sessão válida, expirada ou revogada.

### 90 — Armazenamento seguro de senhas
As senhas não são armazenadas em texto puro. O projeto utiliza PBKDF2-HMAC-SHA256 com salt aleatório e 310.000 iterações. A política exige 12 caracteres, minúscula, maiúscula, número e caractere especial.

### 91–92 — Autorização e níveis de acesso
A autorização ocorre no servidor. Os papéis `user`, `manager` e `admin` possuem níveis explícitos. Operações administrativas, como listagem de usuários e alteração de permissões, exigem nível administrativo.

### 93–94 — Isolamento e propriedade
Consultas de documentos, pastas, etiquetas e operações relacionadas validam o proprietário no servidor. Um usuário que conheça o identificador de outro documento recebe `404`, sem exposição de existência ou dados do recurso.

### 95 — Operações administrativas
Rotas administrativas verificam o papel do usuário autenticado. Alterações administrativas relevantes também geram eventos de auditoria.

### 96–97 — Segredos e ambiente
Nenhum segredo é definido no código de produção. `.env` é ignorado pelo Git e `.env.example` contém somente valores de desenvolvimento/documentação. Configurações são carregadas por variáveis de ambiente.

### 98 — Histórico do Git
O script `scripts/security-secret-scan.sh` verifica a árvore atual e o histórico Git disponível em busca de padrões de credenciais de alta confiança. O workflow da Fase 5 executa a verificação com `fetch-depth: 0`.

### 99 — Logs
Eventos de auditoria passam por uma camada de redação que remove valores associados a senha, token, segredo, autorização, cookie, chave de API e conteúdo sensível. O fluxo de recuperação registra somente o identificador interno do usuário, sem registrar o e-mail recebido.

### 100 — Testes de segurança
`backend/tests/test_security.py` valida hash e salt de senhas, política de senha, logout/revogação, proteção de documentos entre usuários, proteção administrativa, níveis de acesso, ausência de senha nas respostas, redação de logs e cabeçalhos de segurança. O CI também executa testes de integração contra MongoDB real e a varredura de credenciais atual/histórica.

## Proteções HTTP adicionais

A API aplica CORS restrito à origem configurada, `X-Content-Type-Options`, `X-Frame-Options`, `Referrer-Policy`, `Permissions-Policy` e HSTS em produção. Endpoints de cadastro, login e recuperação possuem limite de tentativas por origem de cliente para reduzir abuso automatizado.

## Critério de conclusão

A Fase 5 é considerada concluída quando o workflow `Fase 5 - Seguranca` passa integralmente, incluindo testes unitários, integração com MongoDB, regressão da API e varredura da árvore e histórico Git.

**Status: implementação completa da Fase 5.**