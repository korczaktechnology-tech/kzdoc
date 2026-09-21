# Fase 12 — Auditoria e Histórico

## Checklist oficial

195. Registrar criação.  
196. Registrar edição.  
197. Registrar exclusão.  
198. Registrar restauração.  
199. Registrar alterações de permissão.  
200. Registrar alterações administrativas.  
201. Registrar autenticações relevantes.  
202. Criar consulta de eventos.  
203. Criar filtros de auditoria.  
204. Garantir integridade dos registros.

## Implementação

A coleção `eventos` funciona como registro append-only no nível da aplicação. As operações destrutivas e administrativas não possuem rota de alteração ou exclusão de eventos.

Cada novo evento contém:
- `id`;
- `user_id`;
- `actor_id`;
- `type`;
- `action`;
- `resource`;
- `resource_id`;
- `result`;
- `payload` redigido;
- `created_at`;
- `integrity_hash`.

O hash SHA-256 é calculado sobre uma representação canônica dos campos do evento que devem permanecer íntegros, incluindo identidade do ator, ação, recurso, resultado, payload e data. A consulta de auditoria recalcula o hash e retorna `integrity_valid`, permitindo detectar alteração indevida de registros. A redaction é recursiva para impedir que dados sensíveis sejam gravados dentro de objetos ou listas aninhados.

## Eventos cobertos

- criação de documentos e pastas;
- edição e salvamento;
- exclusão e restauração;
- criação/restauração de versões;
- alterações de permissões de documentos e pastas;
- criação, alteração e operações administrativas de usuários;
- criação, associação e remoção de membros de grupos;
- login, logout, recuperação e falhas de autenticação;
- operações de etiquetas e favoritos.

## Consulta

`GET /api/v1/audit` permite paginação e filtros por:
- tipo do evento;
- documento;
- ator;
- recurso;
- resultado;
- período.

Administradores e gestores podem consultar a visão global. Usuários comuns consultam somente seus próprios eventos. O servidor não aceita que um usuário comum consulte o histórico de outro ator.

## Privacidade

O payload passa por uma camada de redaction antes do armazenamento. Campos como senha, token, segredo, autorização, cookie, chave de API e conteúdo integral do documento não são gravados na auditoria.

## Validação

A integração testa:
- eventos de criação;
- alteração de permissões;
- autenticação falha;
- consulta paginada;
- filtros;
- isolamento por ator;
- presença do hash;
- detecção de adulteração do payload e do ator;
- regressão do backend;
- build e testes do frontend.

## Critério de conclusão

Os itens 195–204 somente são considerados concluídos quando a implementação e o workflow específico da Fase 12 passam, juntamente com as regressões das fases anteriores.
