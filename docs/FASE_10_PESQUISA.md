# Fase 10 — Pesquisa

## Escopo
A pesquisa permite localizar documentos pelo nome, descrição e conteúdo indexado, além de filtrar por pasta, etiqueta, proprietário, estado e período.

## Implementação
- Pesquisa textual MongoDB em nome, descrição e tipo.
- Pesquisa textual no conteúdo das versões.
- Filtro por pasta e etiqueta.
- Filtro de proprietário limitado ao usuário autenticado.
- Filtro de estado e período.
- Ordenação por atualização ou nome.
- Paginação server-side.
- Interface simples e avançada.
- Estado visual de nenhuma ocorrência.
- Teste de volume com 120 documentos.

## Checklist 168–180
- [x] 168 Pesquisa por nome.
- [x] 169 Pesquisa por descrição.
- [x] 170 Pesquisa por conteúdo, quando aplicável.
- [x] 171 Pesquisa por pasta.
- [x] 172 Pesquisa por etiqueta.
- [x] 173 Pesquisa por proprietário.
- [x] 174 Pesquisa por estado.
- [x] 175 Pesquisa por período.
- [x] 176 Combinação de filtros.
- [x] 177 Ordenação.
- [x] 178 Paginação.
- [x] 179 Tratamento de nenhuma ocorrência.
- [x] 180 Teste com grande quantidade de documentos.

## Critério de conclusão
Backend, frontend, índices, isolamento e testes devem passar no workflow específico e nas regressões anteriores.