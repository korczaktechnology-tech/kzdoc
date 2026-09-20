# KORCZAK DOCUMENTS — FASE 3
## BANCO DE DADOS

**Fase:** 3 de 30  
**Itens:** 45–59  
**Banco:** `KZDocs`  
**Estado:** implementação completa, aguardando validação operacional final

### Coleções

O banco utiliza as seguintes coleções da aplicação:

1. `usuarios` — dados dos usuários e informações necessárias à autenticação e gestão de contas.
2. `documentos` — documentos pertencentes aos usuários e seus metadados.
3. `versoes` — versões dos documentos e seus conteúdos versionados.
4. `pastas` — estrutura de organização hierárquica dos documentos.
5. `etiquetas` — etiquetas associadas aos documentos e organizadas por proprietário.
6. `sessoes` — sessões autenticadas e seus respectivos períodos de expiração.
7. `eventos` — registros de eventos e ações relevantes para histórico e auditoria.
8. `notificacoes` — notificações destinadas aos usuários e seu estado de leitura.
9. `grupos` — grupos de usuários e sua relação com os respectivos proprietários e membros.

Além dessas coleções funcionais, o banco possui a coleção técnica `migrations`, utilizada pelo mecanismo de migração para registrar as versões estruturais já aplicadas.

O bootstrap materializa as coleções necessárias para que a estrutura inicial do banco seja verificável desde a primeira inicialização.

### Conexão

A conexão usa PyMongo Async e recebe a URI por variável de ambiente. O nome do banco é configurado separadamente como `KZDocs`, evitando credenciais e endpoints no código.

### Índices

Foram definidos índices iniciais para identidade de usuário, propriedade e atualização de documentos, numeração de versões, hierarquia de pastas, etiquetas por usuário, expiração de sessões, histórico de eventos, notificações não lidas e identificação de grupos.

Também existe uma restrição de unicidade para o e-mail dos usuários e um índice de expiração automática para sessões.

### Referências e integridade

Os vínculos são mantidos por identificadores (`owner_id`, `user_id`, `document_id`, `parent_id`) e regras de integridade ficam na camada de validação/serviço. Os modelos Pydantic representam os contratos de dados da aplicação.

### Dados iniciais

O seed não cria usuários nem credenciais. Ele grava somente um marcador `system.bootstrap` em `eventos`, registrando a inicialização. Isso evita criar uma conta administrativa insegura durante o bootstrap.

### Evolução do banco

A versão de migração é registrada em `migrations`, permitindo evoluir a estrutura por versões rastreáveis. A coleção `migrations` é técnica e não representa uma entidade funcional do sistema.

### Backup e recuperação

Foram implementados `mongodump` e `mongorestore`. A integração automatizada executa um ciclo real: grava um marcador, gera um dump, remove o marcador, restaura o dump e confirma que o registro voltou ao banco.

### Validação

A Fase 3 possui testes unitários para modelos, integridade e comandos de backup, além de teste de integração com MongoDB que valida bootstrap, materialização das coleções, índices, seed e recuperação física de backup. O workflow instala as ferramentas necessárias e executa essa integração em um serviço MongoDB isolado.

### Estrutura final da Fase 3

A estrutura de dados documentada nesta fase é, portanto:

`usuarios` · `documentos` · `versoes` · `pastas` · `etiquetas` · `sessoes` · `eventos` · `notificacoes` · `grupos`

com `migrations` como coleção técnica de controle de versões.

A documentação passa a refletir a estrutura efetivamente implementada, incluindo `grupos` e deixando explícito o papel técnico de `migrations`.
