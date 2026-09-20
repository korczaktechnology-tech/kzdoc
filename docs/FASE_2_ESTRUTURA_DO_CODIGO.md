# KORCZAK DOCUMENTS — FASE 2
## ESTRUTURA DO CÓDIGO

**Fase:** 2 de 30  
**Itens:** 29–44  
**Estado:** implementada e preparada para validação operacional

### Matriz

| Item | Entrega | Estado |
|---:|---|---|
| 29 | `/aplicacao-web/` | CONCLUÍDO |
| 30 | `/api/` | CONCLUÍDO |
| 31 | `/testes/` | CONCLUÍDO |
| 32 | `/documentacao/` | CONCLUÍDO |
| 33 | `/scripts/` | CONCLUÍDO |
| 34 | Componentes | CONCLUÍDO |
| 35 | Serviços | CONCLUÍDO |
| 36 | Repositórios | CONCLUÍDO |
| 37 | Modelos | CONCLUÍDO |
| 38 | Rotas | CONCLUÍDO |
| 39 | Validações | CONCLUÍDO |
| 40 | Configurações | CONCLUÍDO |
| 41 | Erros centralizados | CONCLUÍDO |
| 42 | Logs | CONCLUÍDO |
| 43 | Configuração de desenvolvimento | CONCLUÍDO |
| 44 | Configuração de produção | CONCLUÍDO |

### Organização

A API foi separada em camadas de rotas, validações, serviços, repositórios e modelos. Configuração, erros e logging possuem módulos próprios. A aplicação Web possui pontos formais para componentes, serviços e configuração. As raízes de aplicação, API, testes, documentação e scripts também foram criadas.

### Erros

Erros de aplicação possuem uma exceção base (`AppError`) e subclasses para recursos inexistentes e validações. Um registrador central converte esses erros em respostas HTTP padronizadas.

### Logs

O logging é configurado em um único ponto e respeita o nível definido pelas configurações do ambiente. O código de aplicação usa o logger em vez de imprimir diretamente no processo.

### Ambientes

O módulo de configurações utiliza variáveis de ambiente e possui configurações explícitas para desenvolvimento e produção. Segredos continuam fora do repositório.

### Critério de conclusão

Os itens 29–44 possuem estrutura e código inicial versionados. Foi adicionada uma suíte de testes para as camadas e um workflow próprio da Fase 2 para validar backend, frontend, build e testes em ambiente limpo. A fase só será marcada como operacionalmente concluída após a execução bem-sucedida desse workflow.
