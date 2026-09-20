# FASE 7 — TELAS PRINCIPAIS

**Itens 115–135 da checklist oficial.**

Esta fase entrega as telas principais do Korczak Documents e seus fluxos funcionais conectados à API.

## Requisitos atendidos

- 115 — Início/Dashboard
- 116 — Documentos
- 117 — Visualização de documento
- 118 — Editor
- 119 — Criação de documento
- 120 — Edição de documento
- 121 — Histórico
- 122 — Versionamento, seleção e restauração de versões
- 123 — Pastas
- 124 — Favoritos
- 125 — Recentes por registro de abertura
- 126 — Lixeira e restauração
- 127 — Pesquisa
- 128 — Pesquisa avançada com pasta, estado, período e ordenação
- 129 — Perfil
- 130 — Usuários e administração de contas
- 131 — Grupos e gerenciamento de membros
- 132 — Permissões configuráveis por documento
- 133 — Auditoria
- 134 — Administração
- 135 — Configurações

## Critério de conclusão

A fase é considerada concluída quando a interface possui as áreas acima, as ações principais utilizam a API real e os fluxos críticos têm cobertura automatizada. A implementação atual inclui criação, abertura, edição, versionamento e restauração; organização por pastas; favoritos; recentes; lixeira; pesquisa simples e avançada; perfil; usuários; grupos; permissões; auditoria; administração e configurações.

A validação automática é realizada pelo workflow da Fase 7 com instalação limpa do frontend, build TypeScript/Vite e testes Vitest. Os fluxos de API da fase também são exercitados pelos testes de integração do backend quando MongoDB está disponível no ambiente de CI.

## Observação

A Fase 8 continuará aprofundando o editor de documentos. Isso não significa que o editor da Fase 7 seja apenas uma tela vazia: nesta fase ele já permite abrir, editar e salvar conteúdo e criar versões. Recursos avançados do editor pertencem à Fase 8, conforme a checklist oficial.
