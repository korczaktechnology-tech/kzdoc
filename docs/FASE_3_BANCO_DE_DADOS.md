# KORCZAK DOCUMENTS — FASE 3
## BANCO DE DADOS

**Fase:** 3 de 30  
**Itens:** 45–59  
**Banco:** `KZDocs`  
**Estado:** implementação completa, aguardando validação operacional final

### Coleções

O banco utiliza as coleções `usuarios`, `documentos`, `versoes`, `pastas`, `etiquetas`, `sessoes`, `eventos` e `notificacoes`. O bootstrap materializa todas as coleções para que a estrutura inicial do banco seja verificável desde a primeira inicialização.

### Conexão

A conexão usa PyMongo Async e recebe a URI por variável de ambiente. O nome do banco é configurado separadamente como `KZDocs`, evitando credenciais e endpoints no código.

### Índices

Foram definidos índices iniciais para identidade de usuário, propriedade e atualização de documentos, numeração de versões, hierarquia de pastas, etiquetas por usuário, expiração de sessões, histórico de eventos e notificações não lidas.

### Referências e integridade

Os vínculos são mantidos por identificadores (`owner_id`, `user_id`, `document_id`, `parent_id`) e regras de integridade ficam na camada de validação/serviço. Os modelos Pydantic representam os contratos de dados da aplicação.

### Dados iniciais

O seed não cria usuários nem credenciais. Ele grava somente um marcador `system.bootstrap` em `eventos`, registrando a inicialização. Isso evita criar uma conta administrativa insegura durante o bootstrap.

### Evolução do banco

A versão de migração é registrada em `migrations`, permitindo evoluir a estrutura por versões rastreáveis.

### Backup e recuperação

Foram implementados `mongodump` e `mongorestore`. A integração automatizada executa um ciclo real: grava um marcador, gera um dump, remove o marcador, restaura o dump e confirma que o registro voltou ao banco.

### Validação

A Fase 3 possui testes unitários para modelos, integridade e comandos de backup, além de teste de integração com MongoDB que valida bootstrap, materialização das coleções, índices, seed e recuperação física de backup. O workflow instala as ferramentas necessárias e executa essa integração em um serviço MongoDB isolado.
