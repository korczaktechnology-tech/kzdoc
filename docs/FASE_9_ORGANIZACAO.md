# Fase 9 — Organização

**Itens:** 154–167  
**Objetivo:** completar a organização documental do Korczak Documents, garantindo que pastas, movimentação, etiquetas, favoritos, recentes e lixeira tenham comportamento real, persistente e verificável.

## Escopo fechado

### 154 — Criar pastas
A interface permite criar pastas e subpastas. O backend valida a pasta pai e grava a pasta na coleção `pastas` com proprietário e estado ativo.

### 155 — Renomear pastas
Pastas existentes podem ser renomeadas. A alteração é persistida pelo endpoint PATCH de pastas e registrada na auditoria.

### 156 — Excluir pastas
A exclusão de uma pasta é lógica: a pasta passa ao estado `deleted`, evitando remoção física imediata e permitindo recuperação.

### 157 — Restaurar pastas quando aplicável
Pastas excluídas ficam disponíveis na lixeira de pastas e podem ser restauradas pelo endpoint próprio. A restauração devolve o estado `active`.

### 158 — Mover documentos
O documento possui `folder_id` persistente. A interface disponibiliza a ação “Mover para pasta”, incluindo a opção de remover o documento de qualquer pasta.

### 159 — Criar etiquetas
O usuário pode criar etiquetas nomeadas. O backend impede duplicação da mesma etiqueta dentro da conta.

### 160 — Aplicar etiquetas
Uma etiqueta existente ou recém-criada pode ser aplicada ao documento. O documento mantém os nomes das etiquetas em `tag_names`.

### 161 — Remover etiquetas
Cada etiqueta aplicada aparece no visualizador do documento e pode ser removida individualmente.

### 162 — Criar favoritos
O documento pode ser marcado como favorito. A operação usa `$addToSet`, evitando duplicação e registrando evento.

### 163 — Remover favoritos
O favorito pode ser removido individualmente e a interface atualiza o estado do documento.

### 164 — Registrar documentos recentes
A abertura de um documento chama o endpoint de registro de abertura. O backend mantém eventos `document.opened` e a lista de recentes elimina duplicidades preservando a ordem da abertura mais recente.

### 165 — Implementar lixeira
Documentos excluídos passam ao estado `deleted` e aparecem na tela Lixeira. A operação não remove imediatamente o conteúdo do banco.

### 166 — Implementar restauração
Documentos da lixeira podem ser restaurados para o estado `active`.

### 167 — Implementar exclusão definitiva
A Lixeira oferece exclusão definitiva com confirmação. A API remove o documento e suas versões de forma permanente.

## Regras de segurança

- Todas as operações são vinculadas ao usuário autenticado.
- A API valida propriedade antes de modificar pastas e documentos.
- Exclusão definitiva exige operação explícita.
- A interface pede confirmação antes da exclusão permanente.
- Etiquetas e favoritos pertencem ao usuário autenticado.
- O estado de lixeira não é confundido com exclusão física.
- As operações relevantes geram eventos de auditoria.

## Fluxos validados

1. criar pasta → renomear → mover documento → excluir pasta → restaurar pasta;
2. criar etiqueta → aplicar → remover;
3. favoritar → listar favoritos → desfavoritar;
4. abrir documento → registrar recente → listar recentes;
5. excluir documento → visualizar lixeira → restaurar;
6. excluir documento → lixeira → excluir definitivamente;
7. tentar operar sobre recursos de outro usuário.

## Validação automática

O workflow `.github/workflows/phase-9-organization.yml` executa:

- testes unitários do backend;
- integração real com MongoDB;
- criação e renomeação de pastas;
- lixeira e restauração de pastas;
- movimentação de documentos;
- etiquetas;
- favoritos;
- recentes;
- lixeira de documentos;
- restauração;
- exclusão definitiva;
- build TypeScript/Vite;
- testes do frontend.

A Fase 9 somente é marcada como concluída após o workflow terminar com sucesso.
