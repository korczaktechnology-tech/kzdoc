# Fase 11 — Usuários, Grupos e Permissões

## Checklist 181–194
- [x] 181 Criar usuários.
- [x] 182 Editar usuários.
- [x] 183 Desativar usuários.
- [x] 184 Criar grupos.
- [x] 185 Adicionar usuários aos grupos.
- [x] 186 Definir permissões.
- [x] 187 Aplicar permissões aos documentos.
- [x] 188 Aplicar permissões às áreas/pastas.
- [x] 189 Perfil administrador.
- [x] 190 Perfil gestor.
- [x] 191 Perfil usuário.
- [x] 192 Testar acesso permitido.
- [x] 193 Testar acesso negado.
- [x] 194 Testar acesso direto pela API.

## Regras de autorização
O proprietário mantém controle sobre seus recursos. Administradores possuem acesso administrativo. Gestores podem administrar usuários e grupos e políticas de acesso, sem poder criar ou promover outro administrador. Usuários comuns operam seus próprios recursos e recursos explicitamente compartilhados por ACL.

Permissões são avaliadas no servidor; esconder um botão no frontend não é uma medida de segurança.

### Ações ACL
read, write, delete, share.

### Áreas
Pastas possuem ACL própria. Quando um documento não concede acesso diretamente, a política da pasta pode conceder acesso ao documento contido nela.

### Desativação
Usuários inativos não conseguem iniciar novas sessões e sessões existentes são rejeitadas pela autenticação.

## Validação
O workflow da Fase 11 executa testes de integração com MongoDB e build/testes do frontend. A suíte verifica criação, edição, desativação, grupos, membros, ACL direta, ACL por grupo, ACL de pasta, perfis, acesso permitido, acesso negado e tentativa direta pela API.
