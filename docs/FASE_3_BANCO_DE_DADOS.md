# KORCZAK DOCUMENTS — FASE 3
## BANCO DE DADOS

**Fase:** 3 de 30  
**Itens:** 45–59  
**Banco:** `KZDocs`  
**Estado:** implementada e preparada para validação operacional

### Coleções

O banco utiliza as coleções `usuarios`, `documentos`, `versoes`, `pastas`, `etiquetas`, `sessoes`, `eventos` e `notificacoes`. A aplicação mantém os nomes em um único catálogo para evitar divergência entre código e documentação.

### Conexão

A conexão usa PyMongo Async e recebe a URI por variável de ambiente. O nome do banco é configurado separadamente como `KZDocs`, evitando credenciais e endpoints no código. A documentação oficial do MongoDB recomenda uma URI de conexão e um cliente PyMongo; para aplicações assíncronas, a documentação atual apresenta `AsyncMongoClient`. citeturn0search0turn0search2

### Índices

Foram definidos índices iniciais para identidade de usuário, propriedade e atualização de documentos, numeração de versões, hierarquia de pastas, etiquetas por usuário, expiração de sessões, histórico de eventos e notificações não lidas.

### Referências e integridade

Os vínculos são mantidos por identificadores (`owner_id`, `user_id`, `document_id`, `parent_id`) e as regras de integridade ficam na camada de serviço/validação. MongoDB não recebe dependências de esquema relacional que limitem a evolução do produto.

### Dados iniciais

O seed não cria usuários nem credenciais. Ele grava somente um marcador `system.bootstrap` em `eventos`, registrando a inicialização das coleções. Isso evita criar uma conta administrativa insegura durante o bootstrap.

### Backup e recuperação

Foram criados scripts de backup e restauração com `mongodump` e `mongorestore`. As credenciais permanecem fora do repositório.

### Validação

A suíte da Fase 3 valida a configuração, o catálogo de coleções, os índices, o bootstrap/seed e os scripts sem exigir uma credencial real no CI. A validação contra um deployment MongoDB real depende da configuração de `MONGODB_URI` no ambiente de execução.
