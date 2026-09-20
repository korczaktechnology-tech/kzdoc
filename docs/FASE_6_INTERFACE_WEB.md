# FASE 6 — INTERFACE WEB

Itens 101–114 da checklist oficial foram implementados.

101 login; 102 recuperação e sessão; 103 layout; 104 menu lateral; 105 cabeçalho; 106 conteúdo; 107 navegação; 108 modais; 109 notificações; 110 tabelas; 111 carregamento; 112 estados vazios; 113 erros; 114 feedback.

A camada frontend/src/services/api.ts centraliza autenticação Bearer, tratamento de 401 e URL configurável por VITE_API_BASE_URL. A interface é responsiva para desktop, telas médias e dispositivos móveis.

A validação operacional é feita pelo workflow da Fase 6 com instalação, build TypeScript/Vite e testes Vitest.