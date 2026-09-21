# FASE 8 — EDITOR DE DOCUMENTOS

**Itens:** 136–153 da checklist oficial  
**Estado:** implementação concluída e submetida à validação automática

## Objetivo

A Fase 8 transforma o editor existente em uma área de trabalho efetiva para criação, edição, salvamento, leitura e preservação de documentos.

O editor trabalha com conteúdo textual estruturado em Markdown controlado pela aplicação. Isso permite manter o conteúdo independente de HTML bruto e, ao mesmo tempo, oferecer formatação por uma barra de ferramentas.

## Itens implementados

- **136 — Criar editor:** área central de edição com título, conteúdo, metadados e ações.
- **137 — Criar barra de ferramentas:** negrito, itálico, riscado, títulos, listas, citação, código, link, tabela, desfazer e refazer.
- **138 — Criar criação de conteúdo:** criação de documentos com conteúdo inicial.
- **139 — Criar edição:** alteração de título, tipo e conteúdo.
- **140 — Implementar salvar:** endpoint dedicado de salvamento.
- **141 — Indicação de estado do salvamento:** salvo, alterações locais, salvando, conflito e erro.
- **142 — Implementar desfazer:** histórico local de alterações.
- **143 — Implementar refazer:** pilha de alterações futuras.
- **144 — Implementar saída segura:** aviso antes de abandonar a página enquanto há alterações pendentes.
- **145 — Implementar visualização somente leitura:** editor pode ser colocado em modo de leitura sem controles de edição.
- **146 — Implementar criação de nova versão:** cada salvamento de conteúdo gera uma nova versão.
- **147 — Implementar histórico:** versões e eventos podem ser consultados a partir do documento.
- **148 — Implementar restauração de versão:** restauração gera uma nova versão, preservando o histórico.
- **149 — Implementar proteção contra perda acidental:** rascunho local, preservação em falha e detecção de conflito entre sessões.
- **150 — Testar documentos pequenos:** fluxo de criação e salvamento coberto na integração.
- **151 — Testar documentos grandes:** integração salva e recupera conteúdo com mais de 200 mil caracteres.
- **152 — Testar interrupção durante salvamento:** falhas de rede/salvamento preservam o rascunho local; a saída da página também é protegida enquanto há alterações pendentes.
- **153 — Testar abertura simultânea:** o salvamento exige a versão-base atual; uma segunda sessão com versão antiga recebe conflito HTTP 409 e não sobrescreve a alteração mais recente.

## Salvamento concorrente

O endpoint POST /api/v1/documents/{document_id}/save recebe:

- nome;
- tipo;
- conteúdo;
- base_version_id.

O servidor compara a versão-base enviada pelo editor com a versão atualmente registrada no documento. Se forem diferentes, o servidor rejeita o salvamento com conflito, evitando sobrescrita silenciosa.

Quando o salvamento é aceito:

1. uma nova versão é criada;
2. o documento passa a apontar para essa versão;
3. nome e tipo são atualizados;
4. o evento de salvamento é registrado;
5. a resposta devolve o documento atualizado e o conteúdo persistido.

## Proteção local

Enquanto existem alterações não salvas, o conteúdo é mantido como rascunho local por documento. A aplicação também registra a intenção de saída da página para que o navegador possa alertar sobre alterações pendentes.

Em falha de salvamento, o rascunho permanece disponível e o estado visual informa que a operação precisa ser repetida.

## Segurança do conteúdo

O conteúdo salvo é textual. A visualização converte o Markdown permitido para HTML somente depois de escapar o conteúdo recebido, evitando interpretar HTML bruto fornecido pelo usuário.

Links são aceitos somente no formato controlado de URL HTTP/HTTPS na conversão visual.

## Validação

O workflow phase-8-editor.yml executa:

- testes unitários do backend;
- integração real com MongoDB;
- salvamento;
- conflito concorrente;
- documentos grandes;
- build TypeScript/Vite;
- testes do editor;
- validação da conversão de conteúdo;
- proteção contra interpretação de HTML bruto.

A conclusão da Fase 8 fica condicionada ao resultado verde desses testes no GitHub Actions.
