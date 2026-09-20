# KORCZAK DOCUMENTS — FASE 0
## Definição e congelamento do projeto

**Status:** CONCLUÍDA  
**Fase:** 0 de 30  
**Versão de especificação:** 0.1.0  
**Data:** 20 de setembro de 2026

---

## 1. Objetivo da Fase 0

A Fase 0 estabelece o contrato funcional e estrutural do Korczak Documents antes do início da implementação. Depois deste documento, alterações de escopo devem ser tratadas como mudança de versão da especificação, e não como alteração informal durante o desenvolvimento.

A Fase 0 cobre os 16 itens definidos no plano geral de conclusão:

1. escopo;
2. funcionalidades obrigatórias;
3. funcionalidades futuras;
4. plataformas;
5. comportamento comum;
6. diferenças por plataforma;
7. identidade visual;
8. nomenclatura;
9. regras de negócio;
10. permissões;
11. documentos;
12. usuários;
13. pastas;
14. versões;
15. auditoria;
16. documentação oficial.

---

# 2. Escopo definitivo

O Korczak Documents será um sistema multiplataforma para criação, organização, edição, armazenamento, versionamento, pesquisa e administração de documentos.

O produto terá uma única lógica de negócio centralizada. Web, desktop e mobile serão diferentes formas de acesso ao mesmo sistema, e não produtos independentes.

A arquitetura deverá preservar:

- conta e sessão do usuário;
- documentos;
- editor;
- pastas;
- etiquetas;
- favoritos;
- documentos recentes;
- lixeira;
- pesquisa;
- grupos;
- permissões;
- histórico e versionamento;
- auditoria;
- notificações;
- configurações;
- administração;
- sincronização entre dispositivos.

A API será a camada responsável pela comunicação entre os clientes e os dados persistidos.

---

# 3. Funcionalidades obrigatórias

A versão inicial deverá contemplar:

### Conta e sessão
- criação de conta;
- login;
- logout;
- gerenciamento de sessão;
- proteção de áreas autenticadas;
- gerenciamento de credenciais conforme a implementação de segurança definida posteriormente.

### Documentos
- criação;
- visualização;
- edição;
- salvamento;
- exclusão;
- restauração;
- organização em pastas;
- etiquetas;
- favoritos;
- documentos recentes.

### Editor
- criação e edição de conteúdo;
- salvar;
- indicação do estado de salvamento;
- desfazer;
- refazer;
- leitura;
- criação de versões;
- histórico;
- restauração de versão;
- proteção contra perda acidental.

### Organização
- criação, renomeação e exclusão de pastas;
- movimentação de documentos;
- etiquetas;
- favoritos;
- recentes;
- lixeira;
- restauração;
- exclusão definitiva.

### Pesquisa
- nome;
- descrição;
- conteúdo quando suportado;
- pasta;
- etiqueta;
- proprietário;
- estado;
- período;
- combinação de filtros;
- ordenação;
- paginação.

### Administração
- usuários;
- grupos;
- permissões;
- auditoria;
- configurações administrativas.

### Sincronização
- documentos;
- versões;
- pastas;
- favoritos;
- configurações globais aplicáveis;
- sessão conforme política de segurança;
- tratamento de perda e retomada de conexão;
- tratamento de alterações concorrentes.

---

# 4. Funcionalidades fora da versão inicial

Para impedir crescimento informal do escopo, os seguintes recursos não fazem parte da obrigação da primeira versão, salvo decisão posterior registrada em uma nova versão da especificação:

- integrações externas não necessárias ao funcionamento central;
- recursos avançados de colaboração em tempo real;
- recursos avançados de inteligência artificial;
- automações externas;
- recursos empresariais não especificados;
- funcionalidades de armazenamento offline completo;
- recursos nativos específicos de uma plataforma que não tenham equivalente funcional no núcleo.

Esses recursos poderão ser adicionados posteriormente sem alterar o núcleo já definido.

---

# 5. Plataformas oficiais

O Korczak Documents deverá ser disponibilizado para seis ambientes:

1. Web;
2. Windows;
3. macOS;
4. Linux;
5. Android;
6. iOS.

A Web será acessível por navegador e preparada para publicação por GitHub Pages.

Desktop e mobile utilizarão o mesmo backend e o mesmo modelo de dados do produto.

---

# 6. Comportamento comum entre plataformas

As seguintes regras são comuns:

- a conta do usuário é a mesma;
- os documentos pertencem ao mesmo ambiente de dados;
- versões devem permanecer consistentes;
- permissões são definidas pelo servidor;
- alterações realizadas em um dispositivo devem poder aparecer nos demais;
- a interface deve preservar a mesma hierarquia de informação;
- ações equivalentes devem possuir comportamento equivalente;
- erros devem possuir tratamento consistente;
- operações críticas devem apresentar confirmação ou proteção contra perda;
- nenhuma plataforma poderá conceder uma permissão que o servidor não autorize.

O servidor será a fonte de verdade para dados persistentes.

---

# 7. Particularidades por plataforma

## Web

A versão Web será otimizada para navegação por navegador, teclado e diferentes tamanhos de tela. Deverá funcionar como aplicação real conectada à API, sem dados fictícios.

## Windows

A aplicação deverá possuir janela própria, instalação, execução, atualização e desinstalação adequadas ao ambiente Windows.

## macOS

A aplicação deverá respeitar o modelo de distribuição e execução do macOS, mantendo o mesmo comportamento funcional do núcleo.

## Linux

A aplicação deverá ser distribuída em formato definido na etapa de empacotamento e manter o mesmo núcleo funcional.

## Android

A interface deverá priorizar toque, telas menores, teclado virtual, orientação e retomada de conexão.

## iOS

A interface deverá seguir o mesmo princípio funcional do Android, adaptada às características do iOS.

Nenhuma diferença visual de plataforma poderá alterar as regras de negócio.

---

# 8. Identidade visual

A identidade visual será definida como parte do produto e deverá ser aplicada de forma consistente.

Princípios obrigatórios:

- aparência profissional;
- hierarquia visual clara;
- consistência entre telas;
- espaçamento coerente;
- tipografia legível;
- estados de carregamento, sucesso, erro e vazio;
- feedback visual para ações;
- adaptação a telas pequenas;
- acessibilidade considerada desde a implementação.

A identidade visual detalhada deverá ser registrada em documentação própria antes da conclusão da interface.

---

# 9. Nomenclatura oficial

Os nomes abaixo ficam congelados para a primeira versão:

- Korczak Documents — produto;
- Dashboard/Início — área inicial;
- Documentos — área principal de documentos;
- Editor — área de edição;
- Pastas — organização hierárquica;
- Favoritos — documentos marcados;
- Recentes — documentos acessados recentemente;
- Lixeira — itens removidos;
- Pesquisa — busca geral;
- Pesquisa avançada — filtros combinados;
- Perfil — dados do usuário;
- Usuários — administração de usuários;
- Grupos — agrupamento de usuários;
- Permissões — controle de acesso;
- Auditoria — registro de eventos;
- Administração — administração geral;
- Configurações — preferências e configurações.

Os nomes de API e banco devem ser mantidos tecnicamente consistentes com essa nomenclatura.

---

# 10. Regras de negócio

1. Todo documento deve possuir identificação única.
2. Todo documento deve possuir proprietário ou contexto de propriedade definido.
3. Um usuário só poderá executar uma operação quando possuir autorização para ela.
4. A interface nunca será considerada autoridade de segurança.
5. Toda operação protegida deverá ser validada no servidor.
6. Exclusão lógica deverá ser diferenciada de exclusão definitiva.
7. Uma versão restaurada deverá manter histórico coerente.
8. Alterações importantes deverão ser registradas na auditoria.
9. Alterações concorrentes não poderão causar sobrescrita silenciosa.
10. Erros de comunicação não poderão ser tratados como salvamento confirmado.
11. Dados fictícios não poderão permanecer como substitutos de dados reais na versão final.
12. Toda ação visível ao usuário deverá possuir comportamento correspondente.
13. Documentos de um usuário não poderão ficar acessíveis apenas pela alteração manual de identificadores.
14. A sincronização deverá preservar a consistência do servidor.
15. Operações destrutivas deverão possuir proteção adequada contra execução acidental.

---

# 11. Modelo de permissões

A primeira versão utilizará três perfis funcionais básicos:

### Administrador
Responsável pela administração do ambiente, usuários, grupos, permissões e auditoria conforme as regras definidas pelo sistema.

### Gestor
Responsável pelas operações administrativas que lhe forem atribuídas, sem receber automaticamente todos os poderes do administrador.

### Usuário
Responsável pelo uso cotidiano dos documentos dentro das permissões concedidas.

Além dos perfis, o sistema deverá permitir permissões específicas quando necessário.

A autorização deverá ser aplicada no backend. O frontend apenas refletirá permissões já determinadas pelo servidor.

---

# 12. Modelo de documentos

Cada documento deverá possuir, no mínimo, um conjunto de informações capaz de identificar:

- identificador;
- título/nome;
- descrição quando existente;
- proprietário;
- pasta;
- etiquetas;
- estado;
- versão atual;
- datas relevantes;
- informações necessárias para auditoria;
- referência ao conteúdo conforme a estratégia de armazenamento adotada.

O documento e seu histórico de versões serão tratados como conceitos relacionados, porém distintos.

---

# 13. Modelo de usuários

Um usuário deverá possuir identidade própria no sistema e informações necessárias para:

- autenticação;
- identificação;
- estado da conta;
- perfil;
- grupos;
- permissões;
- sessões;
- auditoria;
- preferências aplicáveis.

Credenciais nunca deverão ser armazenadas de forma insegura.

---

# 14. Modelo de pastas

Pastas terão finalidade de organização.

Deverão suportar:

- criação;
- renomeação;
- exclusão;
- restauração quando aplicável;
- movimentação de documentos;
- hierarquia quando prevista pelo modelo;
- controle de acesso quando aplicável.

A exclusão de uma pasta deverá possuir comportamento explicitamente definido para os documentos contidos nela, evitando perda silenciosa de dados.

---

# 15. Modelo de versões

Cada alteração que constituir uma nova versão deverá preservar o histórico anterior.

O sistema deverá permitir:

- identificação da versão;
- identificação do documento;
- registro de autoria;
- registro temporal;
- acesso ao conteúdo da versão;
- consulta ao histórico;
- restauração.

Restaurar uma versão não deverá apagar silenciosamente as versões posteriores. A operação deverá preservar o histórico.

---

# 16. Modelo de auditoria

A auditoria deverá registrar eventos relevantes, incluindo:

- criação;
- edição;
- exclusão;
- restauração;
- alterações de permissões;
- alterações administrativas;
- autenticações relevantes;
- demais eventos de segurança ou administração definidos durante a implementação.

Os registros deverão ser protegidos contra alterações indevidas e deverão permitir consulta e filtragem.

---

# 17. Contrato de sincronização

O servidor será a fonte central dos dados persistentes.

Cada documento deverá possuir identificação estável. Versões também deverão possuir identificação própria.

A sincronização deverá:

1. enviar uma alteração ao servidor;
2. receber confirmação;
3. atualizar o estado local;
4. refletir a alteração em outros clientes;
5. detectar conflitos;
6. impedir sobrescrita silenciosa;
7. permitir recuperação quando houver falha de conexão.

O comportamento offline detalhado será definido na implementação, sem transformar indisponibilidade temporária em confirmação falsa de salvamento.

---

# 18. Critério de congelamento

A Fase 0 é considerada concluída quando:

- o escopo está registrado;
- as funcionalidades obrigatórias estão registradas;
- o que fica fora da primeira versão está registrado;
- as seis plataformas estão definidas;
- o comportamento comum está definido;
- as diferenças de plataforma estão registradas;
- a identidade visual possui princípios definidos;
- a nomenclatura está congelada;
- as regras de negócio estão registradas;
- as permissões estão registradas;
- os modelos de documento, usuário, pasta e versão estão registrados;
- a auditoria está definida;
- toda a decisão está armazenada no repositório.

---

# 19. Regra de mudança após o congelamento

Depois da conclusão desta fase, uma mudança que altere:

- escopo;
- comportamento;
- modelo de dados;
- permissões;
- plataformas;
- nomenclatura;
- regras de negócio;
- requisitos de sincronização;

deverá ser registrada como alteração da especificação.

Não será permitido alterar silenciosamente este contrato apenas para acomodar uma implementação.

---

# 20. Registro oficial

Este documento é a referência oficial da Fase 0 do Korczak Documents.

A implementação das fases seguintes deverá consultar este documento antes de introduzir novas funcionalidades ou alterar comportamentos definidos.

**Estado da Fase 0: CONCLUÍDA.**
