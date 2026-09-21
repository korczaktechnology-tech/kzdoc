# Fase 11 — Usuários, Grupos e Permissões

A Fase 11 implementa identidade administrativa, agrupamento e autorização no backend e na interface.

## Checklist 181–194
- [x] 181 Criar usuários — cadastro público e criação administrativa.
- [x] 182 Editar usuários — perfil e administração.
- [x] 183 Desativar usuários — estado inativo impede autenticação.
- [x] 184 Criar grupos.
- [x] 185 Adicionar usuários aos grupos.
- [x] 186 Definir permissões.
- [x] 187 Aplicar permissões aos documentos.
- [x] 188 Aplicar permissões às áreas/pastas.
- [x] 189 Perfil administrador.
- [x] 190 Perfil gestor.
- [x] 191 Perfil usuário.
- [x] 192 Acesso permitido.
- [x] 193 Acesso negado.
- [x] 194 Tentativa de acesso direto pela API.

## Modelo de autorização
A autorização é verificada no servidor. Proprietários têm controle sobre seus recursos; administradores possuem acesso administrativo; demais acessos dependem da ACL do documento ou da pasta.

Cada ACL registra papel da política, ações read/write/delete/share, usuários autorizados e grupos autorizados.

Permissões de uma pasta podem conceder acesso aos documentos pertencentes àquela área. A API continua sendo a autoridade final.

## Perfis
- Administrador: administração de usuários, grupos e políticas.
- Gestor: perfil disponível para usuários administrativos/operacionais e sujeito às ACLs dos recursos.
- Usuário: acesso normal conforme propriedade e ACLs concedidas.

## Validação
O workflow da fase executa testes de contrato, integração com MongoDB e build/testes do frontend. Os cenários incluem criação e desativação de usuários, grupos, associação, permissões por grupo, acesso permitido, revogação e tentativa de acesso direto à API.
