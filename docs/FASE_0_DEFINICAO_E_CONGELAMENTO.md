# KORCZAK DOCUMENTS — FASE 0
## DEFINIÇÃO E CONGELAMENTO DO PROJETO

**Projeto:** Korczak Documents  
**Fase:** 0 de 30  
**Status da especificação:** 100% CONCLUÍDA  
**Status de implementação:** NÃO É OBJETIVO DA FASE 0  
**Versão:** 1.0.0  
**Data de fechamento:** 20 de setembro de 2026  
**Branch:** main

---

# 1. FINALIDADE DESTE DOCUMENTO

A Fase 0 existe para transformar a ideia do Korczak Documents em um contrato de produto claro, verificável e congelado antes da execução das fases técnicas.

O objetivo não é afirmar que o sistema já foi programado. O objetivo é garantir que, antes da implementação, esteja definido:

- o que o produto é;
- o que ele deve fazer;
- o que não faz na primeira versão;
- em quais plataformas estará disponível;
- como as plataformas devem se comportar;
- qual é a identidade visual;
- quais nomes serão utilizados;
- quais regras de negócio serão obedecidas;
- como funciona a autorização;
- como os documentos são estruturados;
- como os usuários são estruturados;
- como as pastas funcionam;
- como o versionamento funciona;
- como a auditoria funciona;
- como todas essas decisões serão preservadas durante as fases seguintes.

A partir deste documento, nenhuma decisão pertencente à Fase 0 deverá ser alterada informalmente durante a implementação.

---

# 2. RESULTADO DA REVISÃO

A revisão desta fase foi feita contra os 16 itens oficiais da checklist de conclusão.

## Matriz oficial

| Item | Setor | Estado |
|---:|---|---|
| 1 | Escopo definitivo | 100% fechado |
| 2 | Funcionalidades obrigatórias | 100% fechado |
| 3 | Funcionalidades futuras | 100% fechado |
| 4 | Seis plataformas | 100% fechado |
| 5 | Comportamento comum | 100% fechado |
| 6 | Particularidades por plataforma | 100% fechado |
| 7 | Identidade visual | 100% fechado |
| 8 | Nomenclatura | 100% fechado |
| 9 | Regras de negócio | 100% fechado |
| 10 | Permissões | 100% fechado |
| 11 | Modelo de documentos | 100% fechado |
| 12 | Modelo de usuários | 100% fechado |
| 13 | Modelo de pastas | 100% fechado |
| 14 | Modelo de versões | 100% fechado |
| 15 | Modelo de auditoria | 100% fechado |
| 16 | Documentação oficial | 100% fechado |

**Resultado: 16/16 setores definidos.**

Isso significa **100% de conclusão da Fase 0 como especificação de produto**.

Isso não significa que o software esteja 100% implementado. A implementação começa nas fases posteriores.

---

# 3. ESCOPO DEFINITIVO

O Korczak Documents é um sistema multiplataforma de gestão documental.

Seu núcleo permite ao usuário:

1. criar documentos;
2. editar documentos;
3. salvar documentos;
4. organizar documentos;
5. localizar documentos;
6. consultar documentos;
7. controlar versões;
8. restaurar versões;
9. excluir e restaurar documentos;
10. trabalhar com pastas e etiquetas;
11. marcar favoritos;
12. consultar documentos recentes;
13. administrar usuários;
14. administrar grupos;
15. controlar permissões;
16. consultar auditoria;
17. sincronizar os dados entre dispositivos;
18. configurar o ambiente e a conta.

O produto possui um núcleo lógico único.

Web, Windows, macOS, Linux, Android e iOS são clientes diferentes para o mesmo sistema. Nenhum cliente poderá criar uma regra de negócio incompatível com o núcleo.

---

# 4. LIMITE DA PRIMEIRA VERSÃO

A primeira versão obrigatoriamente cobre:

- autenticação;
- sessão;
- documentos;
- editor;
- pastas;
- etiquetas;
- favoritos;
- recentes;
- lixeira;
- pesquisa;
- usuários;
- grupos;
- permissões;
- auditoria;
- versionamento;
- configurações;
- sincronização;
- interface funcional;
- tratamento de erros;
- proteção contra perda de dados.

A primeira versão não terá como requisito obrigatório:

- colaboração avançada em tempo real;
- inteligência artificial avançada;
- automações externas;
- integrações externas não necessárias ao núcleo;
- armazenamento offline completo e ilimitado;
- recursos empresariais não especificados neste contrato;
- recursos exclusivos de uma plataforma que quebrem a equivalência funcional do produto.

Esses itens poderão entrar futuramente por alteração formal de especificação.

---

# 5. FUNCIONALIDADES OBRIGATÓRIAS

## 5.1 Conta e autenticação

Devem existir:

- criação de conta;
- entrada na conta;
- saída da conta;
- manutenção de sessão;
- expiração de sessão;
- proteção de áreas autenticadas;
- recuperação de acesso;
- alteração de credenciais;
- encerramento de sessões quando aplicável;
- tratamento de conta desativada;
- mensagens de erro sem exposição de informações sensíveis.

Credenciais não poderão ser armazenadas em texto puro.

## 5.2 Documentos

Cada usuário autorizado deverá poder:

- criar;
- abrir;
- visualizar;
- editar;
- salvar;
- renomear;
- mover;
- etiquetar;
- favoritar;
- remover dos favoritos;
- excluir;
- restaurar;
- consultar histórico;
- restaurar uma versão.

## 5.3 Editor

O editor deverá possuir:

- área de conteúdo;
- estado de edição;
- estado de salvamento;
- salvamento confirmado;
- salvamento pendente;
- erro de salvamento;
- desfazer;
- refazer;
- leitura;
- edição;
- histórico;
- restauração;
- proteção contra saída com alteração pendente.

Nunca será exibido "salvo" quando o servidor não tiver confirmado a persistência correspondente.

## 5.4 Organização

O sistema deverá possuir:

- pastas;
- hierarquia de pastas;
- movimentação;
- etiquetas;
- favoritos;
- recentes;
- lixeira;
- restauração;
- exclusão definitiva.

## 5.5 Pesquisa

A pesquisa deverá suportar:

- nome;
- descrição;
- conteúdo quando indexado;
- pasta;
- etiqueta;
- proprietário;
- estado;
- período;
- combinação de filtros;
- ordenação;
- paginação.

Os resultados deverão respeitar as permissões do usuário.

## 5.6 Administração

A administração deverá permitir, conforme a autorização:

- consultar usuários;
- criar usuários quando aplicável;
- alterar estado de usuários;
- consultar grupos;
- criar e administrar grupos;
- conceder e remover permissões;
- consultar auditoria;
- administrar configurações permitidas.

## 5.7 Sincronização

A sincronização deverá cobrir:

- documentos;
- versões;
- pastas;
- etiquetas;
- favoritos;
- estados relevantes;
- configurações sincronizáveis;
- alterações realizadas em outros dispositivos.

Falhas de conexão deverão ser distinguíveis de operações confirmadas.

---

# 6. FUNCIONALIDADES FUTURAS

Os seguintes recursos ficam explicitamente fora do congelamento da primeira versão:

### Colaboração avançada
- edição simultânea em tempo real;
- presença de usuários;
- comentários colaborativos avançados;
- cursores compartilhados.

### Inteligência e automação
- geração avançada de conteúdo;
- classificação automática avançada;
- automações externas;
- agentes;
- fluxos inteligentes não necessários ao núcleo.

### Integrações
- serviços externos;
- armazenamento externo;
- provedores corporativos;
- integrações de terceiros.

### Recursos empresariais adicionais
- estruturas organizacionais não especificadas;
- políticas corporativas adicionais;
- recursos avançados de conformidade;
- módulos não definidos neste contrato.

A inclusão desses recursos exige nova especificação ou aditivo formal.

---

# 7. PLATAFORMAS OFICIAIS

O produto deverá possuir seis destinos oficiais:

1. Web;
2. Windows;
3. macOS;
4. Linux;
5. Android;
6. iOS.

## 7.1 Web

A aplicação Web deverá:

- funcionar em navegador moderno;
- ser responsiva;
- possuir navegação por mouse e teclado;
- comunicar-se com a API real;
- não depender de dados fictícios;
- estar preparada para publicação em GitHub Pages;
- tratar estados de carregamento, erro, vazio e sucesso.

## 7.2 Windows

A aplicação Windows deverá possuir:

- janela própria;
- instalação;
- inicialização;
- atualização quando definida;
- desinstalação;
- integração adequada com o ambiente;
- acesso ao mesmo núcleo funcional.

## 7.3 macOS

Deverá possuir:

- aplicação própria;
- instalação/distribuição compatível;
- comportamento de janela adequado;
- atalhos coerentes;
- integração com o ambiente quando aplicável;
- mesmo núcleo funcional.

## 7.4 Linux

Deverá possuir:

- pacote de distribuição definido na fase de empacotamento;
- execução como aplicação própria;
- comportamento consistente;
- mesmo núcleo funcional.

## 7.5 Android

Deverá considerar:

- toque;
- teclado virtual;
- telas pequenas;
- diferentes densidades;
- rotação quando suportada;
- retomada da aplicação;
- perda e recuperação de conexão;
- navegação por gestos e componentes adequados.

## 7.6 iOS

Deverá considerar:

- toque;
- teclado virtual;
- diferentes tamanhos de tela;
- ciclo de vida da aplicação;
- retomada;
- conectividade;
- navegação adaptada ao iOS.

Nenhuma diferença de plataforma poderá modificar regras de negócio.

---

# 8. COMPORTAMENTO COMUM

Todos os clientes deverão obedecer às seguintes regras:

- mesma conta;
- mesmo ambiente de dados;
- mesmos documentos;
- mesmas versões;
- mesmas permissões;
- mesmas regras de segurança;
- mesma identificação dos objetos;
- mesmas regras de exclusão;
- mesma lógica de auditoria;
- mesma lógica de autorização.

Uma ação disponível em múltiplas plataformas deverá produzir o mesmo resultado lógico.

Diferenças de interface são permitidas. Diferenças de regra de negócio não são.

O backend é a autoridade para:

- identidade;
- autorização;
- persistência;
- versionamento;
- auditoria;
- estado definitivo.

---

# 9. IDENTIDADE VISUAL CONGELADA

A identidade visual da primeira versão seguirá uma linguagem:

- profissional;
- tecnológica;
- limpa;
- consistente;
- funcional;
- discreta;
- orientada à produtividade.

## 9.1 Princípios

Todas as telas deverão possuir:

- hierarquia visual;
- espaçamento consistente;
- tipografia legível;
- componentes reutilizáveis;
- estados de carregamento;
- estados vazios;
- estados de erro;
- estados de sucesso;
- feedback de interação;
- contraste adequado;
- foco visível;
- adaptação responsiva.

## 9.2 Sistema visual

A implementação deverá centralizar:

- tipografia;
- tamanhos;
- pesos;
- espaçamentos;
- raios;
- sombras;
- bordas;
- ícones;
- componentes;
- estados;
- breakpoints;
- tokens de cor.

Nenhuma tela deverá inventar valores visuais isoladamente quando existir um token equivalente.

## 9.3 Acessibilidade

A interface deverá considerar:

- contraste;
- foco;
- navegação por teclado onde aplicável;
- tamanho adequado de áreas de toque;
- mensagens compreensíveis;
- identificação textual de ações importantes;
- não depender exclusivamente de cor para comunicar estado.

---

# 10. NOMENCLATURA OFICIAL

Os nomes funcionais ficam congelados:

- Korczak Documents;
- Início;
- Dashboard;
- Documentos;
- Editor;
- Pastas;
- Favoritos;
- Recentes;
- Lixeira;
- Pesquisa;
- Pesquisa avançada;
- Perfil;
- Usuários;
- Grupos;
- Permissões;
- Auditoria;
- Administração;
- Configurações;
- Sessões;
- Histórico;
- Versões.

"Korczak Documents" é o nome oficial do produto.

A nomenclatura técnica de código, API e banco deverá possuir correspondência clara com esses conceitos.

---

# 11. REGRAS DE NEGÓCIO

As seguintes regras são obrigatórias:

1. Todo documento possui identificador único e estável.
2. Todo documento possui proprietário ou contexto de propriedade.
3. Toda operação protegida é autorizada no servidor.
4. O frontend não é autoridade de segurança.
5. Identificadores não podem ser utilizados para contornar autorização.
6. Documento excluído logicamente não deve desaparecer imediatamente do histórico administrativo.
7. Exclusão definitiva é diferente de exclusão lógica.
8. Operações destrutivas devem possuir proteção contra acionamento acidental.
9. Uma restauração de versão preserva o histórico existente.
10. Alterações relevantes devem gerar auditoria.
11. Conflitos não podem ser resolvidos por sobrescrita silenciosa.
12. Falha de rede não pode ser apresentada como salvamento confirmado.
13. Dados fictícios não podem substituir dados reais na versão final.
14. Uma ação apresentada na interface deve possuir comportamento real correspondente.
15. O usuário somente pode consultar objetos que sua autorização permita.
16. A busca deve filtrar resultados de acordo com a autorização.
17. Uma conta desativada não pode continuar operando como conta ativa.
18. Mudanças de permissão devem possuir rastreabilidade.
19. Alterações de conteúdo devem manter autoria e temporalidade.
20. O servidor é a fonte de verdade para dados persistidos.
21. A sincronização deve preservar integridade dos dados.
22. O sistema deve informar claramente quando uma operação falhar.
23. Nenhum cliente poderá criar permissões superiores às determinadas pelo servidor.
24. Dados sensíveis não devem aparecer desnecessariamente em mensagens, logs ou interfaces.
25. Operações administrativas devem ser protegidas por autorização apropriada.

---

# 12. MODELO DE PERMISSÕES

A autorização será composta por perfil funcional e permissões específicas.

## 12.1 Administrador

Pode, conforme as regras do ambiente:

- administrar usuários;
- administrar grupos;
- administrar permissões;
- consultar auditoria;
- administrar configurações administrativas;
- executar operações de manutenção autorizadas.

## 12.2 Gestor

Pode executar as funções administrativas que forem explicitamente concedidas.

Ser Gestor não significa possuir automaticamente todos os poderes do Administrador.

## 12.3 Usuário

Pode operar documentos e recursos pessoais ou compartilhados conforme as permissões recebidas.

## 12.4 Permissões específicas

A implementação deverá trabalhar com permissões granulares para ações como:

- visualizar;
- criar;
- editar;
- excluir;
- restaurar;
- mover;
- compartilhar quando houver compartilhamento;
- administrar;
- auditar.

A decisão final de autorização sempre será do backend.

---

# 13. MODELO DE DOCUMENTOS

Um documento deverá possuir, conceitualmente:

- id;
- título;
- descrição;
- proprietário;
- pasta;
- etiquetas;
- estado;
- versão atual;
- data de criação;
- data de atualização;
- autor da última alteração;
- estado de exclusão;
- referências de armazenamento;
- informações necessárias para auditoria.

## Estados mínimos

- ativo;
- na lixeira;
- restaurado;
- excluído definitivamente.

O conteúdo e o histórico de versões serão tratados como entidades relacionadas ao documento, e não como substitutos do documento.

---

# 14. MODELO DE USUÁRIOS

Um usuário deverá possuir:

- identificador;
- dados de identificação;
- credenciais protegidas;
- estado da conta;
- perfil;
- grupos;
- permissões efetivas;
- sessões;
- preferências;
- datas relevantes;
- informações de auditoria.

Estados mínimos:

- ativo;
- desativado.

A autenticação e a autorização são conceitos separados.

---

# 15. MODELO DE PASTAS

Uma pasta deverá possuir:

- identificador;
- nome;
- proprietário ou contexto;
- pasta pai quando houver hierarquia;
- datas relevantes;
- estado;
- regras de acesso quando aplicáveis.

Operações:

- criar;
- renomear;
- mover;
- excluir;
- restaurar quando aplicável.

A exclusão de uma pasta deverá definir explicitamente o destino dos documentos e subpastas envolvidos. Não poderá haver perda silenciosa de conteúdo.

---

# 16. MODELO DE VERSÕES

Uma versão deverá possuir:

- identificador próprio;
- documento relacionado;
- número ou identificador de versão;
- conteúdo ou referência ao conteúdo;
- autor;
- data;
- motivo/metadados quando definidos;
- estado necessário à restauração.

Regras:

- versões anteriores são preservadas;
- uma nova versão não apaga a anterior;
- restauração não destrói versões posteriores;
- restauração gera estado rastreável;
- histórico deve ser consultável por usuários autorizados.

---

# 17. MODELO DE AUDITORIA

A auditoria deverá registrar eventos relevantes.

Cada evento deverá possuir, conceitualmente:

- identificador;
- data e hora;
- ator;
- ação;
- tipo de recurso;
- identificador do recurso quando aplicável;
- resultado;
- contexto técnico necessário;
- informações suficientes para investigação sem registrar dados sensíveis desnecessários.

Eventos mínimos:

- criação;
- edição;
- exclusão;
- restauração;
- restauração de versão;
- alteração de permissões;
- alteração de grupos;
- alterações administrativas;
- autenticações relevantes;
- alterações de conta;
- eventos de segurança relevantes.

Os registros de auditoria não poderão ser editados pelo fluxo administrativo comum.

---

# 18. SINCRONIZAÇÃO

A sincronização deverá utilizar o servidor como fonte de verdade.

Fluxo mínimo:

1. cliente identifica alteração;
2. cliente envia alteração;
3. servidor valida identidade;
4. servidor valida autorização;
5. servidor valida consistência;
6. servidor persiste;
7. servidor confirma;
8. cliente atualiza seu estado;
9. demais clientes podem receber o novo estado.

## Falhas

Se a comunicação falhar:

- o cliente não deve declarar a operação como confirmada;
- o estado pendente deve ser reconhecido;
- a aplicação deve permitir recuperação;
- uma repetição não deve criar duplicidade indevida.

## Conflitos

Quando duas alterações incompatíveis forem detectadas:

- o servidor não deve sobrescrever silenciosamente uma alteração válida;
- o conflito deve ser identificado;
- o cliente deve receber informação suficiente para tratá-lo;
- a resolução deverá preservar rastreabilidade.

A implementação detalhada do mecanismo será definida nas fases técnicas, mas estas regras não poderão ser violadas.

---

# 19. ESTRUTURA DE DADOS E RELACIONAMENTOS

Os conceitos mínimos são:

- Usuário;
- Grupo;
- Permissão;
- Sessão;
- Documento;
- Pasta;
- Etiqueta;
- Versão;
- Auditoria;
- Configuração.

Relacionamentos fundamentais:

- usuário possui sessões;
- usuário pertence a grupos;
- grupo possui permissões;
- usuário pode possuir permissões específicas;
- documento pertence a um contexto de propriedade;
- documento pode estar em uma pasta;
- documento possui versões;
- documento pode possuir etiquetas;
- ações relevantes geram auditoria.

A implementação poderá dividir essas entidades em tabelas, coleções ou estruturas equivalentes, desde que preserve os contratos funcionais.

---

# 20. ESTADOS PADRONIZADOS DA INTERFACE

Todo recurso que execute operação remota deverá possuir, quando aplicável:

- carregando;
- pronto;
- vazio;
- salvando;
- salvo;
- erro;
- indisponível;
- sem autorização;
- conflito;
- operação pendente.

A interface não deverá apresentar estado de sucesso sem confirmação real.

---

# 21. SEGURANÇA DEFINIDA NA FASE 0

A Fase 0 fixa os seguintes princípios:

- autenticação é obrigatória para áreas protegidas;
- autorização ocorre no backend;
- credenciais devem ser protegidas;
- sessões devem possuir política de validade;
- operações administrativas exigem autorização;
- recursos devem ser protegidos contra acesso por identificador;
- dados sensíveis não devem ser expostos desnecessariamente;
- auditoria deve rastrear eventos relevantes;
- clientes não podem elevar seus próprios privilégios.

Os detalhes de implementação criptográfica, infraestrutura e testes pertencem às fases técnicas seguintes, mas deverão obedecer a estes princípios.

---

# 22. TRATAMENTO DE ERROS

Os erros deverão ser classificados, no mínimo, em:

- validação;
- autenticação;
- autorização;
- não encontrado;
- conflito;
- indisponibilidade;
- falha de persistência;
- falha de sincronização;
- erro inesperado.

A mensagem exibida ao usuário deverá ser compreensível e não deverá expor informações internas desnecessárias.

---

# 23. RESPONSABILIDADE POR CAMADA

## Cliente

Responsável por:

- apresentação;
- interação;
- validações de experiência;
- estados visuais;
- envio de solicitações;
- apresentação de respostas.

## API/backend

Responsável por:

- autenticação;
- autorização;
- regras de negócio;
- validação definitiva;
- persistência;
- versionamento;
- auditoria;
- sincronização;
- consistência.

## Banco/armazenamento

Responsável por:

- persistência;
- integridade;
- recuperação conforme a arquitetura;
- armazenamento do conteúdo e metadados.

Nenhuma camada de apresentação poderá substituir a autoridade do backend.

---

# 24. CRITÉRIOS DE ACEITAÇÃO DA FASE 0

A Fase 0 somente pode ser considerada fechada quando os 16 setores abaixo estiverem documentados:

### 1. Escopo
Deve existir definição clara do produto e seus limites.

### 2. Funcionalidades obrigatórias
Cada grupo funcional deve estar listado.

### 3. Funcionalidades futuras
O que não pertence à primeira versão deve estar explicitamente separado.

### 4. Plataformas
As seis plataformas devem estar identificadas.

### 5. Comportamento comum
As regras compartilhadas devem estar definidas.

### 6. Particularidades
Cada plataforma deve ter suas responsabilidades específicas registradas.

### 7. Identidade visual
Os princípios e o sistema visual devem estar definidos.

### 8. Nomenclatura
Os nomes funcionais devem estar congelados.

### 9. Regras de negócio
As regras que não podem ser quebradas pela implementação devem estar registradas.

### 10. Permissões
Perfis e princípios de autorização devem estar definidos.

### 11. Documentos
O modelo conceitual e seus estados devem estar definidos.

### 12. Usuários
O modelo conceitual e estados devem estar definidos.

### 13. Pastas
Estrutura e comportamento devem estar definidos.

### 14. Versões
Histórico e restauração devem estar definidos.

### 15. Auditoria
Eventos e estrutura mínima devem estar definidos.

### 16. Documentação oficial
Tudo deve estar armazenado no repositório oficial.

**Todos os 16 critérios estão atendidos por esta versão.**

---

# 25. O QUE SIGNIFICA "100%" NESTA FASE

"100% concluída" significa:

**100% dos requisitos da Fase 0 foram definidos e registrados.**

Não significa:

- 100% do código pronto;
- 100% da API pronta;
- 100% do banco criado;
- 100% da interface criada;
- 100% dos aplicativos compilados;
- 100% dos testes executados;
- 100% das plataformas publicadas.

Esses resultados pertencem às fases posteriores.

Essa distinção é obrigatória para evitar que planejamento seja confundido com implementação.

---

# 26. CONTROLE DE ALTERAÇÕES

Após o fechamento da Fase 0, qualquer mudança que altere:

- escopo;
- funcionalidade obrigatória;
- funcionalidade futura;
- plataforma;
- comportamento comum;
- comportamento específico;
- identidade;
- nomenclatura;
- regra de negócio;
- permissão;
- modelo de documento;
- modelo de usuário;
- modelo de pasta;
- modelo de versão;
- auditoria;
- sincronização;

deverá gerar uma nova revisão da especificação.

Nenhuma alteração desse tipo deverá ser feita silenciosamente durante as fases seguintes.

---

# 27. VEREDITO DA REVISÃO

## Fase 0: 100% CONCLUÍDA

**16 de 16 setores fechados.**

### Cobertura
- Escopo: fechado.
- Funcionalidades: fechadas.
- Futuro: fechado.
- Plataformas: fechadas.
- Comportamento comum: fechado.
- Particularidades: fechadas.
- Visual: fechado em nível de especificação.
- Nomenclatura: fechada.
- Negócio: fechado.
- Permissões: fechadas.
- Documentos: fechado.
- Usuários: fechado.
- Pastas: fechado.
- Versões: fechado.
- Auditoria: fechado.
- Documentação: registrada.

### Limite importante

A partir deste ponto, a existência de uma definição não deve ser confundida com a existência da implementação correspondente.

A Fase 0 está completa porque o contrato de produto está fechado.

As fases seguintes são responsáveis por transformar esse contrato em software funcional, testado, publicado e homologado.

---

# 28. REGISTRO OFICIAL

Este arquivo é a referência oficial da Fase 0 do Korczak Documents.

Qualquer documento posterior deverá respeitar este contrato ou registrar formalmente a alteração correspondente.

**STATUS FINAL DA FASE 0: 100% CONCLUÍDA.**

**16/16 setores: OK.**
